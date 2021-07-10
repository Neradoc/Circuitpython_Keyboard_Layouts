"""
This makes the bundle zip files and the json file.
Next step: upload as artifacts/release files in github.
"""

import datetime
import glob
import json
import os
import shutil
import stat
import subprocess
import sys
import zipfile

import requests

# make the dirs for putting the things in it
TAG = datetime.date.today().strftime("%Y%m%d")
BUILD_DIR = "_build"
BUILD_DEPS = "_build_deps"
BUILD_ZIPS = "_build_zips"
BUNDLE_NAME = "neradoc-keyboard-layouts"
BUNDLE_JSON = os.path.join(BUILD_DIR, f"{BUNDLE_NAME}-{TAG}.json")
# platform dependent
BUNDLE_PATH_NAME = f"{BUNDLE_NAME}-{{platform}}-{TAG}"
BUNDLE_DIR = os.path.join(BUILD_DIR, BUNDLE_PATH_NAME)
BUNDLE_ZIP = os.path.join(BUILD_ZIPS, BUNDLE_PATH_NAME + ".zip")
BUNDLE_LIB_DIR = os.path.join(BUNDLE_DIR, "lib")
# py platform directory
BUNDLE_REQ_DIR = os.path.join(BUNDLE_DIR.format(platform="py"), "requirements")
BUNDLE_ZIP_JSON = os.path.join(
    BUNDLE_DIR.format(platform="py"), f"{BUNDLE_NAME}-{TAG}.json"
)

SOURCEDIR = "src"
REQUIREMENTS_FILE = "requirements-modules.txt"

# TODO: retrieve the version number from git
# TODO: give each file a different version number possibly (that of the latest released change)
VERSION_NUMBER = "0.0.1"
THIS_REPOSITORY = "https://github.com/Neradoc/Neradoc-Circuitpython-Keyboard-Layouts"

PLATFORMS = ["mpy6", "mpy7"]

# https://adafruit-circuit-python.s3.amazonaws.com/index.html?prefix=bin/mpy-cross/
# TODO: identify current OS and pick one
MPYCROSS_URL = "https://adafruit-circuit-python.s3.amazonaws.com/bin/mpy-cross/"
MPYCROSSES = {
    "darwin": {
        "mpy6": "mpy-cross-macos-catalina-6.3.0",
        "mpy7": "mpy-cross-macos-universal-7.0.0-alpha.4",
    },
    "linux": {
        "mpy6": "mpy-cross.static-amd64-linux-6.3.0",
        "mpy7": "mpy-cross.static-amd64-linux-7.0.0-alpha.4",
    },
    "win32": {
        "mpy6": "mpy-cross.static-x64-windows-6.3.0.exe",
        "mpy7": "mpy-cross.static-x64-windows-7.0.0-alpha.4.exe",
    },
    "raspbian": {
        "mpy6": "mpy-cross.static-raspbian-6.3.0",
        "mpy7": "mpy-cross.static-raspbian-7.0.0-alpha.4",
    },
}
MPYCROSS = MPYCROSSES[sys.platform]


def fmt(path, platform="py"):
    """shortcut for the py directory"""
    return path.format(platform=platform)


# find in python
def list_all_files(path):
    """clean list of all files in sub folders"""
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
    """erase and create build directories"""
    # create build directories
    os.makedirs(BUILD_DEPS, exist_ok=True)
    os.makedirs(BUILD_ZIPS, exist_ok=True)
    os.makedirs(fmt(BUNDLE_DIR), exist_ok=True)

    # cleanup build directories
    for platform in ["py"] + PLATFORMS:
        bun_dir = BUNDLE_DIR.format(platform=platform)
        zip_file = BUNDLE_ZIP.format(platform=platform)
        if os.path.isdir(bun_dir):
            shutil.rmtree(bun_dir)
        if os.path.isfile(zip_file):
            os.unlink(zip_file)


def make_bundle_files():
    """create the .py bundle directory"""
    # copy all the layouts and keycodes
    shutil.copytree(SOURCEDIR, fmt(BUNDLE_LIB_DIR))

    # list of the modules
    all_modules = [mod.replace(".py", "") for mod in os.listdir(SOURCEDIR)]

    json_data = {}

    for module in all_modules:
        # create the requirements directory for each module
        target_dir = os.path.join(BUNDLE_REQ_DIR, module)
        os.makedirs(target_dir, exist_ok=True)
        # copy the common requirements file
        target = os.path.join(target_dir, "requirements.txt")
        shutil.copy(REQUIREMENTS_FILE, target)
        # create the json entry
        json_data[module] = {
            "package": False,
            "pypi_name": "",
            "version": VERSION_NUMBER,
            "repo": THIS_REPOSITORY,
            "path": "lib/" + module,
            "dependencies": ["adafruit_hid"],
            "external_dependencies": [],
        }

    # create the json file
    with open(BUNDLE_JSON, "w") as out_file:
        json.dump(json_data, out_file, indent=2)


def make_the_mpy_bundles():
    """create the mpy bundle(s) directory(ies) and mpy-cross the modules"""
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

    # duplicate the py dir to mpy6 and mpy7
    for platform in PLATFORMS:
        cross = os.path.join(BUILD_DEPS, MPYCROSS[platform])
        bun_dir = BUNDLE_DIR.format(platform=platform)
        lib_dir = BUNDLE_LIB_DIR.format(platform=platform)
        shutil.copytree(fmt(BUNDLE_DIR), bun_dir)
        # run mpy-cross in each of those
        for lib_file in glob.glob(os.path.join(lib_dir, "*.py")):
            mpy_file = lib_file.replace(".py", ".mpy")
            subprocess.call([cross, lib_file, "-o", mpy_file])
            os.unlink(lib_file)


def do_the_zips():
    """finally create the zip files for release"""
    # now do the zips
    for platform in ["py"] + PLATFORMS:
        bun_dir = BUNDLE_DIR.format(platform=platform)
        zip_file = BUNDLE_ZIP.format(platform=platform)
        all_files = list_all_files(bun_dir)
        with zipfile.ZipFile(zip_file, "w") as bundle:
            # metadata (bundler version)
            # build_metadata = {"build-tools-version": build_tools_version}
            # bundle.comment = json.dumps(build_metadata).encode("utf-8")
            for ffile in all_files:
                bundle.write(os.path.join(bun_dir, ffile), ffile)


if __name__ == "__main__":
    init_directories()
    make_bundle_files()
    make_the_mpy_bundles()
    do_the_zips()
