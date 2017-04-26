#import TempConv

#print('32摄氏度= %.2f华氏度' % TempConv.c2f(32))
#print('99华氏度= %.2f摄氏度' % TempConv.f2c(99))

#from TempConv import c2f , f2c
#from TempConv import * # 强烈建议不要使用
import backage.TempConv as tc

print('32摄氏度= %.2f华氏度' % tc.c2f(32))
print('99华氏度= %.2f摄氏度' % tc.f2c(99))

print('__name__      ',__name__)
print('tc.__name__   ',tc.__name__)
# 搜索路径
