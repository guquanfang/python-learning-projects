from calculator import calculator, view_assets
from monthly import update_monthly_records,load_monthly_records,show_all_monthly_records,show_monthly_summary
from asset_history import load_asset_history,update_asset_history,show_all_asset_history,show_asset_changes,show_net_worth_changes
from charts import plot_net_worth_history

def main():
    monthly_records = load_monthly_records()
    asset_history = load_asset_history()
    while True:    
        print("1.请输入新资产并保存")
        print("2.查看已保存资产")
        print("3.输入并查看月度收支")
        print("4.查看全部月度收支")
        print("5.查看累计收支汇总")
        print("6.记录月度资产快照")
        print("7.查看历史资产")
        print("8.查看资产变化")
        print("9.查看净资产变化")
        print("10.查看净资产折线图")
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
        elif choice == "6":
            asset_history = update_asset_history(asset_history)
        elif choice == "7":
            show_all_asset_history(asset_history)
        elif choice == "8":
            show_asset_changes(asset_history)
        elif choice == "9":
            show_net_worth_changes(asset_history)
        elif choice == "10":
            plot_net_worth_history(asset_history)
        elif choice =="0":
            print("已退出")
            break 
        else:
            print("无效选项")

        

if __name__ == "__main__":
    main()