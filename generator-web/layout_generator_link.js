function download_layout() {
    $(".download_link").hide();

    var url = $("#input").val();
    var zip_url = "make_zip_bundle.php?url=" + url;
    console.log(zip_url);

    var platform = "win";
    var lang = url.split("/").pop().replace("kbd", "");

    zips = [
        { extension: ".py", extout: ".py", id: "", version: "py" },
        { extension: "6.mpy", extout: ".mpy", id: "6", version: "mpy6" },
        { extension: "7.mpy", extout: ".mpy", id: "7", version: "mpy7" },
    ];
    for( z in zips ) {
        var zipper = zips[z];
        //
        var zurl = zip_url + "&cpversion="+zipper.id;
        var zip_name = "keyboard_layout_" + platform + "_" + lang + "-{}.zip";
        var zip_file = zip_name.replace("{}", zipper.version);

        //
        $("#download_link"+zipper.id).attr("href", zurl);
        // $("#download_link"+zipper.id).attr("download", zip_file);
        $("#download_link"+zipper.id).attr("title", zip_file);
        $("#download_link"+zipper.id).show();
    }
}
