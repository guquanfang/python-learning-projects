from inputs import get_amount,get_month
import json

def get_monthly_record():
    month = get_month()
    income = get_amount("输入本月收入：")
    expense = get_amount("输入本月支出：")
    record = {
              "月份":month,
              "收入":income,
              "支出":expense
             }
    return record

def show_monthly_record(record):
    balance = record["收入"] - record["支出"]
    print(f'月份：{record["月份"]}')
    print(f'收入:{record["收入"]:.2f}元')
    print(f'支出：{record["支出"]:.2f}元')
    print(f"结余：{balance:.2f}元")
    if record["收入"] == 0:
        print("收入为0,无法计算储蓄率")
    else:
        savings_rate = balance/record["收入"]*100
        print(f"储蓄率为：{savings_rate:.2f}%")

def update_monthly_records(monthly_records):
    record = get_monthly_record()
    if record["月份"] in monthly_records:
        key = input("输入y确认覆盖,其他输入取消\n")
        if key != "y":
            print("已取消覆盖")
            return monthly_records
        else:
            monthly_records[record["月份"]] = record           
    else:    
        monthly_records[record["月份"]] = record
    save_monthly_records(monthly_records)
    show_monthly_record(record)
    return monthly_records 

def load_monthly_records():
    try:
        with open("monthly_records.json", "r", encoding = "utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_monthly_records(monthly_records):  
    json_text = json.dumps(monthly_records, ensure_ascii=False, indent=4)
    with open("monthly_records.json", "w", encoding = "utf-8") as file:
        file.write(json_text)


def show_all_monthly_records(monthly_records):
    if monthly_records == {}:
        print("暂无月度收支记录")
        return
    else:
        for month in sorted(monthly_records):
            record = monthly_records[month]
            show_monthly_record(record)
 

def show_monthly_summary(monthly_records):
    if monthly_records == {}:
        print("无月度收支记录")
        return
    else:
        total_income = 0
        total_expense = 0
    for record in monthly_records.values():
        total_income += record["收入"]
        total_expense += record["支出"]
    total_balance = total_income - total_expense
    print(f"累计收入：{total_income:.2f}元")
    print(f"累计支出：{total_expense:.2f}元")
    print(f"累计结余：{total_balance:.2f}元")
        