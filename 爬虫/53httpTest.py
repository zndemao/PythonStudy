Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib.request
>>> response=urllib.request.urlopen('http://www.fishc.com')
>>> html =response .read()
>>> print(html)
b'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\r\n\t"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\r\n\r\n<!-- \r\n(c) 2011 \xc4\xbdubom\xc3\xadr Krupa, CC BY-ND 3.0\r\n -->\t\r\n\r\n<html xmlns="http://www.w3.org/1999/xhtml">\r\n\t<head>\r\n\t\t<meta http-equiv="content-type" content="text/html; charset=utf-8" />\r\n\t\t<link rel="stylesheet" type="text/css" href="lib/style.css"/>\r\n\t\t<script type="text/javascript" src="lib/jquery-1.6.1.min.js"></script>\r\n\t\t<script type="text/javascript" src="lib/jquery.animation.easing.js"></script>\r\n\t\t<script type="text/javascript" src="lib/jquery.mousewheel.min.js"></script>\r\n\t\t<script type="text/javascript" src="source.js"></script>\r\n\t\t<script type="text/javascript" src="lib/script.js"></script>\r\n\t\t\r\n\t\t<title>\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4-\xe5\x85\x8d\xe8\xb4\xb9\xe7\xbc\x96\xe7\xa8\x8b\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6|\xe7\xbc\x96\xe7\xa8\x8b\xe6\x8a\x80\xe6\x9c\xaf\xe4\xba\xa4\xe6\xb5\x81|C\xe8\xaf\xad\xe8\xa8\x80\xe6\x95\x99\xe5\xad\xa6|\xe6\xb1\x87\xe7\xbc\x96\xe6\x95\x99\xe5\xad\xa6|win32\xe6\x95\x99\xe5\xad\xa6|Delphi\xe6\x95\x99\xe5\xad\xa6|\xe5\x8a\xa0\xe5\xaf\x86\xe4\xb8\x8e\xe8\xa7\xa3\xe5\xaf\x86|Linux\xe6\x95\x99\xe5\xad\xa6</title>\r\n\t\t<meta name="keywords" content="\xe7\xbc\x96\xe7\xa8\x8b\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6|C\xe8\xaf\xad\xe8\xa8\x80\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6|\xe6\xb1\x87\xe7\xbc\x96\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6|Win32\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6|Delphi\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6|Linux\xe6\x95\x99\xe5\xad\xa6|\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\x8f\x8a\xe5\xae\x89\xe5\x85\xa8\xe6\x9e\xb6\xe6\x9e\x84\xe6\x95\x99\xe5\xad\xa6" />\r\n\t\t<meta name="description" content="\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4\xe8\x87\xb4\xe5\x8a\x9b\xe4\xba\x8e\xe5\xae\x8c\xe5\x85\xa8\xe5\x85\x8d\xe8\xb4\xb9\xe7\xbc\x96\xe7\xa8\x8b\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6,\xe4\xb8\xbb\xe8\xa6\x81\xe6\xb6\x89\xe5\x8f\x8a\xe7\x9a\x84\xe5\x86\x85\xe5\xae\xb9\xe6\x9c\x89C\xe8\xaf\xad\xe8\xa8\x80\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6,\xe6\xb1\x87\xe7\xbc\x96\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6,Win32\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6,Delphi\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6,Linux\xe6\x95\x99\xe5\xad\xa6,\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\x8f\x8a\xe5\xae\x89\xe5\x85\xa8\xe6\x9e\xb6\xe6\x9e\x84\xe6\x95\x99\xe5\xad\xa6" />\r\n\t</head>\r\n\t<body>\r\n\t\t<div id="place">\r\n\t\t\t<div id="name1"></div>\r\n\t\t\t<div id="wrapper1">\r\n\t\t\t\t<div id="weather"><iframe src="http://www.thinkpage.cn/weather/weather.aspx?uid=&cid=101010100&l=zh-CHS&p=CMA&a=1&u=C&s=3&m=0&x=1&d=0&fc=FFFFFF&bgc=&bc=&ti=1&in=1&li=2&ct=iframe" frameborder="0" scrolling="no" width="215" height="113" allowTransparency="true"></iframe></div>\r\n\t\t\t    <div id="thumb1-2"></div>\r\n\t\t        <div id="thumb1-3"></div>\r\n\t\t\t\t<div id="thumb1-4"></div>\r\n\t\t\t\t<div id="thumb1-5"></div>\r\n\t\t\t\t<div id="thumb1-6"></div>\r\n\t\t\t\t<div id="thumb1-7"></div>\r\n\t\t\t\t<div id="thumb1-8"></div>\r\n\t\t\t\t<div id="thumb1-9"></div>\r\n\t\t\t\t<div id="thumb1-10"></div>\r\n\t\t\t\t<div id="thumb1-11"></div>\r\n\t\t\t\t<div id="thumb1-12"></div>\r\n\t\t\t\r\n\t\t\t\t<form action="" method="get" target="_blank">\r\n\t\t\t\t\t<input type="text" name="q" value="" /><button type="submit"></button>\r\n\t\t\t\t\t<div id="engines1">\r\n\t\t\t\t\t\t<div id="google1"></div>\r\n\t\t\t\t\t\t<div id="bing1"></div>\r\n\t\t\t\t\t\t<div id="yahoo1"></div>\r\n\t\t\t\t\t\t<div id="wikipedia1"></div>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<div id="search-engine1"></div>\r\n\t\t\t\t</form>\r\n\t\t\t</div><!-- end wrapper1 -->\r\n\t\t\t<div id="button1to2"></div>\r\n\t\t\t<div id="button2to1"></div>\r\n\t\t\t<div id="name2"></div>\r\n\t\t\t<div id="wrapper2">\r\n\t\t\t\t<div id="thumb2-1"></div>\r\n\t\t\t\t<div id="thumb2-2"></div>\r\n\t\t\t\t<div id="thumb2-3"></div>\r\n\t\t\t\t<div id="thumb2-4"></div>\r\n\t\t\t\t<div id="thumb2-5"></div>\r\n\t\t\t\t<div id="thumb2-6"></div>\r\n\t\t\t\t<div id="thumb2-7"></div>\r\n\t\t\t\t<div id="thumb2-8"></div>\r\n\t\t\t\t<div id="thumb2-9"></div>\r\n\t\t\t\t<div id="thumb2-10"></div>\r\n\t\t\t\t<div id="thumb2-11"></div>\r\n\t\t\t\t<div id="thumb2-12"></div>\r\n\t\t\t\r\n\t\t\t\t<form action="" method="get">\r\n\t\t\t\t\t<input type="text" name="q" value="" placeholder="" /><button type="submit"></button>\r\n\t\t\t\t\t<div id="engines2">\r\n\t\t\t\t\t\t<div id="google2"></div>\r\n\t\t\t\t\t\t<div id="bing2"></div>\r\n\t\t\t\t\t\t<div id="yahoo2"></div>\r\n\t\t\t\t\t\t<div id="wikipedia2"></div>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<div id="search-engine2"></div>\r\n\t\t\t\t</form>\r\n\t\t\t</div><!-- end wrapper2 -->\r\n\t\t\t<div id="button2to3"></div>\r\n\t\t\t<div id="button3to2"></div>\r\n\t\t\t<div id="name3"></div>\r\n\t\t\t<div id="wrapper3">\r\n\t\t\t\t<div id="thumb3-1"></div>\r\n\t\t\t\t<div id="thumb3-2"></div>\r\n\t\t\t\t<div id="thumb3-3"></div>\r\n\t\t\t\t<div id="thumb3-4"></div>\r\n\t\t\t\t<div id="thumb3-5"></div>\r\n\t\t\t\t<div id="thumb3-6"></div>\r\n\t\t\t\t<div id="thumb3-7"></div>\r\n\t\t\t\t<div id="thumb3-8"></div>\r\n\t\t\t\t<div id="thumb3-9"></div>\r\n\t\t\t\t<div id="thumb3-10"></div>\r\n\t\t\t\t<div id="thumb3-11"></div>\r\n\t\t\t\t<div id="thumb3-12"></div>\r\n\t\t\t\r\n\t\t\t\t<form action="" method="get">\r\n\t\t\t\t\t<input type="text" name="q" value="" placeholder="" /><button type="submit"></button>\r\n\t\t\t\t\t<div id="engines3">\r\n\t\t\t\t\t\t<div id="google3"></div>\r\n\t\t\t\t\t\t<div id="bing3"></div>\r\n\t\t\t\t\t\t<div id="yahoo3"></div>\r\n\t\t\t\t\t\t<div id="wikipedia3"></div>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<div id="search-engine3"></div>\r\n\t\t\t\t</form>\r\n\t\t\t</div><!-- end wrapper3 -->\r\n\t\t</div><!-- end place -->\r\n\t\t<div style="display:none">        \r\n    \t\t\t<script type="text/javascript">\r\nvar _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");\r\ndocument.write(unescape("%3Cscript src=\'" + _bdhmProtocol + "hm.baidu.com/h.js%3F49739b392c8b45caf83863be633c629f\' type=\'text/javascript\'%3E%3C/script%3E"));\r\n    \t\t\t</script>\r\n\t\t</div>\r\n\t</body>\r\n</html>\r\n'
>>> html=html.decode('utf-8')
>>> print(html)
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<!-- 
(c) 2011 Ľubomír Krupa, CC BY-ND 3.0
 -->	

<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<link rel="stylesheet" type="text/css" href="lib/style.css"/>
		<script type="text/javascript" src="lib/jquery-1.6.1.min.js"></script>
		<script type="text/javascript" src="lib/jquery.animation.easing.js"></script>
		<script type="text/javascript" src="lib/jquery.mousewheel.min.js"></script>
		<script type="text/javascript" src="source.js"></script>
		<script type="text/javascript" src="lib/script.js"></script>
		
		<title>鱼C工作室-免费编程视频教学|编程技术交流|C语言教学|汇编教学|win32教学|Delphi教学|加密与解密|Linux教学</title>
		<meta name="keywords" content="编程视频教学|C语言视频教学|汇编视频教学|Win32视频教学|Delphi视频教学|Linux教学|服务器及安全架构教学" />
		<meta name="description" content="鱼C工作室致力于完全免费编程视频教学,主要涉及的内容有C语言视频教学,汇编视频教学,Win32视频教学,Delphi视频教学,Linux教学,服务器及安全架构教学" />
	</head>
	<body>
		<div id="place">
			<div id="name1"></div>
			<div id="wrapper1">
				<div id="weather"><iframe src="http://www.thinkpage.cn/weather/weather.aspx?uid=&cid=101010100&l=zh-CHS&p=CMA&a=1&u=C&s=3&m=0&x=1&d=0&fc=FFFFFF&bgc=&bc=&ti=1&in=1&li=2&ct=iframe" frameborder="0" scrolling="no" width="215" height="113" allowTransparency="true"></iframe></div>
			    <div id="thumb1-2"></div>
		        <div id="thumb1-3"></div>
				<div id="thumb1-4"></div>
				<div id="thumb1-5"></div>
				<div id="thumb1-6"></div>
				<div id="thumb1-7"></div>
				<div id="thumb1-8"></div>
				<div id="thumb1-9"></div>
				<div id="thumb1-10"></div>
				<div id="thumb1-11"></div>
				<div id="thumb1-12"></div>
			
				<form action="" method="get" target="_blank">
					<input type="text" name="q" value="" /><button type="submit"></button>
					<div id="engines1">
						<div id="google1"></div>
						<div id="bing1"></div>
						<div id="yahoo1"></div>
						<div id="wikipedia1"></div>
					</div>
					<div id="search-engine1"></div>
				</form>
			</div><!-- end wrapper1 -->
			<div id="button1to2"></div>
			<div id="button2to1"></div>
			<div id="name2"></div>
			<div id="wrapper2">
				<div id="thumb2-1"></div>
				<div id="thumb2-2"></div>
				<div id="thumb2-3"></div>
				<div id="thumb2-4"></div>
				<div id="thumb2-5"></div>
				<div id="thumb2-6"></div>
				<div id="thumb2-7"></div>
				<div id="thumb2-8"></div>
				<div id="thumb2-9"></div>
				<div id="thumb2-10"></div>
				<div id="thumb2-11"></div>
				<div id="thumb2-12"></div>
			
				<form action="" method="get">
					<input type="text" name="q" value="" placeholder="" /><button type="submit"></button>
					<div id="engines2">
						<div id="google2"></div>
						<div id="bing2"></div>
						<div id="yahoo2"></div>
						<div id="wikipedia2"></div>
					</div>
					<div id="search-engine2"></div>
				</form>
			</div><!-- end wrapper2 -->
			<div id="button2to3"></div>
			<div id="button3to2"></div>
			<div id="name3"></div>
			<div id="wrapper3">
				<div id="thumb3-1"></div>
				<div id="thumb3-2"></div>
				<div id="thumb3-3"></div>
				<div id="thumb3-4"></div>
				<div id="thumb3-5"></div>
				<div id="thumb3-6"></div>
				<div id="thumb3-7"></div>
				<div id="thumb3-8"></div>
				<div id="thumb3-9"></div>
				<div id="thumb3-10"></div>
				<div id="thumb3-11"></div>
				<div id="thumb3-12"></div>
			
				<form action="" method="get">
					<input type="text" name="q" value="" placeholder="" /><button type="submit"></button>
					<div id="engines3">
						<div id="google3"></div>
						<div id="bing3"></div>
						<div id="yahoo3"></div>
						<div id="wikipedia3"></div>
					</div>
					<div id="search-engine3"></div>
				</form>
			</div><!-- end wrapper3 -->
		</div><!-- end place -->
		<div style="display:none">        
    			<script type="text/javascript">
var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3F49739b392c8b45caf83863be633c629f' type='text/javascript'%3E%3C/script%3E"));
    			</script>
		</div>
	</body>
</html>

>>> 
