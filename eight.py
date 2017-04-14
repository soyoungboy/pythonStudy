# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# import time
#
# print 'time.altzone = ', time.altzone  # 返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
# print 'time.asctime() = ', time.asctime()  # 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
# print 'time.clock() = ', time.clock()  # 用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
# print 'time.ctime() = ', time.ctime()  # 作用相当于asctime(localtime(secs))，未给参数相当于asctime()
# print 'time.gmtime() = ', time.gmtime()  # 接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
# print 'time.localtime() = ', time.localtime()  # 接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）
# t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
# secs = time.mktime(t)
# print 'time.mktime(time.localtime(secs)) = ', time.mktime(time.localtime(secs))  # 接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。
# time.sleep(3)  # 推迟调用线程的运行，secs指秒数。
# print 'time.strftime("%y %m %d:%H %M %S", time.gmtime(secs)) = ', time.strftime("%y %m %d:%H %M %S", time.gmtime(secs))
#
# struct_time = time.strptime("30 Nov 00", "%d %b %y")
# print "returned tuple: %s " % struct_time
# print '当前时间的时间戳 = ', time.time()  # 返回当前时间的时间戳（1970纪元后经过的浮点秒数）

# !/usr/bin/python
# -*- coding: UTF-8 -*-
import calendar

calendar.setfirstweekday(6)  # 设置每周的起始日期码。0（星期一）到6（星期日）,在显示日历之前设置比较好
print '---------calendar方法----------'
print  calendar.calendar(2017, 2, 1,
                         6)  # calendar.calendar(year,w=2,l=1,c=6)返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
print calendar.firstweekday
print 'calendar.isleap(2017) = ', calendar.isleap(2017)  # 判断2017年是否是闰年 是闰年返回True，否则为false。
print '2000年到2017年之间所有的闰年总数 = ', calendar.leapdays(2000, 2017)
print '---------2017年4月份的日历----------'
print calendar.month(2017, 4, 2, 1)
print '---------2017年5月份的列表数据----------'
print calendar.monthcalendar(2017, 5)  # 返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
print calendar.monthrange(2017, 4)  # 返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
print '---------prcal方法----------'
print calendar.prcal(2017, 2, 1, 6)  # 相当于 print calendar.calendar(year,w,l,c).
print '---------prmonth方法----------'
print calendar.prmonth(2017, 5, 2, 1)  # 相当于 print calendar.calendar（year，w，l，c）。
# print 	calendar.timegm(tupletime) #和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。没搞懂，暂时搁置
print calendar.weekday(2017, 4, 11)  # 返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
