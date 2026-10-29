import json
from inputs import get_amount
def calculator():

    assets = get_assets()

    show_assets(assets)
    
    json_text = json.dumps(assets, ensure_ascii=False, indent=4)

    with open("assets.json", "w", encoding="utf-8") as file:
        file.write(json_text)

def load_assets():
    with open("assets.json", "r", encoding="utf-8") as file:
        return json.load(file)

def show_assets(assets):
    total_assets = sum(assets.values())  
    if total_assets == 0:
         print("总资产为0,无法计算占比。") 
    else:
        for key, value in assets.items():
            percentage = (value / total_assets) * 100
            print(f"{key}: {value:.2f}元 -- {percentage:.2f}%")
    print(f"Total Assets: {total_assets:.2f}元") 

def view_assets():
        try:
            assets = load_assets()
            show_assets(assets)
        except FileNotFoundError:
            print("还没有保存的资产,请先选择1输入并保存")
        except json.JSONDecodeError:
            print("资产文件格式有误,暂时无法读取")

def get_assets():
        cash = get_amount("输入现金账户: ")
        bank = get_amount("输入银行账户: ")
        long_term_investment = get_amount("输入长期投资: ")
        trading_account = get_amount("输入交易账户: ")
    
        assets = {
        "现金": cash,
        "银行": bank,
        "长期投资": long_term_investment,
        "交易账户": trading_account
        }

        return assets