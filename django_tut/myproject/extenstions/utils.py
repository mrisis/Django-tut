from . import jalali
from django.utils import timezone


def jalali_convertor(time):
    j_months = ['فروردین','اردیبشبهت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند',]
    time = timezone.localtime(time)
    time_to_str = '{},{},{}'.format(time.year, time.month, time.day)
    time_jalali = jalali.Gregorian(time_to_str).persian_tuple()
    time_jalali_list = list(time_jalali)

    for index, month in enumerate(j_months):
        if time_jalali_list[1] == index + 1 :
            time_jalali_list[1] = month
            break
        output = "{} {} {} time:{}:{}".format(
            time_jalali_list[2],
            time_jalali_list[1],
            time_jalali_list[0],
            time.hour,
            time.minute
        )

