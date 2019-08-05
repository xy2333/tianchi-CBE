#encoding=utf-8

# 将train表的数据整理出四个is_morning,afternoon,night,midnight等

t1 = '2018-07-23 17:58:40' # 星期1
t2 = '2018-07-24 17:58:40' # 星期2
t3 = '2018-07-25 17:58:40' # 星期3
t4 = '2018-07-26 17:58:40' # 星期4
t5 = '2018-07-27 10:58:40' # 星期5
t6 = '2018-07-28 17:58:40' # 星期6
t7 = '2018-07-29 17:58:40' # 星期7
t8 = '2018-07-30 17:58:40' # 星期7
import time
t_1 = time.strptime(t1,"%Y-%m-%d %H:%M:%S")
t_2 = time.strptime(t2,"%Y-%m-%d %H:%M:%S")
t_3 = time.strptime(t3,"%Y-%m-%d %H:%M:%S")
t_4 = time.strptime(t4,"%Y-%m-%d %H:%M:%S")
t_5 = time.strptime(t5,"%Y-%m-%d %H:%M:%S")
t_6 = time.strptime(t6,"%Y-%m-%d %H:%M:%S")
t_7 = time.strptime(t7,"%Y-%m-%d %H:%M:%S")
t_8 = time.strptime(t8,"%Y-%m-%d %H:%M:%S")
# is weekday
# def is_weekday(dt):
#     if dt.tm_wday<5:
#         print "Weekday"
#     else:
#         print "Weekend"
# print is_weekday(t_1)
# print is_weekday(t_2)
# print is_weekday(t_3)
# print is_weekday(t_4)
# print is_weekday(t_5)

# is morning

def is_morning(dt):  # 5:00-11:00
    if 4 < dt.tm_hour and dt.tm_hour < 12:
        return 1
    else:
        return 0


def is_afternoon(dt):  # 11:00-17:00
    if 10 < dt.tm_hour and dt.tm_hour < 18:
        return 1
    else:
        return 0


def is_night(dt):  # 17:00-23:00
    if 16 < dt.tm_hour and dt.tm_hour < 24:
        return 1
    else:
        return 0


def is_midnight(dt):  # 23:00-5:00
    if dt < 5 or dt.tm_hour == 24:
        return 1
    else:
        return 0


is_morning(t_5)
print ""

