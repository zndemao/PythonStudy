import time as t


class MyTimer():
    def __init__(self):
        self.unit = ['年', '月', '日', '小时', '分钟', '秒']
        self.prompt = 'no start timer'
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        prompt = '总共运行了'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += str(result[index]) + self.unit[index]
        return prompt

    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = '请先调用stop（） 停止计时'
        print('start timer')

    # stop timer
    def stop(self):
        if not self.begin:
            print('请先调用start（） start计时')
        else:
            self.end = t.localtime()
            self.__calc()
            print('timer stop')

    # 内部方法，计算时间
    def __calc(self):
        self.lasted = []
        self.prompt = 'run time '
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]
        # 为下一轮计时初始化变量
        self.begin = 0
        self.end = 0
