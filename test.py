def discounts(price ,rate):
    final_price = price * rate
    return final_price


old_price=float(input('请输入'))
rate=float(input('请输入折扣率'))
new_price=discounts(old_price,rate)

print('打折后的价格'+ str(new_price))
print("打折后的价格",new_price)
print('这里试图打印final_price的值:',final_price)
