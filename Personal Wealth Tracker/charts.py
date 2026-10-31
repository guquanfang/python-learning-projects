import matplotlib.pyplot as plt
from asset_history import prepare_net_worth_data

plt.rcParams["font.family"] = "Microsoft YaHei"

def plot_net_worth_history(asset_history):
    if asset_history == {}:
        print("暂无资产历史记录")
        return
    else:
        data = prepare_net_worth_data(asset_history)
        month = data["月份"]
        net_worth = data["净资产"]
        plt.figure()
        plt.plot(month, net_worth, marker="o")
        plt.title("净资产历史")
        plt.xlabel("月份")
        plt.ylabel("净资产(CNY)")
        plt.show()
