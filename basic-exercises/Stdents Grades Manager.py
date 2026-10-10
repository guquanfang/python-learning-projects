# 用字典保存学生姓名及其成绩，姓名作为键，成绩作为值。
scores = {}

# 将输入的学生人数转换为整数，作为录入次数。
student_number = int(input("How many students are in the class? "))

# 逐个录入学生信息；_ 表示这里不需要使用循环序号。
for _ in range(student_number):
    name = input("Enter the student's name: ")
    # 用浮点数保存成绩，以支持带小数的分数。
    score = float(input("Enter the student's score: "))
    # 如果姓名重复，新的成绩会覆盖该姓名之前的成绩。
    scores[name] = score

# 初始化总分、及格人数和不及格人数。
total_score = 0
passed_students = 0
failed_students = 0

# 遍历字典中的姓名，累加成绩并统计及格情况。
for name in scores:
    score = scores[name]
    total_score += score
    # 以 60 分为及格线。
    if score >= 60:
        passed_students += 1
    else:
        failed_students += 1
    print(f"{name}: {score}")

# 按实际保存的成绩数量计算平均分，空字典时使用 0，避免除零错误。
average_score = total_score / len(scores) if scores else 0

# \n 表示换行，让各项统计结果分行显示。
print(f"Average: {average_score}\nPassed: {passed_students}\nFailed: {failed_students}")
