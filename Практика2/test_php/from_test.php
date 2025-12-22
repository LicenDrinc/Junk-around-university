#!/usr/bin/php
<?php
$fromDir = "/mnt/c/test/";
$out = "/mnt/c/test/out/";
$from =[
	0 => [ 
		0 => $fromDir."WindFieldkit.png",
		1 => "-typeconvert",
		2 => "ImageToImage",
		3 => $out."1.png"
	],
	1 => [
		0 => $fromDir."WindFieldkit.png",
		1 => "-typeconvert",
		2 => "ImageToImage",
		3 => "-resize",
		4 => "640x640",
		5 => $out."2.png"
	],
	2 => [
		0 => $fromDir."WindFieldkit.png",
		1 => "-typeconvert",
		2 => "ImageToImage",
		3 => "-resize",
		4 => "640x",
		5 => $out."3.png"
	],
	3 => [
		0 => $fromDir."WindFieldkit.png",
		1 => "-typeconvert",
		2 => "ImageToImage",
		3 => "-resize",
		4 => "x640",
		5 => $out."4.png"
	],
	4 => [
		0 => $fromDir."WindFieldkit.png",
		1 => "-typeconvert",
		2 => "ImageToImage",
		3 => "-resize",
		4 => "150%",
		5 => $out."5.png"
	],
	5 => [
		0 => $fromDir."WindFieldkit.png",
		1 => "-typeconvert",
		2 => "ImageToImage",
		3 => "-quality",
		4 => "100",
		5 => $out."6.jpg"
	],
	6 => [
		0 => $fromDir."WindFieldkit.png",
		1 => "-typeconvert",
		2 => "ImageToImage",
		3 => "-quality",
		4 => "50",
		5 => $out."7.jpg"
	],
	7 => [
		0 => $fromDir."WindFieldkit.png",
		1 => "-typeconvert",
		2 => "ImageToImage",
		3 => "-rotate",
		4 => "40",
		5 => $out."8.png"
	],
	8 => [
		0 => $fromDir."WindFieldkit.png",
		1 => "-typeconvert",
		2 => "ImageToImage",
		3 => "-blur",
		4 => "0x8",
		5 => $out."9.png"
	],
	9 => [
		0 => $fromDir."WindFieldkit.png",
		1 => "-typeconvert",
		2 => "ImageToImage",
		3 => "-bordercolor",
		4 => "blue",
		5 => "-border",
		6 => "16",
		7 => $out."10.png"
	],
	10 => [
		0 => $fromDir."WindFieldkit.png",
		1 => $fromDir."result.pbm",
		2 => $fromDir."ggg0.png",
		3 => "-typeconvert",
		4 => "ImageToPdf",
		5 => $out."11.pdf"
	],
	11 => [
		0 => $fromDir."pp01.png",
		1 => $fromDir."pp02.png",
		2 => $fromDir."pp03.png",
		3 => $fromDir."pp04.png",
		4 => $fromDir."pp05.png",
		5 => $fromDir."pp06.png",
		6 => "-typeconvert",
		7 => "ImageToGif",
		8 => "-delay",
		9 => "20",
		10 => "-loop",
		11 => "1",
		12 => $out."12.gif"
	],
	12 => [
		0 => $fromDir."t.docx",
		1 => "-typeconvert",
		2 => "WriterToOdt",
		3 => $out."13.odt"
	],
	13 => [
		0 => $fromDir."t.docx",
		1 => "-typeconvert",
		2 => "WriterToDoc",
		3 => $out."14.doc"
	],
	14 => [
		0 => $fromDir."t1.doc",
		1 => "-typeconvert",
		2 => "WriterToDocx",
		3 => $out."15.docx"
	],
	15 => [
		0 => $fromDir."t.docx",
		1 => "-typeconvert",
		2 => "WriterToRtf",
		3 => $out."16.rtf"
	],
	16 => [
		0 => $fromDir."t.docx",
		1 => "-typeconvert",
		2 => "WriterToHtml",
		3 => $out."17.html"
	],
	17 => [
		0 => $fromDir."t.docx",
		1 => "-typeconvert",
		2 => "WriterToPdf",
		3 => $out."18.pdf"
	],
	18 => [
		0 => $fromDir."t2.xls",
		1 => "-typeconvert",
		2 => "CalcToOds",
		3 => $out."19.ods"
	],
	19 => [
		0 => $fromDir."t3.xlsx",
		1 => "-typeconvert",
		2 => "CalcToXls",
		3 => $out."20.xls"
	],
	20 => [
		0 => $fromDir."t2.xls",
		1 => "-typeconvert",
		2 => "CalcToXlsx",
		3 => $out."21.xlsx"
	],
	21 => [
		0 => $fromDir."t2.xls",
		1 => "-typeconvert",
		2 => "CalcToCsv",
		3 => $out."22.csv"
	],
	22 => [
		0 => $fromDir."t2.xls",
		1 => "-typeconvert",
		2 => "CalcToPdf",
		3 => $out."23.pdf"
	],
	23 => [
		0 => $fromDir."t5.pptx",
		1 => "-typeconvert",
		2 => "ImpressToOdp",
		3 => $out."24.odp"
	],
	24 => [
		0 => $fromDir."t5.pptx",
		1 => "-typeconvert",
		2 => "ImpressToPpt",
		3 => $out."25.ppt"
	],
	25 => [
		0 => $fromDir."t5.pptx",
		1 => "-typeconvert",
		2 => "ImpressToPdf",
		3 => $out."26.pdf"
	]
];