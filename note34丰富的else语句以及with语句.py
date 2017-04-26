Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # 丰富的else语句
>>> # if-else 要么怎样，要么不怎样
>>> # for(while)-else 干完了能怎样，不干完就别想怎样
>>> # try-else 没有问题，那就干吧
>>> def showMaxFactor(num):
	count = num // 2
	while count > 1:
		if num % count == 0:
			print('%d最大的约数是%d' % (num,count))
			break
		count -= 1
	else :
		print('%d是素数！' % num)

		
>>> num = int (input('input'))
input3
>>> showMaxFactor(num)
3是素数！
>>> showMaxFactor(2)
2是素数！
>>> showMaxFactor(4)
4最大的约数是2
>>> # 只要try语句里的内容没有异常，就执行else语句
>>> try :
	int('ab')
except ValueError as reason:
	print('error',str(reason))
else :
	print ('no error')

	
error invalid literal for int() with base 10: 'ab'
>>> try :
	int(1)
except ValueError as reason:
	print('error',str(reason))
else :
	print ('no error')

	
1
no error
>>> # with 语句,文件操作，抽象出文件操作中try 等细节，
>>> # 使用with大大减少代码量
>>> import os
>>> os.getcwd()
'E:\\Users\\zxl96\\AppData\\Local\\Programs\\Python\\Python36-32'
>>> os.chdir ('F:\\A')
>>> os.getcwd()
'F:\\A'

	
error 
>>> try :
	f= open('data.txt','w')
	for each in f:
		print(each)
except OSError as reason :
	print('error ')
finally :
	f.close()

	
error 
>>> # 改为 with 形式
>>> try :
	with open('data.txt','w') as f:
		for each in f:
			print(each)
except OSError as reason :
	print('error ',str(reason))

	
error  not readable
>>> 
