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
