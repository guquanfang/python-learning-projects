from calculator import calculator, view_assets
from monthly import update_monthly_records,load_monthly_records,show_all_monthly_records,show_monthly_summary

def main():
    monthly_records = load_monthly_records()
    while True:    
        print("1.请输入新资产并保存")
        print("2.查看已保存资产")
        print("3.输入并查看月度收支")
        print("4.查看全部月度收支")
        print("5.查看累计收支汇总")
        print("0.退出")
        choice = input("请选择：")
        if choice == "1":
            calculator()
        elif choice == "2":
           view_assets()
        elif choice == "3":
            monthly_records = update_monthly_records(monthly_records)
        elif choice == "4":
            show_all_monthly_records(monthly_records)
        elif choice == "5":
            show_monthly_summary(monthly_records)
        elif choice =="0":
            print("已退出")
            break 
        else:
            print("无效选项")

        

if __name__ == "__main__":
    main()