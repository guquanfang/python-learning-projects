from inputs import get_month,get_amount
from calculator import get_assets,show_assets
import json

def get_asset_snapshot():
    month = get_month()
    assets = get_assets()
    liabilities = get_amount("输入负债")

    snapshot = {
        "月份": month,
        "资产": assets,
        "负债": liabilities
    }

    return snapshot

def load_asset_history():
    try:
        with open("asset_history.json", "r", encoding = "utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_asset_history(asset_history):
    json_text = json.dumps(asset_history, ensure_ascii=False, indent=4)
    with open("asset_history.json", "w", encoding = "utf-8") as file:
        file.write(json_text)

def update_asset_history(asset_history):
    snapshot = get_asset_snapshot()
    if snapshot["月份"] in asset_history:
        key = input("输入y确认覆盖,输入其他取消\n")
        if key != "y":
            print("已取消覆盖")
            return asset_history
        else:
            asset_history[snapshot["月份"]] = snapshot
    else:
         asset_history[snapshot["月份"]] = snapshot
    save_asset_history(asset_history)
    print("资产快照已保存")
    return asset_history

def show_asset_snapshot(snapshot):
    print(f"{snapshot['月份']}")
    show_assets(snapshot["资产"])
    if "负债" in snapshot:
        net_worth = calculate_net_worth(snapshot)
        print(f"负债：{snapshot['负债']:.2f}元  净资产：{net_worth:.2f}元")
    else:
        print("未记录负债,无法计算净资产")

def show_all_asset_history(asset_history):
    if asset_history == {}:
        print("暂无资产历史记录")
        return
    else:
        for month in sorted(asset_history):
            snapshot = asset_history[month]
            show_asset_snapshot(snapshot)

def show_asset_changes(asset_history):
    if asset_history == {}:
        print("暂无资产历史记录")
        return
    else:
        previous_total = None
        for month in sorted(asset_history):
            snapshot = asset_history[month]
            current_total = sum(snapshot["资产"].values())
            if previous_total is None:
                print(f"{month}:总资产{current_total:.2f}元")
            else:
                changes_total = current_total - previous_total
                if previous_total == 0:
                    print("上一条总资产为0,无法计算变化率")
                    print(f"{month}:总资产{current_total:.2f}元--变化{changes_total:.2f}元")
                else:
                    change_rate = changes_total / previous_total * 100
                    print(f"{month}:总资产{current_total:.2f}元--变化{changes_total:.2f}元--变化率{change_rate:.2f}%")
            previous_total = current_total


def calculate_net_worth(snapshot):
    if "负债" not in snapshot:
        return None
    else:
        net_worth = sum(snapshot["资产"].values()) - snapshot["负债"]
        return net_worth
