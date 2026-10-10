# 读取一个整数，并根据判断结果输出奇偶性。
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("The number is even.")
    else:
        print("The number is odd.")
# 判断 x 是否为偶数，返回布尔值 True 或 False。
def is_even(x):
    # % 是取余运算；除以 2 的余数为 0 表示该整数是偶数。
    if x % 2 == 0:
        return True
    else:
        return False

# 调用入口函数，开始执行程序。
main()
