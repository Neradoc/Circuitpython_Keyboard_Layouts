<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$source_url = "";
$platform = "win";
$lang = "";
$target = "";
$debug = false;

if( isset($_GET["debug"]) ) {
	$debug = true;
}
if( isset($_GET["url"]) ) {
	$source_url = $_GET["url"];
}
if( isset($_GET["platform"]) ) {
	$platform = $_GET["platform"];
}
if( isset($_GET["lang"]) ) {
	$lang = $_GET["lang"];
}
if( isset($_GET["cpversion"]) ) {
	$cpversion = $_GET["cpversion"];
}

$LANG_NAMES = [
	// "gr": "de",
];

$VERSION0 = '__version__ = "0.0.0-auto.0"';
$VERSION = '__version__ = "0.0.1-alpha.0"';

if( preg_match(",^https://kbdlayout.info/kbd([a-zA-Z0-9_-]+)$,", $source_url, $m) ) {
	$filepath_xml = "data/kbdlaytout-info-" . $m[1] . ".xml";
	$fileurl = $source_url . "/download/xml";

	if( $lang == "") {
		if( isset($LANG_NAMES[$m[1]]) ) {
			$lan = $LANG_NAMES[$m[1]];
		} else {
			$lang = $m[1];
		}
	}

	$data = file_get_contents($fileurl);
	if( strlen($data) > 1000000 ) {
		die("source URL file too big");
	}
	file_put_contents($filepath_xml, $data);

} else {
	# other platforms or sources
	die("bad input data");
}

$layout_out = array();
exec("python3 -m generator -k ".$filepath_xml." -v layout", $layout_out, $result_code);
$layout = join("\n", $layout_out);
if($result_code != 0) { print("Error Layout\n"); }

$layout = preg_replace("/".preg_quote($VERSION0)."/", $VERSION, $layout);

$keycodes_out = array();
exec("python3 -m generator -k ".$filepath_xml." -v keycode", $keycodes_out, $result_code);
$keycodes = join("\n", $keycodes_out);
if($result_code != 0) { print("Error Keycodes\n"); }

$keycodes = preg_replace("/".preg_quote($VERSION0)."/", $VERSION, $keycodes);

function make_zip($layout, $keycodes, $cpversion, $platform, $lang) {
	global $debug;
	$deletes = array();

	if( $cpversion == "6" ) {
		$filepath_zip = "data/layout_files_".$platform."_".$lang."-6mpy.zip";
	} elseif( $cpversion == "7" ) {
		$filepath_zip = "data/layout_files_".$platform."_".$lang."-7mpy.zip";
	} else {
		$filepath_zip = "data/layout_files_".$platform."_".$lang."-py.zip";
	}

	$zip = new ZipArchive();
	if ($zip->open($filepath_zip, ZipArchive::CREATE) !== true) {
		?><p>Cannot open <?=$filepath_zip?></p>?><?
	} else {
		ob_start();
		print("cpversion $cpversion\n");
		print("$filepath_zip\n");
		
		$layout_file = "keyboard_layout_" . $platform . "_" . $lang . ".py";
		$keycodes_file = "keycode_" . $platform . "_" . $lang . ".py";
		
		if( $cpversion == "6" || $cpversion == "7" ) {
			# layout
			$layout_name = preg_replace("/\.py$/", ".mpy", $layout_file);
			$tempfile = "data/" . uniqid() . "_" . $layout_file;
			file_put_contents($tempfile, $layout);
			exec("mpy-cross/mpy-cross.static-amd64-linux-".$cpversion." ".$tempfile, $out, $res);
			$mpyfile = preg_replace("/\.py$/", ".mpy", $tempfile);
			$zip->addFile($mpyfile, $layout_name);
			$deletes[] = $tempfile;
			$deletes[] = $mpyfile;
			# keycodes
			$keycodes_name = preg_replace("/\.py$/", ".mpy", $keycodes_file);
			$tempfile = "data/" . uniqid() . $keycodes_file;
			file_put_contents($tempfile, $keycodes);
			exec("mpy-cross/mpy-cross.static-amd64-linux-".$cpversion." ".$tempfile);
			$mpyfile = preg_replace("/\.py$/", ".mpy", $tempfile);
			$zip->addFile($mpyfile, $keycodes_name);
			$deletes[] = $tempfile;
			$deletes[] = $mpyfile;
			# layout base
			$zip->addFile("src/keyboard_layout".$cpversion.".mpy", "keyboard_layout.mpy");
		} else {
			$zip->addFromString($layout_file, $layout);
			$zip->addFromString($keycodes_file, $keycodes);
			$zip->addFile("src/keyboard_layout.py", "keyboard_layout.py");
		}

		$data = file_get_contents("src/sample_code_template.py");
		$data = preg_replace("/<platform>/", $platform, $data);
		$data = preg_replace("/<lang>/", $lang, $data);
		$zip->addFromString("sample_code.py", $data);

		$zip->close();

		if( !$debug ) {
			header('Content-Description: File Transfer');
			header('Content-Type: application/octet-stream');
			header('Content-Disposition: attachment; filename="'.basename($filepath_zip).'"');
			header('Expires: 0');
			header('Cache-Control: must-revalidate');
			header('Pragma: public');
			header('Content-Length: ' . filesize($filepath_zip));
		}
		
		if($debug) {
			print("END FLUSH\n");
			ob_end_flush();
		} else {
			ob_end_clean();
			readfile($filepath_zip);
			$deletes[] = $filepath_zip;
		}

		foreach($deletes as $file) {
			if( $debug ) {
				print("DELETE $file\n");
			}
			if( file_exists($file) ) {
				unlink($file);
			}
		}
	}
}

make_zip($layout, $keycodes, $cpversion, $platform, $lang);
