# 程序入口函数：调用结果展示函数，开始录入并统计学生成绩。
def main():
    show_results()

# 读取非负整数；prompt 是调用函数时传入的输入提示文字。
def get_int(prompt):
    # 持续要求输入，直到通过 return 返回有效数据。
    while True:
        try:
            # input() 返回字符串，int() 将它转换为整数。
            value = int(input(prompt))
            if value < 0:
                print("Invalid input. Please enter a non-negative integer.")
            else:
                # return 返回结果，同时结束当前函数和其中的循环。
                return value
        # 无法转换为整数时（例如输入 abc 或 2.5），捕获异常并提示重新输入。
        except ValueError:
            print("Invalid input. Please enter an integer.")

# 读取 0 到 100 之间的成绩，允许带小数。
def get_score(prompt):
    while True:
        try:
            value = float(input(prompt))
            # 0 <= value <= 100 判断是否在有效范围内；not 将真假结果反转。
            # 因此，成绩不在有效范围内时，执行下面的错误提示。
            if not 0 <= value <= 100:
                print("Invalid input. Please enter a valid score between 0 and 100.")
            else:
                return value
        # 输入无法转换为浮点数时，提示重新输入。
        except ValueError:
            print("Invalid input. Please enter a valid score.")

# 录入学生姓名和成绩，返回保存这些对应关系的字典。
def record_students():
    # {} 创建空字典；后续用姓名作为键、成绩作为值。
    scores = {}
    num_students = get_int("How many students are in the class? ")
    # range(num_students) 控制录入次数；_ 表示不需要使用本次循环的序号。
    for _ in range(num_students):
        name = input("Enter the student's name: ")
        score = get_score("Enter the student's score: ")
        # 此处 [] 根据键访问字典：添加或更新这个姓名对应的成绩。
        # 如果姓名重复，新成绩会覆盖同名学生之前的成绩。
        scores[name] = score
    return scores

# 统计总分、最高分、最低分，并为每名学生确定成绩等级。
def sum_scores():
    students_scores = record_students()
    total_score = 0
    # 有效成绩为 0 到 100：-1 低于所有有效成绩，100 是最低分的初始上限。
    highest_score = -1
    lowest_score = 100
    # [] 创建空列表，用来按顺序保存每名学生的姓名、成绩和等级。
    score_grads = []
    # items() 逐个提供字典的键和值，分别赋给 name 和 score。
    for name, score in students_scores.items():
        # += 累加成绩，相当于 total_score = total_score + score。
        total_score += score
        # 遇到更高或更低的成绩时，更新当前保存的最高分或最低分。
        if score > highest_score:
            highest_score = score
        if score < lowest_score:
            lowest_score = score
        # 从高到低判断等级；if/elif/else 只执行第一个满足条件的分支。
        if 90 <= score <= 100:
            grade = "A"
        elif 80 <= score < 90:
            grade = "B"
        elif 70 <= score < 80:
            grade = "C"
        elif 60 <= score < 70:
            grade = "D"
        else:
            grade = "F"
        # (name, score, grade) 将三个值组成一个元组，代表一条学生记录。
        # append() 将这整个元组作为一个元素，添加到列表末尾。
        score_grads.append((name, score, grade))
    # 用逗号分隔的四个返回值会组成一个元组，交给调用这个函数的代码。
    return score_grads, total_score, highest_score, lowest_score

# 显示每名学生的成绩等级，以及班级的平均分、最高分和最低分。
def show_results():
    # 将返回的四个值按顺序拆开，分别赋给左边的四个变量。
    score_grads, total_score, highest_score, lowest_score = sum_scores()
    # 空列表在条件判断中为假，not 空列表为真，表示没有录入成绩。
    if not score_grads:
        print("No student scores recorded.")
        # 提前结束函数，避免后面计算平均分时除以零。
        return
    # len() 返回列表的元素数量，即实际保存的学生记录数量。
    average_score = total_score / len(score_grads)
    # 遍历列表，将每条记录中的三个值分别赋给 name、score 和 grade。
    for name, score, grade in score_grads:
        # f 字符串将花括号中的变量值填入输出文字。
        print(f"{name}: {score} - Grade: {grade}")
    print(f"Average Score: {average_score}")
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")

# 直接运行这个文件时调用 main()；被其他文件导入时不执行此处的调用。
if __name__ == "__main__":
    main()
