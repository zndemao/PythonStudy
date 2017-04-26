Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # URLError
>>> import urllib.request
>>> import urllib.error
>>> req=urllib.request.Request('http://www.zn.com')
>>> try:
	urllib.request.urlopen(req)
except urllib.error.URLError as e:
	print(e)

	
<http.client.HTTPResponse object at 0x038E80D0>
>>> req=urllib.request.Request('http://www.ooxx-fishc.com')
>>> try:
	urllib.request.urlopen(req)
except urllib.error.URLError as e:
	print(e.reason)

	
[Errno 11001] getaddrinfo failed
>>> # HttpError
>>> req=urllib.request.Request('http://www.ooxx-fishc.com/ooxx.html')
>>> try:
	urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
	print(e.reason)

	
Traceback (most recent call last):
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1318, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1239, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1285, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1234, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1026, in _send_output
    self.send(msg)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 964, in send
    self.connect()
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 936, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\socket.py", line 704, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\socket.py", line 743, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    urllib.request.urlopen(req)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 526, in open
    response = self._open(req, data)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 544, in _open
    '_open', req)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 504, in _call_chain
    result = func(*args)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1346, in http_open
    return self.do_open(http.client.HTTPConnection, req)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1320, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>
>>> try:
	urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
	print(e.code)
	print(e.read())

	
Traceback (most recent call last):
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1318, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1239, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1285, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1234, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1026, in _send_output
    self.send(msg)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 964, in send
    self.connect()
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 936, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\socket.py", line 704, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\socket.py", line 743, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#18>", line 2, in <module>
    urllib.request.urlopen(req)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 526, in open
    response = self._open(req, data)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 544, in _open
    '_open', req)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 504, in _call_chain
    result = func(*args)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1346, in http_open
    return self.do_open(http.client.HTTPConnection, req)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1320, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>
>>> req=urllib.request.Request('http://www.ooxx-fishc.com/ooxx.html')
>>> try:
	urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
	print(e.code)
	print(e.read())

	
Traceback (most recent call last):
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1318, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1239, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1285, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1234, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1026, in _send_output
    self.send(msg)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 964, in send
    self.connect()
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 936, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\socket.py", line 704, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\socket.py", line 743, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#21>", line 2, in <module>
    urllib.request.urlopen(req)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 526, in open
    response = self._open(req, data)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 544, in _open
    '_open', req)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 504, in _call_chain
    result = func(*args)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1346, in http_open
    return self.do_open(http.client.HTTPConnection, req)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1320, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>
>>> req=urllib.request.Request('http://www.google.com')
>>> try:
	urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
	print(e.code)
	print(e.read())

	
Traceback (most recent call last):
  File "<pyshell#24>", line 2, in <module>
    urllib.request.urlopen(req)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 526, in open
    response = self._open(req, data)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 544, in _open
    '_open', req)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 504, in _call_chain
    result = func(*args)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1346, in http_open
    return self.do_open(http.client.HTTPConnection, req)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1321, in do_open
    r = h.getresponse()
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1331, in getresponse
    response.begin()
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 297, in begin
    version, status, reason = self._read_status()
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 258, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\socket.py", line 586, in readinto
    return self._sock.recv_into(b)
ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
>>> 
