def time_for_milk_and_cookies(dt):
    if dt.day == 24 and dt.month == 12:
        return True
    return False 

print(time_for_milk_and_cookies())