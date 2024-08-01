# 2) შექმენით ფუნქცია სახელად manual_replace, რომელიც მიიღებს სია, ჩასანაცლებელ ელემენტს და იმ ელემენტს, რომლითაც უნდა ჩანაცვლდეს. თქვენი დავალებაა, რომ დააბრუნოთ ახალი კოლექცია, სადაც გექნებათ ჩანაცვლებული ყველა ელემენტი მესამე პარამეტრით.
def manual_replaces(list, rev, add):
    result_list = []
    for element in list:
        if element == rev:
            result_list.append(add)
        else:
            result_list.append(element)
    return result_list

print(manual_replaces([10, 11, 10, 11], 10, 20))