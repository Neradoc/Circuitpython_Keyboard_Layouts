"""
This makes the bundle zip files and the json file.
"""

import datetime
import glob
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import zipfile

import requests
import semver


def get_git_command(command):
    """Execute and return the result of a git command without error."""
    path = os.getcwd()
    procs = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        cwd=path,
    )
    if procs.returncode != 0:
        return None
    return procs.stdout.decode("utf8").strip()


def get_current_version():
    """Get current version string."""
    return get_git_command("git describe --tags --exact-match".split())


def date_to_version(tag):
    """Convert a tag from YYYYMMDD to y.M.D where y is years after 2020."""
    if re.match(r"\d\d\d\d\d\d\d\d", tag):
        year = int(tag[2:4]) - 20
        month = int(tag[4:6])
        day = int(tag[6:8])
        return f"{year}.{month}.{day}"
    return tag


# the date tag for the generated files and stuff
# TODO: retrieve the version number from git or something
# TODO: give each file a different version number possibly
#       (that of the latest released change if possible)
TAG = get_current_version() or datetime.date.today().strftime("%Y%m%d")
# the dirs for putting the things in it
BUILD_DIR = "_build"
BUILD_DEPS = os.path.join(BUILD_DIR, "deps")
BUILD_RELEASE = os.path.join(BUILD_DIR, "release")
# the bundle commone name and file
BUNDLE_NAME = "circuitpython-keyboard-layouts"
BUNDLE_JSON = os.path.join(BUILD_RELEASE, f"{BUNDLE_NAME}-{TAG}.json")
# platform dependent
BUNDLE_PATH_NAME = f"{BUNDLE_NAME}-{{platform}}-{TAG}"
BUNDLE_DIR = os.path.join(BUILD_DIR, BUNDLE_PATH_NAME)
BUNDLE_ZIP = os.path.join(BUILD_RELEASE, BUNDLE_PATH_NAME + ".zip")
BUNDLE_LIB_DIR = os.path.join(BUNDLE_DIR, "lib")
# py platform directory
BUNDLE_REQ_DIR = os.path.join(BUNDLE_DIR.format(platform="py"), "requirements")
BUNDLE_ZIP_JSON = os.path.join(BUNDLE_DIR.format(platform="py"), f"{BUNDLE_NAME}.json")
# where the modules are
MODULES_DIR = "libraries/*/"
# the base requirement file
REQUIREMENTS_FILE = "requirements-modules.txt"
# in-file informations to update (or not)
SET_VERSION_PATTERN = "\n__version__ = '{}'\n"
THIS_REPOSITORY = "https://github.com/Neradoc/Circuitpython_Keyboard_Layouts.git"

PLATFORMS = ["mpy6", "mpy7", "mpy8"]
PLATFORM_NAMES = {
    "py": "py",
    "mpy6": "6.x-mpy",
    "mpy7": "7.x-mpy",
    "mpy8": "8.x-mpy",
}

# https://adafruit-circuit-python.s3.amazonaws.com/index.html?prefix=bin/mpy-cross/
# TODO: identify current OS and pick one
MPYCROSS_URL = "https://adafruit-circuit-python.s3.amazonaws.com/bin/mpy-cross/"
MPYCROSSES = {
    "darwin": {
        "mpy6": "mpy-cross-macos-catalina-6.3.0",
        "mpy7": "mpy-cross-macos-universal-7.3.0",
        "mpy8": "mpy-cross-macos-11-8.0.0-beta.0-x64",
    },
    "linux": {
        "mpy6": "mpy-cross.static-amd64-linux-6.3.0",
        "mpy7": "mpy-cross.static-amd64-linux-7.3.0",
        "mpy8": "mpy-cross.static-amd64-linux-8.0.0-beta.0",
    },
    "win32": {
        "mpy6": "mpy-cross.static-x64-windows-6.3.0.exe",
        "mpy7": "mpy-cross.static-x64-windows-7.3.0.exe",
        "mpy8": "mpy-cross.static-x64-windows-8.0.0-beta.0.exe",
    },
    "raspbian": {
        "mpy6": "mpy-cross.static-raspbian-6.3.0",
        "mpy7": "mpy-cross.static-raspbian-7.3.0",
        "mpy8": "mpy-cross.static-raspbian-8.0.0-beta.0",
    },
}
MPYCROSS = MPYCROSSES[sys.platform]


def file_version_tag(path):
    """
    Find a suitable version tag for a file using commit dates.
    """
    logs = get_git_command(["git", "log", "--pretty=%H", path])
    num_commits = len(logs.split("\n"))
    #
    major = 0
    minor = num_commits // 10
    patch = num_commits % 10
    #
    with open(path, "r") as fp:
        data = fp.read()
        m = re.search(r'__version__ = ["\']([0-9.]+)-auto\.0["\']', data)
        if m:
            file_version = semver.VersionInfo.parse(m.group(1))
            #
            line = len(data.split("__version__")[0].split("\n"))
            vtag = get_git_command(["git", "blame", "-L", f"{line},{line}", path]).split(" ")[0]
            logs = get_git_command(["git", "log", "--pretty=%H", f"--after={vtag}", path]).split("\n")
            # print(f"-tag: {vtag} {line:2d} {num_commits:2d} {len(logs):2d} {path}")
            #
            if file_version.major:
                major = file_version.major
                num_commits = len(logs)
                minor = num_commits // 10
                patch = num_commits % 10
            if file_version.minor:
                minor = file_version.minor
                num_commits = len(logs)
                patch = num_commits
            # if file_version.patch:
            #     patch = file_version.patch
    #
    ver = f"{major}.{minor}.{patch}"
    return ver


def fmt(path, platform="py"):
    """Shortcut for the py directory."""
    return path.format(platform=PLATFORM_NAMES[platform])


# find in python
def list_all_files(path):
    """Clean list of all files in sub folders."""
    pwd = os.getcwd()
    os.chdir(path)
    liste = [
        file
        for file in glob.glob(os.path.join("**"), recursive=True)
        if os.path.isfile(file)
    ]
    os.chdir(pwd)
    return liste


def init_directories():
    """Erase and create build directories."""
    # create build directories
    os.makedirs(BUILD_DIR, exist_ok=True)
    os.makedirs(BUILD_DEPS, exist_ok=True)
    os.makedirs(BUILD_RELEASE, exist_ok=True)
    os.makedirs(fmt(BUNDLE_DIR), exist_ok=True)

    # cleanup build directories
    for platform in ["py"] + PLATFORMS:
        bun_dir = BUNDLE_DIR.format(platform=PLATFORM_NAMES[platform])
        zip_file = BUNDLE_ZIP.format(platform=PLATFORM_NAMES[platform])
        if os.path.isdir(bun_dir):
            shutil.rmtree(bun_dir)
        if os.path.isfile(zip_file):
            os.unlink(zip_file)


def write_version_to(module_local_path, file_tag):
    """Write the version tag to the __version__ property of the module file."""
    module_file = os.path.join(
        fmt(BUNDLE_LIB_DIR),
        module_local_path,
    )
    with open(module_file, "r") as fp:
        data = fp.read()
    if "__version__" in data:
        data = re.sub(
            r'\n__version__ = ["\']([0-9.]+)-auto\.0["\']\n',
            SET_VERSION_PATTERN.format(file_tag),
            data,
        )
        with open(module_file, "w") as fp:
            fp.write(data)


def make_bundle_files():
    """Create the .py bundle directory."""
    # copy all the layouts and keycodes
    for mdir in glob.glob(MODULES_DIR):
        shutil.copytree(mdir, fmt(BUNDLE_LIB_DIR), dirs_exist_ok=True)

    module_versions = {}
    # change the version number of all the bundles
    for module_local in glob.glob(MODULES_DIR + "*"):
        module_name = os.path.basename(module_local).replace(".py","")
        module_base = os.path.dirname(module_local)
        if os.path.isdir(module_local):
            raise OSError("Package modules not implemented yet.")
            # get all versions
            versions = []
            for sub_module in list_all_files(module_local):
                sub_local_file = os.path.join(module_local, sub_module)
                file_tag = file_version_tag(sub_local_file)
                versions.append(semver.VersionInfo.parse(file_tag))
            # keep the highest one
            file_tag = max(versions)
            # set all versions
            for sub_module in list_all_files(module_local):
                module_path = os.path.relpath(module_local, module_base)
                sub_local_file = os.path.join(module_path, sub_module)
                write_version_to(sub_local_file, file_tag)
            module_versions[module_name] = file_tag
        elif module_local.endswith(".py"):
            file_tag = file_version_tag(module_local)
            module_path = os.path.basename(module_local)
            write_version_to(module_path, file_tag)
            module_versions[module_name] = file_tag

    # list of the modules
    all_modules = [
        os.path.basename(mod)
        for mod in glob.glob(MODULES_DIR + "*")
        if not mod.startswith(".")
    ]

    json_data = {}

    for module in all_modules:
        module_name = module.replace(".py", "")
        is_package = (module_name == module)
        # create the requirements directory for each module
        target_dir = os.path.join(BUNDLE_REQ_DIR, module_name)
        os.makedirs(target_dir, exist_ok=True)
        # copy the common requirements file
        target = os.path.join(target_dir, "requirements.txt")
        shutil.copy(REQUIREMENTS_FILE, target)
        # create the json entry
        json_data[module_name] = {
            "package": is_package,
            "pypi_name": "",
            "version": str(module_versions[module_name]),
            "repo": THIS_REPOSITORY,
            "path": "lib/" + module_name,
            "dependencies": [],  # "adafruit_hid"
            "external_dependencies": ["adafruit-circuitpython-hid"],
        }

    # create the json file
    with open(BUNDLE_JSON, "w") as out_file:
        json.dump(json_data, out_file, indent=2)


def make_the_mpy_bundles():
    """Create the mpy bundle(s) directory(ies) and mpy-cross the modules."""
    # copy for the zips
    shutil.copy(BUNDLE_JSON, fmt(BUNDLE_ZIP_JSON))

    # download the mpycrosses
    for cross in MPYCROSS:
        cross_file = os.path.join(BUILD_DEPS, MPYCROSS[cross])
        if not os.path.isfile(cross_file):
            url = MPYCROSS_URL + MPYCROSS[cross]
            response = requests.get(url)
            with open(cross_file, "wb") as cross_fp:
                cross_fp.write(response.content)
            fstats = os.stat(cross_file)
            os.chmod(cross_file, fstats.st_mode | stat.S_IEXEC)

    # duplicate the py dir to mpy dirs
    pwd = os.getcwd()
    for platform in PLATFORMS:
        cross = os.path.join(BUILD_DEPS, MPYCROSS[platform])
        cross = os.path.abspath(cross)
        bun_dir = BUNDLE_DIR.format(platform=PLATFORM_NAMES[platform])
        lib_dir = BUNDLE_LIB_DIR.format(platform=PLATFORM_NAMES[platform])
        shutil.copytree(fmt(BUNDLE_DIR), bun_dir)
        # run mpy-cross in each of those
        os.chdir(lib_dir)
        for lib_file in glob.glob(os.path.join("*.py")):
            mpy_file = lib_file.replace(".py", ".mpy")
            subprocess.call([cross, lib_file, "-o", mpy_file])
            os.unlink(lib_file)
        os.chdir(pwd)


def do_the_zips():
    """Finally create the zip files for release."""
    # now do the zips
    for platform in ["py"] + PLATFORMS:
        in_path = BUNDLE_PATH_NAME.format(platform=PLATFORM_NAMES[platform])
        bun_dir = BUNDLE_DIR.format(platform=PLATFORM_NAMES[platform])
        zip_file = BUNDLE_ZIP.format(platform=PLATFORM_NAMES[platform])
        all_files = list_all_files(bun_dir)
        with zipfile.ZipFile(zip_file, "w") as bundle:
            # metadata (bundler version)
            # build_metadata = {"build-tools-version": build_tools_version}
            # bundle.comment = json.dumps(build_metadata).encode("utf-8")
            for ffile in all_files:
                in_file_path = in_path + "/" + ffile
                bundle.write(os.path.join(bun_dir, ffile), in_file_path)


if __name__ == "__main__":
    init_directories()
    make_bundle_files()
    make_the_mpy_bundles()
    do_the_zips()
