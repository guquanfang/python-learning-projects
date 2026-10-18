def is_valid_password(password):
    #1. 长度至少 8
    if len(password) < 8:
        return False
    #2. 至少包含一个大写字母
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    #3. 至少包含一个小写字母
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    #4. 至少包含一个数字
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    #5. 密码长度不能超过 18
    if len(password) > 18:
        return False

    return has_upper and has_lower and has_digit