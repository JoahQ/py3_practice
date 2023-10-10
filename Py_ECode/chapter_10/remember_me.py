import json
"""
# 如果以前存储了用户名，就加载它。
# 否则，提示用户输入用户名并存储它。
"""
def get_stored_username():
    filename = 'user_name.json'
    try:
        with open(filename) as f:
            user_name = json.load(f)
    except FileNotFoundError:
       return None
    else:
        return user_name

def get_new_username():
    user_name = input("What is your name? ")
    filename = 'user_name.json'
    with open(filename, 'w') as f:
        json.dump(user_name, f)
    return user_name


def greet_user():
    user_name = get_stored_username()
    if user_name:
        print(f"Welcome back, {user_name}!")
    else:
        user_name = get_new_username()
        print(f"We'll remember you when you com back, {user_name}!")

greet_user()