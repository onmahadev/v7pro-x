#!/usr/local/bin/python3
# from crontab import CronTab
#import time
# from ast import If
# from dataclasses import dataclass
# import datetime
# import subprocess
from operator import itemgetter, attrgetter, methodcaller
from time import time
from icecream import ic
# import mysql.connector
# from mysql.connector import Error
import dbmod as dm

print("v7 c0rE job!")
start_time = time()


# artist = Artist.get(Artist.artist_id == 1)
# attget = dm.att.get(dm.att.id == 19)
query = dm.att.select()
# print(query)
att_selected = query.dicts().execute()
#print(att_selected)

# for att in att_selected:
#     print('att: ', att)

# ic(dm.clear_op())
# ic(dm.set_nop(22))
# ic(dm.get_min_w_s1())
# asd=dm.get_min_w_s1()
# ssd=dm.get_id_w_min_s1()

# s1 = dm.get_id_min_w_s1(exclude_id=22)
s1 = dm.get_id_min_w_s1()
s2 = dm.get_id_min_w_s2()
s3 = dm.get_id_min_w_s3()


ic('####################################################')
# ic(d[1]['id'])
# ic((asd))
# print(asd[1]['id'])
ic(s1)
ic(s2)
ic(s3)


# zzz=dm.get_tst_s2()
ic('####################################################')


sel_op_id = dm.sel_op_id(s1, s2, s3)

if(sel_op_id is None):
    sel_op_id = 999

s1nop = dm.get_id_min_w_s1()
s2nop = dm.get_id_min_w_s2()
s3nop = dm.get_id_min_w_s3()
ic(s1nop)
ic(s2nop)
ic(s3nop)
sel_nop_id = dm.sel_nop_id(s1nop, s2nop, s3nop)

ic(sel_op_id)
ic(sel_nop_id)

# print("Minimum===: "); print(min(dic.values()))
# max_value = min(dic.values())
# z = {key:value for key, value in dic.items() if value == max_value}
# ic(max_value)
# ic(z)

# dm.tezto([1,2,3,4,5])
# cron=CronTab(user="cc")
# job1=cron.new(command="python3.10 timer1.py")
# job1.minute.every(2)
# job2=cron.new(command="python3.10 timer2.py")
# job2.minute.every(1)
# cron.write()

# SELECT id, doublesum, place FROM `v7now` ORDER BY `doublesum` DESC, `id` ASC;
#UPDATE v7now SET place = place+1 ORDER BY `doublesum` DESC, `id` ASC;
#SELECT id, doublesum, place FROM `v7now` ORDER BY `doublesum` DESC, `id` ASC;;


###UPDATE v7now SET place = place+1 ORDER BY `doublesum` DESC, `id` ASC;
####SELECT id, doublesum, place FROM `v7now` ORDER BY `doublesum` DESC, `id` ASC;;
###SET @n_place := 1;
###UPDATE `v7now` SET `place` = @n_place := @n_place + 1 ORDER BY `doublesum` DESC, `id` ASC;
###

# student_tuples = [
#         ('буба', 1, 222),
#         ('женя', 6, 108),
#         ('мира', 5, 255),
#         ('бхава', 2, 222),
#         ('кука', 4, 218),
#         ('кука', 3, 222),
#     ]

# ic('*****SORTING***********')
# # ic(sorted(student_tuples, key=itemgetter(2, 1), reverse=True))
# ic(sorted(student_tuples, key=itemgetter(2), reverse=True))
# # sorted(student_objects, key=attrgetter('grade', 'age'))
# ic('*****SORTING***********')



ic(f"Time taken {time() - start_time}")

ic(dm.idOPZzz)