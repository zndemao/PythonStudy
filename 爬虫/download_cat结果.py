Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: E:/Users/zxl96/Documents/python/爬虫/download_cat.py ========
>>> response.geturl()
'http://placekitten.com.s3.amazonaws.com/homepage-samples/200/286.jpg'
>>> response.info()
<http.client.HTTPMessage object at 0x03DADD30>
>>> print(response.info())
x-amz-id-2: veU/fyF/LQKBvyife2EeD4kUkyVDUGmqWurm7mlfYUOcj6j8fk6dxNoc8z7zcnJGrb4+5HVb9uk=
x-amz-request-id: 7D667155C5BBD758
Date: Thu, 13 Apr 2017 00:27:28 GMT
Last-Modified: Mon, 28 Feb 2011 23:45:51 GMT
ETag: "c8e8cc83e6eeb60061ba11c9d8ba9a11"
Cache-Control: max-age=172800, public, must-revalidate
Expires: Sun, 17 Jan 2038 19:14:07 GMT
Accept-Ranges: bytes
Content-Type: image/jpeg
Content-Length: 11824
Server: AmazonS3
Connection: close


>>> response.getcode()
200
>>> 
