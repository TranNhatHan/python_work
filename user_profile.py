def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

han = build_profile('Han', 'Tran', age=21, city='Nottingham')
print(han)