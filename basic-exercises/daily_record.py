# 程序入口：先录入当天完成的任务，再汇总任务耗时。
def main():
    tasks = tasks_record()
    tasks_sum(tasks)

# 录入任务信息，并返回包含所有任务的列表。
def tasks_record():

    # 每个列表元素都是一个保存任务名称和耗时的字典。
    tasks = []

    tasks_number = int(input("How many tasks have you completed today? "))

    # 根据输入的任务数量，逐个读取名称和耗时。
    for _ in range(tasks_number):

        task_name = input("Enter the task name: ")
        # 耗时以小时为单位，使用浮点数以支持小数。
        task_time = float(input("Enter the time spent on the task (in hours): "))

        # 将一个任务的相关信息放在同一个字典中。
        task = {
            "name":task_name ,
            "time":task_time
        }

        # 把当前任务加入列表，保留之前录入的任务。
        tasks.append(task)

    # 将录入结果交给调用此函数的代码。
    return tasks

# 输出每个任务的耗时，并统计总耗时及耗时最长的任务。
def tasks_sum(tasks):

    # 初始化统计值，后续在遍历任务时更新。
    total_time = 0
    longest_task = ""
    longest_time = 0

    for index, task in enumerate(tasks):

        # 读取当前任务的字段，并累加到总耗时中。
        task_time = task["time"]
        task_name = task["name"]
        total_time += task_time

        # 遇到耗时更长的任务时，同时更新最长耗时和任务名称。
        # 耗时相同时不更新，因此保留此前记录的任务。
        if index == 0 or task_time > longest_time:
            longest_time = task_time
            longest_task = task_name

        print(f"{task_name}: {task_time} hours")


    # 遍历结束后，输出最终统计结果。
    print(f"Total time spent on tasks: {total_time} hours")
    if tasks:
        print(f"Longest task: {longest_task} ({longest_time} hours)")
    else:
        print("No tasks recorded.")


# 调用入口函数，开始执行程序。
main()
