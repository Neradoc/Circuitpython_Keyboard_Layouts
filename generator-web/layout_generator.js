// import { name_to_virtualkey } from './src/keycode_name_to_virtualkey.js';
// import { Keycode } from './src/keycode_us_ref.js';
// import { VIRTUAL_KEY_US } from './src/virtualkey_table_us.js';

// var base_url = "http://kbdlayout.info";
// var keyboard_fr_url = base_url + "/kbdfr";
// var keyboard_fr_xml_url = keyboard_fr_url + "/download/xml";

var COMMON_HEADER_COPYRIGHT = (
`# SPDX-FileCopyrightText: 2021 Neradoc NeraOnGit@ri1.fr
#
# SPDX-License-Identifier: MIT
"""
This file was automatically generated using Circuitpython_Keyboard_Layouts
"""
`)

// "https://raw.githubusercontent.com/Neradoc/Circuitpython_Keyboard_Layouts/main/libraries/keyboard_layout.txt"
var BASE_LAYOUT = "./src/keyboard_layout.py";
var BASE_LAYOUT_NAME = "keyboard_layout.py";
var BASE_LAYOUT_DATA = "";

var SAMPLE_CODE = "./src/sample_code.py";
var SAMPLE_CODE_NAME = "sample_code.py";
var SAMPLE_CODE_DATA = "";


$.get(BASE_LAYOUT,
    (data) => {
        BASE_LAYOUT_DATA = data;
//         BASE_LAYOUT_DATA = BASE_LAYOUT_DATA.replace(
//             '__version__ = "0.0.0-auto.0"', VERSION
//         );
    },
    "text"
);
$.get(SAMPLE_CODE, (data) => { SAMPLE_CODE_DATA = data; }, "text");


SPECIAL_KEYCODES = {
    // key, shift, option, shift-option
    0x56: 0x64,  // ["<",">","≤","≥"]
    0x29: 0x35,  // ["@","#","•","Ÿ"] ² on windows
}

function toTitle(text) {
    return text
        .split("_")
        .map(
            (x) => {
                return x[0].toLocaleUpperCase()
                    + x.slice(1).toLocaleLowerCase();
            }
        )
        .join("_")
}

function filter_codepoints(text) {
    return text.replace("\r", "\n");
}

var virtualkey_to_keyname = {};

for(name in name_to_virtualkey) {
    vkey = name_to_virtualkey[name];
    if( ! (vkey in virtualkey_to_keyname) ) {
        virtualkey_to_keyname[vkey] = [];
    }
    virtualkey_to_keyname[vkey].push(name);
}


function list_keycode_name(key, value) {
    var output = [];
    if(key in virtualkey_to_keyname) {
        for(var i in virtualkey_to_keyname[key]) {
            name = virtualkey_to_keyname[key][i];
            output.push( [name, value] );
        }
    } else {
        output = [[key, value]];
    }
    return output;
}


function get_name_to_keycode() {
    var name_to_kc = {};
    var kcnums = [];
    for( name in Keycode ) {
        kcnums.push( [name, Keycode[name]] );
    }
    kcnums.sort()
    for( i in kcnums ) {
        var name = kcnums[i][0];
        var kc = kcnums[i][1];
        if(name in name_to_virtualkey) {
            name = name_to_virtualkey[name];
        }
        name_to_kc[name] = kc;
    }
    return name_to_kc;
}


function get_vk_to_sc(data) {
    parser = new DOMParser();
    keything = parser.parseFromString(data,"text/xml");

    physical_keys = $(keything)
        .children("KeyboardLayout")
        .children("PhysicalKeys")
        .children("PK");
    
    var vk_to_sc = {};
    function set_res(kname, wit, text) {
        switch( wit ) {
        case "VK_NUMLOCK":
            vk_to_sc[kname]["numpad"] = text;
            break;
        case "VK_SHIFT":
            vk_to_sc[kname]["shift"] = text;
            break;
        case "VK_CONTROL VK_MENU":
            vk_to_sc[kname]["altgr"] = text;
            break;
        case "VK_MENU":
            vk_to_sc[kname]["alt"] = text;
            break;
        default:
            vk_to_sc[kname]["letter"] = text;
            break;
        }
    }
    physical_keys.each((id, key) => {
        // console.log(key);
        var name = $(key).attr("VK").replace("VK_", "");
        var sckey = parseInt($(key).attr("SC"), 16);
        // console.log(name, sckey);
        vk_to_sc[name] = {
            "scancode": sckey,
        };
        //
        $(key).children("Result").each((idx, res) => {
            var VK = $(res).attr("VK");
            // TODO: html unescape ?
            var text = $(res).attr("Text");
            if( VK ) {
                var kname = VK.replace("VK_", "");
                vk_to_sc[kname] = {
                    "scancode": sckey,
                };
                // TODO: html unescape ?
                var text = $(res).attr("Text");
                var wit = $(res).attr("With");
                set_res(kname, wit, text);
            } else if ( text ) {
                var wit = $(res).attr("With");
                set_res(name, wit, text);
            } else {
                var tcp = $(res).attr("TextCodepoints");
                if( tcp ) {
                    var text = String.fromCharCode(parseInt(tcp, 16));
                    text = filter_codepoints(text);
                    var wit = $(res).attr("With");
                    set_res(name, wit, text);
                } else {
                    $(res).children("DeadKeyTable").children("Result").each(
                    (index, deadres) => {
                        var wit = $(deadres).attr("With");
                        if( wit == " ") {
                            var text = $(deadres).attr("Text");
                            set_res(name, wit, text);
                        } else {
                            // TODO: multi-keys dead keys ?
                            // set_res(vk_to_sc, name, text)
                        }
                    });
                }
            }
        });
    });
    return vk_to_sc;
}

function get_scancode_to_keycode() {
    var name_to_kc = get_name_to_keycode();
    var name_to_kc_left = new Set(Object.keys(name_to_kc));
    var vk_to_sc = get_vk_to_sc(VIRTUAL_KEY_US);
    var vk_to_sc_left = new Set(Object.keys(vk_to_sc));

    var sc_to_kc = {};
    for( key in name_to_kc ) {
        if( key in vk_to_sc ) {
            vk_to_sc_left.delete(key);
            name_to_kc_left.delete(key);
            sc_to_kc[vk_to_sc[key]["scancode"]] = name_to_kc[key];
        }
    }

    return sc_to_kc;
}

function LayoutData(asciis, charas, altgr, high, keycodes) {
    return {
        asciis: asciis,
        charas: charas,
        altgr: altgr,
        high: high,
        keycodes: keycodes,
    };
}

function get_layout_data(virtual_key_defs_lang) {
    var asciis = new Array(128); // [0] * 128
    var charas = new Array(128); // [""] * 128
    var SHIFT_FLAG = 0x80;
    var NEED_ALTGR = [];
    var HIGHER_ASCII = {};

    var scancode_to_keycode = get_scancode_to_keycode();

    var KEYCODES = {};

    // loop the list of virtual keycodes that exist in the language
    Object.keys(virtual_key_defs_lang).forEach((virtualkey, num) => {
        // the info on the key
        var key_info = virtual_key_defs_lang[virtualkey];
        // scancode of the key
        var scancode = key_info["scancode"];

        // matching keycodes
        var keycode = null;
        if( scancode in scancode_to_keycode ) {
            keycode = scancode_to_keycode[scancode];
        }
        if( scancode in SPECIAL_KEYCODES ) {
            if( keycode == null ) {
                keycode = SPECIAL_KEYCODES[scancode];
            } else {
                if( keycode != SPECIAL_KEYCODES[scancode] ) {
                    console.log("Different:", keycode, SPECIAL_KEYCODES[scancode]);
                }
            }
        }
        if( keycode == null ) {
            // TODO: check there's none missing
            // console.log("Unknown scancode", virtualkey, key_info);
            return;
        }

        list_keycode_name(virtualkey, keycode).forEach( (item) => {
            KEYCODES[item[0]] = item[1];
        });
        // KEYCODES[virtualkey] = keycode

        // find the letter somehow
        // letter as defined in the keyboard definition
        if( "letter" in key_info ) {
            var letter = key_info["letter"];
            var pos = letter.charCodeAt(0);
            if( pos < 128 ) {
                if( charas[pos] == null ) {
                    asciis[pos] = keycode;
                    charas[pos] = letter;
                    list_keycode_name(virtualkey, keycode).forEach( (item) => {
                        KEYCODES[item[0]] = item[1];
                    });
                    // KEYCODES[virtualkey] = keycode
                }
            } else {
                if( !(letter in HIGHER_ASCII) ) {
                    HIGHER_ASCII[letter] = keycode;
                    list_keycode_name(virtualkey, keycode).forEach( (item) => {
                        KEYCODES[item[0]] = item[1];
                    });
                    // KEYCODES[virtualkey] = keycode
                } else {
                    console.log("double", letter, HIGHER_ASCII[letter]);
                }
            }
        }

        if( "shift" in key_info ) {
            var letter = key_info["shift"];
            var pos = letter.charCodeAt(0);
            if( pos < 128 ) {
                if( charas[pos] == null ) {
                    asciis[pos] = keycode | SHIFT_FLAG;
                    charas[pos] = letter;
                }
            } else {
                if( !(letter in HIGHER_ASCII) ) {
                    HIGHER_ASCII[letter] = keycode | SHIFT_FLAG;
                }
            }
        }

        if( "altgr" in key_info ) {
            var letter = key_info["altgr"];
            if( letter in NEED_ALTGR ) {
                console.log("Already in NEED_ALTGR", letter);
            } else {
                NEED_ALTGR.push(letter);
            }
            var pos = letter.charCodeAt(0);
            if( pos < 128 ) {
                if( charas[pos] == null ) {
                    asciis[pos] = keycode;
                    charas[pos] = letter;
                }
            } else {
                if( !(letter in HIGHER_ASCII) ) {
                    HIGHER_ASCII[letter] = keycode;
                }
            }
        }
    });

    return LayoutData(
        asciis,
        charas,
        NEED_ALTGR,
        HIGHER_ASCII,
        KEYCODES
    );
}

function output_layout_file(layout_data, platform, lang) {
    var class_name = "KeyboardLayout" + toTitle(platform) + toTitle(lang);
    var output_file_data = (
        COMMON_HEADER_COPYRIGHT
        + "from keyboard_layout import KeyboardLayoutBase\n"
        + "class KeyboardLayout(KeyboardLayoutBase):\n"
        + "    ASCII_TO_KEYCODE = (\n"
    );
    for( x = 0; x < 128; ++x ) {
        var keycode = layout_data.asciis[x];
        if( keycode == null ) keycode = 0;
        keycode = keycode.toString(16);
        while( keycode.length < 2 ) {
            keycode = "0" + keycode;
        }
        var chara = layout_data.charas[x];
        if( chara == null ) chara = "";
        output_file_data += "        b'\\x" + keycode + "'  # " + chara + "\n";
    }
    layout_data.altgr.sort();
    the_altgr = layout_data.altgr.join("")
        .replace("'", '\\\'')
        .replace("\\", '\\\\');
    output_file_data += (
        "    )\n"
        + "    NEED_ALTGR = '" + (the_altgr) + "'\n"
        + "    HIGHER_ASCII = {\n"
    );
    for( k in layout_data.high ) {
        var c = layout_data.high[k];
        output_file_data += "        '" + k + "': 0x" + c.toString(16) + ",\n";
    }
    output_file_data += "    }\n";
    return output_file_data;
}

function output_keycode_file(layout_data, platform, lang) {
    var output_file_data = (
        COMMON_HEADER_COPYRIGHT + "class Keycode:\n"
    );
    function ck(x) {
        var l = x[0];
        if( len(l) == 2 ) {
            l = l + " ";
        }
        if( len(l) > 5 ) {
            l = l.ljust(20);
        }
        return [len(l), l];
    }
    for( name in layout_data.keycodes ) {
        var keycode = layout_data.keycodes[name];
        if( keycode == null ) keycode = 0;
        keycode = keycode.toString(16);
        while( keycode.length < 2 ) {
            keycode = "0" + keycode;
        }
        output_file_data += "    " + name + " = 0x" + keycode.toString(16) + "\n";
    }
    output_file_data += `
    @classmethod
    def modifier_bit(cls, keycode):
        """Return the modifer bit to be set in an HID keycode report if this is a
        modifier key; otherwise return 0."""
        return (
            1 << (keycode - 0xE0) if cls.LEFT_CONTROL <= keycode <= cls.RIGHT_GUI else 0
        )
    `
    return output_file_data;
}

function download_layout() {
    $("#download_link").hide();

    var platform = "win";
    var url = $("#input").val();
    var lang = url.split("/").pop().replace("kbd", "");
    if( lang == "") lang = "lang";
    url = url + "/download/xml";
    console.log(url);

    $.get(url, (data) => {
        console.log(data);

        var virtual_key_defs_lang = get_vk_to_sc(data);
        var layout_data = get_layout_data(virtual_key_defs_lang);

        console.log(layout_data);

        zip_name = "keyboard_layout_" + platform.toLocaleLowerCase() + "_" + lang.toLocaleLowerCase() + ".zip";

        output_layout_name = "keyboard_layout_" + platform.toLocaleLowerCase() + "_" + lang.toLocaleLowerCase() + ".py";
        output_layout_data = output_layout_file(layout_data, platform, lang);
        // console.log(output_keycode_data);
        $("#output_layout_name").html(output_layout_name);
        $("#output_layout_data").html(output_layout_data);

        output_keycode_name = "keycode_" + platform.toLocaleLowerCase() + "_" + lang.toLocaleLowerCase() + ".py";
        output_keycode_data = output_keycode_file(layout_data, platform, lang);
        // console.log(output_keycode_data);
        $("#output_keycode_name").html(output_keycode_name);
        $("#output_keycode_data").html(output_keycode_data);

        var outputZip = new JSZip();
        outputZip.file(output_layout_name, output_layout_data);
        outputZip.file(output_keycode_name, output_keycode_data);
        outputZip.file(BASE_LAYOUT_NAME, BASE_LAYOUT_DATA);
        outputZip.file(SAMPLE_CODE_NAME, SAMPLE_CODE_DATA);
        // TODO: add keyboard_layout.py
        outputZip.generateAsync({type:"base64"}).then(function (base64) {
            zip_data = "data:application/zip;base64," + base64;
            $("#download_link a").attr("href", zip_data);
            $("#download_link a").attr("download", zip_name);
            $("#download_link").show();
            // window.location = zip_name
        }, function (err) {
            console.log(err);
        });
    }, "text");
}
