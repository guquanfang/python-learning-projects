# 读取用户输入的整数，并输出它的平方。
def main():
    # input() 返回字符串，int() 将其转换为整数。
    x = int(input("What's x? "))
    print("x squared is", square(x))

# 接收一个数，将它与自身相乘后返回平方值。
def square(n):
    return n * n

# 调用入口函数，开始执行程序。
main()
