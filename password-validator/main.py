from password_validator import is_valid_password

def main():
    password = input("请输入密码：")
    if is_valid_password(password):
        print("密码有效。")
    else:
        print("密码无效。")

if __name__ == "__main__":
    main()