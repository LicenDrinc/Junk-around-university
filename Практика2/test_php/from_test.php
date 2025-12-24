#!/usr/bin/php
<?php
$fromDir = "/mnt/c/test/";
$out = "/mnt/c/test/out/";
$from = array(
	array($fromDir."WindFieldkit.png", "-typeconvert", "ImageToImage", $out."ImageToImage.png"),
	array($fromDir."WindFieldkit.png", "-typeconvert", "ImageToImage", "-resize", "640x640", $out."resize-640x640.png"),
	array($fromDir."WindFieldkit.png", "-typeconvert", "ImageToImage", "-resize", "640x", $out."resize-640x.png"),
	array($fromDir."WindFieldkit.png", "-typeconvert", "ImageToImage", "-resize", "x640", $out."resize-x640.png"),
	array($fromDir."WindFieldkit.png", "-typeconvert", "ImageToImage", "-resize", "150%", $out."resize-150.png"),
	array($fromDir."WindFieldkit.png", "-typeconvert", "ImageToImage", "-quality", "100", $out."quality-100.jpg"),
	array($fromDir."WindFieldkit.png", "-typeconvert", "ImageToImage", "-quality", "50", $out."quality-50.jpg"),
	array($fromDir."WindFieldkit.png", "-typeconvert", "ImageToImage", "-rotate", "40", $out."rotate-40.png"),
	array($fromDir."WindFieldkit.png", "-typeconvert", "ImageToImage", "-blur", "0x8", $out."blur-0x8.png"),
	array($fromDir."WindFieldkit.png", "-typeconvert", "ImageToImage", "-bordercolor", "blue", "-border", "16", $out."bordercolor-blue-border-16.png"),

	array($fromDir."WindFieldkit.png", $fromDir."result.pbm", $fromDir."ggg0.png", "-typeconvert", "ImageToPdf", $out."ImageToPdf.pdf"),

	array($fromDir."pp01.png", $fromDir."pp02.png", $fromDir."pp03.png", $fromDir."pp04.png", $fromDir."pp05.png", $fromDir."pp06.png", 
		"-typeconvert", "ImageToGif", "-delay", "20", "-loop", "0", $out."ImageToGif.gif"),

	array($fromDir."t.docx", "-typeconvert", "WriterToOdt", $out."WriterToOdt.odt"),
	array($fromDir."t.docx", "-typeconvert", "WriterToDoc", $out."WriterToDoc.doc"),
	array($fromDir."t1.doc", "-typeconvert", "WriterToDocx", $out."WriterToDocx.docx"),
	array($fromDir."t.docx", "-typeconvert", "WriterToRtf", $out."WriterToRtf.rtf"),
	array($fromDir."t.docx", "-typeconvert", "WriterToHtml", $out."WriterToHtml.html"),
	array($fromDir."t.docx", "-typeconvert", "WriterToPdf", $out."WriterToPdf.pdf"),

	array($fromDir."t2.xls", "-typeconvert", "CalcToOds", $out."CalcToOds.ods"),
	array($fromDir."t3.xlsx", "-typeconvert", "CalcToXls", $out."CalcToXls.xls"),
	array($fromDir."t2.xls", "-typeconvert", "CalcToXlsx", $out."CalcToXlsx.xlsx"),
	array($fromDir."t2.xls", "-typeconvert", "CalcToCsv", $out."CalcToCsv.csv"),
	array($fromDir."t2.xls", "-typeconvert", "CalcToPdf", $out."CalcToPdf.pdf"),
	
	array($fromDir."t5.pptx", "-typeconvert", "ImpressToOdp", $out."ImpressToOdp.odp"),
	array($fromDir."t5.pptx", "-typeconvert", "ImpressToPpt", $out."ImpressToPpt.ppt"),
	array($fromDir."t5.pptx", "-typeconvert", "ImpressToPdf", $out."ImpressToPdf.pdf")
);
