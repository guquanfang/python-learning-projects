def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("金额不能为负数，请重新输入。")
                continue
            else:
                return amount
        except ValueError:
            print("输入无效，请输入数字。")

def get_month():
    while True:
        month = input("请输入月份：")
        parts = month.split("-")
        if len(parts) != 2 or len(parts[0]) != 4 or len(parts[1]) != 2:
            print("月份输入有误,请重新输入")   
        elif parts[0].isdigit() == False or parts[1].isdigit() == False:
            print("月份输入有误,请重新输入")
            continue
        else:
            try:
                y = int(parts[0])
                m = int(parts[1])
            except ValueError:
                print("月份输入有误，请重新输入")
                continue
            if y > 0 and 1 <= m <=12:
                return month
            else:
                print("月份输入有误，请重新输入")
