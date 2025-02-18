# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 13:04:38 2024

@author: Steven, Hsin
@email: steveh8758@gmail.com

"""

# -------------------------------------------
# 自動建立打卡時間。
# 1. 自動避開打卡時間個位數不為 0, 5 的時間。
# 2. 在 DATE 那邊可以以 [10, 15] 匹配 10, 11, 12, 13, 14, 15。
# 3. DATE_TEMPLATE 輸入，已修改時間串。
# 4. TOTAL_HOUR 可更改需要打多長時間。
# -------------------------------------------

# -------------------------------------------
NEED_SPLIT = True
TOTAL_HOUR = 20
DATE_TEMPLATE = r"2025/4/"
DATE = [[1,31]]
# -------------------------------------------


from random import randint as rint


def print_day_hour(lstring):
    if not hasattr(print_day_hour, "split_counter"):
        print_day_hour.split_counter = 0
    rt_minute = 0
    for s1 in [7 * 60, 14 * 60]:
        if (print_day_hour.split_counter % 15 == 0) and NEED_SPLIT:
            print()
        offset = rint(0, 120)
        hr_r = rint(220, 230)
        while (tt := (s1 + offset)) % 60 % 5 == 0:
            offset = rint(0, 120)
        print_day_hour.split_counter += 1

        offset = rint(0, 120)
        while (ttt := (s1 + offset + hr_r)) % 60 % 5 == 0:
            hr_r = rint(220, 260)
        print_day_hour.split_counter += 1

        print(f"{lstring}\t{tt//60:02}:{tt%60:02}\t{ttt//60:02}:{ttt%60:02}\t")
        rt_minute += ttt - tt
    return rt_minute


def Get_post_time_mapping():

    def inner(val):
        nonlocal total
        total += print_day_hour(f"{DATE_TEMPLATE}{val}")
        if total >= TOTAL_HOUR * 60:
            print(f"\nTotal time: {total//60} hr {total%60} min")
            return True

    total = 0
    for i in DATE:
        if isinstance(i, list):
            for j in range(i[0], i[1]+1):
                if inner(j):
                    return
        else:
            if inner(i):
                return

if __name__ == '__main__':
    Get_post_time_mapping()
