from calculator import calculator, load_assets, show_assets
import json

def main():
    while True:    
        print("1.请输入新资产并保存")
        print("2.查看已保存资产")
        print("0.退出")
        choice = input("请选择：")
        if choice == "1":
            calculator()
        elif choice == "2":
            try:
                assets = load_assets()
                show_assets(assets)
            except FileNotFoundError:
                print("还没有保存的资产,请先选择1输入并保存")
            except json.JSONDecodeError:
                print("资产文件格式有误,暂时无法读取")
        elif choice =="0":
            print("已退出")
            break 
        else:
            print("无效选项")

        

if __name__ == "__main__":
    main()