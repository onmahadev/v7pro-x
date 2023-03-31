#!flask/bin/python
#import sys
####################import runpy
import uuid
#import os
# from functools import lru_cache
from random import randint
import random
import os, time, datetime
#import psutil
#import logging
from time import time
from icecream import ic
from flask import Flask, jsonify, render_template, request, session, flash, redirect,url_for, make_response
from flask_sqlalchemy import SQLAlchemy
import configparser
from peewee import *
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from threading import Lock
from faker import Faker

import sinclair as sincl 

#kEgrQvNvH!qYVMNnw2g584rJ2d2$
# last:
# CUgp6L1^fi7jaywDN@$l!h1T&pDU

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CUgp6L1^fi7jaywDN@$l!h1T&pDU'
app.config['SESSION_COOKIE_NAME'] = 'v7pro_'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://v7user:v7password@0.0.0.0:8889/v7'
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app)
BASE_URL = "/att"

socketio = SocketIO(app)
thread = None
thread_lock = Lock()
db = SQLAlchemy(app)
faker = Faker('ru_RU')
#######################################################################
##### get config
cfg = configparser.ConfigParser()
cfg.read('v7.cfg')
mylHost=cfg.get('mysql', 'host')
mylUser=cfg.get('mysql', 'user')
mylPwd=cfg.get('mysql', 'passwd')
mylDb=cfg.get('mysql', 'database')
mylPort=cfg.get('mysql', 'port')
#other cfg
appHost=cfg.get('main', 'appIP')
appPort=cfg.get('main', 'appPORT')
g_dbl_ow=cfg.get('gui-double', 'ownweight')
g_dbl_city=cfg.get('gui-double', 'city')
#######################################################################
db = MySQLDatabase(host=mylHost,user=mylUser,password=mylPwd,database=mylDb,port=8889,)



#is Snatch|Jerk apps now
SN = True
CJ = False

class v7(Model):
    class Meta:
        database = db

class att(v7):
    id = AutoField(column_name='id')
    op = IntegerField(column_name='op')
    nop = IntegerField(column_name='nextop')
    sex = IntegerField(column_name='sex')
    #cat = IntegerField(column_name='wcat_id')
    ow = FloatField(column_name='ownweight')
    s1 = IntegerField(column_name='snatch1')
    s1ig = IntegerField(column_name='snatch1isget')
    s2 = IntegerField(column_name='snatch2')
    s2ig = IntegerField(column_name='snatch2isget')
    s3 = IntegerField(column_name='snatch3')
    s3ig = IntegerField(column_name='snatch3isget')
    sres = IntegerField(column_name='snatchresult')
    j1 = IntegerField(column_name='cleanjerk1')
    j1ig = IntegerField(column_name='cleanjerk1isget')
    j2 = IntegerField(column_name='cleanjerk2')
    j2ig = IntegerField(column_name='cleanjerk2isget')
    j3 = IntegerField(column_name='cleanjerk3')
    j3ig = IntegerField(column_name='cleanjerk3isget')
    jres = IntegerField(column_name='cleanjerkresult')
    dblsum = IntegerField(column_name='doublesum')
    country_id = IntegerField(column_name='country_id')
    city = TextField(column_name='city')
    city_id = TextField(column_name='city_id')
    wcat_id = IntegerField(column_name='wcat_id')
    wcat = TextField(column_name='wcat_')
    rank_id = IntegerField(column_name='rank_id')
    flow = IntegerField(column_name='flow_')
    aend = IntegerField(column_name='actionend')
    s_place = IntegerField(column_name='snatch_place')
    j_place = IntegerField(column_name='cleanjerk_place')
    place = IntegerField(column_name='place')
    country = TextField(column_name='country_')
    birth = TextField(column_name='birth')
    sinc = TextField(column_name='sincler')
    avatar = TextField(column_name='avatar')

    nr = IntegerField(column_name='newrank')
    sc = IntegerField(column_name='score')
    pos = IntegerField(column_name='position')
    isend = IntegerField(column_name='actionend')
    sname = TextField(column_name='secondname')
    fname = TextField(column_name='firstname')
    exnow = TextField(column_name='exnow')
    wnow = IntegerField(column_name='weightnow')
    trynow = IntegerField(column_name='trynow')
    
    s1d = TextField(column_name='s1d')
    s1ch1 = TextField(column_name='s1ch1')
    s1ch2 = TextField(column_name='s1ch2')
    s2d = TextField(column_name='s2d')
    s2ch1 = TextField(column_name='s2ch1')
    s2ch2 = TextField(column_name='s2ch2')
    s3d = TextField(column_name='s3d')
    s3ch1 = TextField(column_name='s3ch1')
    s3ch2 = TextField(column_name='s3ch2')   
    gn =  TextField(column_name='guru1name')   

    j1d = TextField(column_name='cleanjerk1d')
    j1ch1 = TextField(column_name='cleanjerk1ch1')
    j1ch2 = TextField(column_name='cleanjerk1ch2')
    j2d = TextField(column_name='cleanjerk2d')
    j2ch1 = TextField(column_name='cleanjerk2ch1')
    j2ch2 = TextField(column_name='cleanjerk2ch2')
    j3d = TextField(column_name='cleanjerk3d')
    j3ch1 = TextField(column_name='cleanjerk3ch1')
    j3ch2 = TextField(column_name='cleanjerk3ch2')


    def obj_to_dict(self):  # for build json format
        return {
            "id": self.id,
            "op": self.op,
            "nop": self.nop,
            "fname": self.fname,
            "sname": self.sname,
            "sres": self.sres,
            "aend": self.aend,
            "country_id": self.country_id,
            "country": self.country,
            "city_id": self.city_id,
            "city": self.city,
            "wcat_id": self.wcat_id,
            "wcat": self.wcat,
            "ow": self.ow,
            "avatar": self.avatar,
            "sex": self.sex,
            "s1": self.s1,
            "s1ig": self.s1ig,
            "s2": self.s2,
            "s2ig": self.s2ig,
            "s3": self.s3,
            "s3ig": self.s3ig,
            "sres": self.sres,
            "j1": self.j1,
            "j1ig": self.j1ig,
            "j2": self.j2,
            "j2ig": self.j2ig,
            "j3": self.j3,
            "j3ig": self.j3ig,
            "jres": self.jres,            
            "dblsum": self.dblsum,
            "exnow": self.exnow,
            "wnow": self.wnow,
            "s1d": self.s1d,
            "s1ch1":self.s1ch1,
            "s1ch2":self.s1ch2,
            "s2d": self.s2d,
            "s2ch1":self.s2ch1,
            "s2ch2":self.s2ch2,
            "s3d": self.s3d,
            "s3ch1":self.s3ch1,
            "s3ch2":self.s3ch2,
            "j1d": self.j1d,
            "flow": self.flow,
            "j1ch1":self.j1ch1,
            "j1ch2":self.j1ch2,
            "j2d": self.j2d,
            "j2ch1":self.j2ch1,
            "j2ch2":self.j2ch2,
            "j3d": self.j3d,
            "j3ch1":self.j3ch1,
            "place":self.place,
            "sc":self.sc,
            "nr":self.nr,
            "sinc":self.sinc,
            "gn":self.gn,
            "s_place":self.s_place,
            "j_place":self.j_place,
            "j3ch2":self.j3ch2,
            "trynow":self.trynow,
            "rank_id":self.rank_id,
        
        }    
       
    class Meta:
        table_name='v7now'

#####################################################################

class country(v7):
    country_id = AutoField(column_name='id')
    name =  CharField(column_name='name')
    flag =  CharField(column_name='flag')
    img =  CharField(column_name='img')
    m3code =  CharField(column_name='mok3code')
    
    #cntr = ForeignKeyField(att, column_name='id')
    
    def obj_to_dict(self):  # for build json format
        return {
            "id": self.country_id,
            "name": self.name,
            "flag": self.flag,
            "m3code": self.m3code,
            "img": self.img,
        }         

    class Meta:
        table_name='country'

#####################################################################

class cat(v7):
    wcat_id = AutoField(column_name='id')
    sex =  IntegerField(column_name='sex')
    wcat =  IntegerField(column_name='wcat')
    lwcat =  CharField(column_name='label')
    def obj_to_dict(self):  # for build json format
        return {
            "id": self.wcat_id,
            "sex": self.sex,
            "wcat": self.wcat,
            "lwcat": self.lwcat,
        } 
    class Meta:
        table_name='wcat'

#####################################################################

class ranks(v7):
    rid = AutoField(column_name='id')
    sex =  IntegerField(column_name='sex')
    wcat =  IntegerField(column_name='wcat')
    wcat_id =  CharField(column_name='wcat_id')
    r_msmk =  CharField(column_name='msmk')
    r_ms =  CharField(column_name='ms')
    r_kms =  CharField(column_name='kms')
    r_r1 =  CharField(column_name='rank1')
    r_r2 =  CharField(column_name='rank2')
    r_r3 =  CharField(column_name='rank3')
    r_r1j =  CharField(column_name='rank1jun')
    r_r2j =  CharField(column_name='rank2jun')
    r_r3j =  CharField(column_name='rank3jun')
    wr =  CharField(column_name='worldrecord')
    wr_who =  CharField(column_name='wr_who')
    wr_where =  CharField(column_name='wr_where')
    wr_when =  CharField(column_name='wr_when')
    # ranks
    wr_snatch = IntegerField(column_name='wr_snatch')
    wr_cj = IntegerField(column_name='wr_cj')
    wr_total = IntegerField(column_name='wr_total')
    #wcal_id
    class Meta:
        table_name='ranks'

#####################################################################
class cities(v7):
    cities_id = AutoField(column_name='id')
    region_id =  IntegerField(column_name='id_region')
    country_id =  IntegerField(column_name='id_country')
    cname =  CharField(column_name='name')
    def obj_to_dict(self):  # for build json format
        return {
            "id": self.cities_id,
            "rid": self.region_id,
            "cid": self.cname,
            "name": self.cname,
        }         
    class Meta:
        table_name='cities'

#####################################################################
#####################################################################

class v7t(v7):
    vt_id = AutoField(column_name='id')
    vt_start =  CharField(column_name='start_timestamp')
    vt_status =  IntegerField(column_name='status')
    vt_currtime =  CharField(column_name='curr_timestamp')
    vt_uend =  CharField(column_name='until_end')
    vt_t2d =  CharField(column_name='time2display')
    vt_otm =   IntegerField(column_name='one_two_min')
    
    def obj_to_dict(self):  # for build json format
        return {
            "vt_id": self.vt_id,
            "vt_start": self.vt_start,
            "vt_status": self.vt_status,
            "vt_currtime": self.vt_currtime,
            "vt_uend": self.vt_uend,
            "vt_otm": self.vt_otm,
        }      
    class Meta:
        table_name='v7timer'

#####################################################################


class opt(v7):
    opt_id = AutoField(column_name='id')
    o_name =  IntegerField(column_name='name')
    o_val =  IntegerField(column_name='value')
    o_descoff =  IntegerField(column_name='descript_off')
    o_desc =  CharField(column_name='descript')
    o_param =  CharField(column_name='param')
    #wcal_id
    def obj_to_dict(self):  # for build json format
        return {
            "id": self.opt_id,
            "name": self.o_name,
            "value": self.o_val,
            "desc": self.o_desc,
            "descoff": self.o_descoff,
            "param": self.o_param,
        }      
    class Meta:
        table_name='opt'




#####################################################################


class jgroup(v7):
    j_id = AutoField(column_name='id')
    j_group =  IntegerField(column_name='flow_gpoup')
    j_nane =  IntegerField(column_name='name')
    j_post =  IntegerField(column_name='post')
    j_post_ru =  IntegerField(column_name='post_ru')
    j_city =  CharField(column_name='city')
    j_cat =  CharField(column_name='category')
    def obj_to_dict(self):  # for build json format
        return {
            "id": self.j_id,
            "name": self.j_nane,
            "group": self.j_group,
            "post": self.j_post,
            "post_ru": self.j_post_ru,
            "city": self.j_city,
            "cat": self.j_cat,
        }      
    class Meta:
        table_name='v7staff'




#####################################################################
# class athlete(v7):
#     id = AutoField(column_name='id')
#     op = IntegerField(column_name='op')
#     nop = IntegerField(column_name='nextop')
#     sex = IntegerField(column_name='sex')
#     #wcat = IntegerField(column_name='wcat_id')
#     #cat = IntegerField(column_name='wcat_id')
#     ow = FloatField(column_name='ownweight')
#     s1 = IntegerField(column_name='snatch1')
#     s1ig = IntegerField(column_name='snatch1isget')
#     s2 = IntegerField(column_name='snatch2')
#     s2ig = IntegerField(column_name='snatch2isget')
#     s3 = IntegerField(column_name='snatch3')
#     s3ig = IntegerField(column_name='snatch3isget')
#     sres = IntegerField(column_name='snatchresult')
#     j1 = IntegerField(column_name='cleanjerk1')
#     j1ig = IntegerField(column_name='cleanjerk1isget')
#     j2 = IntegerField(column_name='cleanjerk2')
#     j2ig = IntegerField(column_name='cleanjerk2isget')
#     j3 = IntegerField(column_name='cleanjerk3')
#     j3ig = IntegerField(column_name='cleanjerk3isget')
#     jres = IntegerField(column_name='cleanjerkresult')
#     dblsum = IntegerField(column_name='doublesum')
#     country_id = IntegerField(column_name='country_id')
#     country = TextField(column_name='country_')
#     city = TextField(column_name='city')
#     city_id = TextField(column_name='city_id')
#     wcat_id = IntegerField(column_name='wcat_id')
#     wcat = IntegerField(column_name='wcat_')
#     rank_id = IntegerField(column_name='rank_id')

#     s_place = IntegerField(column_name='snatch_place')
#     j_place = IntegerField(column_name='cleanjerk_place')
#     place = IntegerField(column_name='place')
#     flow = IntegerField(column_name='flow')


#     isend = IntegerField(column_name='actionend')
#     sname = TextField(column_name='secondname')
#     fname = TextField(column_name='firstname')
#     exnow = TextField(column_name='exnow')
#     wnow = TextField(column_name='weightnow')
#     trynow = TextField(column_name='trynow')
#     country = TextField(column_name='country')
    
#     s1d = TextField(column_name='s1d')
#     s1ch1 = TextField(column_name='s1ch1')
#     s1ch2 = TextField(column_name='s1ch2')
#     s2d = TextField(column_name='s2d')
#     s2ch1 = TextField(column_name='s2ch1')
#     s2ch2 = TextField(column_name='s2ch2')
#     s3d = TextField(column_name='s3d')
#     s3ch1 = TextField(column_name='s3ch1')
#     s3ch2 = TextField(column_name='s3ch2')    

#     j1d = TextField(column_name='cleanjerk1d')
#     j1ch1 = TextField(column_name='cleanjerk1ch1')
#     j1ch2 = TextField(column_name='cleanjerk1ch2')
#     j2d = TextField(column_name='cleanjerk2d')
#     j2ch1 = TextField(column_name='cleanjerk2ch1')
#     j2ch2 = TextField(column_name='cleanjerk2ch2')
#     j3d = TextField(column_name='cleanjerk3d')
#     j3ch1 = TextField(column_name='cleanjerk3ch1')
#     j3ch2 = TextField(column_name='cleanjerk3ch2')



#     def obj_to_dict(self):  # for build json format
#         return {
#             "id": self.id,
#             "op": self.op,
#             "flow": self.flow,
#             "nop": self.nop,
#             "fname": self.fname,
#             "sname": self.sname,
#             "sres": self.sres,
#             "country_id": self.country_id,
#             "country": self.country,
#             "city_id": self.city_id,
#             "city": self.city,
#             "wcat_id": self.wcat_id,
#             "wcat": self.wcat,
#             "ow": self.ow,
#             "sex": self.sex,
#             "s1": self.s1,
#             "s1ig": self.s1ig,
#             "s2": self.s2,
#             "s2ig": self.s2ig,
#             "s3": self.s3,
#             "s3ig": self.s3ig,
#             "sres": self.sres,
#             "j1": self.j1,
#             "j1ig": self.j1ig,
#             "j2": self.j2,
#             "j2ig": self.j2ig,
#             "j3": self.j3,
#             "j3ig": self.j3ig,
#             "jres": self.jres,            
#             "dblsum": self.dblsum,
#             "exnow": self.exnow,
#             "wnow": self.wnow,
#             "s1d": self.s1d,
#             "s1ch1":self.s1ch1,
#             "s1ch2":self.s1ch2,
#             "s2d": self.s2d,
#             "s2ch1":self.s2ch1,
#             "s2ch2":self.s2ch2,
#             "s3d": self.s3d,
#             "s3ch1":self.s3ch1,
#             "s3ch2":self.s3ch2,
#             "j1d": self.j1d,
#             "j1ch1":self.j1ch1,
#             "j1ch2":self.j1ch2,
#             "j2d": self.j2d,
#             "j2ch1":self.j2ch1,
#             "j2ch2":self.j2ch2,
#             "j3d": self.j3d,
#             "j3ch1":self.j3ch1,
#             "place":self.place,
#             "s_place":self.s_place,
#             "j_place":self.j_place,
#             "j3ch2":self.j3ch2,
#             "trynow":self.trynow,
#             "rank_id":self.rank_id,
        
#         }    
       
#     class Meta:
#         table_name='v7athlete'


#####################################################################
#####################################################################
#####################################################################


#####################################################################
#####################################################################
#####################################################################
# for backups and reports, +new flow
# class bkp(v7):
#     vt_id = AutoField(column_name='id')
#     vt_start =  CharField(column_name='start_timestamp')
#     vt_status =  IntegerField(column_name='status')
#     vt_currtime =  CharField(column_name='curr_timestamp')
#     vt_uend =  CharField(column_name='until_end')
#     vt_otm =   IntegerField(column_name='one_two_min')
    
#     def obj_to_dict(self):  # for build json format
#         return {
#             "vt_id": self.vt_id,
#             "vt_start": self.vt_start,
#             "vt_status": self.vt_status,
#             "vt_currtime": self.vt_currtime,
#             "vt_uend": self.vt_uend,
#             "vt_otm": self.vt_otm,
#         }      
#     class Meta:
#         table_name='v7bkp'

#####################################################################


#####################################################################
##### try/except DB connection
#####  -> id, one id with min weight in s3
try:
    db.connect()
except InternalError as therror:
    print(str(therror))

def dict_helper(objlist):
    result2 = [item.obj_to_dict() for item in objlist]
    return result2

########################
### diff viean device
@app.route(BASE_URL+'/', methods=['GET'])
@cross_origin()
def get_all_att():
    ##########
    # set app now!
    #run v7core DAEMON
    set_app_weight_now()


    #exec(open('v7core.py').read())
    # daemod_run = subprocess.run(['python3.10', 'v7core.py'])
    #set_opnop()
    
    # set try_now&xXchX now!
    #change_app_weight()
    ## select all all
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.exnow,att.wnow,
    att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,
    att.s3d,att.s3ch1,att.s3ch2,
    att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
    att.j3d,att.j3ch1,att.j3ch2,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    # country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id))
    cat.lwcat,cities.cname).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id))
    attdata = [t for t in qu]
    attz = dict_helper(attdata)
    #return jsonify({'athletes': attz})
    return jsonify(attz=attz)

########################
### diff viean device
@app.route(BASE_URL+'/total_athl', methods=['GET'])
@cross_origin()
def total_athl():
    ##########
    # set app now!
    set_app_weight_now()
    #set_opnop()
    
    # set try_now&xXchX now!
    #change_app_weight()
    ## select all all
    qu = att.select(att.id).count()
    # print(qu + '^^^^')
    # attdata = [t for t in qu]
    # attz = dict_helper(attdata)
    #return jsonify({'athletes': attz})
    return jsonify(qu)



############################################################
############## get (JSON) ALL WEIGHT CATEGORY ##############
################# for MALE (sex 1) MAN/boy #################
############################################################
@app.route('/m_wcat', methods=['GET'])
@cross_origin()
def get_male_wcat():
    wcat_all =  cat.select(cat.wcat_id,cat.sex,cat.wcat,cat.lwcat).where(cat.sex==1)
    wcatdata_z = dict_helper(wcat_all)
    return jsonify(wcatdata_z=wcatdata_z)





############################################################
############## get (JSON) v7 timer-get-seconds #############
############## *************************      ##############
############################################################

@app.route('/timer-get-seconds', methods=['GET','POST'])
@cross_origin()
def v7timer_get_seconds():
    ########## GET TIMER
    ## select 1
    # qu = v7t.select(v7t.vt_uend,v7t.vt_status)
    # attdata = [t for t in qu]
    # v7timer = dict_helper(attdata)
    mycursor = db.cursor()    
    sql = "SELECT ROUND(TIME_TO_SEC(TIMEDIFF((SELECT `curr_timestamp` FROM `v7timer` WHERE 1),(SELECT `start_timestamp` FROM `v7timer` WHERE 1))),0);"


# IF(condition, value_if_true, value_if_false)
# SELECT ROUND(TIME_TO_SEC(TIMEDIFF((SELECT `curr_timestamp` FROM `v7timer` WHERE 1),(SELECT `start_timestamp` FROM `v7timer` WHERE 1))),0);


    mycursor.execute(sql)
    query_result = mycursor.fetchone()
    print(query_result,'@@@')
    # v7timer[0]['DIFF'] = query_result[0]
    # return jsonify(secccc=v7timer[0]['DIFF'])
    # return jsonify(cc=query_result[0], c_time=v7timer[0]['vt_status'])
    mycursor.close()
    return jsonify(cc=query_result[0])
    # return jsonify(v7timer=v7timer,asd=asd,qr=query_result[0])

@app.route('/timer-get-otm', methods=['GET','POST'])
@cross_origin()
def v7timer_get_otm():
    ########## GET TIMER
    ## select 1
    # qu = v7t.select(v7t.vt_uend,v7t.vt_status)
    # attdata = [t for t in qu]
    # v7timer = dict_helper(attdata)
    mycursor = db.cursor()    
    sql = "SELECT one_two_min FROM v7timer WHERE 1;"
    mycursor.execute(sql)
    query_result = mycursor.fetchone()
    print(query_result,'@@@')
    # v7timer[0]['DIFF'] = query_result[0]
    # return jsonify(secccc=v7timer[0]['DIFF'])
    # return jsonify(cc=query_result[0], c_time=v7timer[0]['vt_status'])
    mycursor.close()
    return jsonify(cc=query_result[0])
    # return jsonify(v7timer=v7timer,asd=asd,qr=query_result[0])


@app.route('/timer-get-status', methods=['GET','POST'])
@cross_origin()
def v7timer_get_status():
    ########## GET TIMER
    ## select all all
    # qu = v7t.select(v7t.vt_start,v7t.vt_status,v7t.vt_currtime,v7t.vt_uend,v7t.vt_otm)
    # attdata = [t for t in qu]
    # v7timer = dict_helper(attdata)
    mycursor = db.cursor()    
    sql = "SELECT status FROM v7timer WHERE 1;"
    mycursor.execute(sql)
    query_result = mycursor.fetchone()
    print(query_result,'@@@')    
    # return jsonify(v7timer=v7timer)
    mycursor.close()
    return jsonify(cc=query_result[0])



@app.route('/timer-tablo-dataz', methods=['GET','POST'])
@cross_origin()
def v7timer_get_all2tablo():
    ########## GET TIMER2TABLO
    mycursor = db.cursor()    
    sqlz = "SELECT id,weightnow,exnow,firstname,secondname FROM `v7now` WHERE op=1;"
    mycursor.execute(sqlz)
    id2tablo = mycursor.fetchone()     
    if(id2tablo is None): 
        id2tablo[0] ="999"        
    # return jsonify(cc=query_result[0],qr=qr)
    mycursor.close()
    return jsonify(id=id2tablo[0],wnow=id2tablo[1],exnow=id2tablo[2],fn=id2tablo[3],sn=id2tablo[4])



# @app.route('/timer-get-sec-on-tablo', methods=['GET','POST'])
@app.route('/timer-get-sec-on-tablo', methods=['GET'])
@cross_origin()
def v7timer_get_sec2tablo():
    ########## GET TIMER2TABLO
    mycursor = db.cursor()    
    # GET 1 or 2 min
    # sql = "SELECT one_two_min FROM v7timer WHERE 1;"
    # mycursor.execute(sql)
    # query_result = mycursor.fetchone()
    # if query_result[0]==1: # 1 or 2 minutes of timer
    #     sql = "SELECT status FROM v7timer WHERE 1;"
    #     mycursor.execute(sql)
    #     q_result = mycursor.fetchone()
    #     if q_result[0]==1: # 1 - RUN, 2 - PAUSE, 0 - STOP/RESET
    #         sql = "SELECT ROUND(TIME_TO_SEC(TIMEDIFF((SELECT `curr_timestamp` FROM `v7timer` WHERE 1),(SELECT `start_timestamp` FROM `v7timer` WHERE 1))),0);"
    #         mycursor.execute(sql)
    #         sec2tablo = mycursor.fetchone()
    #     elif q_result[0]==2: # 1 - RUN, 2 - PAUSE, 0 - STOP/RESET
    #         sql = "SELECT ROUND(TIME_TO_SEC(TIMEDIFF((SELECT `curr_timestamp` FROM `v7timer` WHERE 1),(SELECT `start_timestamp` FROM `v7timer` WHERE 1))),0);"
    #         mycursor.execute(sql)
    #         sec2tablo = mycursor.fetchone()
    #     elif q_result[0]==0: # 1 - RUN, 2 - PAUSE, 0 - STOP/RESET
    #         sql = "SELECT IF((SELECT `one_two_min` FROM `v7timer` WHERE 1)=1, '60', '120')"
    #         mycursor.execute(sql)
    #         sec2tablo = mycursor.fetchone()    
    # if query_result[0]==2: # 1 or 2 minutes of timer
    #     sql = "SELECT status FROM v7timer WHERE 1;"
    #     mycursor.execute(sql)
    #     q_result = mycursor.fetchone()
    #     if q_result[0]==1: # 1 - RUN, 2 - PAUSE, 0 - STOP/RESET
    #         sql = "SELECT ROUND(TIME_TO_SEC(TIMEDIFF((SELECT `curr_timestamp` FROM `v7timer` WHERE 1),(SELECT `start_timestamp` FROM `v7timer` WHERE 1))),0);"
    #         mycursor.execute(sql)
    #         sec2tablo = mycursor.fetchone()
    #     elif q_result[0]==2: # 1 - RUN, 2 - PAUSE, 0 - STOP/RESET
    #         sql = "SELECT ROUND(TIME_TO_SEC(TIMEDIFF((SELECT `curr_timestamp` FROM `v7timer` WHERE 1),(SELECT `start_timestamp` FROM `v7timer` WHERE 1))),0);"
    #         mycursor.execute(sql)
    #         sec2tablo = mycursor.fetchone()
    #     elif q_result[0]==0: # 1 - RUN, 2 - PAUSE, 0 - STOP/RESET
    #         sql = "SELECT IF((SELECT `one_two_min` FROM `v7timer` WHERE 1)=1, '60', '120')"
    #         mycursor.execute(sql)
    #         sec2tablo = mycursor.fetchone()    
    sqlz = "SELECT id FROM `v7now` WHERE op=1;"
    mycursor.execute(sqlz)
    id2tablo = mycursor.fetchone() 

    sql = "SELECT `time2display` FROM `v7timer` WHERE 1;"
    mycursor.execute(sql)
    sec2tablo = mycursor.fetchone()  

    sql = "SELECT `one_two_min` FROM `v7timer` WHERE 1;"
    mycursor.execute(sql)
    otm2tablo = mycursor.fetchone()  
    
    sql = "SELECT `status` FROM `v7timer` WHERE 1;"
    mycursor.execute(sql)
    status2tablo = mycursor.fetchone()


    if sec2tablo == None:
        sql = "SELECT 0 WHERE 1;"
        mycursor.execute(sql)
        sec2tablo = mycursor.fetchone()  
    if id2tablo == None:
        sql = "SELECT 0 WHERE 1;"
        mycursor.execute(sql)
        id2tablo = mycursor.fetchone()
    if otm2tablo == None:
        sql = "SELECT 0 WHERE 1;"
        mycursor.execute(sql)
        otm2tablo = mycursor.fetchone()  
    if status2tablo == None:
        sql = "SELECT 0 WHERE 1;"
        mycursor.execute(sql)
        status2tablo = mycursor.fetchone()                  
   
    # sql = "SELECT one_two_min FROM v7timer WHERE 1;"    
    # sql = "SELECT one_two_min FROM v7timer WHERE 1;"
    # mycursor.execute(sql)
    # query_result = mycursor.fetchone()
    # print(query_result,'@@@')
    
    # if NONE
    # if(sec2tablo is None): 
    #     sec2tablo[0] =-1    
    # return jsonify(cc=query_result[0],qr=qr)
    mycursor.close()
    return jsonify(sec2tablo=sec2tablo[0],id2tablo=id2tablo[0],otm2tablo=otm2tablo[0],status2tablo=status2tablo[0])
    



############################################################
############## get (JSON) v7 TIMER STOP       ##############
############## *************************      ##############
############################################################

@app.route('/timer-get-time', methods=['GET','POST'])
@cross_origin()
def v7timer_get():
    ########## GET TIMER
    ## select all all
    asd = 777
    qu = v7t.select(v7t.vt_start,v7t.vt_status,v7t.vt_currtime,v7t.vt_uend,v7t.vt_otm)
    attdata = [t for t in qu]
    v7timer = dict_helper(attdata)
    start_time = v7timer[0]['vt_start'] 
    curr_time = v7timer[0]['vt_currtime'] 
    
    mycursor = db.cursor()    
    sql = "SELECT ROUND(TIME_TO_SEC(TIMEDIFF((SELECT `curr_timestamp` FROM `v7timer` WHERE 1),(SELECT `start_timestamp` FROM `v7timer` WHERE 1))),0);"
    mycursor.execute(sql)
    query_result = mycursor.fetchone()
    # //  GET START - STOP = ВОЛЯ БЛЯ!
    # //  GET START - STOP = ВОЛЯ БЛЯ!


    print(query_result,'@@@')

    v7timer[0]['DIFF'] = query_result[0]


    # if NONE
    if(v7timer is None): 
        v7timer =-0

    mycursor.close()
    return jsonify(v7timer=v7timer)
    # return jsonify(v7timer=v7timer,asd=asd,qr=query_result[0])



@app.route('/timer-set/<int:one_two_min>', methods=['GET','POST'])
@cross_origin()
def v7timer_set(one_two_min):
    ########## 1 or 2 minits!
    ex_upd=v7t.update({v7t.vt_otm:one_two_min}).where( (v7t.vt_id!=0) )
    ex_upd.execute()    
    ## select all all
    qu = v7t.select(v7t.vt_start,v7t.vt_status,v7t.vt_currtime,v7t.vt_uend,v7t.vt_otm)
    # UPDATE `v7timer` SET `start_timestamp`=(SELECT UNIX_TIMESTAMP()) ,`status`=1 WHERE 1;
    attdata = [t for t in qu]
    v7timer = dict_helper(attdata)
    #return jsonify({'athletes': attz})
    
    return jsonify(v7timer=v7timer)



############################################################
############## reset (JSON) v7 TIMER RESET       ##############
############## *************************      ##############
############################################################
@app.route('/timer-reset', methods=['GET','POST'])
@cross_origin()
def v7timer_reset():
    ########## 1 or 2 minits!
    ex_upd=v7t.update({v7t.vt_otm:1,v7t.vt_status:0,v7t.vt_uend:0,v7t.vt_t2d:60}).where( (v7t.vt_id!=0) )
    ex_upd.execute()    
    ## select all all
    qu = v7t.select(v7t.vt_start,v7t.vt_status,v7t.vt_currtime,v7t.vt_uend,v7t.vt_otm)
    # UPDATE `v7timer` SET `start_timestamp`=(SELECT UNIX_TIMESTAMP()) ,`status`=1 WHERE 1;
    attdata = [t for t in qu]
    v7timer = dict_helper(attdata)
    #return jsonify({'athletes': attz})
    return jsonify(v7timer=v7timer)









@app.route('/timer-write/<string:secz>', methods=['GET','POST'])
@cross_origin()
def v7timer_writeone(secz):
    ########## 
    # timestampp = datetime.datetime.now()

    ex_upd=v7t.update({v7t.vt_t2d:secz}).where( (v7t.vt_id!=0) )
    ex_upd.execute()    


    mycursor = db.cursor()    
    sql = "SELECT ROUND(TIME_TO_SEC(TIMEDIFF((SELECT `curr_timestamp` FROM `v7timer` WHERE 1),(SELECT `start_timestamp` FROM `v7timer` WHERE 1))),0);"
# IF(condition, value_if_true, value_if_false)
# SELECT ROUND(TIME_TO_SEC(TIMEDIFF((SELECT `curr_timestamp` FROM `v7timer` WHERE 1),(SELECT `start_timestamp` FROM `v7timer` WHERE 1))),0);
    mycursor.execute(sql)
    query_result = mycursor.fetchone()
    print(query_result,'% theTimer')
    # v7timer[0]['DIFF'] = query_result[0]
    # return jsonify(secccc=v7timer[0]['DIFF'])
    # # return jsonify(cc=query_result[0], c_time=v7timer[0]['vt_status'])
    # return jsonify(cc=query_result[0])
    ## select all all
    qu = v7t.select(v7t.vt_start,v7t.vt_status,v7t.vt_currtime,v7t.vt_uend,v7t.vt_otm)
    # UPDATE `v7timer` SET `start_timestamp`=(SELECT UNIX_TIMESTAMP()) ,`status`=1 WHERE 1;
    attdata = [t for t in qu]
    v7timer = dict_helper(attdata)
    #return jsonify({'athletes': attz})
    mycursor.close()
    return jsonify(v7timer=v7timer,cc=query_result[0])









@app.route('/timer-write', methods=['GET','POST'])
@cross_origin()
def v7timer_write():
    ########## 
    # timestampp = datetime.datetime.now()

    # ex_upd=v7t.update({v7t.vt_t2d:v7t.vt_t2d-1}).where( (v7t.vt_id!=0) )
    # ex_upd.execute()    




    mycursor = db.cursor()    
    sql = "SELECT ROUND(TIME_TO_SEC(TIMEDIFF((SELECT `curr_timestamp` FROM `v7timer` WHERE 1),(SELECT `start_timestamp` FROM `v7timer` WHERE 1))),0);"




# IF(condition, value_if_true, value_if_false)
# SELECT ROUND(TIME_TO_SEC(TIMEDIFF((SELECT `curr_timestamp` FROM `v7timer` WHERE 1),(SELECT `start_timestamp` FROM `v7timer` WHERE 1))),0);


    mycursor.execute(sql)
    query_result = mycursor.fetchone()
    print(query_result,'% theTimer')
    # v7timer[0]['DIFF'] = query_result[0]
    # return jsonify(secccc=v7timer[0]['DIFF'])
    # # return jsonify(cc=query_result[0], c_time=v7timer[0]['vt_status'])
    # return jsonify(cc=query_result[0])
    ## select all all
    qu = v7t.select(v7t.vt_start,v7t.vt_status,v7t.vt_currtime,v7t.vt_uend,v7t.vt_otm)
    # UPDATE `v7timer` SET `start_timestamp`=(SELECT UNIX_TIMESTAMP()) ,`status`=1 WHERE 1;
    attdata = [t for t in qu]
    v7timer = dict_helper(attdata)
    #return jsonify({'athletes': attz})
    mycursor.close()
    return jsonify(v7timer=v7timer,cc=query_result[0])





############################################################
############## get (JSON) v7 TIMER STOP       ##############
############## *************************      ##############
############################################################


@app.route('/timer-stop', methods=['GET','POST'])
@cross_origin()
def v7timer_stop():
    ########## 
    # timestampp = datetime.datetime.now()
    ex_upd=v7t.update({v7t.vt_status:0}).where( (v7t.vt_id!=0) )
    ex_upd.execute()    
    ## select all all
    qu = v7t.select(v7t.vt_start,v7t.vt_status,v7t.vt_currtime,v7t.vt_uend,v7t.vt_otm)
    # UPDATE `v7timer` SET `start_timestamp`=(SELECT UNIX_TIMESTAMP()) ,`status`=1 WHERE 1;
    attdata = [t for t in qu]
    v7timer = dict_helper(attdata)
    #return jsonify({'athletes': attz})
    return jsonify(v7timer=v7timer)

############################################################
############## get (JSON) v7 TIMER PAUSE      ##############
############## *************************      ##############
############################################################

@app.route('/timer-pause', methods=['GET','POST'])
@cross_origin()
def v7timer_pause():
    ########## 
    # timestampp = datetime.datetime.now()
    ex_upd=v7t.update({v7t.vt_status:2}).where( (v7t.vt_id!=0) )
    ex_upd.execute()    
    ## select all all
    qu = v7t.select(v7t.vt_start,v7t.vt_status,v7t.vt_currtime,v7t.vt_uend,v7t.vt_otm)
    
    # UPDATE `v7timer` SET `start_timestamp`=(SELECT UNIX_TIMESTAMP()) ,`status`=1 WHERE 1;
    # SELECT ROUND(TIME_TO_SEC(TIMEDIFF((SELECT `curr_timestamp` FROM `v7timer` WHERE 1),(SELECT `start_timestamp` FROM `v7timer` WHERE 1))),0);
    
    attdata = [t for t in qu]
    v7timer = dict_helper(attdata)
    
    # assss = {"id": 0, "organizer": "Some Name", "eventStart": "09:30 AM", "eventEnd": "10:00 AM", "subject": "rental procedure", "attendees": "Some Name<br />Person 2<br />Person 3"}
    # v7timer = []
    # v7timer.append(assss)
    #return jsonify({'athletes': attz})
    return jsonify(v7timer=v7timer)




############################################################
############## get (JSON) v7 TIMER START      ##############
############## *************************      ##############
############################################################

@app.route('/timer-start/<int:one_two_min>', methods=['GET','POST'])
@cross_origin()
def v7timer_start(one_two_min=1):
    ########## 
    qst = v7t.get(v7t.vt_id==1)
    # print(qst,'!!!!')
    # ПРОВЕРЯЕМ IF статус = 1(start) -> ни хуя не делаем!
    # ПРОВЕРЯЕМ IF статус = 2(pause) -> ни хуя не делаем!
    # А ЕСЛИ ЖЕ IF статус = 0(nostart) -> СТАРТУЕМ!!!

    # if():# if():# if():# if():# if():# if():

    timestampp = datetime.datetime.now()
    ex_upd=v7t.update({v7t.vt_start:timestampp,v7t.vt_otm:one_two_min,v7t.vt_status:1}).where( (v7t.vt_id!=0) )
    ex_upd.execute()    
    qu = v7t.select(v7t.vt_start,v7t.vt_status,v7t.vt_currtime,v7t.vt_uend,v7t.vt_otm)
    attdata = [t for t in qu]
    v7timer = dict_helper(attdata)
    return jsonify(v7timer=v7timer)



############################################################
############## get (JSON) ALL WEIGHT CATEGORY ##############
############## for FEMALE (sex 0) WOOMAN/girl ##############
############################################################
@app.route('/f_wcat', methods=['GET'])
@cross_origin()
def get_female_wcat():
    wcat_all =  cat.select(cat.wcat_id,cat.sex,cat.wcat,cat.lwcat).where(cat.sex==0)
    wcatdata_z = dict_helper(wcat_all)
    return jsonify(wcatdata_z=wcatdata_z)


############################################################
############## get (JSON) 1(one) ATHLETE data ##############
############################################################
@app.route(BASE_URL+'/<int:id>', methods=['GET'])
@cross_origin()
def get_att(id):
    ##########
    try:
        athlete = att.get(id)
        return jsonify(athlete.obj_to_dict())
    except DoesNotExist: 
         return render_template('404.html', title = 'Not Foubd - 404 !'), 404 

    # qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    # att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    # att.country_id,att.city_id,
    # att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    # country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id))
    
    #attdata = [t for t in qu]
    #attz = dict_helper(attdata)
    #return jsonify({'athletes': attz})
    #if athlete is None:
        #page_not_found()
    

@app.route('/dbl', methods = ['POST', 'GET'])
def double_menu():
    return render_template('double_menu.html')


@app.route('/double', methods=['GET'])
@cross_origin()
def double():
########## options 
    #run v7core DAEMON
    set_app_weight_now()
    set_op_now(id=0)
    set_nop_now(id=0)
    #daemod_run = subprocess.run(['python3.10', 'v7core.py'])
    #exec(open('v7core.py').read())
    qopt = opt.select(opt.opt_id,opt.o_name,opt.o_val,opt.o_desc,opt.o_param)
    qoptdata = [t for t in qopt]
    attcfg = dict_helper(qoptdata)    
    ##########
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.place,att.s_place,att.j_place,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    att.s1ch1,att.s1ch2,att.s2ch1,att.s2ch2,att.s3ch1,att.s3ch2,
    country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where(att.flow.is_null(0))
    attdata = [t for t in qu]
    attz = dict_helper(attdata)
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()

    if "iphone" in user_agent:
        attdata = [t for t in qu]
        return render_template('dbl-clean.html', attdata=attdata, attz=attz,CJ=CJ,SN=SN)
    elif "android" in user_agent:
        return render_template('dbl-clean.html', attdata=attdata, attz=attz,CJ=CJ,SN=SN)
    else:
        return render_template('double_g.html', attdata=attdata, attz=attz,attcfg=attcfg,CJ=CJ,SN=SN)
########################    

@app.route('/dbl_s', methods=['GET'])
@cross_origin()
def double_snatch():
########## options 
    set_app_weight_now()
    qopt = opt.select(opt.opt_id,opt.o_name,opt.o_val,opt.o_desc,opt.o_param)
    qoptdata = [t for t in qopt]
    attcfg = dict_helper(qoptdata)    
    ##########
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.place,att.s_place,att.j_place,
    att.s2ch1,att.s2ch2,att.s1ch1,att.s1ch2,att.s3ch1,att.s3ch2,
    att.j2ch1,att.j2ch2,att.j1ch1,att.j1ch2,att.j3ch1,att.j3ch2,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where(att.flow.is_null(0))
    attdata = [t for t in qu]
    attz = dict_helper(attdata)
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()

    if "iphone" in user_agent:
        attdata = [t for t in qu]
        return render_template('dbl-clean.html', attdata=attdata, attz=attz,CJ=CJ,SN=SN)
    elif "android" in user_agent:
        return render_template('dbl-clean.html', attdata=attdata, attz=attz,CJ=CJ,SN=SN)
    else:
        return render_template('double_s.html', attdata=attdata, attz=attz,attcfg=attcfg,CJ=CJ,SN=SN)
########################    


@app.route('/dbl_j', methods=['GET'])
@cross_origin()
def double_cleanjerk():
########## options 
    set_app_weight_now()
    qopt = opt.select(opt.opt_id,opt.o_name,opt.o_val,opt.o_desc,opt.o_param)
    qoptdata = [t for t in qopt]
    attcfg = dict_helper(qoptdata)    
    ##########
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.place,att.s_place,att.j_place,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where(att.flow.is_null(0))
    attdata = [t for t in qu]
    attz = dict_helper(attdata)
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()

    if "iphone" in user_agent:
        attdata = [t for t in qu]
        return render_template('dbl-clean.html', attdata=attdata, attz=attz,CJ=CJ,SN=SN)
    elif "android" in user_agent:
        return render_template('dbl-clean.html', attdata=attdata, attz=attz,CJ=CJ,SN=SN)
    else:
        return render_template('double_j.html', attdata=attdata, attz=attz,attcfg=attcfg,CJ=CJ,SN=SN)
########################    


# ### diff viean device
# @app.route(BASE_URL+'/', methods=['GET'])
# @cross_origin()
# def change_app_weight():
# #def set_app_s1ch1():
#     ## set/update app's weight & try_now
#     # ex_upd=att.update({att.s1ch1:att.s1, att.trynow:"2"}).where( 
#     # (att.s1ig.is_null(1))
#     # & (att.s1ch2.is_null(1)) & (att.s3ch1.is_null(1))
#     # & (att.s2ch1.is_null(1)) & (att.s2ch2.is_null(1))
#     # & (att.s3ch2.is_null(1)))
#     # ex_upd.execute()

#     # exb_upd=att.update({att.s1ch2:att.s1, att.trynow:"3"}).where( 
#     # (att.s1ig.is_null(0))
#     # & (att.s1ch2.is_null(1)) & (att.s3ch1.is_null(1))
#     # & (att.s2ch1.is_null(1)) & (att.s2ch2.is_null(1))
#     # & (att.s3ch2.is_null(1)))
#     # exb_upd.execute()

#     #return jsonify({'athletes': attz})
#     return jsonify(attz=attz,CJ=CJ,SN=SN)


@app.route('/', methods=['GET'])
@cross_origin()
def index():
    indexData = 'v7pro'
    print('###',indexData,'###')
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('index-clean.html',  indexData=indexData)
    elif "android" in user_agent:
        return render_template('index-clean.html', indexData=indexData)
    else:
        return render_template('index.html', indexData=indexData)


# @app.route('/opt/<int:optid>/<int:valueo>', methods=['GET', 'POST'], defaults={'optid': 0,'valueo': 0})
# @cross_origin()
# def options_change(optid,valueo):
#     opt_upd=opt.update({opt.o_val:valueo}).where(opt.opt_id==valueo)
#     opt_upd.execute()
#     # mycursor = db.cursor()
#     # sql = "UPDATE v7now SET snatch1= %s WHERE id= %s AND exnow='s1' AND s1ch1 IS NOT NULL AND s1ch2 IS NULL"
#     # val = (appw,id)
#     # mycursor.execute(sql,val)
#     # db.commit()
#     #return render_template('opt.html',opt=mycursor.rowcount)
#     return render_template('opt.html')

# @app.route('/opt/<int:optid>/<int:valueo>', methods=['GET', 'POST'], defaults={'optid': 0,'valueo': 0})
# @cross_origin()
# def options_change(optid,valueo):
#     opt_upd=opt.update({opt.o_val:valueo}).where(opt.opt_id==valueo)
#     opt_upd.execute()
#     # mycursor = db.cursor()
#     # sql = "UPDATE v7now SET snatch1= %s WHERE id= %s AND exnow='s1' AND s1ch1 IS NOT NULL AND s1ch2 IS NULL"
#     # val = (appw,id)
#     # mycursor.execute(sql,val)
#     # db.commit()
#     #return render_template('opt.html',opt=mycursor.rowcount)

@app.route('/stat', methods=['GET', 'POST'])
@cross_origin()
def statsz():
    if request.method == 'POST':
        mycursor = db.cursor()
        sql = "UPDATE opt SET value = %s WHERE id= %s"
        val = (0,0)
        mycursor.execute(sql,val)
        db.commit()
        asddd = opt.update({opt.o_val:0}).where((opt.opt_id==0)).execute()

    #return jsonify({'All athletes': attz})
    return render_template('stat.html')




@app.route('/qr-codez', methods=['GET', 'POST'])
@cross_origin()
def qrcodez():
    #return jsonify({'All athletes': attz})
    return render_template('qr-codez.html')


@app.route('/new-ath-inflow', methods = ['POST', 'GET'])
def newatinflow(): 
    # set_opnop()
    ### q for all
### q for all
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.wnow,att.exnow,
    att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,
    att.s3d,att.s3ch1,att.s3ch2,att.city,att.flow,att.wcat,
    att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
    att.j3d,att.j3ch1,att.j3ch2,att.gn,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where(att.flow==1).order_by(att.id.desc())
    attdata_ = [t for t in qu]
    attz_= dict_helper(attdata_)
    id=0
    #for counters
    #all
    qua = att.select(att.id) # ALL
    attdata_a = [t for t in qua]
    attz_a= dict_helper(attdata_a)  
    quc = att.select(att.id).where(att.flow==2) # Finished
    attdata_c = [t for t in quc]
    attz_c= dict_helper(attdata_c)  
    qur = att.select(att.id).where(att.flow.is_null(True)) # new! jus registref!
    attdata_r = [t for t in qur]
    attz_r= dict_helper(attdata_r)       
    qup = att.select(att.id).where(att.flow==1) # in Flow NOW!
    attdata_p = [t for t in qup]
    attz_p= dict_helper(attdata_p)           
    
    # return render_template('new_at.html', optdata__oz=optdata__oz,cntrydata_o=cntrydata_o,cntrydata__oz=cntrydata__oz,cpdata_o=cpdata_o,cpdata__oz=cpdata__oz,wcatdata_o=wcatdata_o, wcatdata__oz=wcatdata__oz, sname_ph=sname_ph, fname_ph=fname_ph, CJ=CJ,SN=SN,id=id,appHost=appHost,appPort=appPort)
    return render_template('new_at_inflow.html', attz_a=attz_a, attz_r=attz_r, attdata_p=attdata_p, attz_p=attz_p,attdata_c=attdata_c, attz_c=attz_c,attdata_=attdata_, attz_=attz_,CJ=CJ,SN=SN,id=id,appHost=appHost,appPort=appPort)
########################    


@app.route('/new-ath-reg', methods = ['POST', 'GET'])
def newatreg(): 
    # set_opnop()
    ### q for all
### q for all
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.wnow,att.exnow,
    att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,
    att.s3d,att.s3ch1,att.s3ch2,att.city,att.flow,att.wcat,
    att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
    att.j3d,att.j3ch1,att.j3ch2,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where(att.flow.is_null(True)).order_by(att.id.desc())
    attdata_ = [t for t in qu]
    attz_= dict_helper(attdata_)
    id=0
    #for counters
    qua = att.select(att.id) # ALL
    attdata_a = [t for t in qua]
    attz_a= dict_helper(attdata_a)     
    quc = att.select(att.id).where(att.flow==2) # Finished
    attdata_c = [t for t in quc]
    attz_c= dict_helper(attdata_c)  
    qur = att.select(att.id).where(att.flow.is_null(True)) # new! jus registref!
    attdata_r = [t for t in qur]
    attz_r= dict_helper(attdata_r)       
    qup = att.select(att.id).where(att.flow==1) # in Flow NOW!
    attdata_p = [t for t in qup]
    attz_p= dict_helper(attdata_p)         
    
    # return render_template('new_at.html', optdata__oz=optdata__oz,cntrydata_o=cntrydata_o,cntrydata__oz=cntrydata__oz,cpdata_o=cpdata_o,cpdata__oz=cpdata__oz,wcatdata_o=wcatdata_o, wcatdata__oz=wcatdata__oz, sname_ph=sname_ph, fname_ph=fname_ph, CJ=CJ,SN=SN,id=id,appHost=appHost,appPort=appPort)
    return render_template('new_at_reg.html', attz_a=attz_a, attz_r=attz_r,attdata_p=attdata_p, attz_p=attz_p,attdata_c=attdata_c, attz_c=attz_c,attdata_=attdata_, attz_=attz_,CJ=CJ,SN=SN,id=id,appHost=appHost,appPort=appPort)
########################    





@app.route('/new-ath-endz', methods = ['POST', 'GET'])
def newatendz(): 
    # set_opnop()
    ### q for all
### q for all
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.wnow,att.exnow,
    att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,
    att.s3d,att.s3ch1,att.s3ch2,att.city,att.flow,att.wcat,
    att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
    att.j3d,att.j3ch1,att.j3ch2,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where(att.flow==2).order_by(att.id.desc())
    attdata_ = [t for t in qu]
    attz_= dict_helper(attdata_)
    id=0
    #for counters
    qua = att.select(att.id) # ALL
    attdata_a = [t for t in qua]
    attz_a= dict_helper(attdata_a) 
    quc = att.select(att.id).where(att.flow==2) # Finished
    attdata_c = [t for t in quc]
    attz_c= dict_helper(attdata_c)  
    qur = att.select(att.id).where(att.flow.is_null(True)) # new! jus registref!
    attdata_r = [t for t in qur]
    attz_r= dict_helper(attdata_r)       
    qup = att.select(att.id).where(att.flow==1) # in Flow NOW!
    attdata_p = [t for t in qup]
    attz_p= dict_helper(attdata_p)       
    
    # return render_template('new_at.html', optdata__oz=optdata__oz,cntrydata_o=cntrydata_o,cntrydata__oz=cntrydata__oz,cpdata_o=cpdata_o,cpdata__oz=cpdata__oz,wcatdata_o=wcatdata_o, wcatdata__oz=wcatdata__oz, sname_ph=sname_ph, fname_ph=fname_ph, CJ=CJ,SN=SN,id=id,appHost=appHost,appPort=appPort)
    return render_template('new_at_endz.html', attz_a=attz_a, attz_r=attz_r,attdata_p=attdata_p, attz_p=attz_p,attdata_c=attdata_c, attz_c=attz_c,attdata_=attdata_, attz_=attz_,CJ=CJ,SN=SN,id=id,appHost=appHost,appPort=appPort)
########################    


###|    At flow(marshal)  module / model
###|
###|
@app.route('/new-athlete', methods = ['POST', 'GET'])
def newat(): 
    # set_opnop()
    ### q for all
### q for all
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.wnow,att.exnow,att.gn,
    att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,
    att.s3d,att.s3ch1,att.s3ch2,att.city,att.flow,att.wcat,
    att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
    att.j3d,att.j3ch1,att.j3ch2,cat.wcat,att.wcat_id,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).order_by(att.id.desc())
    attdata_ = [t for t in qu]
    attz_= dict_helper(attdata_)
    id=0
## Weight category
    q_wcat = cat.select(cat.sex,cat.wcat_id,cat.wcat,cat.lwcat)
    wcatdata_o = [t for t in q_wcat] 
    wcatdata__oz = dict_helper(wcatdata_o)
## Countryz    
    q_cntry = country.select(country.country_id,country.name,country.flag,country.img).order_by(country.country_id.asc())
    cntrydata_o = [t for t in q_cntry] 
    cntrydata__oz = dict_helper(cntrydata_o)
    #for counters
    quc = att.select(att.id).where(att.flow==2) # Finished
    attdata_c = [t for t in quc]
    attz_c= dict_helper(attdata_c)  
    qur = att.select(att.id).where(att.flow.is_null(True)) # new! jus registref!
    attdata_r = [t for t in qur]
    attz_r= dict_helper(attdata_r)       
    qup = att.select(att.id).where(att.flow==1) # in Flow NOW!
    attdata_p = [t for t in qup]
    attz_p= dict_helper(attdata_p)        
    
    # return render_template('new_at.html', optdata__oz=optdata__oz,cntrydata_o=cntrydata_o,cntrydata__oz=cntrydata__oz,cpdata_o=cpdata_o,cpdata__oz=cpdata__oz,wcatdata_o=wcatdata_o, wcatdata__oz=wcatdata__oz, sname_ph=sname_ph, fname_ph=fname_ph, CJ=CJ,SN=SN,id=id,appHost=appHost,appPort=appPort)
    return render_template('new_at.html', cntrydata_o=cntrydata_o,cntrydata__oz=cntrydata__oz,wcatdata_o=wcatdata_o,wcatdata__oz=wcatdata__oz,attdata_r=attdata_r, attz_r=attz_r, attdata_p=attdata_p, attz_p=attz_p,attdata_c=attdata_c, attz_c=attz_c,attdata_=attdata_, attz_=attz_,CJ=CJ,SN=SN,id=id,appHost=appHost,appPort=appPort)
########################    



###|    Staff(group)  module / model
###|
###|
@app.route('/staff', methods = ['POST', 'GET'])
def staff():
    ### edit staff data
    if request.method == "POST":
        jid = request.form.get("jgrpid")
        jname = request.form.get("id_jnamez_")
        jpost = request.form.get("id_jpostruz_")
        jcat = request.form.get("id_catz_")
        jcity = request.form.get("id_jcityz_")
        ex_upd=jgroup.update({jgroup.j_nane:jname,jgroup.j_post_ru:jpost,jgroup.j_cat:jcat,jgroup.j_city:jcity}).where(jgroup.j_id==jid)
        ex_upd.execute()
        
    ### q for all
    args = request.args
    jgrp1 = args.get("g1", default="0", type=int)
    jgrp2 = args.get("g2", default="0", type=int)
    jgrp3 = args.get("g3", default="0", type=int)
    jgrp4 = args.get("g4", default="0", type=int)
    jgrp5 = args.get("g5", default="0", type=int)
    quj = jgroup.select(jgroup.j_id,jgroup.j_nane,jgroup.j_group,jgroup.j_post,jgroup.j_post_ru,jgroup.j_city,jgroup.j_cat)#.where(jgroup.j_group==1)
    if jgrp1==1:
        quj = jgroup.select(jgroup.j_id,jgroup.j_nane,jgroup.j_group,jgroup.j_post,jgroup.j_post_ru,jgroup.j_city,jgroup.j_cat).where(jgroup.j_group==1)
    if jgrp2==1:
        quj = jgroup.select(jgroup.j_id,jgroup.j_nane,jgroup.j_group,jgroup.j_post,jgroup.j_post_ru,jgroup.j_city,jgroup.j_cat).where(jgroup.j_group==2)
    if jgrp3==1:
        quj = jgroup.select(jgroup.j_id,jgroup.j_nane,jgroup.j_group,jgroup.j_post,jgroup.j_post_ru,jgroup.j_city,jgroup.j_cat).where(jgroup.j_group==3)
    if jgrp4==1:
        quj = jgroup.select(jgroup.j_id,jgroup.j_nane,jgroup.j_group,jgroup.j_post,jgroup.j_post_ru,jgroup.j_city,jgroup.j_cat).where(jgroup.j_group==4)
    if jgrp5==1:
        quj = jgroup.select(jgroup.j_id,jgroup.j_nane,jgroup.j_group,jgroup.j_post,jgroup.j_post_ru,jgroup.j_city,jgroup.j_cat).where(jgroup.j_group==5)

    # return redirect(url_for('user', name = username))
    attdata_ = [t for t in quj]
    attz_= dict_helper(attdata_)
      
    return render_template('staff.html',attdata_=attdata_, attz_=attz_,CJ=CJ,SN=SN,id=id,appHost=appHost,appPort=appPort)
########################    



###|    At flow(marshal)  module / model
###|
###|

# @lru_cache(maxsize=None)
@app.route('/flow', methods = ['POST', 'GET'])
def flow(): 
    # set_opnop()
    set_app_weight_now()
    set_op_now(id=0)
    set_nop_now(id=0)

### q for op
    qop = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.wnow,att.exnow,att.city,
    att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,
    att.s3d,att.s3ch1,att.s3ch2,ranks.rid,ranks.wcat_id,ranks.wcat,
    ranks.r_ms,ranks.r_kms,ranks.r_r1,ranks.r_r2,ranks.r_r3,
    ranks.r_r1j,ranks.r_r2j,ranks.r_r3j,ranks.wr,ranks.r_msmk,
    ranks.wr_snatch,ranks.wr_cj,ranks.wr_total,
    ranks.wr_when,ranks.wr_where,ranks.wr_who,
    att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
    att.j3d,att.j3ch1,att.j3ch2,cat.wcat,att.wcat_id,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    # country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).switch(att).join(ranks,on=(att.rank_id == ranks.rid)).where(att.op==1)
    country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).switch(att).join(ranks,on=(att.rank_id == ranks.wcat_id)).where(att.op==1)


    


    # //
    # --.join(ranks,on=(att.rank_id == ranks.rid))
    # country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where(att.op==1)
    attopdata = [t for t in qop]
### q for all
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.wnow,att.exnow,
    att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,
    att.s3d,att.s3ch1,att.s3ch2,att.city,
    att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
    att.j3d,att.j3ch1,att.j3ch2,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where(att.flow.is_null(0))
    attdata = [t for t in qu]
    attz = dict_helper(attdata)
    id=0
    fname_ph=faker.first_name_male()
    sname_ph=faker.last_name_male()

    # file_extension(category='image')

    # sname_ph=faker.name_female()
    
## OPTIONS ARRAY
    q_opt = opt.select(opt.o_name,opt.o_val,opt.opt_id,opt.o_desc,opt.o_descoff,opt.o_param)
    optdata_o = [t for t in q_opt] 
    optdata__oz = dict_helper(optdata_o)    
## OTHER ATT DATAZ
## Weight category
    q_wcat = cat.select(cat.sex,cat.wcat_id,cat.wcat,cat.lwcat)
    wcatdata_o = [t for t in q_wcat] 
    wcatdata__oz = dict_helper(wcatdata_o)
## Countryz    
    q_cntry = country.select(country.country_id,country.name,country.flag,country.img).order_by(country.country_id.asc())
    cntrydata_o = [t for t in q_cntry] 
    cntrydata__oz = dict_helper(cntrydata_o)
## City / place    
    # idList = [1,2,6,15,17,22,61,71,74,75,82,88,90,97,100,141,170,188,190,192,218]
    idList = [97]
    # q_cp = cities.select(cities.cities_id,cities.region_id,cities.country_id,cities.cname).where(cities.country_id==1).join(country,on=(cities.country_id == country.country_id)).order_by((country.name.asc()))
    # q_cp = cities.select(cities.cities_id,cities.region_id,cities.country_id,cities.cname).where(cities.country_id==1).order_by((cities.cname.asc()))
    q_cp = cities.select(cities.cities_id,cities.region_id,cities.country_id,cities.cname).where(cities.country_id.in_(idList)).order_by(cities.cname.asc())
    # q_cp = cities.select(cities.cities_id,cities.region_id,cities.country_id,cities.cname).where(cities.country_id==country.country_id).join(country,on=(cities.country_id == country.country_id)).order_by(cities.cname.asc())
    cpdata_o = [t for t in q_cp] 
    cpdata__oz = dict_helper(cpdata_o)
    
    
    #######return jsonify({'All athletes': attz})
    #return render_template('double.html', attdata=attdata, attz=attz,CJ=CJ,SN=SN)
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()

    # ???????
    # exec(open('v7core.py').read())
    # exec(open('v7core.py').read())
    # daemod_run = subprocess.run(['python3.10', 'v7core.py'])
    # attopdata
    

    if "iphone" in user_agent:
        attdata = [t for t in qu]
        return render_template('flow-clean.html', attdata=attdata, attz=attz,CJ=CJ,SN=SN)
    elif "android" in user_agent:
        return render_template('flow-clean.html', attdata=attdata, attz=attz,CJ=CJ,SN=SN)
    else:
        return render_template('flow.html', optdata__oz=optdata__oz,cntrydata_o=cntrydata_o,cntrydata__oz=cntrydata__oz,cpdata_o=cpdata_o,cpdata__oz=cpdata__oz,wcatdata_o=wcatdata_o, wcatdata__oz=wcatdata__oz, sname_ph=sname_ph, fname_ph=fname_ph,attopdata=attopdata, attdata=attdata, attz=attz,CJ=CJ,SN=SN,id=id,appHost=appHost,appPort=appPort)
########################    

@app.route(BASE_URL+'/nf', methods =  ['POST'])
def new_flow():
 # print(f'name: {faker.name()}')
    # print(f'address: {faker.address()}')
    # print(f'text: {faker.text()}')
    # print(f'First name: {faker.first_name()}')
    # print(f'Last name: {faker.last_name()}')

    # print(f'Random int: {faker.random_int(0, 100)}')
    # print(f'Random digit: {faker.random_digit()}')
    # faker.city()
    # faker.country()
    # faker.country_code()

    if request.method == 'POST':
        #sex = request.form['genderadd']
        #sex = request.form.get('genderadd')
        # sname = request.form['snameadd']
        # fname = request.form['fnameadd']
        # s1 = request.form['s1add']
        # j1 = request.form['j1add']
## Also Att dataz
        # own_weight = request.form['owadd']
        # weight_cat = request.form['wcatadd']
        # countryz = request.form['countrieszadd']
        # place =  request.form['placeszadd']
        
        bday = '22/12/2022'
        


        weight_cat = 7
        #my_data = att(sex, sname, fname, s1, j1)
        # db.session.add(my_data)
        # db.session.commit()
        # mycursor = db.cursor()
        # sql = "INSERT INTO v7now (sex, secondname, firstname, snatch1, cleanjerk1, ownweight, wcat_id, country_id, city_id, birth) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # val = (1, sname, fname, s1, j1, own_weight, weight_cat, countryz, place, bday)
        # mycursor.execute(sql, val)
        # db.commit()
        # print(mycursor.rowcount, "record inserted.")
        #fn=faker.first_name()
        #sn=faker.second_name()
        print("1 record inserted, ID:", )
        
        flash("Employee Inserted Successfully")

   
    return render_template('flow-new.html')


@app.route(BASE_URL+'/setop/<int:id>', methods=['GET', 'POST','DELETE'])
def setop_alhlete(id):
    mycursor = db.cursor()    
    if request.method == 'POST':
        val = id
        #clean OP
        sql_cl = "UPDATE v7now SET op=0,nextop=0 WHERE 1"
        mycursor.execute(sql_cl)
        db.commit()
        sql = "UPDATE v7now SET op=1 WHERE id= %s"
        #sql = "DELETE FROM v7now WHERE id= %s"
        #val = (id)
        mycursor.execute(sql, val)
        db.commit()
        print(mycursor.rowcount, "record deleted.") 
        print("1 record OPed, ID:", mycursor.lastrowid)
        flash("SETOP AT is Successfully!")
    mycursor.close()
    return redirect(url_for('flow',delcount=mycursor.rowcount))




#######################
#######################    
#######################
@app.route(BASE_URL+'/chge/<int:id>/<int:status>', methods=['GET', 'POST','DELETE'])
def chge_status_flow(id,status):
    mycursor = db.cursor()    
    if request.method == 'POST':
        sql = "UPDATE v7now SET flow_=%s WHERE id=%s"
        val = (status,id)
        mycursor.execute(sql, val)
        db.commit()
        print(mycursor.rowcount, "record deleted.") 
        print("1 record deleted, ID:", mycursor.lastrowid)
        flash("DELETING AT is Successfully!")
    mycursor.close()        
    return redirect(url_for('newat',delcount=mycursor.rowcount))



#######################
#######################    
#######################
@app.route(BASE_URL+'/del/<int:id>', methods=['GET', 'POST','DELETE'])
def del_alhlete(id):
    mycursor = db.cursor()    
    if request.method == 'POST':
        sql = "DELETE FROM v7now WHERE id = %s"
        val = id
        #sql = "DELETE FROM v7now WHERE id= %s"
        #val = (id)
        mycursor.execute(sql, val)
        db.commit()
        print(mycursor.rowcount, "record deleted.") 
        print("1 record deleted, ID:", mycursor.lastrowid)
        flash("DELETING AT is Successfully!")
    #run v7core DAEMON
    set_app_weight_now()
    #exec(open('v7core.py').read())
    # daemod_run = subprocess.run(['python3.10', 'v7core.py'])        
    mycursor.close()
    return redirect(url_for('newat',delcount=mycursor.rowcount))



@app.route(BASE_URL+'/set_ava/<int:id>', methods=['GET', 'POST','DELETE'])
def set_ava(id):
    mycursor = db.cursor()   

    # initialize the camera
    # cam = VideoCapture(0)   # 0 -> index of camera
    # s, img = cam.read()
    # if s:    # frame captured without any errors
        # namedWindow("cam-test",CV_GUI_NORMAL)
        # imshow("cam-test",img)
        # namedWindow("cam-test")
        # imshow("cam-test",img)        
        # waitKey(0)
        # destroyWindow("cam-test")
        # imwrite("filename.jpg",img) #save image

    if request.method == 'POST':
        presentDate = randint(0, 9) 
        sql = "UPDATE v7now SET avatar='/img/avatars/defava0.png' WHERE id = %s"
        val = id
        #sql = "DELETE FROM v7now WHERE id= %s"
        #val = (id)
        mycursor.execute(sql, val)
        db.commit()
        print(mycursor.rowcount, "record UPD.") 
        print("1 record upd!, ID:", mycursor.lastrowid)
        flash("UPD AT is Successfully!")
    #run v7core DAEMON
    set_app_weight_now()
    #exec(open('v7core.py').read())
    # daemod_run = subprocess.run(['python3.10', 'v7core.py'])        
    mycursor.close()
    return redirect(url_for('newat',delcount=mycursor.rowcount))


#######################
#######################   
#       rejectapp
#######################
@app.route(BASE_URL+'/rejectapp/<int:id>', methods=['GET', 'POST','DELETE'])
def rejectapp(id):
    mycursor = db.cursor()    
    if request.method == 'POST':
        appNOW =''
        sql = "SELECT exnow FROM v7now WHERE id = %s"
        val = id
        mycursor.execute(sql, val)
        query_result = mycursor.fetchone()
        print(query_result,'@@@')
        print(type(query_result))
        for tmpz_ in query_result:
            appNOW = tmpz_
            print(tmpz_,'--',appNOW, '========')

# //

        print('@@',appNOW)
        if(appNOW=='s1'):          
            rej_q = att.update({att.s1ig:-1,att.s2:att.s1,att.s2ig:-1,att.s3:att.s2,att.s3ig:-1}).where((att.id==id)).execute()
            print(id,': IDz !!!')      
            print('***** SNATCH 1')
        if(appNOW=='s2'):
            rej_q = att.update({att.s2ig:-1,att.s3ig:-1}).where((att.id==id)).execute()
            print('***** SNATCH 2')
        if(appNOW=='s3'):
            rej_q = att.update({att.s3ig:-1}).where((att.id==id)).execute()
            print('***** SNATCH 3')
        if(appNOW=='j1'):
            rej_q = att.update({att.j1ig:-1,att.j2:att.j1,att.j2ig:-1,att.j3:att.j2,att.j3ig:-1}).where((att.id==id)).execute()
            print('***** cJERK 1')
        if(appNOW=='j2'):
            rej_q = att.update({att.j2ig:-1,att.j2:att.j1,att.j3ig:-1,att.j3:att.j2}).where((att.id==id)).execute()
            print('***** cJERK 2')
        if(appNOW=='j3'):
            rej_q = att.update({att.j3ig:-1,att.j3:att.j2}).where((att.id==id)).execute()
            print('***** cJERK 3')    

    #run v7core DAEMON
    set_app_weight_now()
    #and_onemore() %))))))))
    # daemod_run = subprocess.run(['python3.10', 'v7core.py'])
    #exec(open('v7core.py').read())
    mycursor.close()
    db.close()
    return redirect(url_for('flow',rowcount=mycursor.rowcount))



#######################
#######################    
#######################
@app.route('/judge-cmd-1/', methods=['GET', 'POST','DELETE'])
def jcmd1():



    

    mycursor = db.cursor()    
    mycursor.execute("SELECT id FROM v7now WHERE op=1;")
    q_res = mycursor.fetchone()
    # print(q_res[0], '  --**!')
    id = q_res[0]
    mycursor = db.cursor()    


    # mycursor.execute("SELECT exnow FROM v7now WHERE op=1;")
    # qe_res = mycursor.fetchone()    
    # exnow = qe_res[0]

    # match  qe_res[0]:
    #     case 's3':
    #         print(exnow, 'id:', id,  'S3  _______**!')
    #         sql = "UPDATE v7now SET snatch3isget=1 WHERE op=1 AND exnow='s3' AND snatch1isget IS NOT NULL AND snatch2isget IS NOT NULL AND snatch3isget IS NULL AND cleanjerk1isget IS NULL AND cleanjerk2isget IS NULL AND cleanjerk3isget IS NULL"            
    #         mycursor.execute(sql)  
    #         db.commit()
    #         #do #1 & // set_app_weight_now()
    #         set_app_weight_now()
    #         #do #2!
    #         set_op_now(id)
    #         set_nop_now(id)
    #         #
    #     case 's2':
    #         print(exnow, 'id:', id,  'S2  _______**!')
    #         sql = "UPDATE v7now SET snatch2isget=1 WHERE op=1 AND exnow='s2' AND snatch1isget IS NOT NULL AND snatch2isget IS NULL AND snatch3isget IS NULL AND cleanjerk1isget IS NULL AND cleanjerk2isget IS NULL AND cleanjerk3isget IS NULL"
    #         mycursor.execute(sql)  
    #         db.commit()            
    #     case 's1':
    #         print(exnow, 'id:', id,  'S1  _______**!')
    #         sql = "UPDATE v7now SET snatch1isget=1 WHERE op=1 AND exnow='s1' AND snatch1isget IS NULL AND snatch2isget IS NULL AND snatch3isget IS NULL AND cleanjerk1isget IS NULL AND cleanjerk2isget IS NULL AND cleanjerk3isget IS NULL"
    #         mycursor.execute(sql)  
    #         db.commit()            
    #     case 'j3':
    #         print(exnow, 'id:', id,  'J3  _______**!')
    #         sql = "UPDATE v7now SET cleanjerk3=1 WHERE op=1 AND exnow='j3' AND snatch1isget IS NOT NULL AND snatch2isget IS NOT NULL AND snatch3isget IS NOT NULL AND cleanjerk1isget IS NOT NULL AND cleanjerk2isget IS NOT NULL AND cleanjerk3isget IS NULL"            
    #         mycursor.execute(sql)  
    #         db.commit()            
    #     case 'j2':
    #         print(exnow, 'id:', id,  'J2  _______**!')
    #         sql = "UPDATE v7now SET cleanjerk2=1 WHERE op=1 AND exnow='j2' AND snatch1isget IS NOT NULL AND snatch2isget IS NOT NULL AND snatch3isget IS NOT NULL AND cleanjerk1isget IS NOT NULL AND cleanjerk2isget IS NULL AND cleanjerk3isget IS NULL"      
    #         mycursor.execute(sql)  
    #         db.commit()                        
    #     case 'j1':
    #         print(exnow, 'id:', id,  'J1  _______**!')
    #         sql = "UPDATE v7now SET cleanjerk1=1 WHERE op=1 AND exnow='j1' AND snatch1isget IS NOT NULL AND snatch2isget IS NOT NULL AND snatch3isget IS NOT NULL AND cleanjerk1isget IS NULL AND cleanjerk2isget IS NULL AND cleanjerk3isget IS NULL"      
    #         mycursor.execute(sql)  
    #         db.commit()                                    


    # print(mycursor.rowcount, "record UPDATEd.") 
    # print("1 record UPDATEd, ID:", mycursor.lastrowid)
    # flash("UPDATING AT is Successfully!")
    # set_app_weight_now()
    # return redirect(url_for('tablo',delcount=mycursor.rowcount))
    return redirect(url_for('tablo',delcount=mycursor.rowcount))

#######################
#######################    
#######################




@app.route('/judge-cmd-0/', methods=['GET', 'POST','DELETE'])
def jcmd0():

    # mycursor = db.cursor()    
    # mycursor.execute("SELECT id FROM v7now WHERE op=1;")
    # q_res = mycursor.fetchone()
    # # print(q_res[0], '  --**!')
    # id = q_res[0]
    mycursor = db.cursor()    
    mycursor.execute("SELECT exnow FROM v7now WHERE op=1;")
    qe_res = mycursor.fetchone()    
    exnow = qe_res[0]


# ????  СКОПОМ ВСЕХ НЕ ЗАЩИТЫВАЕТ ((((((( (суко пля)
# ????  СКОПОМ ВСЕХ НЕ ЗАЩИТЫВАЕТ ((((((( (суко пля)
# ????  СКОПОМ ВСЕХ НЕ ЗАЩИТЫВАЕТ ((((((( (суко пля)
# ????  СКОПОМ ВСЕХ НЕ ЗАЩИТЫВАЕТ ((((((( (суко пля)
# ????  СКОПОМ ВСЕХ НЕ ЗАЩИТЫВАЕТ ((((((( (суко пля)
# ????  СКОПОМ ВСЕХ НЕ ЗАЩИТЫВАЕТ ((((((( (суко пля)
# ????  СКОПОМ ВСЕХ НЕ ЗАЩИТЫВАЕТ ((((((( (суко пля)
# ????  СКОПОМ ВСЕХ НЕ ЗАЩИТЫВАЕТ ((((((( (суко пля)
# ????  СКОПОМ ВСЕХ НЕ ЗАЩИТЫВАЕТ ((((((( (суко пля)
# ????  СКОПОМ ВСЕХ НЕ ЗАЩИТЫВАЕТ ((((((( (суко пля)
# ????  СКОПОМ ВСЕХ НЕ ЗАЩИТЫВАЕТ ((((((( (суко пля)
# ????  СКОПОМ ВСЕХ НЕ ЗАЩИТЫВАЕТ ((((((( (суко пля)
# ************
    # mycursor = db.cursor()    
    # # sql = "UPDATE v7now SET snatch3=%s,s3ch1=%s,s3ch2=%s WHERE id= %s"
    # sql = "UPDATE v7now SET snatch3=%s,s3ch1=snatch3,s3ch2=snatch3 WHERE id= %s"
    # val = (s3,id)
    # mycursor.execute(sql,val)
    # db.commit()

    # sql = "UPDATE v7now SET snatch1= %s WHERE id= %s AND exnow='s1' AND s1ch1 IS NOT NULL AND s1ch2 IS NULL"
    # val = (appw,id)
    # mycursor.execute(sql,val)
    # db.commit()
    


    # if(exnow=='s1'):
    #     print(exnow, 'id:', id,  'S1  _______**!')
    #     sql = "UPDATE v7now SET snatch1isget=0 WHERE op=1 AND exnow='s1' AND snatch1isget IS NULL AND snatch2isget IS NULL AND snatch3isget IS NULL AND cleanjerk1isget IS NULL AND cleanjerk2isget IS NULL AND cleanjerk3isget IS NULL"
    #     mycursor.execute(sql)  
    #     db.commit()         
    # if (exnow=='s2'):
    #     print(exnow, 'id:', id,  'S2  _______**!')
    #     sql = "UPDATE v7now SET snatch2isget=0 WHERE op=1 AND exnow='s2' AND snatch1isget IS NOT NULL AND snatch2isget IS NULL AND snatch3isget IS NULL AND cleanjerk1isget IS NULL AND cleanjerk2isget IS NULL AND cleanjerk3isget IS NULL"
    #     mycursor.execute(sql)  
    #     db.commit()                     
    # if(exnow=='s3'):
    #     sql = "UPDATE v7now SET snatch3isget=0 WHERE op=1 AND exnow='s3' AND snatch1isget IS NOT NULL AND snatch2isget IS NOT NULL AND snatch3isget IS NULL AND cleanjerk1isget IS NULL AND cleanjerk2isget IS NULL AND cleanjerk3isget IS NULL"            
    #     mycursor.execute(sql)  
    #     db.commit()


    #    match  qe_res[0]:
    #     case 's3':
    #         print(exnow, 'id:', id,  'S3  _______**!')
    #         sql = "UPDATE v7now SET snatch3isget=0 WHERE op=1 AND exnow='s3' AND snatch1isget IS NOT NULL AND snatch2isget IS NOT NULL AND snatch3isget IS NULL AND cleanjerk1isget IS NULL AND cleanjerk2isget IS NULL AND cleanjerk3isget IS NULL"            
    #         mycursor.execute(sql)  
    #         db.commit()
    #     case 's2':
    #         print(exnow, 'id:', id,  'S2  _______**!')
    #         sql = "UPDATE v7now SET snatch2isget=0 WHERE op=1 AND exnow='s2' AND snatch1isget IS NOT NULL AND snatch2isget IS NULL AND snatch3isget IS NULL AND cleanjerk1isget IS NULL AND cleanjerk2isget IS NULL AND cleanjerk3isget IS NULL"
    #         mycursor.execute(sql)  
    #         db.commit()            
    #     case 's1':
    #         print(exnow, 'id:', id,  'S1  _______**!')
    #         sql = "UPDATE v7now SET snatch1isget=0 WHERE op=1 AND exnow='s1' AND snatch1isget IS NULL AND snatch2isget IS NULL AND snatch3isget IS NULL AND cleanjerk1isget IS NULL AND cleanjerk2isget IS NULL AND cleanjerk3isget IS NULL"
    #         mycursor.execute(sql)  
    #         db.commit()            
    #     case 'j3':
    #         print(exnow, 'id:', id,  'J3  _______**!')
    #         sql = "UPDATE v7now SET cleanjerk3=0 WHERE op=1 AND exnow='j3' AND snatch1isget IS NOT NULL AND snatch2isget IS NOT NULL AND snatch3isget IS NOT NULL AND cleanjerk1isget IS NOT NULL AND cleanjerk2isget IS NOT NULL AND cleanjerk3isget IS NULL"            
    #         mycursor.execute(sql)  
    #         db.commit()            
    #     case 'j2':
    #         print(exnow, 'id:', id,  'J2  _______**!')
    #         sql = "UPDATE v7now SET cleanjerk2=0 WHERE op=1 AND exnow='j2' AND snatch1isget IS NOT NULL AND snatch2isget IS NOT NULL AND snatch3isget IS NOT NULL AND cleanjerk1isget IS NOT NULL AND cleanjerk2isget IS NULL AND cleanjerk3isget IS NULL"      
    #         mycursor.execute(sql)  
    #         db.commit()                        
    #     case 'j1':
    #         print(exnow, 'id:', id,  'J1  _______**!')
    #         sql = "UPDATE v7now SET cleanjerk1=0 WHERE op=1 AND exnow='j1' AND snatch1isget IS NOT NULL AND snatch2isget IS NOT NULL AND snatch3isget IS NOT NULL AND cleanjerk1isget IS NULL AND cleanjerk2isget IS NULL AND cleanjerk3isget IS NULL"      
    #         mycursor.execute(sql)  
    #         db.commit()   



        # print(mycursor.rowcount, "record UPDATEd.") 
        # print("1 record UPDATEd, ID:", mycursor.lastrowid)
        # flash("UPDATING AT is Successfully!")
    # set_app_weight_now()
    return redirect(url_for('tablo',delcount=mycursor.rowcount))








# // для judge-cmd-1 - НАДО ИСПРАВИТЬ!!!
@app.route('/judge-cmd-1/<int:id>/<string:exnow>', methods=['GET','POST','DELETE'])
def jcmd1full(id,exnow):
    if(exnow=='s3'):
        ex_upd3=att.update({att.s3ig:1}).where( (att.s3ig.is_null(1))
    & (att.s2ig.is_null(0))
    & (att.s1ig.is_null(0))
    & (att.j1ig.is_null(1)) & (att.j2ig.is_null(1)) & (att.j3ig.is_null(1))
    & (att.exnow==exnow)
    & (att.id==id)
    )
        u3 = ex_upd3.execute()
    # ex_upd1.execute()
    if(exnow=='s2'):
        ex_upd2=att.update({att.s2ig:1}).where( (att.s2ig.is_null(1))
    & (att.s3ig.is_null(1))
    & (att.j1ig.is_null(1)) & (att.j2ig.is_null(1)) & (att.j3ig.is_null(1))
    & (att.exnow==exnow)
    & (att.id==id)
    )
        u2 = ex_upd2.execute()
    # ex_upd2.execute()
    if(exnow=='s1'):
        ex_upd1=att.update({att.s1ig:1}).where( (att.s1ig.is_null(1))
    & (att.s3ig.is_null(1))
    & (att.s2ig.is_null(1))
    & (att.j1ig.is_null(1)) & (att.j2ig.is_null(1)) & (att.j3ig.is_null(1))
    & (att.exnow==exnow)
    & (att.id==id)
    )
        
        u1 = ex_upd1.execute()


# + CLEAN&JERK


    if(exnow=='j3'):
        ex_upd3=att.update({att.j3ig:1}).where( (att.j3ig.is_null(1))
    & (att.s2ig.is_null(0))
    & (att.s1ig.is_null(0))
    & (att.j1ig.is_null(0)) & (att.j2ig.is_null(0)) & (att.j3ig.is_null(1))
    & (att.s1ig.is_null(0))
    & (att.exnow==exnow)
    & (att.id==id)
    )
        u3 = ex_upd3.execute()
    # ex_upd1.execute()
    if(exnow=='j2'):
        ex_upd2=att.update({att.j2ig:1}).where( (att.j2ig.is_null(1))
    & (att.s3ig.is_null(0))
    & (att.j1ig.is_null(0)) & (att.j2ig.is_null(1)) & (att.j3ig.is_null(1))
    & (att.s1ig.is_null(0))
    & (att.exnow==exnow)
    & (att.id==id)
    )
        u2 = ex_upd2.execute()
    # ex_upd2.execute()
    if(exnow=='j1'):

        # *********** YES!!!
        ex_upd1=att.update({att.j1ig:1,att.j2:att.j1+1}).where( (att.j1ig.is_null(1))
    & (att.s3ig.is_null(0))
    & (att.s2ig.is_null(0))
    & (att.s1ig.is_null(0))
    & (att.j1ig.is_null(1)) & (att.j2ig.is_null(1)) & (att.j3ig.is_null(1))
    & (att.exnow==exnow)
    & (att.id==id)
    )
        u1 = ex_upd1.execute()




    set_app_weight_now()

    # sql = "UPDATE v7now SET cleanjerk2=0 WHERE id=%s AND exnow=%s AND snatch1isget IS NOT NULL AND snatch2isget IS NOT NULL AND snatch3isget IS NOT NULL AND cleanjerk1isget IS NOT NULL AND cleanjerk2isget IS NULL AND cleanjerk3isget IS NULL"      
    # mycursor.execute(sql)  
    # db.commit()       
    # set_app_weight_now()
    # return redirect(url_for('tablo'))
    # return jsonify({'athletes UPD:': ex_upd[0]})
    log1='000'
    log2='000'
    log3='000'
    try:
        u1
        log1 = u1
        print('s1')
    except NameError:
        log1 = 'eRRorZzz s1'
        print('XXXX s1')
    try:
        u2
        log2 = u2
        print('s2')
    except NameError:
        log2 = 'eRRorZzz s2'
        print('XXXX s2')
    try:
        u3
        log3 = u3
        print('s3')
    except NameError:
        log3 = 'eRRorZzz s3'
        print('XXXX s3')        

    db.close()
    return {
        "updID1": log1,
        "updID2": log2,
        "updID3": log3,
    }


# // & for 1
# // для judge-cmd-1 - НАДО ИСПРАВИТЬ!!!
# ??????????
@app.route('/judge-cmd-0/<int:id>/<string:exnow>', methods=['GET', 'POST','DELETE'])
def jcmd0full(id,exnow):
    # mycursor = db.cursor()       


    if(exnow=='s3'):
        ex_upd3=att.update({att.s3ig:0}).where( (att.s3ig.is_null(1))
    & (att.s2ig.is_null(0))
    & (att.s1ig.is_null(0))
    & (att.j1ig.is_null(1)) & (att.j2ig.is_null(1)) & (att.j3ig.is_null(1))
    & (att.exnow==exnow)
    & (att.id==id)
    )
        u3 = ex_upd3.execute()
    # ex_upd1.execute()
    if(exnow=='s2'):
        ex_upd2=att.update({att.s2ig:0}).where( (att.s2ig.is_null(1))
    & (att.s3ig.is_null(1))
    & (att.j1ig.is_null(1)) & (att.j2ig.is_null(1)) & (att.j3ig.is_null(1))
    & (att.exnow==exnow)
    & (att.id==id)
    )
        u2 = ex_upd2.execute()
    # ex_upd2.execute()
    if(exnow=='s1'):
        ex_upd1=att.update({att.s1ig:0}).where( (att.s1ig.is_null(1))
    & (att.s3ig.is_null(1))
    & (att.s2ig.is_null(1))
    & (att.j1ig.is_null(1)) & (att.j2ig.is_null(1)) & (att.j3ig.is_null(1))
    & (att.exnow==exnow)
    & (att.id==id)
    )
        u1 = ex_upd1.execute()



    if(exnow=='j3'):
        ex_upd3=att.update({att.j3ig:0}).where( (att.j3ig.is_null(1))
    & (att.s2ig.is_null(0))
    & (att.s1ig.is_null(0))
    & (att.j1ig.is_null(0)) & (att.j2ig.is_null(0)) & (att.j3ig.is_null(1))
    & (att.exnow==exnow)
    & (att.id==id)
    )
        u3 = ex_upd3.execute()
    # ex_upd1.execute()
    if(exnow=='j2'):
        ex_upd2=att.update({att.j2ig:0}).where( (att.j2ig.is_null(1))
    & (att.s3ig.is_null(0))
    & (att.j1ig.is_null(0)) & (att.j2ig.is_null(1)) & (att.j3ig.is_null(1))
    & (att.exnow==exnow)
    & (att.id==id)
    )
        u2 = ex_upd2.execute()
    # ex_upd2.execute()
    if(exnow=='j1'):
        ex_upd1=att.update({att.j1ig:0}).where( (att.j1ig.is_null(1))
    & (att.s3ig.is_null(0))
    & (att.s2ig.is_null(0))
    & (att.j1ig.is_null(1)) & (att.j2ig.is_null(1)) & (att.j3ig.is_null(1))
    & (att.exnow==exnow)
    & (att.id==id)
    )
        u1 = ex_upd1.execute()



    #run v7core DAEMON
    set_app_weight_now()

    # sql = "UPDATE v7now SET cleanjerk2=0 WHERE id=%s AND exnow=%s AND snatch1isget IS NOT NULL AND snatch2isget IS NOT NULL AND snatch3isget IS NOT NULL AND cleanjerk1isget IS NOT NULL AND cleanjerk2isget IS NULL AND cleanjerk3isget IS NULL"      
    # mycursor.execute(sql)  
    # db.commit()       
    # set_app_weight_now()
    # return redirect(url_for('tablo'))
    log1='000'
    log2='000'
    log3='000'
    try:
        u1
        log1 = u1
        print('s1')
    except NameError:
        log1 = 'eRRorZzz s1'
        print('XXXX s1')
    try:
        u2
        log2 = u2
        print('s2')
    except NameError:
        log2 = 'eRRorZzz s2'
        print('XXXX s2')
    try:
        u3
        log3 = u3
        print('s3')
    except NameError:
        log3 = 'eRRorZzz s3'
        print('XXXX s3')        

    # return jsonify({'athletes UPD:': ex_upd[0]})
    db.close()
    return {
        "updID s1": log1,
        "updID s2": log2,
        "updID s3": log3,
    }
   



######################################################
######################################################
######################################################
# s1
######################################################
@app.route('/post_s1/<int:id>/<path:s1>', methods=['GET', 'POST'])
def edit_s1(id,s1):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET snatch1=%s,s1ch1=snatch1,s1ch2=snatch1 WHERE id= %s"
    # sql = "UPDATE v7now SET snatch1=%s,s1ch1=%s,s1ch2=%s WHERE id= %s"
    val = (s1,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT FNAME UPDATEd Successfully")
    mycursor.close()
    return jsonify({'athletes UPD:': mycursor.rowcount})

######################################################
######################################################
######################################################
# s2
######################################################
@app.route('/post_s2/<int:id>/<path:s2>', methods=['GET', 'POST'])
def edit_s2(id,s2):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET snatch2=%s,s2ch1=snatch2,s2ch2=snatch2 WHERE id= %s"
    # sql = "UPDATE v7now SET snatch2=%s,s2ch1=%s,s2ch2=%s WHERE id= %s"
    val = (s2,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT FNAME UPDATEd Successfully")
    mycursor.close()
    return jsonify({'athletes UPD:': mycursor.rowcount})
######################################################
######################################################
######################################################
# s3
######################################################
@app.route('/post_s3/<int:id>/<path:s3>', methods=['GET', 'POST'])
def edit_s3(id,s3):
    mycursor = db.cursor()    
    # sql = "UPDATE v7now SET snatch3=%s,s3ch1=%s,s3ch2=%s WHERE id= %s"
    sql = "UPDATE v7now SET snatch3=%s,s3ch1=snatch3,s3ch2=snatch3 WHERE id= %s"
    val = (s3,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT FNAME UPDATEd Successfully")
    mycursor.close()
    return jsonify({'athletes UPD:': mycursor.rowcount})



######################################################
######################################################
######################################################
# j1
######################################################
@app.route('/post_j1/<int:id>/<path:j1>', methods=['GET', 'POST'])
def edit_j1(id,j1):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET cleanjerk1=%s,cleanjerk1ch1=cleanjerk1,cleanjerk1ch2=cleanjerk1 WHERE id= %s"
    val = (j1,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT FNAME UPDATEd Successfully")
    mycursor.close()
    return jsonify({'athletes UPD:': mycursor.rowcount})

######################################################
######################################################
######################################################
# j2
######################################################
@app.route('/post_j2/<int:id>/<path:j2>', methods=['GET', 'POST'])
def edit_j2(id,j2):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET cleanjerk2=%s,cleanjerk2ch1=cleanjerk2,cleanjerk2ch2=cleanjerk2 WHERE id= %s"
    val = (j2,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT FNAME UPDATEd Successfully")
    mycursor.close()
    return jsonify({'athletes UPD:': mycursor.rowcount})
######################################################
######################################################
######################################################
# j3
######################################################
@app.route('/post_j3/<int:id>/<path:j3>', methods=['GET', 'POST'])
def edit_j3(id,j3):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET cleanjerk3=%s,cleanjerk3ch1=cleanjerk3,cleanjerk3ch2=cleanjerk3 WHERE id= %s"
    val = (j3,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT FNAME UPDATEd Successfully")
    mycursor.close()
    return jsonify({'athletes UPD:': mycursor.rowcount})



######################################################
######################################################
######################################################
# AT WCAT
######################################################
@app.route('/post_wcat/<int:id>/<int:wcatid>', methods=['GET', 'POST'])
def edit_wcat(id,wcatid):
    mycursor = db.cursor()    
    # sql = "UPDATE v7now SET country_id=%s WHERE id= %s"
    sql = "UPDATE v7now SET wcat_id=%s WHERE id= %s"
    val = (wcatid,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT FNAME UPDATEd Successfully")
    mycursor.close()
    return jsonify({'athletes UPD:':  mycursor.rowcount,'dataz:': wcatid})


######################################################
######################################################
######################################################
# AT Country
######################################################
@app.route('/post_country/<int:id>/<path:cname>', methods=['GET', 'POST'])
def edit_country(id,cname):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET country_id=%s WHERE id= %s"
    val = (cname,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT FNAME UPDATEd Successfully")
    mycursor.close()
    return jsonify({'athletes UPD:': mycursor.rowcount})


#######################
#######################     AT city/place
#######################
@app.route('/post_cityplace/<int:id>/<path:cityplace>', methods=['GET', 'POST'])
def post_cityplace(id,cityplace):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET city=%s WHERE id= %s"
    val = (cityplace,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT FNAME UPDATEd Successfully")
    mycursor.close()
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))
    return jsonify({'athletes UPD:': mycursor.rowcount})



#######################
#######################     AT OW
#######################
@app.route('/post_ow/<int:id>/<path:ow>', methods=['GET', 'POST'])
def post_ow(id,ow):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET ownweight=%s WHERE id= %s"
    val = (ow,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT FNAME UPDATEd Successfully")
    mycursor.close()
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))
    return jsonify({'athletes UPD:': mycursor.rowcount})


#######################
#######################     AT SEX
#######################
@app.route('/post_sex/<int:id>/<path:sex>', methods=['GET', 'POST'])
def post_sex(id,sex):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET sex=%s WHERE id= %s"
    val = (sex,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT FNAME UPDATEd Successfully")
    mycursor.close()
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))
    return jsonify({'athletes UPD:': mycursor.rowcount})


#######################
#######################     AT bday
#######################
@app.route('/post_bday/<int:id>/<path:bday>', methods=['GET', 'POST'])
def post_bday(id,bday):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET birth=%s WHERE id= %s"
    val = (bday,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT FNAME UPDATEd Successfully")
    mycursor.close()
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))
    return jsonify({'athletes UPD:': mycursor.rowcount})



#######################
#######################     first name
#######################
@app.route('/edit_idef_edit_/<int:id>/<path:fname>', methods=['GET', 'POST'])
def edit_idef_edit_(id,fname):
    # mycursor = db.cursor()    
    # sql = "UPDATE v7now SET firstname= %s WHERE id= %s"
    # val = (fname,id)
    # mycursor.execute(sql,val)
    # db.commit()
    # flash("AT FNAME UPDATEd Successfully")

    # # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))

    # mycursor.close()
    ex_upd1=att.update({att.sname:fname}).where((att.id == id ))
    u1 = ex_upd1.execute()                  
    return jsonify({'athletes UPD:': u1})


#######################
#######################    second name
#######################
@app.route('/edit_ides_edit_/<int:id>/<path:fname>', methods=['GET', 'POST'])
def edit_ides_edit_(id,fname):
    # mycursor = db.cursor()    
    # sql = "UPDATE v7now SET secondname= %s WHERE id= %s"
    # val = (fname,id)
    # mycursor.execute(sql,val)
    # db.commit()
    # flash("AT FNAME UPDATEd Successfully")
    ex_upd1=att.update({att.fname:fname}).where((att.id == id ))
    u1 = ex_upd1.execute()              
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': u1})



#######################
#######################    s1YES
#######################
@app.route('/post_s1yes/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_s1yes(id,isget):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET snatch1isget= %s WHERE id= %s"
    val = (isget,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT isget UPDATEd Successfully")
    mycursor.close()
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': mycursor.rowcount})


#######################
#######################    s1NOT
#######################
@app.route('/post_s1not/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_s1not(id,isget):
    # mycursor = db.cursor()    
    # sql = "UPDATE v7now SET snatch1isget= %s WHERE id= %s"
    # val = (isget,id)
    # mycursor.execute(sql,val)
    # db.commit()
    # flash("AT isget UPDATEd Successfully")
    # mycursor.close()
    ex_upd1=att.update({att.s1ig:0,att.s2:att.s1,att.exnow:'s2'}).where((att.id == id ))
    u1 = ex_upd1.execute()              
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': u1})

#######################
#######################    s1 REJECT/cancel
#######################
@app.route('/post_s1rej/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_s1rej(id,isget):
    # mycursor = db.cursor()    
    # sql = "UPDATE v7now SET snatch1isget= %s WHERE id= %s"
    # val = (isget,id)
    # mycursor.execute(sql,val)
    # db.commit()
    # flash("AT isget UPDATEd Successfully")
    # mycursor.close()
    ex_upd1=att.update({att.s1ig:None,att.exnow:'s1'}).where((att.id == id ))
    u1 = ex_upd1.execute()              
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:':u1})


#######################
#######################    s1 RESET/NULL
#######################
@app.route('/post_s1reset/<int:id>/', methods=['GET', 'POST'])
def post_s1reset(id):
    # mycursor = db.cursor()    
    # sql = "UPDATE v7now SET snatch1isget=NULL WHERE id= %s"
    # val = (id)
    # mycursor.execute(sql,val)
    # db.commit()
    # flash("AT isget UPDATEd Successfully")
    # mycursor.close()
    ex_upd1=att.update({att.s1ig:None,att.s2ig:None,att.s2d:None,att.s2ch1:None,att.s2ch2:None,att.s3ig:None,att.s3d:None,att.s3ch1:None,att.s3ch2:None,att.exnow:'s1'}).where((att.id == id ))
    u1 = ex_upd1.execute()          
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': u1})



#######################
#######################    s2YES
#######################
@app.route('/post_s2yes/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_s2yes(id,isget):
    # mycursor = db.cursor()    
    # sql = "UPDATE v7now SET snatch2isget= %s WHERE id= %s"
    # val = (isget,id)
    # mycursor.execute(sql,val)
    # db.commit()
    # flash("AT isget UPDATEd Successfully")
    ex_upd1=att.update({att.s2ig:1,att.s3:att.s2+1,att.exnow:'s3'}).where((att.id == id ))
    u1 = ex_upd1.execute()              
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': u1})


#######################
#######################    s2NOT
#######################
@app.route('/post_s2not/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_s2not(id,isget):
    # mycursor = db.cursor()    
    # sql = "UPDATE v7now SET snatch2isget= %s WHERE id= %s"
    # val = (isget,id)
    # mycursor.execute(sql,val)
    # db.commit()
    # flash("AT isget UPDATEd Successfully")
    # mycursor.close()
    ex_upd1=att.update({att.s2ig:0,att.exnow:'s3'}).where((att.id == id ))
    u1 = ex_upd1.execute()              
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': u1})


#######################
#######################    s2 REJECT/cancel
#######################
@app.route('/post_s2rej/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_s2rej(id,isget):
    # mycursor = db.cursor()    
    # sql = "UPDATE v7now SET snatch2isget= %s WHERE id= %s"
    # val = (isget,id)
    # mycursor.execute(sql,val)
    # db.commit()
    # flash("AT isget UPDATEd Successfully")
    # mycursor.close()
    ex_upd1=att.update({att.s2ig:-1,att.exnow:'s3'}).where((att.id == id ))
    u1 = ex_upd1.execute()              
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': u1})


#######################
#######################    s2 RESET/NULL
#######################
@app.route('/post_s2reset/<int:id>/', methods=['GET', 'POST'])
def post_s2reset(id):
    # mycursor = db.cursor()    
    # sql = "UPDATE v7now SET snatch2isget=NULL WHERE id= %s"
    # val = (id)
    # mycursor.execute(sql,val)
    # db.commit()
    # sql = "UPDATE v7now SET snatch2=NULL,s2d=NULL,s2ch1=NULL,s2ch2=NULL WHERE id= %s"
    # val = (id)
    # mycursor.execute(sql,val)
    # db.commit()    


    # flash("AT isget UPDATEd Successfully")
    # mycursor.close()
    ex_upd1=att.update({att.s2ig:None,att.s2d:None,att.s2ch1:None,att.s2ch2:None,att.s3ig:None,att.s3d:None,att.s3ch1:None,att.s3ch2:None,att.s3:None,att.exnow:'s2'}).where((att.id == id ))
    u1 = ex_upd1.execute()                        
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': u1})



#######################
#######################    s3YES
#######################
@app.route('/post_s3yes/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_s3yes(id,isget):
    # mycursor = db.cursor()    
    # sql = "UPDATE v7now SET snatch3isget= %s WHERE id= %s"
    # val = (isget,id)
    # mycursor.execute(sql,val)
    # db.commit()
    # flash("AT isget UPDATEd Successfully")
    # mycursor.close()
    ex_upd1=att.update({att.s3ig:1,att.exnow:'j1'}).where((att.id == id ))
    u1 = ex_upd1.execute()                        
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': u1})


#######################
#######################    s3NOT
#######################
@app.route('/post_s3not/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_s3not(id,isget):
    # mycursor = db.cursor()    
    # sql = "UPDATE v7now SET snatch3isget= %s WHERE id= %s"
    # val = (isget,id)
    # mycursor.execute(sql,val)
    # db.commit()
    # flash("AT isget UPDATEd Successfully")
    # mycursor.close()
    ex_upd1=att.update({att.s3ig:0,att.exnow:'j1'}).where((att.id == id ))
    u1 = ex_upd1.execute()                        
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': u1})

#######################
#######################    s3 REJECT/cancel
#######################
@app.route('/post_s3rej/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_s3rej(id,isget):
    # mycursor = db.cursor()    
    # sql = "UPDATE v7now SET snatch3isget= %s WHERE id= %s"
    # val = (isget,id)
    # mycursor.execute(sql,val)
    # db.commit()
    # flash("AT isget UPDATEd Successfully")
    # mycursor.close()
    ex_upd1=att.update({att.s3ig:-1,att.exnow:'s3'}).where((att.id == id ))
    u1 = ex_upd1.execute()                        
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': u1})


#######################
#######################    s3 RESET/NULL
#######################
@app.route('/post_s3reset/<int:id>/', methods=['GET', 'POST'])
def post_s3reset(id):
    # mycursor = db.cursor()    
    # sql = "UPDATE v7now SET snatch3isget=NULL WHERE id= %s"
    # val = (id)
    # mycursor.execute(sql,val)
    # db.commit()
    # sql = "UPDATE v7now SET snatch3=NULL,s3d=NULL,s3ch1=NULL,s3ch2=NULL WHERE id= %s"
    # val = (id)
    # mycursor.execute(sql,val)
    # db.commit()

    # flash("AT isget UPDATEd Successfully")
    # mycursor.close()
        #ex_upd1=att.update({att.s3ig:None,att.s3d:None,att.s3ch1:None,att.s3ch2:None,att.exnow:'j1'}).where((att.id == id ))
        #u1 = ex_upd1.execute()                    
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
        #return jsonify({'athletes UPD:': u1})
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET exnow='s3',cleanjerk3isget=NULL,cleanjerk1d=NULL,cleanjerk1ch1=NULL,cleanjerk1ch2=NULL,cleanjerk2isget=NULL,cleanjerk2=NULL,cleanjerk2d=NULL,cleanjerk2ch1=NULL,cleanjerk2ch2=NULL,cleanjerk3isget=NULL,cleanjerk3=NULL,cleanjerk3d=NULL,cleanjerk3ch1=NULL,cleanjerk3ch2=NULL,  snatch3isget=NULL,s3d=NULL,s3ch1=NULL,s3ch2=NULL WHERE id= %s"
    val = (id)
    mycursor.execute(sql,val)
    db.commit()
    # sql = "UPDATE v7now SET cleanjerk3=NULL,s3d=NULL,s3ch1=NULL,s3ch2=NULL WHERE id= %s"
    # val = (id)
    # mycursor.execute(sql,val)
    # db.commit()

    flash("AT 1 isget UPDATEd Successfully")
    mycursor.close()
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'post_j1reset = UPD:': mycursor.rowcount})        





#######################
#######################    j1YES
#######################
@app.route('/post_j1yes/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_j1yes(id,isget):
    # mycursor = db.cursor()    
    # sql = "UPDATE v7now SET cleanjerk1isget= %s WHERE id= %s"
    # val = (isget,id)
    # mycursor.execute(sql,val)
    # db.commit()
    # flash("AT isget UPDATEd Successfully")
    # mycursor.close()
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    ex_upd1=att.update({att.j1ig:1,att.j2:att.j2+1,att.exnow:'j2'}).where((att.id == id ))
    u1 = ex_upd1.execute()                
    return jsonify({'athletes UPD:': u1})


#######################
#######################    j1NOT
#######################
@app.route('/post_j1not/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_j1not(id,isget):
    ex_upd1=att.update({att.j1ig:0,att.j2:att.j1,att.exnow:'j2'}).where((att.id == id ))
    u1 = ex_upd1.execute()            
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': u1})


#######################
#######################    j1 REJECT/cancel
#######################
@app.route('/post_j1rej/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_j1rej(id,isget):
    # mycursor = db.cursor()    
    # sql = "UPDATE v7now SET cleanjerk1isget= %s WHERE id= %s"
    # val = (isget,id)
    # mycursor.execute(sql,val)
    # db.commit()
    # flash("AT isget UPDATEd Successfully")
    # mycursor.close()
    ex_upd1=att.update({att.j1ig:isget,att.j2ig:isget,att.j3ig:isget,att.exnow:'finished'}).where((att.id == id ))
    u1 = ex_upd1.execute()        
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': u1})


#######################
#######################    j1 RESET/NULL
#######################
@app.route('/post_j1reset/<int:id>', methods=['GET', 'POST'])
def post_j1reset(id):
    # mycursor = db.cursor()    
    # sql = "UPDATE v7now SET cleanjerk1isget	=NULL WHERE id= %s"
    # val = (id)
    # mycursor.execute(sql,val)
    # # SET EXNOW
    # sql = "UPDATE v7now SET exnow=s1 WHERE id= %s"
    # val = (id)
    # mycursor.execute(sql,val)    
    # db.commit()
    # flash("AT isget UPDATEd Successfully")
    # mycursor.close()
    
    
    # ex_upd1=att.update({att.j3d:None,att.j2d:None,att.j3ch1:None,att.j3ch1:None,att.j2ch2:None,att.j2ch1:None,att.j1ig:None,att.j2ig:None,att.j3ig:None,att.s3:None,att.s2:None, att.exnow:'j1'}).where((att.id == id ))
    # u1 = ex_upd1.execute()    
    # ###### return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    # return jsonify({'athletes UPD:': u1})

    mycursor = db.cursor()    
    sql = "UPDATE v7now SET exnow='j1',cleanjerk1isget=NULL,cleanjerk3isget=NULL,cleanjerk1d=NULL,cleanjerk1ch1=NULL,cleanjerk1ch2=NULL,cleanjerk2isget=NULL,cleanjerk2=NULL,cleanjerk2d=NULL,cleanjerk2ch1=NULL,cleanjerk2ch2=NULL,cleanjerk3isget=NULL,cleanjerk3=NULL,cleanjerk3d=NULL,cleanjerk3ch1=NULL,cleanjerk3ch2=NULL WHERE id= %s"
    val = (id)
    mycursor.execute(sql,val)
    db.commit()
    # sql = "UPDATE v7now SET cleanjerk3=NULL,s3d=NULL,s3ch1=NULL,s3ch2=NULL WHERE id= %s"
    # val = (id)
    # mycursor.execute(sql,val)
    # db.commit()

    flash("AT 1 isget UPDATEd Successfully")
    mycursor.close()
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'post_j1reset = UPD:': mycursor.rowcount})            




#######################
#######################    j2YES
#######################
@app.route('/post_j2yes/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_j2yes(id,isget):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET cleanjerk2isget= %s WHERE id= %s"
    val = (isget,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT isget UPDATEd Successfully")
    mycursor.close()
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': mycursor.rowcount})


#######################
#######################    j2NOT
#######################
@app.route('/post_j2not/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_j2not(id,isget):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET cleanjerk2isget= %s WHERE id= %s"
    val = (isget,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT isget UPDATEd Successfully")
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': mycursor.rowcount})


#######################
#######################    j2 REJECT/cancel
#######################
@app.route('/post_j2rej/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_j2rej(id,isget):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET cleanjerk2isget= %s WHERE id= %s"
    val = (isget,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT isget UPDATEd Successfully")
    mycursor.close()
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': mycursor.rowcount})


#######################
#######################    j2 RESET/NULL
#######################
@app.route('/post_j2reset/<int:id>/', methods=['GET', 'POST'])
def post_j2reset(id):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET cleanjerk2isget=NULL WHERE id= %s"
    val = (id)
    mycursor.execute(sql,val)
    db.commit()
    sql = "UPDATE v7now SET cleanjerk2=NULL,cleanjerk2d=NULL,cleanjerk2ch1=NULL,cleanjerk2ch2=NULL,   cleanjerk3=NULL,cleanjerk3d=NULL,cleanjerk3ch1=NULL,cleanjerk3ch2=NULL WHERE id= %s"
    val = (id)
    mycursor.execute(sql,val)
    db.commit()

    flash("AT isget UPDATEd Successfully")
    mycursor.close()
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': mycursor.rowcount})




#######################
#######################    j3YES
#######################
@app.route('/post_j3yes/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_j3yes(id,isget):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET cleanjerk3isget= %s WHERE id= %s"
    val = (isget,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT isget UPDATEd Successfully")
    mycursor.close()
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': mycursor.rowcount})


#######################
#######################    j3NOT
#######################
@app.route('/post_j3not/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_j3not(id,isget):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET cleanjerk3isget= %s WHERE id= %s"
    val = (isget,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT isget UPDATEd Successfully")
    mycursor.close()
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': mycursor.rowcount})



#######################
#######################    j3 REJECT/cancel
#######################
@app.route('/post_j3rej/<int:id>/<path:isget>', methods=['GET', 'POST'])
def post_j3rej(id,isget):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET cleanjerk3isget= %s WHERE id= %s"
    val = (isget,id)
    mycursor.execute(sql,val)
    db.commit()
    flash("AT isget UPDATEd Successfully")
    mycursor.close()
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'athletes UPD:': mycursor.rowcount})


#######################
#######################    j3 RESET/NULL
#######################
@app.route('/post_j3reset/<int:id>/', methods=['GET', 'POST'])
def post_j3reset(id):
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET cleanjerk3isget=NULL,cleanjerk3=NULL,cleanjerk3d=NULL,cleanjerk3ch1=NULL,cleanjerk3ch2=NULL WHERE id= %s"
    val = (id)
    mycursor.execute(sql,val)
    db.commit()
    # sql = "UPDATE v7now SET cleanjerk3=NULL,s3d=NULL,s3ch1=NULL,s3ch2=NULL WHERE id= %s"
    # val = (id)
    # mycursor.execute(sql,val)
    # db.commit()

    flash("AT isget UPDATEd Successfully")
    mycursor.close()
    # return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))    
    return jsonify({'post_j3reset = UPD:': mycursor.rowcount})






@app.route('/clear_jerk', methods=['GET', 'POST'])
def clear_jerk():
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET exnow='j1',cleanjerk1isget=NULL,cleanjerk3isget=NULL,cleanjerk1d=NULL,cleanjerk1ch1=NULL,cleanjerk1ch2=NULL,cleanjerk2isget=NULL,cleanjerk2=NULL,cleanjerk2d=NULL,cleanjerk2ch1=NULL,cleanjerk2ch2=NULL,cleanjerk3isget=NULL,cleanjerk3=NULL,cleanjerk3d=NULL,cleanjerk3ch1=NULL,cleanjerk3ch2=NULL,flow_=1 WHERE 1"
    mycursor.execute(sql)
    db.commit()
    flash("FLOW clear_jerk UPDATEd Successfully")
    mycursor.close()
    return jsonify({'clear_jerk = UPD:': mycursor.rowcount})


@app.route('/clear_snatch', methods=['GET', 'POST'])
def clear_snatch():
    mycursor = db.cursor()    
    sql = "UPDATE v7now SET exnow='s1', snatch1isget=NULL,snatch3isget=NULL,s1d=NULL,s1ch1=NULL,s1ch2=NULL,snatch2isget=NULL,snatch2=NULL,s2d=NULL,s2ch1=NULL,s2ch2=NULL,snatch3isget=NULL,snatch3=NULL,s3d=NULL,s3ch1=NULL,s3ch2=NULL,cleanjerk1isget=NULL,cleanjerk3isget=NULL,cleanjerk1d=NULL,cleanjerk1ch1=NULL,cleanjerk1ch2=NULL,cleanjerk2isget=NULL,cleanjerk2=NULL,cleanjerk2d=NULL,cleanjerk2ch1=NULL,cleanjerk2ch2=NULL,cleanjerk3isget=NULL,cleanjerk3=NULL,cleanjerk3d=NULL,cleanjerk3ch1=NULL,cleanjerk3ch2=NULL WHERE 1"
    mycursor.execute(sql)
    db.commit()
    flash("FLOW clear_jerk UPDATEd Successfully")
    mycursor.close()
    return jsonify({'clear_jerk = UPD:': mycursor.rowcount})

#######################
#######################   
#######################

@app.route('/resetNOP', methods=['GET'])
def resetNOP():
    mycursor = db.cursor()    
    # sql = "UPDATE v7now SET op=1 WHERE id=5"
    sql = "UPDATE v7now SET nextop=0 WHERE 1"
    mycursor.execute(sql)
    db.commit()
    mycursor.close()
    return jsonify({'resetNOP = UPD:': mycursor.rowcount})

#######################
#######################   
#######################

#######################
#######################   
#######################

@app.route('/chk3last', methods=['GET'])
def chk3last():
    mycursor = db.cursor()
    # SELECT IF(STRCMP("hello","hello") = 0, "YES", "NO");
    # SELECT IF(500<1000, 5, 10);
# SELECT op,nextop,id, firstname, snatch1,snatch1isget,snatch2,snatch2isget,snatch3,snatch3isget FROM `v7now` 
# WHERE snatch1isget IS NOT NULL
# AND snatch2isget IS NOT NULL
# AND snatch3isget IS NULL
# AND id!=4;

    # set_app_weight_now()
    # set_op_now(id=0)
    # set_nop_now(id=0)

    
### q for all
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.wnow,att.exnow,att.birth,
    att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,
    att.s3d,att.s3ch1,att.s3ch2,att.country,att.city,
    att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
    att.j3d,att.j3ch1,att.j3ch2,att.avatar,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where(att.flow.is_null(0))
    attdata = [t for t in qu]
    attz = dict_helper(attdata)
    id=0




    sql = "UPDATE v7now SET op=1 WHERE id=5"

    mycursor.execute(sql)

    db.commit()
    mycursor.close()

    # return jsonify({'chk3last = UPD:':attdata})
    return redirect(url_for('flow',attdata=attdata,attz=attz))

#######################
#######################   
#######################


@app.route(BASE_URL+'/editapp/<int:id>/<int:appw>', methods=['GET', 'POST'])
def edit_app(id,appw):
    mycursor = db.cursor()    
    if request.method == 'POST' or 'GET':
        print(id)
        #my_data = att(sex, sname, fname, s1, j1)
        mycursor = db.cursor()

        sql = "UPDATE v7now SET snatch1= %s WHERE id= %s AND exnow='s1' AND s1ch1 IS NOT NULL AND s1ch2 IS NULL"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET s1ch2= %s WHERE id= %s AND exnow='s1' AND s1ch1 IS NOT NULL AND s1ch2 IS NULL AND s1ch1!= %s"
        val = (appw,id,appw)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET snatch1= %s WHERE id= %s AND exnow='s1' AND s1ch1 IS NULL AND s1ch2 IS NULL"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET s1ch1= %s WHERE id= %s AND exnow='s1' AND s1ch1 IS NULL AND s1ch2 IS NULL AND s1d!=snatch1"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()
    #s2
        sql = "UPDATE v7now SET snatch2= %s WHERE id= %s AND exnow='s2' AND s2ch1 IS NOT NULL AND s2ch2 IS NULL"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET s2ch2= %s WHERE id= %s AND exnow='s2' AND s2ch1 IS NOT NULL AND s2ch2 IS NULL AND s2ch1!= %s"
        val = (appw,id,appw)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET snatch2= %s WHERE id= %s AND exnow='s2' AND s2ch1 IS NULL AND s2ch2 IS NULL"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET s2ch1= %s WHERE id= %s AND exnow='s2' AND s2ch1 IS NULL AND s2ch2 IS NULL AND s2d!=snatch2"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()        
    #s3
        sql = "UPDATE v7now SET snatch3= %s WHERE id= %s AND exnow='s3' AND s3ch1 IS NOT NULL AND s3ch2 IS NULL"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET s3ch2= %s WHERE id= %s AND exnow='s3' AND s3ch1 IS NOT NULL AND s3ch2 IS NULL AND s3ch1!= %s"
        val = (appw,id,appw)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET snatch3= %s WHERE id= %s AND exnow='s3' AND s3ch1 IS NULL AND s3ch2 IS NULL"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET s3ch1= %s WHERE id= %s AND exnow='s3' AND s3ch1 IS NULL AND s3ch2 IS NULL AND s3d!=snatch3"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()    




# CJ / РЫВОК FIX / ADD ! & DONE
# *******************************
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        #j1
        sql = "UPDATE v7now SET cleanjerk1= %s WHERE id= %s AND exnow='j1' AND cleanjerk1ch1 IS NOT NULL AND cleanjerk1ch2 IS NULL"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET cleanjerk1ch2= %s WHERE id= %s AND exnow='j1' AND cleanjerk1ch1 IS NOT NULL AND cleanjerk1ch2 IS NULL AND cleanjerk1ch1!= %s"
        val = (appw,id,appw)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET cleanjerk1= %s WHERE id= %s AND exnow='j1' AND cleanjerk1ch1 IS NULL AND cleanjerk1ch2 IS NULL"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET cleanjerk1ch1= %s WHERE id= %s AND exnow='j1' AND cleanjerk1ch1 IS NULL AND cleanjerk1ch2 IS NULL AND cleanjerk1d!=cleanjerk1"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()        
        #j2
        sql = "UPDATE v7now SET cleanjerk2= %s WHERE id= %s AND exnow='j2' AND cleanjerk2ch1 IS NOT NULL AND cleanjerk2ch2 IS NULL"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET cleanjerk2ch2= %s WHERE id= %s AND exnow='j2' AND cleanjerk2ch1 IS NOT NULL AND cleanjerk2ch2 IS NULL AND cleanjerk2ch1!= %s"
        val = (appw,id,appw)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET cleanjerk2= %s WHERE id= %s AND exnow='j2' AND cleanjerk2ch1 IS NULL AND cleanjerk2ch2 IS NULL"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET cleanjerk2ch1= %s WHERE id= %s AND exnow='j2' AND cleanjerk2ch1 IS NULL AND cleanjerk2ch2 IS NULL AND cleanjerk2d!=cleanjerk2"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()          
        #j3
        sql = "UPDATE v7now SET cleanjerk3= %s WHERE id= %s AND exnow='j3' AND cleanjerk3ch1 IS NOT NULL AND cleanjerk3ch2 IS NULL"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET cleanjerk3ch2= %s WHERE id= %s AND exnow='j3' AND cleanjerk3ch1 IS NOT NULL AND cleanjerk3ch2 IS NULL AND cleanjerk3ch1!= %s"
        val = (appw,id,appw)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET cleanjerk3= %s WHERE id= %s AND exnow='j3' AND cleanjerk3ch1 IS NULL AND cleanjerk3ch2 IS NULL"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()

        sql = "UPDATE v7now SET cleanjerk3ch1= %s WHERE id= %s AND exnow='j3' AND cleanjerk3ch1 IS NULL AND cleanjerk3ch2 IS NULL AND cleanjerk3d!=cleanjerk3"
        val = (appw,id)
        mycursor.execute(sql,val)
        db.commit()    

        flash("Employee Inserted Successfully")

    mycursor.close()      
    db.close()  
    return redirect(url_for('flow',chcount=mycursor.rowcount,id=id,appw=appw))
    #return render_template('flow.html',delcount=mycursor.rowcount)
    #return str(mycursor.rowcount)
######################




# *******************
#  NEDD EDIT (copy from TABLO etc)
@app.route('/tablo2TV', methods = ['GET'])
def tablo2TV():
  # set app now!
    set_app_weight_now()
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.exnow,att.wnow,
    att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,
    att.s3d,att.s3ch1,att.s3ch2,att.aend,
    att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
    att.j3d,att.j3ch1,att.j3ch2,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    country.flag,country.name,cat.lwcat,cities.cname).where(att.op==1).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id))
    attdata = [t for t in qu]
    attz = dict_helper(attdata)

    # attz_c = dict_helper(attdata_c)
    #return jsonify({'athletes': attz})
    db.close()
    return render_template('tablo2tv.html',attz=attz,attdata=attdata,appHost=appHost,appPort=appPort)


@app.route('/tablo', methods = ['GET'])
def tablo():
  # set app now!
    #run v7core DAEMON
    set_app_weight_now()
    set_op_now(id=0)  
    set_nop_now(id=0)    

    # daemod_run = subprocess.run(['python3.10', 'v7core.py'])
    
    # ЭТО ПИЗДЕЦ СТОКА!!! 
    # СРАЗУ ПИЗДА ВСЕМУ ПРИХОДИТ!!!
    ######## exec(open('v7core.py').read())



    #set_opnop()
    # set try_now&xXchX now!
    #change_app_weight()

    
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.exnow,att.wnow,
    att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,
    att.s3d,att.s3ch1,att.s3ch2,att.aend,att.city,
    att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
    att.j3d,att.j3ch1,att.j3ch2,country.m3code,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    country.flag,country.name,cat.lwcat,cities.cname).where(att.op==1).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id))
    attdata = [t for t in qu]
    attz = dict_helper(attdata)

    # attz_c = dict_helper(attdata_c)
    #return jsonify({'athletes': attz})
    db.close()
    return render_template('tablo.html',attz=attz,attdata=attdata,appHost=appHost,appPort=appPort)



# # allow both GET and POST requests
# @app.route('/form-example', methods=['GET', 'POST'])
# def form_example():
#     # handle the POST request
#     if request.method == 'POST':
#         language = request.form.get('language')
#         framework = request.form.get('framework')
#         return '''
#                   <h1>The language value is: {}</h1>
#                   <h1>The framework value is: {}</h1>'''.format(language, framework)

#     # otherwise handle the GET request
#     return '''
#            <form method="POST">
#                <div><label>Language: <input type="text" name="language"></label></div>
#                <div><label>Framework: <input type="text" name="framework"></label></div>
#                <input type="submit" value="Submit">
#            </form>'''


@app.route('/signal', methods = ['GET'])
def signal():
    return render_template('signal.html')

@app.route('/break', methods = ['GET'])
def br_eak():
    return render_template('break.html')

@app.route('/chrono', methods = ['GET','POST'])
def chrono():
    return render_template('countdown-timer-view.html')

@app.route('/chronograph', methods = ['GET','POST'])
def chronograph():
    return render_template('chrono_menu.html')


@app.route('/timer', methods = ['GET','POST'])
def timerz():
    return render_template('countdown-timer.html')



@app.route('/judge', methods = ['POST', 'GET'])
def judge():
    return render_template('judge.html')

@app.route('/j1/<int:rez>', methods = ['POST', 'GET'])
def judge1rez(rez):
    #return render_template('judge1rez.html',rez=rez)
    return {"j1 solution:":rez}


@app.route('/j1', methods=['GET'])
def judge1():
    args = request.args
    vote = args.get('vote')
    #return name
    return render_template('judge1.html',vote=vote)    

@app.route('/j2', methods = ['POST', 'GET'])
def judge2():
    args = request.args
    vote = args.get('vote')    
    return render_template('judge2.html',vote=vote)

@app.route('/j3', methods = ['POST', 'GET'])
def judge3():
    args = request.args
    vote = args.get('vote')
    return render_template('judge3.html',vote=vote)


@app.route('/bkp_v7now', methods = ['POST', 'GET'])
def bkp_v7now():
    #  bkp v7now table,  mysql
    mycursor = db.cursor()
    sql = "DROP TABLE IF EXISTS _v7bkp;"
    mycursor.execute(sql)
    sql = "CREATE TABLE _v7bkp LIKE v7now;"
    mycursor.execute(sql)
    sql = "INSERT INTO _v7bkp SELECT * FROM v7now;"
    mycursor.execute(sql)
    mycursor = db.cursor()
    sql = "DROP TABLE IF EXISTS _v7athlete;"
    mycursor.execute(sql)
    sql = "CREATE TABLE _v7athlete LIKE v7now;"
    mycursor.execute(sql)
    sql = "INSERT INTO _v7athlete SELECT * FROM v7now;"
    mycursor.execute(sql)
    presentDate = randint(100, 999) 
    # ДОБАВИТЬ ПРОВЕРКУ НА КОЛИЧЕСТВО ЗАПИСЕЙ В v7now СЕЙЧАС!
    # И ЕСЛИ сейчас там 0 записей = ТОГДА !ТРАНКЭЙТ ТАБЛЕ&COPY ect...
    # 
    qua = att.select(att.id) # ALL
    attdata_a = [t for t in qua]
    attz_a= dict_helper(attdata_a)
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^',len(attz_a))
    if(len(attz_a)<=2):
        pass
    if(len(attz_a)>=3):
        sql = "TRUNCATE TABLE v7now;"
        mycursor.execute(sql)
        newATsql = "INSERT INTO `v7now` (`id`, `op`, `nextop`, `prevop`, `weightnow`, `exnow`, `trynow`, `serialnumber`, `sex`, `ownweight`, `wcat_id`, `rank_id`, `info_id`, `newrank`, `score`, `sincler`, `position`, `snatch1`, `snatch1isget`, `s1d`, `s1ch1`, `s1ch2`, `s1ch3`, `snatch2`, `snatch2isget`, `s2d`, `s2ai`, `s2ch1`, `s2ch2`, `snatch3`, `snatch3isget`, `s3d`, `s3ai`, `s3ch1`, `s3ch2`, `snatchresult`, `snatch_place`, `cleanjerk1`, `cleanjerk1isget`, `cleanjerk1d`, `cleanjerk1ch1`, `cleanjerk1ch2`, `cleanjerk1ch3`, `cleanjerk2`, `cleanjerk2isget`, `cleanjerk2d`, `cleanjerk2ai`, `cleanjerk2ch1`, `cleanjerk2ch2`, `cleanjerk3`, `cleanjerk3isget`, `cleanjerk3d`, `cleanjerk3ai`, `cleanjerk3ch1`, `cleanjerk3ch2`, `cleanjerkresult`, `cleanjerk_place`, `doublesum`, `firstname`, `secondname`, `birth`, `country_id`, `city_id`, `city`, `avatar`, `changets`, `guru1name`, `guru2name`, `ishideordel`, `actionend`, `place`, `flow_`, `country_`, `wcat_`) VALUES (NULL, '0', '0', '0', '0', 's1', '0', NULL, '1', '72.8', '1', '0', '1', NULL, NULL, '', NULL, '44', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0', NULL, '55', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0', NULL, '0', 'Гаура́нга', 'Нитьяна́нда', '07.03.1486', '1', '1', '1', '/img/avatars/defava11.png', current_timestamp(), 'Палькодзян С.А.', 'Палько А.Г.', '0', '0', NULL, 1, 'rus', '102+');"
        mycursor.execute(newATsql)
        now = datetime.datetime.now()
        print ("Current date and time : ")
        print (now.strftime("%Y%m%d%H%M%S"))
        dtnow = now.strftime("%Y%m%d%H%M%S%d")
        print(presentDate, '<---- #############')

        utimestsmp = '__v7bkp_'+str(dtnow)
        sql = "DROP TABLE IF EXISTS `_v7bkp`"+utimestsmp
        sql = "RENAME TABLE `_v7bkp` TO "+utimestsmp
    ########################################
    ########################################
    ########################################
        mycursor.execute(sql)

    if request.method == 'GET':
        staff_g = request.args.get('staff_g')
        # print('=========')
        # print(staff_g)
        # print(type(staff_g))
        if staff_g is None:
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==1)
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)  
        if staff_g=="1":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==1)
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)                  
        if staff_g=="2":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==2)            
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)                             
        if staff_g=="3":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==3)            
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)                                         
        if staff_g=="4":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==4)            
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)                               
        if staff_g=="5":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==5)            
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)                             

    grp_qg = jgroup.select(jgroup.j_group).distinct().order_by(jgroup.j_group).distinct()
    grp_datag = [t for t in grp_qg] 
    grp_datazg = dict_helper(grp_datag) 

    q_wcat = cat.select(cat.sex,cat.wcat_id,cat.wcat,cat.lwcat)
    wcatdata_o = [t for t in q_wcat] 
    wcatdata__oz = dict_helper(wcatdata_o) 


    if request.method == 'POST':
    # if request.method == 'GET':
        staff_g = request.args.get('staff_g')
        sex = request.args.get('sex')
        # sex = request.form['sex']
        if staff_g is None:
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==1)
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)              
        if staff_g=="1":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==1)
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)                     
        if staff_g=="2":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==2)            
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)    
        if staff_g=="3":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==3)            
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)                                         
        if staff_g=="4":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==4)            
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)                               
        if staff_g=="5":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==5)            
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)                

        # sex = request.form['sex']
        wcat = request.form.get('wcat')
        if(wcat=='all'):
            qup = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
        att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
        att.country_id,att.city_id,att.exnow,att.wnow,att.gn,att.sinc,
        att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,att.sc,
        att.s3d,att.s3ch1,att.s3ch2,att.city,att.place,att.gn,att.pos,
        att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
        att.j3d,att.j3ch1,att.j3ch2,att.s_place,att.j_place,
        att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
        country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where((att.sex==1) & (att.flow==2)).order_by(att.place)
            attdatap = [t for t in qup]
            repdata = dict_helper(attdatap)
            # grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat).where(jgroup.j_group==1)
            # grp_data = [t for t in grp_q] 
            # grp_dataz = dict_helper(grp_data) 
            grp_qg = jgroup.select(jgroup.j_group).distinct().order_by(jgroup.j_group).distinct()
            grp_datag = [t for t in grp_qg] 
            grp_datazg = dict_helper(grp_datag)         
        else:
            qup = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
            att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
        att.country_id,att.city_id,att.exnow,att.wnow,att.gn,att.sinc,
        att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,att.sc,
        att.s3d,att.s3ch1,att.s3ch2,att.city,att.place,att.gn,att.pos,
        att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
        att.j3d,att.j3ch1,att.j3ch2,att.s_place,att.j_place,
        att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
        country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where((att.sex==1) & (att.flow==2) & (att.wcat_id==wcat)).order_by(att.place)
        attdatap = [t for t in qup]
        repdata = dict_helper(attdatap)
        grp_qg = jgroup.select(jgroup.j_group).distinct().order_by(jgroup.j_group).distinct()
        grp_datag = [t for t in grp_qg] 
        grp_datazg = dict_helper(grp_datag)                 


        qug = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
        att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
        att.country_id,att.city_id,att.exnow,att.wnow,att.gn,att.sinc,
        att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,att.sc,
        att.s3d,att.s3ch1,att.s3ch2,att.city,att.place,att.gn,att.pos,
        att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
        att.j3d,att.j3ch1,att.j3ch2,att.s_place,att.j_place,
        att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
        country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where((att.sex==1) & (att.flow==2) & (att.wcat_id==wcat)).order_by(att.place)
        cd = datetime.date.today()
        cdy = cd.year
        cdm = cd.month
        cdd = cd.day
        fdate = cd.strftime('%d.%m.%Y')

# get sex/gender att of the att
# get own weight of the att

        mycursor.close()
        db.close()
        return render_template('reports.html',grp_data=grp_data,grp_dataz=grp_dataz,fdate=fdate,cdy=cdy,cdm=cdm,cdd=cdd,repdata=repdata,sex=sex,wcat=wcat)

    rndDigit = random.randint(1, 99999)
    # gDate = datetime.now()
    gDate = datetime.date(2023,1,7)    
    
    mycursor.close()
    db.close()
    return render_template('flow-new.html',grp_datazg=grp_datazg,wcatdata__oz=wcatdata__oz,grp_dataz=grp_dataz,grp_data=grp_data,rndDigit=rndDigit,gDate=gDate)


@app.route('/newflow', methods = ['POST', 'GET'])
def newflow():
    #calc sinclair

    
    # $bodyWeight = sprintf("%.1f", $BW_ROW);
    # if ($sexROW==1) $sinc_coeff = $sinclair_rate_male["$bodyWeight"];
    # if ($sexROW==0) $sinc_coeff = $sinclair_rate_female["$bodyWeight"];
    # $coeffSinc = ($sinc_coeff*$dblsumROW);
    # $coeffSinc = round($coeffSinc,2);

    # $updSincROW = R::exec('UPDATE "'.$table.'" SET sincler="'.$coeffSinc.'" WHERE id='.$ID_ROW);    




    #new flow & bkp mysql
    # mycursor = db.cursor()
    if request.method == 'GET':
        staff_g = request.args.get('staff_g')
        print('=========')
        print(staff_g)
        print(type(staff_g))
        if staff_g is None:
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==1)
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)  
        if staff_g=="1":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==1)
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)                  
        if staff_g=="2":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==2)            
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)
        if staff_g=="3":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==3)            
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)                                       
        if staff_g=="4":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==4)            
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)            
        if staff_g=="5":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==5)            
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)

    grp_qg = jgroup.select(jgroup.j_group).distinct().order_by(jgroup.j_group).distinct()
    grp_datag = [t for t in grp_qg] 
    grp_datazg = dict_helper(grp_datag) 

    q_wcat = cat.select(cat.sex,cat.wcat_id,cat.wcat,cat.lwcat)
    wcatdata_o = [t for t in q_wcat] 
    wcatdata__oz = dict_helper(wcatdata_o) 


    if request.method == 'POST':
        staff_g = request.args.get('staff_g')
        if staff_g is None:
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==1)
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)              
        if staff_g=="1":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==1)
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)                     
        if staff_g=="2":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==2)            
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)   
        if staff_g=="3":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==3)            
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)                 
        if staff_g=="4":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==4)            
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)              
        if staff_g=="5":
            grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat,jgroup.j_post_ru).where(jgroup.j_group==5)            
            grp_data = [t for t in grp_q] 
            grp_dataz = dict_helper(grp_data)                

        sex = request.form['sex']
        wcat = request.form.get('wcat')
        if(wcat=='all'):
            qup = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
        att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
        att.country_id,att.city_id,att.exnow,att.wnow,att.gn,att.nr,att.sinc,
        att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,att.sc,
        att.s3d,att.s3ch1,att.s3ch2,att.city,att.place,att.gn,att.pos,
        att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
        att.j3d,att.j3ch1,att.j3ch2,att.s_place,att.j_place,
        att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
        country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where((att.sex==1) & (att.flow==2)).order_by(att.place)
            # grp_q = jgroup.select(jgroup.j_id,jgroup.j_group,jgroup.j_nane,jgroup.j_post,jgroup.j_city,jgroup.j_cat).where(jgroup.j_group==1)
            # grp_data = [t for t in grp_q] 
            # grp_dataz = dict_helper(grp_data) 
            grp_qg = jgroup.select(jgroup.j_group).distinct().order_by(jgroup.j_group).distinct()
            grp_datag = [t for t in grp_qg] 
            grp_datazg = dict_helper(grp_datag)         
        else:
            qup = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
            att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
        att.country_id,att.city_id,att.exnow,att.wnow,att.gn,att.nr,att.sinc,
        att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,att.sc,
        att.s3d,att.s3ch1,att.s3ch2,att.city,att.place,att.gn,att.pos,
        att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
        att.j3d,att.j3ch1,att.j3ch2,att.s_place,att.j_place,
        att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
        country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where((att.sex==1) & (att.flow==2) & (att.wcat_id==wcat)).order_by(att.place)
        attdatap = [t for t in qup]
        repdata = dict_helper(attdatap)
        grp_qg = jgroup.select(jgroup.j_group).distinct().order_by(jgroup.j_group).distinct()
        grp_datag = [t for t in grp_qg] 
        grp_datazg = dict_helper(grp_datag)                 


        qug = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
        att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
        att.country_id,att.city_id,att.exnow,att.wnow,att.gn,att.nr,att.sinc,
        att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,att.sc,
        att.s3d,att.s3ch1,att.s3ch2,att.city,att.place,att.gn,att.pos,
        att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
        att.j3d,att.j3ch1,att.j3ch2,att.s_place,att.j_place,
        att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
        country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where((att.sex==1) & (att.flow==2) & (att.wcat_id==wcat)).order_by(att.place)
        
        bkp_v7now()
        cd = datetime.date.today()
        cdy = cd.year
        cdm = cd.month
        cdd = cd.day
        fdate = cd.strftime('%d.%m.%Y')
        return render_template('reports.html',grp_data=grp_data,grp_dataz=grp_dataz,fdate=fdate,cdy=cdy,cdm=cdm,cdd=cdd,repdata=repdata,sex=sex,wcat=wcat)

    rndDigit = random.randint(1, 99999)
    # gDate = datetime.now()
    gDate = datetime.date(2023,1,7)

    db.close()
    return render_template('flow-new.html',grp_datazg=grp_datazg,wcatdata__oz=wcatdata__oz,grp_dataz=grp_dataz,grp_data=grp_data,rndDigit=rndDigit,gDate=gDate)



@app.route('/sorokin_menu', methods = ['POST', 'GET'])
def sorokin_menu():
    return render_template('sorokin_menu.html')



@app.route('/sorokin_tv1', methods=['GET'])
def sorokin_tv1():
    args = request.args
    vote = args.get('vote')
    #return name
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.exnow,att.wnow,
    att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,
    att.s3d,att.s3ch1,att.s3ch2,att.city,att.wcat,
    att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
    att.j3d,att.j3ch1,att.j3ch2,att.s_place,att.j_place,att.place,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    country.flag,country.name,cat.lwcat,cat.wcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id))
    attdata = [t for t in qu]
    attz = dict_helper(attdata)

    ######
    # global globaltimer
    # globaltimer = 60
    # countdown(globaltimer)
    ######

    # attz_c = dict_helper(attdata_c)
    #return jsonify({'athletes': attz})
    db.close()
    return render_template('sorokin_tv1.html',vote=vote,attz=attz,attdata=attdata)


@app.route('/sorokin_tv2', methods=['GET'])
def sorokin_tv2():
    args = request.args
    vote = args.get('vote')
    #return name
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.exnow,att.wnow,
    att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,
    att.s3d,att.s3ch1,att.s3ch2,att.city,
    att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
    att.j3d,att.j3ch1,att.j3ch2,att.s_place,att.j_place,att.place,
    country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id))
    attdata = [t for t in qu]
    attz = dict_helper(attdata)
    db.close()
    return render_template('sorokin_tv2.html',vote=vote,attz=attz,attdata=attdata)



@app.route('/sorokin_tv3', methods=['GET'])
def sorokin_tv3():
    args = request.args
    vote = args.get('vote')
    #return name
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.exnow,att.wnow,
    att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,
    att.s3d,att.s3ch1,att.s3ch2,att.city,att.wcat,
    att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
    att.j3d,att.j3ch1,att.j3ch2,att.s_place,att.j_place,att.place,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    country.flag,country.name,cat.lwcat,cat.wcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where(att.nop==1)
    attdata = [t for t in qu]
    attz = dict_helper(attdata)
    db.close()
    return render_template('sorokin_tv3.html',vote=vote,attz=attz,attdata=attdata)


# def countdownGen(t):
#     return (t-i for i in range(t))

# def countdown(t):
#     gen = countdownGen(t)
#     while t > 0:
#         try:
#             globaltimer = next(gen)
#             time.sleep(1)
#         except StopIteration:
#             globaltimer = 0

@app.route('/flow_edit', methods = ['POST', 'GET'])
# def flow_edit():
def flow_edit():
    set_app_weight_now()
    set_op_now(id=0)
    set_nop_now(id=0)
### q for all
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.wnow,att.exnow,att.birth,
    att.s1d,att.s1ch1,att.s1ch2,att.s2d,att.s2ch1,att.s2ch2,
    att.s3d,att.s3ch1,att.s3ch2,att.country,att.city,
    att.j1d,att.j1ch1,att.j1ch2,att.j2d,att.j2ch1,att.j2ch2,
    att.j3d,att.j3ch1,att.j3ch2,att.avatar,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where(att.flow.is_null(0))
    attdata = [t for t in qu]
    attz = dict_helper(attdata)
    id=0
    
## OPTIONS ARRAY
    q_opt = opt.select(opt.o_name,opt.o_val,opt.opt_id,opt.o_desc,opt.o_descoff,opt.o_param)
    optdata_o = [t for t in q_opt] 
    optdata__oz = dict_helper(optdata_o)    
## OTHER ATT DATAZ
## Weight category
    q_wcat = cat.select(cat.sex,cat.wcat_id,cat.wcat,cat.lwcat)
    wcatdata_o = [t for t in q_wcat] 
    wcatdata__oz = dict_helper(wcatdata_o)
## Countryz    
    q_cntry = country.select(country.country_id,country.name,country.flag,country.img).order_by(country.country_id.asc())
    cntrydata_o = [t for t in q_cntry] 
    cntrydata__oz = dict_helper(cntrydata_o)
## City / place    

## get Fak8r    
    fname_ph=faker.first_name_male()
    sname_ph=faker.last_name_male()

    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    
    # UUID
    uuidz = uuid.uuid4()
    # daemod_run = subprocess.run(['python3.10', 'v7core.py'])
    #exec(open('v7core.py').read())

    if "iphone" in user_agent:
        db.close()
        return render_template('index-clean.html', optdata__oz=optdata__oz,cntrydata_o=cntrydata_o,cntrydata__oz=cntrydata__oz,wcatdata_o=wcatdata_o, wcatdata__oz=wcatdata__oz, attdata=attdata, attz=attz,CJ=CJ,SN=SN,id=id,appHost=appHost,appPort=appPort,fname_ph=fname_ph,sname_ph=sname_ph)
    elif "android" in user_agent:
        db.close()
        return render_template('index-clean.html', optdata__oz=optdata__oz,cntrydata_o=cntrydata_o,cntrydata__oz=cntrydata__oz,wcatdata_o=wcatdata_o, wcatdata__oz=wcatdata__oz, attdata=attdata, attz=attz,CJ=CJ,SN=SN,id=id,appHost=appHost,appPort=appPort,fname_ph=fname_ph,sname_ph=sname_ph)
    else:
        db.close()
        return render_template('flow_editor.html', uuidz=uuidz,optdata__oz=optdata__oz,cntrydata_o=cntrydata_o,cntrydata__oz=cntrydata__oz,wcatdata_o=wcatdata_o, wcatdata__oz=wcatdata__oz, attdata=attdata, attz=attz,CJ=CJ,SN=SN,id=id,appHost=appHost,appPort=appPort,fname_ph=fname_ph,sname_ph=sname_ph)


########################    
#     


@app.route(BASE_URL+'/add', methods= ['POST'])
def new_alhlete2():
    sex = request.form['sex']
    if sex == 'male':
        sex = 1
    if sex == 'female':
        sex = 0
    sname = request.form['snameadd']
    fname = request.form['fnameadd']
    s1 = request.form['s1add']
    j1 = request.form['j1add']
    own_weight = request.form['owadd']
    place = request.form['placeszadd']
    bday = request.form['yearz']
    mycursor = db.cursor()
        #sql = "INSERT INTO v7now (sex, secondname, firstname, snatch1, cleanjerk1, ownweight, wcat_id, country_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    sql = "INSERT INTO v7now (sex,firstname,secondname,snatch1,cleanjerk1,ownweight,city,birth) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        #val = (sex, sname, fname, s1, j1, own_weight, weight_cat, countryz)
    val = (sex, sname, fname,s1,j1,own_weight,place,bday)
    mycursor.execute(sql, val)
    db.commit()
        #   print(mycursor.rowcount, "record inserted.")
    set_app_weight_now()
    flash(mycursor.rowcount, "# AT Inserted Successfully")
        # run v7core DAEMON
    # daemod_run = subprocess.run(['python3.10', 'v7core.py'])
    #exec(open('v7core.py').read())

    #   return render_template('flow.html',cur_count=mycursor.rowcount,lc=mycursor.lastrowid)
    mycursor.close()
    return redirect(url_for('newat'))



########################################################################
########################################################################
## MAIN circuit func ov v7core! #1  @@@@@@@ 
########################################################################
########################################################################
# set ON POMOST (op) !Athlete now ()
def set_op_now(id='0'):
    global SN
    global CJ
    # if(id==0):
    #     print(f'set_op_now(id=0) DO NOTHING !!!')
    #     ex_upd = '0'
    


    # if(id!=0):
    #     print(f'set_op_now(id ==): { id } | DO this >>>')        
    #     ex_upd = 'v7pro-SET-OP now!'
    #     ex_upd=att.update({att.op:0})
    #     ex_upd.execute()
    #     ex_upd=att.update({att.op:id})
    #     ex_upd.execute()    

    #     print("v7 c0rE job! = in SET_OP_NOW FUNC#")
    #     x,y  = get_approach()
    #     # FlowGetter = get_approach()
    #     print(f'***-> APP NOW IS: {x}, type: {type(x)}')
    #     print(f'****-> APP NOW COUNT IS: {y}, type: {type(y)}')
        
    s1 = get_id_min_w_s1()
    s2 = get_id_min_w_s2()
    s3 = get_id_min_w_s3()
    ic(s1)
    ic(s2)
    ic(s3) #12,24,0
    ic('################# sop_id = sel_op_id(s1, s2, s3) ######################')
    sop_id = sel_op_id(s1, s2, s3)
    ic(sop_id)
    ic('################# sop_id = sel_op_id(s1, s2, s3) ######################')
    ex_upd = sop_id




    # #start_time = time()
    # if(SN is True and CJ is False):
    #     print('SN is TRUE!!!!!!! DO SNATCH!!!!!')
    #     s1 = get_id_min_w_s1()
    #     s2 = get_id_min_w_s2()
    #     s3 = get_id_min_w_s3()
    #     ic(s1)
    #     ic(s2)
    #     ic(s3) #12,24,0
    #     # ic('########### sel_op_id   #########################')
    #     sop_id = sel_op_id(s1, s2, s3)
    #     ic('#################  sel_op_id ######################')


    # if(CJ is True and SN is False):
    #     print('SN is False!!!!!!! DO CJ!!!!!')
    #     # pass
    #     print('SN is None, now CLEAN&JERK !!!######')



        #     # ############
        # j1=get_min_w_j1()
        # j2=get_min_w_j2()
        # j3=get_min_w_j3()
        # wr_sel_nop_id_cj(j1,j2,j3)
        # print(f"wr_sel_nop_id_cj: {j1}, {j2}, {j3}")

        # j1 = get_id_min_w_j1()
        # j2 = get_id_min_w_j2()
        # j3 = get_id_min_w_j3()
        # ic(j1)
        # ic(j2)
        # ic(j3) #12,24,0
        # ic('#################  wr_sel_op_id_cj  #####################')
        # wr_sel_op_id_cj(j1, j2, j3)
        
        # ?????????????????????????????????
        # ?????????????????????????????????
        # ?????????????????????????????????
        # ?????????????????????????????????
        # ?????????????????????????????????
        # ?????????????????????????????????
        # ?????????????????????????????????
        # ?????????????????????????????????
        # wr_sel_nop_id_cj()
        # ?????????????????????????????????
        # ?????????????????????????????????
        # ?????????????????????????????????
        # ?????????????????????????????????
        # ?????????????????????????????????
        # ?????????????????????????????????
        # ?????????????????????????????????
        # ?????????????????????????????????


        # ******************
        # Тут ХУЙ знает как перейти на ТОЛЧОК....

    # if(SN is False and CJ is False):

    #     print('SN & CJ is False!!! END OF FLOW !!!!!!!')  
    #     clear_nop()
    #     clear_op()
    #     ic('####### END OF FLOW ################################')
    #     ic('############# END #######################################')

    return ex_upd 
########################################################################
########################################################################
## MAIN circuit func ov v7core! #1  @@@@@@@ 
########################################################################
########################################################################
# set ON POMOST (op) !Athlete now ()






########################################################################
########################################################################
## MAIN circuit func ov v7core! #2  @@@@@@@ 
########################################################################
########################################################################
# set NEXT ON POMOST (nop) !Athlete now ()
def set_nop_now(id): #// -> set_nop_now
    global SN
    global CJ
    ex_upd = 'v7pro-SET-NOP now!'
    # # ex_upd=att.update({att.nop:0})
    # # ex_upd.execute()

    # # & (att.s2ig.is_null(1)) & (att.s3ig.is_null(1))
    # # & (att.j1ig.is_null(1)) & (att.j2ig.is_null(1))
    # # & (att.j3ig.is_null(1)))
    # # ex_upd.execute()
    # if(SN is True and CJ is False):    
    #     s1 = get_id_min_w_s1()
    #     s2 = get_id_min_w_s2()
    #     s3 = get_id_min_w_s3()
    #     exidz = sel_op_id(s1, s2, s3)

    #     s1ex = get_id_min_w_s1(exclude_id=exidz)
    #     s2ex = get_id_min_w_s2(exclude_id=exidz)
    #     s3ex = get_id_min_w_s3(exclude_id=exidz)
    #     ic(s1ex)
    #     ic(s2ex)
    #     ic(s3ex)
    #     snp_id = sel_nop_id(s1ex, s2ex, s3ex)
    #     ic('#################  sel_nop_id 1 ######################')
    #     print(f'+++++++++ : ID nop : {snp_id}')

                

    #     if(exidz is None):
    #         exidz = 999


    #         # s1ex = get_id_min_w_s1(exclude_id=exidz)
    #         s1ex = get_id_min_w_s1()
    #         # s2ex = get_id_min_w_s2(exclude_id=exidz)
    #         s2ex = get_id_min_w_s2()
    #         # s3ex = get_id_min_w_s3(exclude_id=exidz)
    #         s3ex = get_id_min_w_s3()
    #         ic(s1ex)
    #         ic(s2ex)
    #         ic(s3ex)
    #         ic('################# sel_nop_id PIZDA!!! ###################')

    #         # s1 = get_id_min_w_s1()
    #         # s2 = get_id_min_w_s2()
    #         # s3 = get_id_min_w_s3()
    #         # sel_op_id(s1, s2, s3)
    #         # *************
    #         sel_nop_id(s1ex, s2ex, s3ex)


    # if(SN is False and CJ is True):    
    #     j1 = get_id_min_w_j1()
    #     j2 = get_id_min_w_j2()
    #     j3 = get_id_min_w_j3()
    #     exidz = sel_op_id(j1, j2, j3)
    #     print(f'DATAZ $$$$$!!!! j1-:{j1} j2-:{j2} j3-:{j3}')
    #     print(f'ZARAZA !!!!!!!!!! exidz:{exidz}')

    #     if(exidz is None):
    #         exidz = 999
    #         j1ex = get_id_min_w_j1()
    #         j2ex = get_id_min_w_j2()
    #         j3ex = get_id_min_w_j3()
    #         ic(j1ex)
    #         ic(j2ex)
    #         ic(j3ex)
    #         print('#############   sel_nop_id 0!  ####################')
    #     # **************************************
    #     # ??????????????????????????????????????
    #         print('MEMBER OF MEZHDU NOG ???? ;) ')

    #         acvfd = sel_nop_id(j1ex, j2ex, j3ex)
    #         print(f'#=CJ TRUE, sel_nop_id ..... {j1ex} ** {j2ex} ** {j3ex} ID={acvfd}')
    #     # print(acvfd)

    #     if(exidz>0):
    #         j1ex = get_id_min_w_j1(exidz)
    #         j2ex = get_id_min_w_j2(exidz)
    #         j3ex = get_id_min_w_j3(exidz)
    #         # j1ex = get_id_min_w_j1()
    #         # j2ex = get_id_min_w_j2()
    #         # j3ex = get_id_min_w_j3()            
    #         print(f'ZALUPA ((((((exidz>0)))))) :: {exidz}')
    #         nopnowzzz = wr_sel_nop_id_cj(j1ex, j2ex, j3ex)
    #         print(f'#= j1 ..... {j1ex} ** {j2ex} ** {j3ex} ID={exidz} wr_NOP: {nopnowzzz}')
    #         print(f'#= j1_2 ..... {j1} ** {j2} ** {j3} ID={exidz} wr_NOP: {nopnowzzz}')
    # # НАДО ПРАВИТЬ ТУТ ТО ⤵ ⤵ ⤵
    # # ПИЗДЕЦ



            
    #         # ?????????????





        # set_nop_now(1)
        # acvfd
        # *******************
        # ??????????????????????????????????????
        # print(acvfd)

    return ex_upd 



########################################################################
########################################################################
## MAIN circuit func ov v7core! 5  @@@@@@@ 
## @main of v7 func/job etc !!!!!!!
########################################################################
########################################################################
# set Athlete an approach now ()
# def get_approach():
# def get_approach():
# def get_approach():
@app.route('/get_approach', methods= ['GET'])
def get_approach():
    # global SN
    # global CJ
    cntAPP = 1
    mycursor = db.cursor()    
    sql = "SELECT id FROM v7now WHERE exnow IN ('s1','s2','s3');"
    mycursor.execute(sql)
    query_result = mycursor.fetchall()
    len_s_rez = len(query_result)
    if(len_s_rez>=1):
        nowEX = 'SN'
        cntAPP = '>=1'
        cntAPP = len_s_rez
        if(len_s_rez==1):
            nowEX = 'SN'
            cntAPP = 1
        if(len_s_rez==2):
            nowEX = 'SN'
            cntAPP = 2

    sql = "SELECT id FROM v7now WHERE exnow IN ('j1','j2','j3');"
    mycursor.execute(sql)
    query_result = mycursor.fetchall()        
    len_j_rez = len(query_result)
    if(len_j_rez>=1 and len_s_rez==0):
        nowEX = 'CJ' 
        cntAPP = '>=1'
        cntAPP = len_j_rez
        if(len_j_rez==1):
            nowEX = 'CJ'
            cntAPP = 1
        if(len_j_rez==2):
            nowEX = 'CJ'
            cntAPP = 2




    mycursor.close()
    db.close()
    # return jsonify(cc=query_result, len_s_rez=len_s_rez, len_j_rez=len_j_rez, EX=nowEX, cntAPP=cntAPP)
    return nowEX, cntAPP 
    # -> nowEX: 'SN' | 'CJ'
    # ,
    # -> cntAPP: int (0,1,2,3,4,5...n)
    # return jsonify(EX=nowEX, app_COUNTER=cntAPP)






########################################################################
########################################################################
## MAIN circuit func ov v7core! @@@@@@@ 
## @main of v7 func/job etc !!!!!!!
########################################################################
########################################################################
# set Athlete an approach now ()
# def set_app_weight_now():
# def set_app_weight_now():
# def set_app_weight_now():
def set_app_weight_now():
    
    global SN
    global CJ
    # s1: s1ch1 -> s1, s1ch2 -> s1
    # x: x -> x, x -> x
    # j3: j3ch1 -> j3, j3ch2 -> j3
                #snatch s1







    # UPD
    # // SET WORLD RECORDS table
    rank_id = att.update(rank_id=att.wcat_id).where(att.id > 0)
    response_z = rank_id.execute()
    # SELECT




    # s1=dm.get_id_min_w_s1()
    # s2=dm.get_id_min_w_s2()
    # s3=dm.get_id_min_w_s3()
    # print(s1,s2,s3)
    # dm.sel_op_id(s1,s2,s3)

    ## set app on ROW:exnow & weightnow
    #snatch s1
    ex_upd=att.update({att.exnow:'s1', att.wnow:att.s1}).where( (att.s1ig.is_null(1))
    & (att.s2ig.is_null(1)) & (att.s3ig.is_null(1))
    & (att.j1ig.is_null(1)) & (att.j2ig.is_null(1))
    & (att.j3ig.is_null(1)))
    ex_upd.execute()

    #s2 automatic surcharge +1
    ex_upd=att.update({att.exnow:'s2', att.wnow:att.s1+1,att.s2:att.s1+1}).where( (att.s2ig.is_null(1))
    & (att.s1ig==1) & (att.s3ig.is_null(1))
    & (att.j1ig.is_null(1)) & (att.j2ig.is_null(1))
    & (att.j3ig.is_null(1)))
    ex_upd.execute()
    #s2 with/out automatic surcharge +1 
    ex_upd=att.update({att.exnow:'s2', att.wnow:att.s1,att.s2:att.s1}).where( (att.s2ig.is_null(1))
    & (att.s1ig==0) & (att.s3ig.is_null(1))
    & (att.j1ig.is_null(1)) & (att.j2ig.is_null(1))
    & (att.j3ig.is_null(1)))
    ex_upd.execute()    
    #s3 automatic surcharge +1
    ex_upd=att.update({att.exnow:'s3', att.wnow:att.s2+1,att.s3:att.s2+1}).where( (att.s3ig.is_null(1))
    & (att.s2ig==1) & (att.s1ig.is_null(0))
    & (att.j1ig.is_null(1)) & (att.j2ig.is_null(1))
    & (att.j3ig.is_null(1)))
    ex_upd.execute()    
    #s3 with/out automatic surcharge +1
    ex_upd=att.update({att.exnow:'s3',att.wnow:att.s2,att.s3:att.s2}).where( (att.s3ig.is_null(1))
    & (att.s2ig==0) & (att.s1ig.is_null(0))
    & (att.j1ig.is_null(1)) & (att.j2ig.is_null(1))
    & (att.j3ig.is_null(1)))
    ex_upd.execute()        

    
    
    
    #jerk j1
    ex_upd=att.update({att.exnow:'j1',att.wnow:att.j1}).where( (att.j1ig.is_null(1))
    & (att.s3ig.is_null(0)) & (att.j2ig.is_null(1))
    & (att.s2ig.is_null(0)) & (att.s1ig.is_null(0))
    & (att.j3ig.is_null(1)))
    ex_upd.execute()
    #j2 automatic surcharge +1
    ex_upd=att.update({att.exnow:'j2',att.wnow:att.j2+1,att.j2:att.j1+1}).where( (att.j2ig.is_null(1))
    & (att.j1ig==1) & (att.j3ig.is_null(1))
    & (att.s3ig.is_null(0)) & (att.s2ig.is_null(0))
    & (att.s1ig.is_null(0)))   
    ex_upd.execute()
    #j2 with/out automatic surcharge +1
    ex_upd=att.update({att.exnow:'j2',att.wnow:att.j2,att.j2:att.j1}).where( (att.j2ig.is_null(1))
    & (att.j1ig==0) & (att.j3ig.is_null(1))
    & (att.s3ig.is_null(0)) & (att.s2ig.is_null(0))
    & (att.s1ig.is_null(0)))   
    ex_upd.execute()    
    #j3 automatic surcharge +1
    ex_upd=att.update({att.exnow:'j3', att.wnow:att.j2+1,att.j3:att.j2+1}).where( (att.j3ig.is_null(1))
    & (att.j2ig==1) & (att.j1ig.is_null(0))
    & (att.s3ig.is_null(0)) & (att.s2ig.is_null(0))
    & (att.s1ig.is_null(0)))    
    ex_upd.execute()
    #j3 with/out automatic surcharge +1
    ex_upd=att.update({att.exnow:'j3', att.wnow:att.j2,att.j3:att.j2}).where( (att.j3ig.is_null(1))
    & (att.j2ig==0) & (att.j1ig.is_null(0))
    & (att.s3ig.is_null(0)) & (att.s2ig.is_null(0))
    & (att.s1ig.is_null(0)))    
    ex_upd.execute()
     
    #exnow is Finished!
    ex_upd=att.update({att.exnow:'finished'}).where(
    (att.s3.is_null(0) & att.j3.is_null(0)) & (att.s3ig.is_null(0))
    & (att.j3ig.is_null(0)) & (att.s2ig.is_null(0))
    & (att.j2ig.is_null(0)) & (att.s1ig.is_null(0))
    & (att.j1ig.is_null(0)))
    ex_upd.execute()
    #exnow is Finished2!
    ex_upd=att.update({att.flow:2}).where(
    (att.s3.is_null(0) & att.j3.is_null(0)) & (att.s3ig.is_null(0))
    & (att.j3ig.is_null(0)) & (att.s2ig.is_null(0))
    & (att.j2ig.is_null(0)) & (att.s1ig.is_null(0))
    & (att.j1ig.is_null(0)))
    ex_upd.execute()
    #exnow is Finished3!
    ex_upd=att.update({att.aend:1}).where(
    (att.s3.is_null(0) & att.j3.is_null(0)) & (att.s3ig.is_null(0))
    & (att.j3ig.is_null(0)) & (att.s2ig.is_null(0))
    & (att.j2ig.is_null(0)) & (att.s1ig.is_null(0))
    & (att.j1ig.is_null(0)))
    ex_upd.execute()


    #snatch declaretived weight set wnow
    att.update({att.s1d:att.s1}).where((att.s1d.is_null(1)) & (att.exnow=='s1')).execute()
    att.update({att.s2d:att.s2}).where((att.s2d.is_null(1)) & (att.exnow=='s2')).execute()
    att.update({att.s3d:att.s3}).where((att.s3d.is_null(1)) & (att.exnow=='s3')).execute()
    #jerk declaretived weight set
    att.update({att.j1d:att.j1}).where((att.j1d.is_null(1)) & (att.exnow=='j1')).execute()
    att.update({att.j2d:att.j2}).where((att.j2d.is_null(1)) & (att.exnow=='j2')).execute()
    att.update({att.j3d:att.j3}).where((att.j3d.is_null(1)) & (att.exnow=='j3')).execute()
    #wnow SNATCH
    att.update({att.wnow:att.s1ch2}).where((att.s1ch2.is_null(0)) & (att.s1ch1.is_null(0)) & (att.exnow=='s1')).execute()
    att.update({att.wnow:att.s1ch1}).where((att.s1ch2.is_null(1)) & (att.s1ch1.is_null(0)) & (att.exnow=='s1')).execute()
    
    att.update({att.wnow:att.s2ch2}).where((att.s2ch2.is_null(0)) & (att.s2ch1.is_null(0)) & (att.exnow=='s2')).execute()
    att.update({att.wnow:att.s2ch1}).where((att.s2ch2.is_null(1)) & (att.s2ch1.is_null(0)) & (att.exnow=='s2')).execute()
    
    att.update({att.wnow:att.s3ch2}).where((att.s3ch2.is_null(0)) & (att.s3ch1.is_null(0)) & (att.exnow=='s3') ).execute()
    att.update({att.wnow:att.s3ch1}).where((att.s3ch2.is_null(1)) & (att.s3ch1.is_null(0)) & (att.exnow=='s3') ).execute()    
    #wnow CLEAN&JERK
    att.update({att.wnow:att.j1ch2}).where((att.j1ch2.is_null(0)) & (att.j1ch1.is_null(0)) & (att.exnow=='j1')).execute()
    att.update({att.wnow:att.j1ch1}).where((att.j1ch2.is_null(1)) & (att.j1ch1.is_null(0)) & (att.exnow=='j1')).execute()
    
    att.update({att.wnow:att.j2ch2}).where((att.j2ch2.is_null(0)) & (att.j2ch1.is_null(0)) & (att.exnow=='j2')).execute()
    att.update({att.wnow:att.j2ch1}).where((att.j2ch2.is_null(1)) & (att.j2ch1.is_null(0)) & (att.exnow=='j2')).execute()
    
    att.update({att.wnow:att.j3ch2}).where((att.j3ch2.is_null(0)) & (att.j3ch1.is_null(0)) & (att.exnow=='j3') ).execute()
    att.update({att.wnow:att.j3ch1}).where((att.j3ch2.is_null(1)) & (att.j3ch1.is_null(0)) & (att.exnow=='j3') ).execute()        

    #s&j place setup
    #att.update({att.j1d:att.j1}).where((att.j1d.is_null(1))).execute()
    result = att.select(att.id).where(1).order_by(att.dblsum).limit(1)
    mycursor = db.cursor()
    sql = "UPDATE v7now SET place = 0, snatch_place = 0, cleanjerk_place = 0 WHERE 1"
    mycursor.execute(sql)
    # sql = "UPDATE v7now SET snatch_place = 0 WHERE 1"
    # mycursor.execute(sql)    
    # sql = "UPDATE v7now SET cleanjerk_place = 0 WHERE 1"
    # mycursor.execute(sql)        


# NEW PLACES / МЕСТА !!!
    #general PLACES
    sql = "SET @n_place := 0;"
    mycursor.execute(sql)
    sql = " UPDATE v7now SET place = @n_place := @n_place + 1 ORDER BY doublesum DESC, id ASC;"
    mycursor.execute(sql)
    #snatch PLACES
    sql = "SET @s_place := 0;"
    mycursor.execute(sql)
    sql = " UPDATE v7now SET snatch_place = @s_place := @s_place + 1 ORDER BY snatchresult DESC, id ASC;"
    mycursor.execute(sql)
    #jerk PLACES
    sql = "SET @j_place := 0;"
    mycursor.execute(sql)
    sql = " UPDATE v7now SET cleanjerk_place = @j_place := @j_place + 1 ORDER BY cleanjerkresult DESC, id ASC;"
    mycursor.execute(sql)


#############################
### CALC OP / NOP
#############################

    # s1 = get_id_min_w_s1(exclude_id=22)

    # s1 = get_id_min_w_s1()
    # s2 = get_id_min_w_s2()
    # s3 = get_id_min_w_s3()

    
    # ic('#################set_app_weight_now ###################################')
    # ic(s1)
    # ic(s2)
    # ic(s3)
    # ic('##################set_app_weight_now##################################')
    # idzzz = sel_op_id(s1, s2, s3)
    # ic(idzzz)

    # if(idzzz is None):
    #     idzzz = 999

    # s1ex = get_id_min_w_s1(exclude_id=idzzz)
    # s2ex = get_id_min_w_s2(exclude_id=idzzz)
    # s3ex = get_id_min_w_s3(exclude_id=idzzz)  

    # ??????
    # getOPnow = get_op()
    # ??????  

    # ic('####################$$$$################################')
    # ic(s1ex)
    # ic(s2ex)
    # ic(getOPnow)    
    # ic(s3ex)
    # ic('#######################$$$$$#############################')
    # # sel_nop_id_pr = sel_nop_id(s1ex, s2ex, int(getOPnow))
    # sel_nop_id_pr = sel_nop_id(s1ex, s2ex, s3ex)
    # print('**********************====^^^^', sel_nop_id_pr)


    # if(SN is False and CJ is True):
    #     print('SN is None, CJ is TRUE = DO CJ TASKS!!!')
    #     j1 = get_id_min_w_j1()
    #     j2 = get_id_min_w_j2()
    #     j3 = get_id_min_w_j3()
    #     ic('#######################---#############################')
    #     ic(j1)
    #     ic(j2)
    #     ic(j3)
    #     ic('#####################----###############################')
    #     idzzz = sel_op_id(j1, j2, j3)
    #     ic(idzzz)

    #     if(idzzz is None):
    #         idzzz = 999
    #     j1ex = get_id_min_w_j1(exclude_id=idzzz)
    #     j2ex = get_id_min_w_j2(exclude_id=idzzz)
    #     j3ex = get_id_min_w_j3(exclude_id=idzzz)    
    #     ic('####################=====################################')
    #     ic(j1ex)
    #     ic(j2ex)
    #     ic(j3ex)    
    #     ic('####################======################################')
    #     sel_nop_id(j1ex, j2ex, j3ex)


    # if(SN is False and CJ is False):  
    #     print('SN is None, CJ is None = END ALL FLOW!!!')






    att.update({att.s3:att.s3ch2}).where((att.s3ch2.is_null(0)) & (att.s3ch1.is_null(0))).execute()
    att.update({att.s3:att.s3ch1}).where((att.s3ch2.is_null(1)) & (att.s3ch1.is_null(0))).execute()
    att.update({att.s3:att.s3d}).where((att.s3ch2.is_null(1)) & (att.s3ch1.is_null(1) & (att.s3d.is_null(0)))).execute()

    att.update({att.s2:att.s2ch2}).where((att.s2ch2.is_null(0)) & (att.s2ch1.is_null(0))).execute()
    att.update({att.s2:att.s2ch1}).where((att.s2ch2.is_null(1)) & (att.s2ch1.is_null(0))).execute()
    att.update({att.s2:att.s2d}).where((att.s2ch2.is_null(1)) & (att.s2ch1.is_null(1) & (att.s2d.is_null(0)))).execute()

    att.update({att.s1:att.s1ch2}).where((att.s1ch2.is_null(0)) & (att.s1ch1.is_null(0))).execute()
    att.update({att.s1:att.s1ch1}).where((att.s1ch2.is_null(1)) & (att.s1ch1.is_null(0))).execute()
    att.update({att.s1:att.s1d}).where((att.s1ch2.is_null(1)) & (att.s1ch1.is_null(1) & (att.s1d.is_null(0)))).execute()    
    
    att.update({att.j3:att.j3ch2}).where((att.j3ch2.is_null(0)) & (att.j3ch1.is_null(0))).execute()
    att.update({att.j3:att.j3ch1}).where((att.j3ch2.is_null(1)) & (att.j3ch1.is_null(0))).execute()
    att.update({att.j3:att.j3d}).where((att.j3ch2.is_null(1)) & (att.j3ch1.is_null(1) & (att.j3d.is_null(0)))).execute()    
    
    att.update({att.j2:att.j2ch2}).where((att.j2ch2.is_null(0)) & (att.j2ch1.is_null(0))).execute()
    att.update({att.j2:att.j2ch1}).where((att.j2ch2.is_null(1)) & (att.j2ch1.is_null(0))).execute()
    att.update({att.j2:att.j2d}).where((att.j2ch2.is_null(1)) & (att.j2ch1.is_null(1) & (att.j2d.is_null(0)))).execute()

    att.update({att.j1:att.j1ch2}).where((att.j1ch2.is_null(0)) & (att.j1ch1.is_null(0))).execute()
    att.update({att.j1:att.j1ch1}).where((att.j1ch2.is_null(1)) & (att.j1ch1.is_null(0))).execute()
    att.update({att.j1:att.j1d}).where((att.j1ch2.is_null(1)) & (att.j1ch1.is_null(1) & (att.j1d.is_null(0)))).execute()


    mycursor.close()
    db.close()
    return ex_upd








##################################################################
##################################################################
# @app.context_processor
# def pythonFct(data):
#     return "This is my data: {0}".format(data)
##################################################################
##################################################################
@app.route('/reports', methods = ['POST', 'GET'])
def reports():
    now='fd32432'
    current_date = datetime.date.today()
    print(current_date)
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    return render_template('reports.html',now=now,current_date=current_date,date_time=date_time)

# ROUTE OF INDEX PAGE
@app.route('/management', methods = ['POST', 'GET'])
def management():
    return render_template('management.html')


@app.route('/screens', methods = ['POST', 'GET'])
def screens():
    return render_template('screens.html')


@app.route('/opt/<int:optid>/<int:optval>', methods=['GET', 'POST'], defaults={'optid': 1,'optval': 0})
@cross_origin()
def options(optid,optval):
    # optval = 1
    # optid = 13
    if request.method == 'POST':
        mycursor = db.cursor()
        sql = "UPDATE opt SET value = %s WHERE id= %s"
        val = (optval,optid)
        mycursor.execute(sql,val)
        db.commit()

    asddd = opt.update({opt.o_val:optval}).where((opt.opt_id==optid)).execute()
    print(optid)
    print(optval)
    ###
    q_opt = opt.select(opt.o_name,opt.o_val,opt.opt_id,opt.o_desc,opt.o_descoff,opt.o_param)#.where(opt.opt_id==7)
    optdata = [t for t in q_opt] 
    optdata_z = dict_helper(optdata)

    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id))
    attdata = [t for t in qu]
    attz = dict_helper(attdata)

    #return jsonify({'All athletes': attz})
    return render_template('opt.html', optdata_z=optdata_z,optdata=optdata, attdata=attdata, attz=attz,CJ=CJ,SN=SN)



@app.route('/about', methods = ['POST', 'GET'])
def about():
    print('v7pro :  ABOUT INFO!')
    # return redirect(url_for('index'))
    return render_template('about.html')








@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = 'Not Foubd - 404 !'), 404        

################## WS 
def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count})

@socketio.event
def my_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']})


@socketio.event
def my_broadcast_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)


@socketio.event
def join(message):
    join_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socketio.event
def leave(message):
    leave_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socketio.on('close_room')
def on_close_room(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response', {'data': 'Room ' + message['room'] + ' is closing.',
                         'count': session['receive_count']},
         to=message['room'])
    close_room(message['room'])


@socketio.event
def my_room_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         to=message['room'])


@socketio.event
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()

    session['receive_count'] = session.get('receive_count', 0) + 1
    # for this emit we use a callback function
    # when the callback function is invoked we know that the message has been
    # received and it is safe to disconnect
    emit('my_response',
         {'data': 'Disconnected!', 'count': session['receive_count']},
         callback=can_disconnect)


@socketio.event
def my_ping():
    emit('my_pong')


@socketio.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected', request.sid)

##################

@app.route('/quit', methods = ['POST', 'GET'])
def quit_app():
    #os._exit(0)
    #sys.exit(0)
    #####     sudo pkill python
    #os.kill(os.getpid(),signal.SIGKILL)
    print('=====================================')
    return redirect(url_for('index'))
# @app.route('/chronograph', methods = ['GET','POST'])
# def chronograph():
#     return render_template('chrono.html')    

@app.route('/stat', methods = ['POST', 'GET'])
def stat():
    print('=====================================')
    # return redirect(url_for('index'))
    return render_template('stat.html')

@app.route('/bmodel', methods = ['POST', 'GET'])
def bmodel():

    # UPD
    rank_id = att.update(rank_id=att.wcat_id).where(att.id > 0)
    response_z = rank_id.execute()
    # SELECT
    qu = att.select(att.id,att.op,att.nop,att.sname,att.fname,att.wcat_id,
    att.sex,att.s1,att.s2,att.s3,att.sres,att.jres,att.j1,att.ow,att.dblsum,
    att.country_id,att.city_id,att.wnow,
    att.j2,att.j3,att.s1ig,att.s2ig,att.s3ig,att.j1ig,att.j2ig,att.j3ig,
    country.flag,country.name,cat.lwcat,cities.cname).join(country,on=(att.country_id == country.country_id)).switch(att).join(cat,on=(att.wcat_id == cat.wcat_id)).switch(att).join(cities,on=(att.city_id == cities.cities_id)).where(att.op==1)
    attdata = [t for t in qu]
    attz = dict_helper(attdata)
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    
    if "iphone" in user_agent:
        return render_template('bmodel.html', attdata=attdata, attz=attz,CJ=CJ,SN=SN)
    elif "android" in user_agent:
        return render_template('bmodel.html', attdata=attdata, attz=attz,CJ=CJ,SN=SN)
    else:
        return render_template('bmodel.html', response_z=response_z, attdata=attdata, attz=attz)
########################        

#####################################################################




#####################################################################
##### v7pro AT METHODS


#####################################################################
##### clear op, set all att.op = 0
def get_op():
    mycursor = db.cursor()    
    sql = "SELECT id FROM v7now WHERE op=1;"
    mycursor.execute(sql)
    query_result = mycursor.fetchone()
    print(query_result,'@@@____________ :::')
    rezuuuuu = -1
    try:
        if(query_result[0] is None):
            query_result[0]=0
    except:
        rezuuuuu = 0
    if(rezuuuuu!=0):
        rezuuuuu = str(query_result[0])
    return rezuuuuu



#####################################################################
##### clear op, set all att.op = 0
def clear_op():
    clear = att.update(op=0).where(att.id > 0)
    response = clear.execute()
    db.close()
    return response

#####################################################################
##### clear nop, set all att.nextop = 0
def clear_nop():
    clear = att.update(nop=0).where(att.id > 0)
    response = clear.execute()
    db.close()
    return response

#####################################################################
##### set op, set att.op=1, by gets ID
def set_op(opid):
    setop = att.update(op=1).where(att.id == opid)
    response = setop.execute()
    db.close()
    return response

#####################################################################
##### set nextop, set att.nexiop=1, by gets ID
def set_nop(nopid):
    setnop = att.update(nop=1).where(att.id == nopid)
    response = setnop.execute()
    db.close()
    return response
#####################################################################
#####################################################################
#####################################################################

#####################################################################
##### set nextop, WO this ID set att.nexiop != ID
def set_nop_ex_this_id(exid):
    # !??!?!?!?
    setnop = att.update(nop=1).where(att.id == 5)
    response = setnop.execute()
    db.close()
    return response
#####################################################################
#####################################################################
#####################################################################



#####################################################################
##### get s1 weight by id
#####  <- weight int
def get_w_s1(id):
    req = att.get(att.id == id).wnow
    # req = att.get(att.id == id).s1
    return req

def get_w_s1_ex(id):
    req = att.get(att.id == id).s1
    return req

#####################################################################
##### get s2 weight by id
#####  <- weight int
def get_w_s2(id):
    req = att.get(att.id == id).wnow
    # req = att.get(att.id == id).s2
    return req

def get_w_s2_ex(id):
    req = att.get(att.id == id).s2
    # req = att.get(att.id == id).s2
    return req

#####################################################################
##### get s3 weight by id
#####  <- weight int
def get_w_s3(id):
    req = att.get(att.id == id).wnow
    # req = att.get(att.id == id).s3
    return req

def get_w_s3_ex(id):
    req = att.get(att.id == id).s3
    # req = att.get(att.id == id).s3
    return req


#####################################################################
##### get j1 weight by id
#####  <- weight int
def get_w_j1(id):
    req = att.get(att.id == id).wnow
    return req

def get_w_j1_ex(id):
    req = att.get(att.id == id).j1
    return req

#####################################################################
##### get j2 weight by id
#####  <- weight int
def get_w_j2(id):
    req = att.get(att.id == id).wnow
    return req

def get_w_j2_ex(id):
    req = att.get(att.id == id).j2
    return req

#####################################################################
##### get j3 weight by id
#####  <- weight int
def get_w_j3(id):
    req = att.get(att.id == id).wnow
    return req

def get_w_j3_ex(id):
    req = att.get(att.id == id).j3
    return req


#####################################################################
#####################################################################
#####################################################################
##### select from (s1&s2&s3) by arg:id min weight and sep op id
#####  -> id (op id)
def sel_op_id(s1,s2,s3):
    global SN
    global CJ
    # if(SN is False):
    #    print('SN is None, now CLEAN&JERK !!!')
    #    wr_sel_op_id_cj()
    # #    !!!!!!!!!!!!!!!!!!
    if(SN!=False):
        print(f'SN!=FalseSN!=FalseSN!=FalseSN!=FalseSN!=False')

        if(s1>0 and s2==0 and s3==0):
            print(f"op= s1@@, id:{s1} weight:{get_w_s1(s1)}")
            clear_op()
            set_op(s1)
            return s1
############################## only s2
        if(s1==0 and s2>0 and s3==0):
            print(f"op= s2**, id:{s2} weight:{get_w_s2(s2)}")
            clear_op()
            set_op(s2)
            return s2
############################## only s3
        if(s1==0 and s2==0 and s3>0):
            print(f"op= s3_+_, id:{s3} weight:{get_w_s3_ex(s3)}")

            clear_op()
            set_op(s3)   
            

            return s3
############################## s1 && s2
        if(s1>0 and s2>0 and s3==0):
            if(get_w_s1(s1))<=(get_w_s2(s2)):
                print(f"op= s1##, id:{s1} weight:{get_w_s1(s1)}")
                clear_op()
                set_op(s1)
                return s1
            elif(get_w_s1(s1))>(get_w_s2(s2)):
                print(f"op= s2*ZZZZZ, id:{s2} weight:{get_w_s2(s2)}")
                print(f'{get_w_s1(s1)} >>>>>>  {get_w_s2(s2)}')
                clear_op()
                set_op(s2)
            elif(get_w_s1(s1))>=(get_w_s2(s2)):
                print(f"op= s1 == SUCK!!!!, id:{s1} weight:{get_w_s1(s1)}")
                clear_op()
                set_op(s1)            
                return s1
############################## s1 && s3
        if(s1>0 and s2==0 and s3>0):
            if(get_w_s1(s1))<=(get_w_s3(s3)):
                print(f"op= s1__, id:{s1} weight:{get_w_s1(s1)}")
                clear_op()
                set_op(s1)
                return s1
            elif(get_w_s1_ex(s1))>(get_w_s3_ex(s3)):
                print(f"op= s3_)(, id:{s3} weight:{get_w_s3_ex(s3)}")
                clear_op()
                set_op(s3)
                return s3
############################## s2 && s3
        if(s1==0 and s2>0 and s3>0):
            if(get_w_s2_ex(s2))<=(get_w_s3_ex(s3)):
                print(f"op= s2%%, id:{s2} weight:{get_w_s2_ex(s2)}")
                clear_op()
                set_op(s2)
                return s2
            elif(get_w_s1(s2))>(get_w_s3(s3)):
                print(f"op= s3____, id:{s3} weight:{get_w_s3(s3)}")
                clear_op()
                set_op(s3)
                return s3
############################## s1 && s2 && s3
        if(s1>0 and s2>0 and s3>0):
            s1w,s2w,s3w = get_w_s1_ex(s1),get_w_s2_ex(s2),get_w_s3_ex(s3)
            # s1w,s2w,s3w = get_w_s1_ex(s1),get_w_s2_ex(s2),get_w_s3_ex(s3)
            # ?????
            clear_op()
            minest = 0
            app = [] # approach=подход s1 ? s2 ? s3
            if(s1w is None):
                s1w = 0
            if(s2w is None):
                s2w = 0
            if(s3w is None):
                s3w = 0                                
            if s1w <= s2w and s1w <= s3w:
                minest = s1w
                set_op(s1)
                print(f"op= s1** id:{s1} w:{s1w}")
                return s1
            elif s2w <= s3w:
                minest = s2w
                set_op(s2)
                # set_op(4) ?????????????????
                print(f"op ::= s2 id:{s2} w:{s2w}")



                # ********** ????****
                
                return s2
            else:
                minest = s3w
                set_op(s3)
                print(f"op= s3 id:{s3} w:{s3w}")


                return s3

### If all weight = 0 - The END of flow!            
        if(s1==0 and s2==0 and s3==0):
            print(f"(1-st) SNATCH THE END!!! ids: {s1}, {s2}, {s3}")
            SN,CJ= False, True
            print(f"Snatch is:  {SN}")
            print(f"Clear&Jerk is:  {CJ}")

        # if(SN is False):
        #     print('SN is None, now CLEAN&JERK !!!######')

        #     # ############
        #     j1=get_min_w_j1()
        #     j2=get_min_w_j2()
        #     j3=get_min_w_j3()
        #     wr_sel_nop_id_cj(j1,j2,j3)
        #     print(f"wr_sel_nop_id_cj: {j1}, {j2}, {j3}")
            
    #    !!!!!!!!!!!!!!!!!!        
    
        else:
    #print(f"a1={s1w} s2={s2w} s3={s3w}, min={minest} app={app}")
    #get_w_s2(s2) = 0
            print(f"ids-ZZZXXXX: {s1}, {s2}, {s3}")
            # return s2 ?????
            if(SN is False):
                print('SN is None, now CLEAN&JERK !!!######')

            # ############
                j1=get_min_w_j1()
                j2=get_min_w_j2()
                j3=get_min_w_j3()
                wr_sel_nop_id_cj(j1,j2,j3)
                print(f"wr_sel_nop_id_cj: {j1}, {j2}, {j3}")        

        if(s1 is None or s2 is None or s3 is None):
            print(f"(s1 is None or s2 is None or s3 is None !!!!!!!!!!!!")
            SN,CJ= False, False
            print(f"Snatch is:  {SN}")
            print(f"Clear&Jerk is:  {CJ}")



def sel_nop_id(s1,s2,s3):
    nowid = -1
    global SN
    global CJ
    #print(f"{s1} {s2} {s3} ____3")
############################## only s1
    if(s1>0 and s2==0 and s3==0):
        print(f"NOP= s1*, id:{s1} weight:{get_w_s1(s1)}")
        clear_nop()
        set_nop(s1)
        nowid = s1
############################## only s2
    if(s1==0 and s2>0 and s3==0):
        print(f"NOP= s2,,,,, id:{s2} weight:{get_w_s2(s2)}")
        clear_nop()
        set_nop(s2)
        nowid = s2
############################## only s3
    if(s1==0 and s2==0 and s3>0):
        print(f"NOP=>>> s3, id:{s3} weight:{get_w_s3(s3)}")
        clear_nop()
        set_nop(s3)        
        nowid = s3
############################## s1 && s2
    if(s1>0 and s2>0 and s3==0):
        if(get_w_s1(s1))<=(get_w_s2(s2)):
            print(f"NOP= s1!, id:{s1} weight:{get_w_s1(s1)}")
            clear_nop()
            set_nop(s1)
            nowid = s1
        elif(get_w_s1_ex(s1))>(get_w_s2_ex(s2)):


            print(f"NOP= s2__, id:{s2} weight:{get_w_s2_ex(s2)}")
            # get_min_w_s1
            # get_min_w_s1 get_min_w_s1 get_min_w_s1
            # /////////// ?????????
            # ?????????????????????
            get_min_w_s2()
            # 



# CLEAN ALL! # CLEAN ALL! # CLEAN ALL! # CLEAN ALL!
# CLEAN ALL! # CLEAN ALL! # CLEAN ALL! # CLEAN ALL!

# CLEAN ALL! # CLEAN ALL! # CLEAN ALL! # CLEAN ALL!
# CLEAN ALL! # CLEAN ALL! # CLEAN ALL! # CLEAN ALL!

            print(f"get_w_s1(s1) > (get_w_s2(s2) : {s1} > {s2} || weight:{get_w_s1_ex(s1)} > {get_w_s2_ex(s2)}")
            clear_nop()
            set_nop(s2)
            # CHK !!! # CHK !!! # CHK !!! # CHK !!! # CHK !!!
            # # CHK !!! # CHK !!! # CHK !!! # CHK !!! # CHK !!! 
            vvp7n = get_op()
            print(f'vvp7n ========== :: {vvp7n} | s1: {s1} | s2: {s2}')
            print(f'vvp7n ========== :: {type(vvp7n)} | s1: {type(s1)} | s2: {type(s2)}')
            if(int(vvp7n)==int(s2)):
                print(f'===== $$$ ## :::')
                clear_nop()
                set_nop(s1)





            # set_nop(s1)
            nowid = s2

            
















            # 
            # ??????????????????
            # ПИЗДЕЦ ??!?!?!?! ХУЙ ЗНАЕТ ПОКА...
            # НАДО ПРОВЕРЯТЬ НА ДУБЛИ ТУТ???
            # ??????????????????


        elif(get_w_s1(s1))==(get_w_s2(s2)):
            print(f"NOP= s2__*&*&_, id:{s2} weight:{get_w_s2(s2)}")
            print(f"get_w_s1(s1) == get_w_s2(s2) : {s1} = {s2} == weight:{get_w_s1_ex(s1)} == {get_w_s2_ex(s2)}")
            clear_nop()
            set_nop(s1)
            nowid = s1            
############################## s1 && s3
    if(s1>0 and s2==0 and s3>0):
        if(get_w_s1(s1))<=(get_w_s3(s3)):
            print(f"NOP= s1**, id:{s1} weight:{get_w_s1(s1)}")
            clear_nop()
            set_nop(s1)
            nowid = s1
        elif(get_w_s1_ex(s1))>(get_w_s3_ex(s3)):
            # get_
            print(f"NOP= s3 % ___, id:{s3} <=>: {get_w_s1(s1)} > {get_w_s3(s3)}")
            clear_nop()
            poolipa=0
            try:
                # get_id_min_w_s3
                poolipa = get_id_min_w_s3()
                print(f'<<<<<<<@ :: poolipa = get_id_min_w_s3() {poolipa}')
            except:
                poolipa = -1
            # set_nop(s1)
            # nowid = s1
            set_nop(s3)
            nowid = s3
            if(poolipa!=-1 and poolipa!=0):
                set_nop(poolipa)
                nowid = poolipa
                        
############################## s2 && s3
    if(s1==0 and s2>0 and s3>0):
        if(get_w_s2(s2))<=(get_w_s3(s3)):
            print(f"NOP= s2_+++--, id:{s2} weight:{get_w_s2(s2)}")
            clear_nop()
            set_nop(s2)
            nowid = s2
        elif(get_w_s1(s2))>(get_w_s3(s3)):
            print(f"NOP= s3=>, id:{s3} weight:{get_w_s3(s3)}")
            clear_nop()
            set_nop(s3)
            nowid = s3
############################## s1 && s2 && s3
    if(s1>0 and s2>0 and s3>0):
        s1w,s2w,s3w = get_w_s1_ex(s1),get_w_s2_ex(s2),get_w_s3_ex(s3)
        clear_nop()
        minest = 0
        app = [] # approach=подход s1 ? s2 ? s3
        if s1w <= s2w and s1w <= s3w:
            minest = s1w
            clear_nop()
            set_nop(s1)
            nowid = s1
            print(f"NOP= s1* id:{s1} w:{s1w}")
        elif s2w <= s3w:
            minest = s2w
            clear_nop()
            set_nop(s2)
            nowid = s2
            print(f"NOP= s2==== id:{s2} w:{s2w}")
        else:
            minest = s3w
            clear_nop()
            set_nop(s3)
            nowid = s3
            print(f"NOP= s3_ id:{s3} w:{s3w}")

### If all weight = 0 - The END of flow!            
    if(s1==0 and s2==0 and s3==0):
        print(f" SNATCH THE END (2nd) !!! ids: {s1}, {s2}, {s3}")
        SN,CJ= False, True
        print(f"Snatch is:  {SN}")
        print(f"Clear&Jerk is:  {CJ}")

        if(SN is False):
            print('SN is None, now CLEAN&JERK @@@@@!!!')
            # wr_sel_op_id_cj(j1,j2,j3)
            #####

    else:

        if(SN is False and CJ is True):
            print('JERK -> JERK -> JERK -> JERK -> JERK -> ')
            # NOP NOP NOP !!!!!!!!
            # NOP NOP NOP !!!!!!!!
            # NOP NOP NOP !!!!!!!!
            print('->>> wr_sel_nop_id_cj  JERK -> JERK -> JERK -> JERK -> ')
            jj1 = get_min_w_j1()
            jj2 = get_min_w_j2()
            jj3 = get_min_w_j3()
            wr_sel_nop_id_cj(jj1,jj2,jj3)


    #print(f"a1={s1w} s2={s2w} s3={s3w}, min={minest} app={app}")
    #get_w_s2(s2) = 0
        print(f" SNATCH !!! THE  _ids: {s1}, {s2}, {s3}")
        # SN,CJ= False, True
        print(f"Snatch is±±±±±±±±±±±:  {SN}")
        print(f"Clear&Jerk is±±±±±±±:  {CJ}")
        
        print(f"input id's: {s1}, {s2}, {s3},[ lastID: {nowid} ]")
        print(f"NEED TO DO!!!  {s1} -  {s2} - {s3},[ lastID: {nowid} ]")
        # print(f"NEED TO DO!!! [ {s1} ]:{get_w_s1(s1)}, {s3}:{get_w_s3(s3)},[ lastID: {nowid} ]")
        # *****************
        # ?????????????????
        ############################## s2 && s3
        # ///////////////// ?????????????????????
        # if(s1==0 and s2>0 and s3>0):
        #     if(get_w_s2(s2))<=(get_w_s3(s3)):
        #         print(f"NOP= s2, id:{s2} weight:{get_w_s2(s2)}")
        #         clear_op()
        #         set_op(s2)
        #         nowid = s2
        #     elif(get_w_s1(s2))>(get_w_s3(s3)):
        #         print(f"NOP= s3, id:{s3} weight:{get_w_s3(s3)}")
        #         clear_op()
        #         set_op(s3)
        #         nowid = s3    
                # ///////////////// ?????????????????????   
        
        return nowid





########################################################
### WRAPPER to SELECT _OP_ CJ #########################
# def wr_sel_op_id_cj(j1=0,j2=0,j3=0):
# def wr_sel_op_id_cj():
# # wr_sel_nop_id_cj
#     print('############## START C&J _OP!')
#     print('############################')
#     global SN
#     global CJ
# ############################## only s1
#     if(j1>0 and j2==0 and j3==0):
#         print(f"op=js1@@, id:{j1} weight:{get_w_j1(j1)}")
#         clear_op()
#         set_op(j1)
#         return j1
# ############################## only s2
#     if(j1==0 and j2>0 and j3==0):
#         print(f"op= j2**, id:{j2} weight:{get_w_j2(j2)}")
#         clear_op()
#         set_op(j2)
#         return j2
# ############################## only s3
#     if(j1==0 and j2==0 and j3>0):
#         print(f"op= j3, id:{j3} weight:{get_w_j3(j3)}")
#         clear_op()
#         set_op(j3)   
#         return j3
# ############################## s1 && s2
#     if(j1>0 and j2>0 and j3==0):
#         if(get_w_j1(j1))<=(get_w_j2(j2)):
#             print(f"op= j1##, id:{j1} weight:{get_w_j1(j1)}")
#             clear_op()
#             set_op(j1)
#             return j1
#         elif(get_w_j1(j1))>(get_w_j2(j2)):
#             print(f"op= j2*, id:{j2} weight:{get_w_j2(j2)}")
#             clear_op()
#             set_op(j2)
#             return j2
# ############################## s1 && s3
#     if(j1>0 and j2==0 and j3>0):
#         if(get_w_j1(j1))<=(get_w_j3(j3)):
#             print(f"op= j1__, id:{j1} weight:{get_w_j1(j1)}")
#             clear_op()
#             set_op(j1)
#             return j1
#         elif(get_w_j1(j1))>(get_w_j3(j3)):
#             print(f"op= j3, id:{j3} weight:{get_w_j3(j3)}")
#             clear_op()
#             set_op(j3)
#             return j3
# ############################## s2 && s3
#     if(j1==0 and j2>0 and j3>0):
#         if(get_w_j2(j2))<=(get_w_j3(j3)):
#             print(f"op= j2%%, id:{j2} weight:{get_w_j2(j2)}")
#             clear_op()
#             set_op(j2)
#             return j2
#         elif(get_w_j1(j2))>(get_w_j3(j3)):
#             print(f"op= j3, id:{j3} weight:{get_w_j3(j3)}")
#             clear_op()
#             set_op(j3)
#             return j3
# ############################## s1 && s2 && s3
#     if(j1>0 and j2>0 and j3>0):
#         j1w,j2w,j3w = get_w_j1(j1),get_w_j2(j2),get_w_j3(j3)
#         clear_op()
#         minest = 0
#         app = [] # approach=подход s1 ? s2 ? s3
#         if j1w <= j2w and j1w <= j3w:
#             minest = j1w
#             set_op(j1)
#             print(f"op= j1** id:{j1} w:{j1w}")
#             return j1
#         elif j2w <= j3w:
#             minest = j2w
#             set_op(j2)
#             print(f"op= j2 id:{j2} w:{j2w}")
#             return j2
#         else:
#             minest = j3w
#             set_op(j3)
#             print(f"op= j3 id:{j3} w:{j3w}")
#             return j3

# ### If all weight = 0 - The END of flow!            
#     if(j1==0 and j2==0 and j3==0):
#         print(f"CLEAN&JERK THE END!!! ids: {j1}, {j2}, {j3}")
#         SN,CJ= False, False
#         print(f"Snatch is:  {SN}")
#         print(f"Clear&Jerk is:  {CJ}")

#         if(SN is False and CJ is False):
#             print('SN is None, CJ is None = END ALL!!!')

#     #    !!!!!!!!!!!!!!!!!!        
    
#     else:
#         print(f"ids-YYY: {j1}, {j2}, {j3}")




#     #wr_sel_nop_id_cj()


########################################################



########################################################
### WRAPPER to SELECT _NOP_ CJ #########################
def wr_sel_nop_id_cj(j1,j2,j3):
    j1=get_min_w_j1()
    j2=get_min_w_j2()
    j3=get_min_w_j3()
    nowid = 0


    print('###### START C&J _NOP!')
    print('####### ERROR ########')
    print('######################')
    print(f"{j1} {j2} {j3} ____=========+++++++ j1-j2-j3")


    # НАДО ПРАВИТЬ ЭТО ⤵ ⤵ ⤵
    # ПИЗДЕЦ
# ############################## only s1
#     if(s1>0 and s2==0 and s3==0):
#         print(f"op J= J1@@, id:{s1} weight:{get_w_s1(s1)}")
#         clear_op()
#         set_op(s1)
#         return s1
# ############################## only s2
#     if(s1==0 and s2>0 and s3==0):
#         print(f"op= J2**, id:{s2} weight:{get_w_s2(s2)}")
#         clear_op()
#         set_op(s2)
#         return s2
# ############################## only s3
#     if(s1==0 and s2==0 and s3>0):
#         print(f"op= J3, id:{s3} weight:{get_w_s3(s3)}")
#         clear_op()
#         set_op(s3)   
#         return s3
# ############################## s1 && s2
#     if(s1>0 and s2>0 and s3==0):
#         if(get_w_s1(s1))<=(get_w_s2(s2)):
#             print(f"op= J1##, id:{s1} weight:{get_w_s1(s1)}")
#             clear_op()
#             set_op(s1)
#             return s1
#         elif(get_w_s1(s1))>(get_w_s2(s2)):
#             print(f"op= J2*ZZZZZ, id:{s2} weight:{get_w_s2(s2)}")
#             print(f'{get_w_s1(s1)} ====== {get_w_s2(s2)}')
#             clear_op()
#             set_op(s2)
#         elif(get_w_s1(s1))>=(get_w_s2(s2)):
#             print(f"op= J1 == SUCK!!!!, id:{s1} weight:{get_w_s1(s1)}")
#             clear_op()
#             set_op(s1)            
#             return s1
# ############################## s1 && s3
#     if(s1>0 and s2==0 and s3>0):
#         if(get_w_s1(s1))<=(get_w_s3(s3)):
#             print(f"op= J1__, id:{s1} weight:{get_w_s1(s1)}")
#             clear_op()
#             set_op(s1)
#             return s1
#         elif(get_w_s1(s1))>(get_w_s3(s3)):
#             print(f"op= J3, id:{s3} weight:{get_w_s3(s3)}")
#             clear_op()
#             set_op(s3)
#             return s3
# ############################## s2 && s3
#     if(s1==0 and s2>0 and s3>0):
#         if(get_w_s2(s2))<=(get_w_s3(s3)):
#             print(f"op= J2%%, id:{s2} weight:{get_w_s2(s2)}")
#             clear_op()
#             set_op(s2)
#             return s2
#         elif(get_w_s1(s2))>(get_w_s3(s3)):
#             print(f"op= J3, id:{s3} weight:{get_w_s3(s3)}")
#             clear_op()
#             set_op(s3)
#             return s3
# ############################## s1 && s2 && s3
#     if(s1>0 and s2>0 and s3>0):
#         s1w,s2w,s3w = get_w_s1(s1),get_w_s2(s2),get_w_s3(s3)
#         clear_op()
#         minest = 0
#         app = [] # approach=подход s1 ? s2 ? s3
#         if s1w <= s2w and s1w <= s3w:
#             minest = s1w
#             set_op(s1)
#             print(f"op= J1** id:{s1} w:{s1w}")
#             return s1
#         elif s2w <= s3w:
#             minest = s2w
#             set_op(s2)
#             print(f"op= J2 id:{s2} w:{s2w}")
#             return s2
#         else:
#             minest = s3w
#             set_op(s3)
#             print(f"op= J3 id:{s3} w:{s3w}")
#             return s3

# ### If all weight = 0 - The END of flow!            
#     if(s1==0 and s2==0 and s3==0):
#         print(f"CLEAN&JERK THE END!!! ids: {s1}, {s2}, {s3}")
#         SN,CJ= False, False
#         print(f"Snatch is:  {SN}")
#         print(f"Clear&Jerk is:  {CJ}")

#         if(SN is False):
#             print('SN is None, now CLEAN&JERK !!!######')
#             # ############
#             # wr_sel_op_id_cj(j1,j2,j3)
#     #    !!!!!!!!!!!!!!!!!!        
    
#     else:
#     #print(f"a1={s1w} s2={s2w} s3={s3w}, min={minest} app={app}")
#     #get_w_s2(s2) = 0
#         print(f"ids-ZZZ: {s1}, {s2}, {s3}")


    return nowid


########################################################

#####################################################################
##### get min s1 with double weigh
#####  -> 1:{id,weight}..n{id,weight}
def get_min_w_s1():
    ma = att.alias()
    rez = {}
    i=0
    # subq = ma.select(fn.MIN(ma.s1))
    query = (att.select(att.id, att.s1))#.where(att.s1 == subq))
    for item in query.dicts().execute():
        i+=1
        rez[i]=item
    print(f'~Z~~~~~~~~~~ ::: REZ: // {rez}')
    return rez




@app.route('/get_min_w_s2', methods=['GET', 'POST'])
def get_min_w_s2():
    ma = att.alias()
    rez = {}
    i=0
    subq = ma.select(fn.MIN(ma.s2))
    # query = (att.select(att.id, att.j2).where(att.j2 == subq,att.j2ig.is_null(0) ))
    # ????????????????????????????
    # ПИЗДЕЦ  ПИЗДЕЦ  ПИЗДЕЦ
    # ????????????????????????????
    query = (att.select(att.id, att.s2).where(att.s2 == subq,att.s2ig.is_null(1) ))
    # ????????????????????????????
    # ПИЗДЕЦ  ПИЗДЕЦ  ПИЗДЕЦ
    # ????????????????????????????
    for item in query.dicts().execute():
        i+=1
        rez[i]=item

# *******************************
# 2 EQUAL WEIGHT in CJ2
# *******************************
    if(i==2):
        print(rez[1])
        print(rez[1]['id'])
        print(rez[1]['s2'])
        print(f's2 ID:{rez[1]["id"]} w:{rez[1]["s2"]} ======= Js ID:{rez[2]["id"]} w:{rez[2]["s2"]} !!!')
        print(f's2 TWO EQUAL WEIGHT !!!!!!!!!!!')

        s1w1 = get_w_s1_ex(rez[1]["id"])
        s1w2 = get_w_s1_ex(rez[2]["id"])
        print(f'±±±±±± => J1 W:{s1w1} & J2 W:{s1w2} ')
        if(s1w1<=s1w2):
            print(f'if(S1w1<=S1w2::::::: {s1w1} = ||||||||||||| {s1w2}')
            print(f'SET_OP: {rez[1]["id"]} && ||||||||||||| SET_NOP: {rez[2]["id"]}')

            # ????????????????????????????
            # ПИЗДЕЦ  ПИЗДЕЦ  ПИЗДЕЦ
            # ????????????????????????????
            # clear_nop()
            # clear_op()
            # set_op(rez[1]["id"])
            # set_nop(rez[2]["id"])
            # ????????????????????????????
            # ПИЗДЕЦ  ПИЗДЕЦ  ПИЗДЕЦ
            # ????????????????????????????




        




# *******************************
# MORE THAN 2 EQUAL WEIGHT in CJ2
# *******************************
    if(i>2):
        print(rez[1])
        print(rez[1]['id'])
        print(rez[1]['s2'])
        # sel_op_id?????





        print(f's2 ID:{rez[1]["id"]} w:{rez[1]["s2"]} ======= S2 ID:{rez[2]["id"]} w:{rez[2]["s2"]} ====== S2 ID:{rez[3]["id"]} w:{rez[3]["s2"]} !*__')
        opIDnow = get_op()
        print(f's2 MORE THAN 2 EQUAL WEIGHT !!!!!!!!!!! ||||| opIDnow: {opIDnow}')
        # нужна проверка...




# ÷??????????÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷
# ÷??????????÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷
# ПИЗДЕЦ ?!
# ÷??????????÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷
        # ndict = {}
        # ndict = rez
        # ####### ndict.pop(opIDnow)
        # keys = list(ndict.keys())
    # создать словарь {'A': 65, 'B': 66, 'C': 67, … , 'Z': 90}
    #     asciiMap = {chr(_): _ for _ in range(65, 91)}
    # # значение для поиска
    #     val = 75
 
    # # печатает К
    #     print(next(ch for ch, code in asciiMap.items() if code == val))
    #     #### // Теперь первый ключ можно получить так keys[0]
    #     print(f'±±±±@!±! ||||| opIDnow: {val} ** {rez[1]} [[[||| {len(rez)}]]]')


        # values = rez.items()
        print(f'###*__+==')
        #print(values) # ['Murzik', 'Vaska', 'Barsik']
        for i in range(1,len(rez)+1):
            print(f'::::::: rez [ {i} ] = {rez[i]} ')
            # print(f'{ rez.get(opIDnow, "That key is not found")} ')
            # if():
            # print(f'{ rez[i].get("id", "That key is not found")} ')
            idzxxbbm = rez[i].get("id", "0")
            if(str(idzxxbbm)==str(opIDnow)):
                print(f'***********************************')
                # rez.pop(rez)
                try:
                    del rez[i]
                    print(f'*******DELETED is DONE! ****************************')
                except:
                    rez.pop(rez[i])
                    print(f'******* ЙЕБАНЕМ МНАЧЕ! ****************************')
            # if(rez[i].get("id", "That key is not found")==opIDnow):
            # print(f'_________________ {type(opIDnow)}')
            #     print(f'***********************************')
        print(f'###*__+==')

                # val = rez.get(2, "That key is not found")
        # print(f'{ rez[1].get("id", "That key is not found")} ')
        print(f'==== {rez} рез ====')
        print(f'==== {opIDnow} ШЫ ====')
        # if(rez[0]):
            # print(f' >>>>>>>>>>> ')

# ÷??????????÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷
# ÷??????????÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷


        # print(rez[1][id])


    if 'rez[1]' in locals():
        rez=rez[1]
        print('Variable s2 exist.')
    else:
        rez=0
        print('Variable s2 don\'t exist.')
        rez = {5:"66"}

    # rez = 5



    # ********************
    return rez
    #return jsonify({'get_min_w_j2': rez, 'count': i})


#####################################################################
##### get min j1 with double weigh
#####  -> 1:{id,weight}..n{id,weight}
@app.route('/get_min_w_j1', methods=['GET', 'POST'])
# def form_example():
def get_min_w_j1():
    ma = att.alias()
    rez = {}
    i=0
    subq = ma.select(fn.MIN(ma.j1))
    query = (att.select(att.id, att.j1).where(att.j1 == subq))
    for item in query.dicts().execute():
        i+=1
        rez[i]=item

    if 'rez[1]' in locals():
        rez=rez[1]
        print('Variable j1 exist.')
    else:
        rez=0
        print('Variable j1 don\'t exist.')
                
    return rez
    # return jsonify({'get_min_w_j1': rez})


@app.route('/get_min_w_j2', methods=['GET', 'POST'])

# ++ADD ++ADD ++ADD ++ADD ++ADD ++ADD ++ADD 
# ++ADD ++ADD ++ADD ++ADD ++ADD ++ADD ++ADD 
# ++ADD ++ADD ++ADD ++ADD ++ADD ++ADD ++ADD 
# ++ADD ++ADD ++ADD ++ADD ++ADD ++ADD ++ADD 
# ++ADD ++ADD ++ADD ++ADD ++ADD ++ADD ++ADD 
# ++ADD ++ADD ++ADD ++ADD ++ADD ++ADD ++ADD 
# добавить EXCLUDE op :ID
# и в путь ПИЗДЕЦ !!!
# ++ADD ++ADD ++ADD ++ADD ++ADD ++ADD ++ADD 
# ++ADD ++ADD ++ADD ++ADD ++ADD ++ADD ++ADD 

# def form_example():
def get_min_w_j2():
    ma = att.alias()
    rez = {}
    i=0
    subq = ma.select(fn.MIN(ma.j2))
    # query = (att.select(att.id, att.j2).where(att.j2 == subq,att.j2ig.is_null(0) ))
    # ????????????????????????????
    # ПИЗДЕЦ  ПИЗДЕЦ  ПИЗДЕЦ
    # ????????????????????????????
    query = (att.select(att.id, att.j2).where(att.j2 == subq,att.j2ig.is_null(1) ))
    # ????????????????????????????
    # ПИЗДЕЦ  ПИЗДЕЦ  ПИЗДЕЦ
    # ????????????????????????????
    for item in query.dicts().execute():
        i+=1
        rez[i]=item

# *******************************
# 2 EQUAL WEIGHT in CJ2
# *******************************
    if(i==2):
        print(rez[1])
        print(rez[1]['id'])
        print(rez[1]['j2'])
        print(f'J2 ID:{rez[1]["id"]} w:{rez[1]["j2"]} ======= J2 ID:{rez[2]["id"]} w:{rez[2]["j2"]} !!!')
        print(f'J2 TWO EQUAL WEIGHT !!!!!!!!!!!')

        j1w1 = get_w_j1_ex(rez[1]["id"])
        j1w2 = get_w_j1_ex(rez[2]["id"])
        # j1w3 = get_w_j1_ex(rez[3]["id"])
        print(f'±±±±±± => J1 W:{j1w1} & J2 W:{j1w2} ')
        if(j1w1<=j1w2):
            print(f'if(j1w1<=j1w2::::::: {j1w1} = ||||||||||||| {j1w2}')
            print(f'SET_OP: {rez[1]["id"]} && ||||||||||||| SET_NOP: {rez[2]["id"]}')

            # ????????????????????????????
            # ПИЗДЕЦ  ПИЗДЕЦ  ПИЗДЕЦ
            # ????????????????????????????
            # clear_nop()
            # clear_op()
            # set_op(rez[1]["id"])
            # set_nop(rez[2]["id"])
            # ????????????????????????????
            # ПИЗДЕЦ  ПИЗДЕЦ  ПИЗДЕЦ
            # ????????????????????????????




        




# *******************************
# MORE THAN 2 EQUAL WEIGHT in CJ2
# *******************************
    if(i>2):
        print(rez[1])
        print(rez[1]['id'])
        print(rez[1]['j2'])
        print(f'J2 ID:{rez[1]["id"]} w:{rez[1]["j2"]} ======= J2 ID:{rez[2]["id"]} w:{rez[2]["j2"]} !!!**')
        print(f'J2 MORE THAN 2 EQUAL WEIGHT !!!!!!!!!!!')



        # print(rez[1][id])


    if 'rez[1]' in locals():
        rez=rez[1]
        print('Variable j2 exist.')
    else:
        rez=0
        print('Variable j2 don\'t exist.')

    return rez
    #return jsonify({'get_min_w_j2': rez, 'count': i})



@app.route('/get_min_w_j3', methods=['GET', 'POST'])
# def form_example():
def get_min_w_j3():
    ma = att.alias()
    rez = {}
    i=0
    subq = ma.select(fn.MIN(ma.j3))
    query = (att.select(att.id, att.j3).where(att.j3 == subq))
    for item in query.dicts().execute():
        i+=1
        rez[i]=item

    if(i==2):
        print(rez[1])
        print(rez[1]['id'])
        print(rez[1]['j3'])
        print(f'J3 ID:{rez[1]["id"]} w:{rez[1]["j3"]} ======= J3 ID:{rez[2]["id"]} w:{rez[2]["j3"]} !!!')
        print(f'J3 TWO EQUAL WEIGHT !!!!!!!!!!!')


    if(i>2):
        print(rez[1])
        print(rez[1]['id'])
        print(rez[1]['j3'])
        print(f'J3 ID:{rez[1]["id"]} w:{rez[1]["j3"]} ======= J3 ID:{rez[2]["id"]} w:{rez[2]["j3"]} !!!')
        print(f'J3 MORE THAN 2 EQUAL WEIGHT !!!!!!!!!!!')



        # print(rez[1][id])

    if 'rez[1]' in locals():
        rez=rez[1]
        print('Variable j3 exist.')
    else:
        rez=0
        print('Variable j3 don\'t exist.')
    return rez
    #return jsonify({'get_min_w_j2': rez, 'count': i})



#####################################################################
##### get id with min weight in s1 w/o doubles (op id s1)
#####  -> id, one id with min weight in s1
def get_id_min_w_s1(exclude_id=0):
    # try:
    #     print(x)
    # except:
    #     print("An exception occurred")
    #     exclude_id=0
    if exclude_id is None:
        exclude_id=-1
        ma = att.alias()
        rez = {}
        i=0
        subq = ma.select(fn.MIN(ma.s1)).where(ma.s1ig.is_null(True))
        query = (att.select(att.id, att.s1).where(
            (att.s1 == subq) &
            (att.s1ig.is_null(True)))
        )
        for item in query.dicts().execute():
            #print(item)
            i+=1
            rez[i]=item
        min_w_dict = {}
        for key in rez:
            min_w_dict[rez[key]['id']]=rez[key]['s1']
        s1min_id_w = min(min_w_dict, key=min_w_dict.get,default=0)        








    if exclude_id>0:
        print('*** EXCLUDE s1 OP ID: [ ', exclude_id, ' ]')
        ma = att.alias()
        rez = {}
        i=0
        subq = ma.select(fn.MIN(ma.s1)).where(ma.s1ig.is_null(True) &
        (ma.id!=exclude_id)
        )
        query = (att.select(att.id, att.s1).where(
            (att.s1 == subq) &
            (att.id!=exclude_id) &
            (att.s1ig.is_null(True)))
        )
        for item in query.dicts().execute():
            print(item,'******---*******%#####')
            i+=1
            rez[i]=item
        min_w_dict = {}
        for key in rez:
            min_w_dict[rez[key]['id']]=rez[key]['s1']
        s1min_id_w = min(min_w_dict, key=min_w_dict.get,default=0)
        return s1min_id_w
# INCLUDE al ID
    else:
        ma = att.alias()
        rez = {}
        i=0
        subq = ma.select(fn.MIN(ma.s1)).where(ma.s1ig.is_null(True))
        query = (att.select(att.id, att.s1).where(
            (att.s1 == subq) &
            (att.s1ig.is_null(True)))
        )
        for item in query.dicts().execute():
            #print(item)
            i+=1
            rez[i]=item
        min_w_dict = {}
        for key in rez:
            min_w_dict[rez[key]['id']]=rez[key]['s1']
        s1min_id_w = min(min_w_dict, key=min_w_dict.get,default=0)
        return s1min_id_w
    



#####################################################################
##### get id with min weight in j1 w/o doubles (op id j1)
#####  -> id, one id with min weight in j1
def get_id_min_w_j1(exclude_id=0):
#    if exclude_id is None:
#        exclude_id=-1    
    if exclude_id>0:
        print('*** EXCLUDE j1 OP ID: [ ', exclude_id, ' ]')
        ma = att.alias()
        rez = {}
        i=0
        subq = ma.select(fn.MIN(ma.j1)).where(ma.j1ig.is_null(True) &
        (ma.id!=exclude_id)
        )
        query = (att.select(att.id, att.j1).where(
            (att.j1 == subq) &
            (att.id!=exclude_id) &
            (att.j1ig.is_null(True)))
        )
        for item in query.dicts().execute():
            print(item,'*****_________')
            i+=1
            rez[i]=item
        min_w_dict = {}
        for key in rez:
            min_w_dict[rez[key]['id']]=rez[key]['j1']
        j1min_id_w = min(min_w_dict, key=min_w_dict.get,default=0)
        return j1min_id_w
# INCLUDE al ID
    else:
        ma = att.alias()
        rez = {}
        i=0
        subq = ma.select(fn.MIN(ma.j1)).where(ma.j1ig.is_null(True))
        query = (att.select(att.id, att.j1).where(
            (att.j1 == subq) &
            (att.j1ig.is_null(True)))
        )
        for item in query.dicts().execute():
            #print(item)
            i+=1
            rez[i]=item
        min_w_dict = {}
        for key in rez:
            min_w_dict[rez[key]['id']]=rez[key]['j1']
        j1min_id_w = min(min_w_dict, key=min_w_dict.get,default=0)
        return j1min_id_w


### NEW ПИЗДЕЦ ОК! ДОБРО!
def get_w_j1_by_id(idz=0):
    rez = {}
    i=0
    query = (att.select(att.j1,att.id).where(
        (att.id==idz) &
        (att.j1ch2.is_null(1) & att.j1ch1.is_null(1))
        ))
    query = (att.select(att.j1ch1,att.id).where(
        (att.id==idz) &
        (att.j1ch2.is_null(1) & att.j1ch1.is_null(0))
        ))
    query = (att.select(att.j1ch2,att.id).where(
        (att.id==idz) &
        (att.j1ch2.is_null(0) & att.j1ch1.is_null(0))
        ))            
    # -1 <= -1
    for item in query.dicts().execute():
        print(item,'±±!!±±!!!!±±±±±±')
        i+=1
        rez[i]=item
        print(f' ИДИ СЮДА ХУЙЛО!!!!!1111111  -Ж-  {rez[i]}')
        print(f' ЗАЛУПКА :: =Ж= : {rez[i]},  И: [ {i} ]')
        # keys =list(rez.keys())
        print(f' ID # ЗАЛУПКА :: ==Ж== : {rez[i]},  И: [ {i} ]')
        # =====
     


        min_w_dict = {}
        for key in rez:
            min_w_dict[rez[key]['j1ch2']]=rez[key]['j1ch2']
            print(f' ИДИ СЮДА ХУЙЛО!!!!!  Ж  {rez[key]["id"]}')
        j1min_id_w = min(min_w_dict, key=min_w_dict.get,default=0)
        print(f'>>>>>>>>>>>>>>>>>> {rez[1]}')
        # j1min_id_w = 99
        return j1min_id_w    
    keys =list(rez.keys())
    print(f' ХУЙ===#####: { keys } [] = key0: {keys[0]}, key1: {keys[1]}')        
    # ???????????
    j1min_id_w =111
    return j1min_id_w
### NEW ПИЗДЕЦ ОК! ДОБРО!



#####################################################################
##### get id with min weight in j1 w/o doubles (op id j1)
#####  -> id, one id with min weight in j1
def get_min_w_j1_all(idz=0):
#    if exclude_id is None:
#        exclude_id=-1    
    exclude_id=0    
    print('j1 ALL: [ get_min_w_j1_all() ]')
    ma = att.alias()
    rez = {}
    i=0
    # subq = ma.select(fn.MIN(ma.j1)).where(ma.j1ig.is_null(False) &
    # (ma.id!=exclude_id)
    # )
    query = (att.select(att.id, att.j1).where(
        (att.id!=exclude_id) &
        (att.id==idz)
        # (att.j1ig.is_null(True))
        )
    )
    for item in query.dicts().execute():
        print(item,'*****_________')
        i+=1
        rez[i]=item
        min_w_dict = {}
        for key in rez:
            min_w_dict[rez[key]['id']]=rez[key]['j1']
        j1min_id_w = min(min_w_dict, key=min_w_dict.get,default=0)
        print(f' zZz == {j1min_id_w}; ')
        set_op(j1min_id_w)
        return j1min_id_w
# # INCLUDE al ID
#     else:
#         ma = att.alias()
#         rez = {}
#         i=0
#         subq = ma.select(fn.MIN(ma.j1)).where(ma.j1ig.is_null(True))
#         query = (att.select(att.id, att.j1).where(
#             (att.j1 == subq) &
#             (att.j1ig.is_null(True)))
#         )

        # for item in query.dicts().execute():
        #     #print(item)
        #     i+=1
        #     rez[i]=item
        # min_w_dict = {}
        # for key in rez:
        #     min_w_dict[rez[key]['id']]=rez[key]['j1']
        # j1min_id_w = min(min_w_dict, key=min_w_dict.get,default=0)
        # return j1min_id_w



#####################################################################
##### get id with min weight in s2  w/o doubles (op id s2)
#####  -> id, one id with min weight in s2
def get_id_min_w_s2(exclude_id=0):
    if exclude_id is None:
        exclude_id=99
        ma = att.alias()
        rez = {}
        i=0
        subq = ma.select(fn.MIN(ma.s2)).where(ma.s2ig.is_null(True))
        query = (att.select(att.id, att.s2).where(
            (att.s2ig.is_null(True)) &
            (att.s2 == subq))
            )
        for item in query.dicts().execute():
            i+=1
            rez[i]=item
    #print('===',rez)
        min_w_dict = {}
        s2_dict = {}
        for key in rez:
            min_w_dict[rez[key]['id']]=rez[key]['s2']
            s2_dict[rez[key]['id']]=get_w_s1(rez[key]['id'])
    #print(f"mdic: {min_w_dict}, s2dic: {s2_dict}")
        if(min_w_dict==s2_dict):
        #print('EQ_s2')
        #rez = min(min_w_dict.keys())
        #print(min_w_dict)
            rez = min(min_w_dict.keys(),default=0)
        else:
        #print('NOT EQ')
            min_val = min(s2_dict.values(),default=0)
        #print(min_val)
        #print(s2_dict)
            z = {key:value for key, value in s2_dict.items() if value == min_val}
            rez = min(z.keys(),default=0)
        #print(rez)
    #print('s2',min_w_dict)
    #print('s1',s1_dict)




#        exclude_id=-1    
    if exclude_id>0:    
        print('*** EXCLUDE s2 OP ID: [ ', exclude_id, ' ]')
        ma = att.alias()
        rez = {}
        i=0
        subq = ma.select(fn.MIN(ma.s2)).where(ma.s2ig.is_null(True)&(ma.id!=exclude_id))
        query = (att.select(att.id, att.s2).where(
            (att.s2ig.is_null(True)) &
            (att.id!=exclude_id) &
            (att.s2 == subq))
            )
        for item in query.dicts().execute():
            i+=1
            rez[i]=item
    #print('===',rez)
        min_w_dict = {}
        s2_dict = {}
        for key in rez:
            min_w_dict[rez[key]['id']]=rez[key]['s2']
            s2_dict[rez[key]['id']]=get_w_s1(rez[key]['id'])
    #print(f"mdic: {min_w_dict}, s2dic: {s2_dict}")
        if(min_w_dict==s2_dict):
            print(f'EQ_s2 ================================= REZ: {rez} | len(REZ): {len(rez)}')
        #rez = min(min_w_dict.keys())
            # print(min_w_dict)
            
            
            #  ?????????????????????????????????????
            #  ?????????????????????????????????????
            #  ?????????????????????????????????????
            #  ?????????????????????????????????????
            #  ?????????????????????????????????????
            rez = min(min_w_dict.keys(),default=0)
            #  ?????????????????????????????????????
            #  ?????????????????????????????????????
            #  ?????????????????????????????????????
            #  ?????????????????????????????????????
            #  ?????????????????????????????????????
            
            print(f'===== REZ: {rez}')
            print(f'===== mwd: {min_w_dict}')
            print(f'===== ms2: {s2_dict}')

            # print(f'len: : {len(get_w_s1)}')

            if(rez==1):
                id_s1_z = list(s2_dict)
                print(f'========1 : {len(s2_dict)}')
                # print(f'=ЛУН_XXX= : { id_s1_z[0]} & { id_s1_z[1]}')
                # print(f'=ЛУН_XXX= : { get_w_s1_ex(id_s1_z[0])} =+++= { get_w_s1_ex(id_s1_z[1])}')

            if(rez==2):
                print(f'========2 : {len(s2_dict)}')
                # print(f'=1 : {s2_dict[1]}')
                # print(f'=2 : {s2_dict[2]}')
                id_s1_ = s2_dict.keys()
                id_s1_z = list(s2_dict)
                # print(f'=ЛУН= : { id_s1_}')
                # print(f'=ЛУН= : { id_s1_z}')
                if(len(id_s1_z)==2):
                    print(f'=LEN= : { len(id_s1_z)}')
                    print(f'=ЛУНZZZ= : { id_s1_z[0]} & { id_s1_z[1]}')
                    print(f'=ЛУНZZZ= : { get_w_s1_ex(id_s1_z[0])} =+++= { get_w_s1_ex(id_s1_z[1])}')
                # if во втором рывке, попались ДВА одинаковых веса,
                # смотрим на из веса в ПЕРВОМ рывке и сравниваем!
                    if(get_w_s1_ex(id_s1_z[0]) > get_w_s1_ex(id_s1_z[1])):
                        print(f's1[0] > s1[1] ')
                        rez = id_s1_z[1]
                    if(get_w_s1_ex(id_s1_z[0]) < get_w_s1_ex(id_s1_z[1])):
                        print(f's1[0] < s1[1] ')
                        rez = id_s1_z[0]
                    if(get_w_s1_ex(id_s1_z[0]) == get_w_s1_ex(id_s1_z[1])):
                        print(f's1[0] == s1[1] ')
                        rez = id_s1_z[0] # ?????????

# #81 issue - parted is DONE ! DONE ! DONE ! ()
# ******* ГОТОВО! ГОТОВО! ГОТОВО! ГОТОВО! ГОТОВО! ГОТОВО! ГОТОВО! //
            if(rez==4):
                id_s1_z = list(s2_dict)
                print(f'========4 : {len(s2_dict)}')
                print(f'======== ()()()() : {id_s1_z}')
                print(f'=ЛУН_ 4444= : { id_s1_z[0]} & { id_s1_z[0]}')
                if(len(id_s1_z)==1):
                    print(f'ZA-ZA-ZA ::: [ 1 ] ||| OP ID ::: -= {id_s1_z[0]} =- ')
                    rez = id_s1_z[0]
                    # set_op_now(id_s1_z[0])
                    print(f'-5 LAST get_id_min_w_s2 === rez :::  {rez}')
                    # set_nop_now(4)



                    
                    

                    
                # print(f'=ЛУН_ 4444= : { get_w_s1_ex(id_s1_z[0])} =+++= { get_w_s1_ex(id_s1_z[1])}')



                

                # print(f'')
                
            # **********
            # **********
            # **********
            # ВО ТУТОЧКИ ПИЗДЕЦ КАК ГОВОРИТЬСЯ!
            # ПРОСТО - добавить проверку на == s1 и выбрать!
            # ЗАЕБОК! заебок! Заебок! ЗАЕБОК! заебок! Заебок! 





# # ЗАЕБОК! заебок! Заебок! ЗАЕБОК! заебок! Заебок! 
# # ЗАЕБОК! заебок! Заебок! ЗАЕБОК! заебок! Заебок! 
# # ЗАЕБОК! заебок! Заебок! ЗАЕБОК! заебок! Заебок!             






        else:
            print('NOT EQ +_+_+_+_+_+_+__')
            min_val = min(s2_dict.values(),default=0)
        #print(min_val)
        #print(s2_dict)
            z = {key:value for key, value in s2_dict.items() if value == min_val}
            rez = min(z.keys(),default=0)
        #print(rez)
    #print('s2',min_w_dict)
    #print('s1',s1_dict)
        # rez = 4
        print(f'-4 LAST get_id_min_w_s2 === rez :::  {rez}')
        print(f'====4   min_w_dict2  :::  {min_w_dict}')





        # rez = 4
        # set_nop_now(4)

        # rez = 4
        # set_op_now(4)
        return rez
    else:
        print('*** EXCLUDE s2 OP ID ????? : [ ', exclude_id, ' ]')    
        ma = att.alias()
        rez = {}
        i=0
        subq = ma.select(fn.MIN(ma.s2)).where(ma.s2ig.is_null(True))
        query = (att.select(att.id, att.s2).where(
            (att.s2ig.is_null(True)) &
            (att.s2 == subq))
            )
        for item in query.dicts().execute():
            i+=1
            rez[i]=item
    #print('===',rez)
        min_w_dict = {}
        s2_dict = {}
        s1_dict = {}
        for key in rez:
            min_w_dict[rez[key]['id']]=rez[key]['s2']
            s2_dict[rez[key]['id']]=get_w_s2_ex(rez[key]['id'])
            s1_dict[rez[key]['id']]=get_w_s1_ex(rez[key]['id'])
    #print(f"mdic: {min_w_dict}, s2dic: {s2_dict}")
        if(min_w_dict==s2_dict):
            print('EQ_ s2 ????*****')

            print(f'EQ_s2 *** ================================= REZ---: {rez} | len(REZ): {len(rez)}')        
            
            
            rez = min(s2_dict.keys(),default=0)
            # rez = 

# //////////////////////////////////////////////////////
# //////////////////////////////////////////////////////
# if(min_w_dict==s2_dict): /////////////////////////////
            
            

# //////////////////////////////////////////////////////
# //////////////////////////////////////////////////////
        


            
        else:
            print('NOT EQ-=-=-=-=-=-')
            min_val = min(s2_dict.values(),default=0)
            z = {key:value for key, value in s2_dict.items() if value == min_val}
            rez = min(z.keys(),default=0)
#            rez = max(z.keys(),default=0)
            print(f'-1 LAST get_id_min_w_s2 === rez :::  {rez}')

        







        print(f'!!! LAST get_id_min_w_s2 === rez :::  {rez}')

        id_s1_ = s2_dict.keys()
        
        min_val = min(s2_dict.values(),default=0)
        z = {key:value for key, value in s2_dict.items() if value == min_val}
        rez = min(z.keys(),default=0)

        id_s1_z = list(s2_dict)
                # print(f'=ЛУН= : { id_s1_}')
                # print(f'=ЛУН= : { id_s1_z}')
        if(len(id_s1_z)==2):
            print(f'=LEN= : { len(id_s1_z)}')
            print(f'=ЛУНZZZ= : { id_s1_z[0]} & { id_s1_z[1]}')
            print(f'=ЛУНZZZ= : { get_w_s1_ex(id_s1_z[0])} =+++= { get_w_s1_ex(id_s1_z[1])}')
                # if во втором рывке, попались ДВА одинаковых веса,
                # смотрим на из веса в ПЕРВОМ рывке и сравниваем!
            if(get_w_s1_ex(id_s1_z[0]) > get_w_s1_ex(id_s1_z[1])):
                print(f's1[0] > s1[1] ')
                rez = id_s1_z[1]
            if(get_w_s1_ex(id_s1_z[0]) < get_w_s1_ex(id_s1_z[1])):
                print(f's1[0] < s1[1] ')
                rez = id_s1_z[0]
            if(get_w_s1_ex(id_s1_z[0]) == get_w_s1_ex(id_s1_z[1])):
                print(f's1[0] == s1[1] ')
                rez = id_s1_z[0] # ?????????


        print(f'_+++++++ {s2_dict}  :::: s2_dict:  {s2_dict}')
        print(f'_+++++++ {s1_dict}  :::: s1_dict:  {s1_dict}')

        # ТУТ ЧЕКАЕМ НА ДУБЛЬ
        # И ВЫБИРАЕМ ПО р1 (1.min весе snatch1, 1.по мандатке )
        try:
            azzxd0 = list(s1_dict.keys())[0]
            azzxd1 = list(s1_dict.keys())[1]
            azzxd0w = list(s1_dict.values())[0]
            azzxd1w = list(s1_dict.values())[1]            
        except:
            azzxd0 = 1
            azzxd1 = 2        
        if(len(s2_dict)==2):
            if( azzxd1w < azzxd0w ):
                print(f's1_dict[4]<s2_dict[4] !!  :::{azzxd1}:{azzxd1w} <  {azzxd0}:{azzxd0w} |=  ')
                print(f's1_dict[4]<VRADJENDRA PR KI JAY!!!!  !!  ::: {azzxd0} <  {azzxd1} ')
                rez = azzxd1
            if( azzxd1w > azzxd0w ):
                print(f's1_dict[4]<s2_dict[4] !!  :::{azzxd1}:{azzxd1w} <  {azzxd0}:{azzxd0w} |=  ')
                print(f's1_dict[4]<VRADJENDRA PR KI JAY!!!!  !!  ::: {azzxd0} <  {azzxd1} ')
                rez = azzxd0
            if( azzxd1w == azzxd0w ):
                print(f's1_dict[4]<s2_dict[4] !!  :::{azzxd1}:{azzxd1w} <  {azzxd0}:{azzxd0w} |=  ')
                print(f's1_dict[4]<VRADJENDRA PR KI JAY!!!!  !!  ::: {azzxd0} <  {azzxd1} ')
                rez = azzxd0                                
            # print(f'******___ len(s2_dict)==2  ::: {len(s2_dict)}')
            print(f'SNATCH 2 == 2 DOUBLE WEIGHT !!!  ::: {len(s2_dict)}')



        if(len(s2_dict)==3):
            if( azzxd1w < azzxd0w ):
                print(f's1_dict[4]<s2_dict[4] !!  :::{azzxd1}:{azzxd1w} <  {azzxd0}:{azzxd0w} |=  ')
                print(f's1_dict[4]<VRADJENDRA PR KI JAY!!!!  !!  ::: {azzxd0} <  {azzxd1} ')
                rez = azzxd1
            if( azzxd1w > azzxd0w ):
                print(f's1_dict[4]<s2_dict[4] !!  :::{azzxd1}:{azzxd1w} <  {azzxd0}:{azzxd0w} |=  ')
                print(f's1_dict[4]<VRADJENDRA PR KI JAY!!!!  !!  ::: {azzxd0} <  {azzxd1} ')
                rez = azzxd0
            if( azzxd1w == azzxd0w ):
                print(f's1_dict[4]<s2_dict[4] !!  :::{azzxd1}:{azzxd1w} <  {azzxd0}:{azzxd0w} |=  ')
                print(f's1_dict[4]<VRADJENDRA PR KI JAY!!!!  !!  ::: {azzxd0} <  {azzxd1} ')
                rez = azzxd0                                
            # print(f'******___ len(s2_dict)==2  ::: {len(s2_dict)}')
            print(f'SNATCH 2 == 3 DOUBLE WEIGHT !!!  ::: {len(s2_dict)}')            

            # rez = 4

        



        return rez







#####################################################################
##### get id with min weight in j2  w/o doubles (op id j2)
#####  -> id, one id with min weight in j2
def get_id_min_w_j2(exclude_id=0):
#    if exclude_id is None:
#        exclude_id=-1    
    if exclude_id>0:    
        print('*** EXCLUDE j2 OP ID: [ ', exclude_id, ' ]')
        ma = att.alias()
        rez = {}
        i=0
        subq = ma.select(fn.MIN(ma.j2)).where(ma.j2ig.is_null(True)&(ma.id!=exclude_id))
        query = (att.select(att.id, att.j2).where(
            (att.j2ig.is_null(True)) &
            (att.id!=exclude_id) &
            (att.j2 == subq))
            )
        for item in query.dicts().execute():
            i+=1
            rez[i]=item
    #print('===',rez)
        min_w_dict = {}
        j2_dict = {}
        for key in rez:
            min_w_dict[rez[key]['id']]=rez[key]['j2']
            j2_dict[rez[key]['id']]=get_w_s1(rez[key]['id'])
        print(f"mdic: {min_w_dict}, s2dic: {j2_dict}")
        if(min_w_dict==j2_dict):
            print('EQ_s2()()()()()()')
        #rez = min(min_w_dict.keys())
        #print(min_w_dict)
            rez = min(min_w_dict.keys(),default=0)
        else:
            print('NOT EQ')
            min_val = min(j2_dict.values(),default=0)
        #print(min_val)
        #print(j2_dict)
            z = {key:value for key, value in j2_dict.items() if value == min_val}
            rez = min(z.keys(),default=0)
        #print(rez)
    #print('s2',min_w_dict)
    #print('s1',s1_dict)
        return rez
    else:
        ma = att.alias()
        rez = {}
        i=0
        subq = ma.select(fn.MIN(ma.j2)).where(ma.j2ig.is_null(True))
        query = (att.select(att.id, att.j2).where(
            (att.j2ig.is_null(True)) &
            (att.j2 == subq))
            )
        for item in query.dicts().execute():
            i+=1
            rez[i]=item
    #print('===',rez)
        min_w_dict = {}
        j2_dict = {}
        for key in rez:
            min_w_dict[rez[key]['id']]=rez[key]['j2']
            j2_dict[rez[key]['id']]=get_w_j1(rez[key]['id'])
    #print(f"mdic: {min_w_dict}, s2dic: {s2_dict}")
        if(min_w_dict==j2_dict):
        #print('EQ_s2')
        #rez = min(min_w_dict.keys())
        #print(min_w_dict)
            rez = min(min_w_dict.keys(),default=0)
        else:
        #print('NOT EQ')
            min_val = min(j2_dict.values(),default=0)
        #print(min_val)
        #print(s2_dict)
            z = {key:value for key, value in j2_dict.items() if value == min_val}
            rez = min(z.keys(),default=0)
        #print(rez)
    #print('s2',min_w_dict)
    #print('s1',s1_dict)
        return rez



#####################################################################
##### get id with min weight in s3  w/o doubles (op id s3)
#####  -> id, one id with min weight in s3
def get_id_min_w_s3(exclude_id=0):
#    if exclude_id is None:
#        exclude_id=-1    
    if exclude_id is None:
        exclude_id=9999


    if exclude_id>0:
        print('*** EXCLUDE s3 OP ID: [ ', exclude_id, ' ]')
        ma = att.alias()
        rez = {}
        # exclude_id = 7
        s3d,s2d,s1d = {},{},{}
        i=0
        # ?????????????????????????
        # ?????????????????????????
        # ?????????????????????????
        # subq = ma.select(fn.MIN(ma.s3)).where((ma.id!=exclude_id) & ma.s3ig.is_null(True))
        # subq2_s3 = att.select(ma.s3).where(att.id!=exclude_id) & ma.s3ig.is_null(True)
                # subq = ma.select(fn.MIN(ma.s3)).where((ma.id!=exclude_id) & ma.s3ig.is_null(True))
        subq2_s3 = att.select((att.s3)).where((att.id!=exclude_id ) 
                                                & att.s3ig.is_null(True) 
                                                & att.s2ig.is_null(False)
                                                & att.s1ig.is_null(False)
                                                )

#         SELECT op,nextop,id, firstname, snatch1,snatch1isget,snatch2,snatch2isget,snatch3,snatch3isget FROM `v7now` 
                    # WHERE snatch1isget IS NOT NULL
                        # AND snatch2isget IS NOT NULL
                            # AND snatch3isget IS NULL !!!!!!!
                                # AND id!=4;


        subq = ma.select(fn.MIN(ma.s3)).where((ma.id!=exclude_id) & ma.s3ig.is_null(True))
        # ?????????????????????????
        # ?????????????????????????
        # ?????????????????????????
        
        query = (att.select(att.id, att.s3).where(
            (att.s3ig.is_null(True)) &
            (att.s2ig.is_null(False)) &
            (att.s1ig.is_null(False)) &
            (att.id != exclude_id) &
            (att.s3 == subq)))
        for item in query.dicts().execute():
            rez[i]=item
            i+=1
        print(f"rezNOW >1 @@: {rez} len: {len(rez)}")

        
        
        iz=0
        for itemz in subq2_s3.dicts().execute():
            # rez[i]=itemz
            print(f'ZALUPA !!!!! ZALUPA !!! ZALUPA !!! {iz} :: {itemz}')
            iz+=1
            # ****************** ПИЗДЕЦ !!!






        print(f"rezNOW >1 @@: {rez} len: {len(rez)}")
        # print(f" ####@@: {list(list(rez.values())[0].values())[0]} @ len: {len(rez)}")





    # if 1 min weight in s3:
        if not rez:
            print("------==")
            rez = 0
        if (isinstance(rez, dict)):
            if len(rez)==1:
                rez = rez[0]['id']
                print(f"11111  @ !!!!!!!!!!!!!! ±±± REZZZŽ {rez}")
                # clear_op()
                # set_op(5)

                # WOW нахуй ПИЗДЕЦ! ) 
                # сработало
                if((get_w_s2_ex(rez)) == (get_w_s3_ex(rez)) ):
                    print(f'....... ::: get_w_s2_ex(rez) :::: {rez} = {get_w_s2_ex(rez)}')
                    # clear_op()
                    # set_op()

# ТУТА ПРОВЕРКА НАДА!!!! ТУТА ПРОВЕРКА НАДА!!!!
                
#  ПИЗДЕЙ ПОЛНЫЙ !!!
#  ПИЗДЕЙ ПОЛНЫЙ !!!
# ПОКА МЮТИМ ЭТО К ХУЙАМ! ПОТОМ ПЕРЕПРОВЕРИМ КАК ТО ТАМ ЙОКАРАНЫЙ....
# ПОКА МЮТИМ ЭТО К ХУЙАМ! ПОТОМ ПЕРЕПРОВЕРИМ КАК ТО ТАМ ЙОКАРАНЫЙ....
# ПОКА МЮТИМ ЭТО К ХУЙАМ! ПОТОМ ПЕРЕПРОВЕРИМ КАК ТО ТАМ ЙОКАРАНЫЙ....
                clear_op()
                set_op(rez)
# ПОКА МЮТИМ ЭТО К ХУЙАМ! ПОТОМ ПЕРЕПРОВЕРИМ КАК ТО ТАМ ЙОКАРАНЫЙ....
# ПОКА МЮТИМ ЭТО К ХУЙАМ! ПОТОМ ПЕРЕПРОВЕРИМ КАК ТО ТАМ ЙОКАРАНЫЙ....
# ПОКА МЮТИМ ЭТО К ХУЙАМ! ПОТОМ ПЕРЕПРОВЕРИМ КАК ТО ТАМ ЙОКАРАНЫЙ....
                # set_nop(5)

                # тут можно новый еще функций!
                # set_nop(ex=id)
#set_nop_ex_this_id(rez)
                # NOT WORKET IN THIS PLACE!!!!
                # NOT WORKET IN THIS PLACE!!!!
                # NOT WORKET IN THIS PLACE!!!!
                # NOT WORKET IN THIS PLACE!!!!

                # get_w_s3_ex(4)
                # set_nop(1)

                # for key in rez:
                #     s3d[rez[key]['id']] = rez[key]['s3']
                #     s2d[rez[key]['id']] = get_w_s2_ex(rez[key]['id'])
                #     s1d[rez[key]['id']] = get_w_s1_ex(rez[key]['id'])
                # rez = rez[0]['id']
                # print(f" s3: {s3d}, s2: {s2d}, s1: {s1d} ")
                # ndict = {}
                # for i in s3d:
                #     print(i,'%%%****___')
                #     if s1d[i] <= s2d[i] <= s3d[i]:
                #         ndict[i]=s1d[i]

                        
                
                # WOW нахуй ПИЗДЕЦ! ) 
                # сработало
                print(rez)
                return rez
                # sel_op_id(rez)
            # sel_op_id
            # set_op(rez)
            # print(rez, "SET OP")
            # exit(1)
            #
    # if more than 1 min weight in s3:
    #print(f"LEN: {rez}, {len(rez)}, {type(rez)}")
        if (isinstance(rez, dict)):
            if len(rez)>=2:
                print(":::(0) >2222222")
                for key in rez:
                    s3d[rez[key]['id']] = rez[key]['s3']
                    s2d[rez[key]['id']] = get_w_s2_ex(rez[key]['id'])
                    s1d[rez[key]['id']] = get_w_s1_ex(rez[key]['id'])
                rez = rez[0]['id']
                print(f" s3: {s3d}, s2: {s2d}, s1: {s1d} ")
                ndict = {}
                for i in s3d:
                    print(i,'%%%****___')
                    if s1d[i] <= s2d[i] <= s3d[i]:
                        ndict[i]=s1d[i]
                print(ndict,'****')
                rez = min(ndict, key = lambda k: ndict[k],default=0)
                print(rez,'@@@****::==::--')


            # if rez==0:
            #     rez = min(s3d)
            # if rez==1:
            #     print(f'!!!!!!!!!!!!!!!!!! if rez==1: ')
            #     # ??????????????????????
            #     rez = max(s3d)                    
            
        #rez = 0
        return rez
    else:
        print(f'KUURWA!!! j3 EXEPT ID is ::: _ 0 _ : {faker.first_name()}')
        # погодь погодь ПИЗДЕЦ!!!!
        # get_id_min_w_s3 ПРОВЕРКУ НА ДУБЛИ!!! НАДО ТУТ!!!

        ma = att.alias()
        rez = {}
        s3d,s2d,s1d = {},{},{}
        i=0
        # subq = ma.select(fn.MIN(ma.s3)).where(ma.s3ig.is_null(True))

        query = (att.select(att.id, att.s3).where(
            (att.s3ig.is_null(True)) &
            (att.s2ig.is_null(False)) &
            (att.s1ig.is_null(False))
            # (att.id != exclude_id) &
            # (att.s3 == subq))
            ))        
        for item in query.dicts().execute():
            rez[i]=item
            i+=1
        # print(f"rezNOW ##################### !! : {rez} len: {len(rez)}")
        # print(f"rezNOW ##################### !@@@! : {rez[0]['id']}")
        # rez = rez[0]['id']
        try:
            rez = rez[0]['id']
            print(f"rezNOW <1 !! : {rez} len: {len(rez)}")
            print(f"rezNOW <1 !@@@! : {rez[0]['id']}")            
        except:
            # rez = 0
            print(f"r&*&*&*&*&*&*&##### !! : {rez}")
            print("@@@ An exception occurred")
            #  И С П Р А В Л Е Н О !!!!!!!!!!!!!!!!!
            # ПИЗДЕЦ! ПРИЕХАЛИ! error errorzzz - DONE!!!
            #  И С П Р А В Л Е Н О !!!!!!!!!!!!!!!!!

            # *****************
            # йа йебу и плачу :)
            # need2FIX 
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # if 1 min weight in s3:
        if not rez:
            print("------==")
            rez = 0
        # if len(rez)!=1:
        #     print("======= 1")
        #     print("======= 1 REZ:::::::" + rez )
        #     rez = rez[0]['id']         
        if (isinstance(rez, dict)):
            if len(rez)==1:
                print("11111")
                rez = rez[0]['id']
            # sel_op_id
            # set_op(rez)
            # print(rez, "SET OP")
            # exit(1)
            #
    # if more than 1 min weight in s3:
    #print(f"LEN: {rez}, {len(rez)}, {type(rez)}")
        if (isinstance(rez, dict)):
            if len(rez)>=2:
                print(":::(1) >2222222")
                for key in rez:
                    s3d[rez[key]['id']] = rez[key]['s3']
                    s2d[rez[key]['id']] = get_w_s2(rez[key]['id'])
                    s1d[rez[key]['id']] = get_w_s1(rez[key]['id'])
                # rez = rez[0]['id']
                print(f" s3: {s3d}, s2: {s2d}, s1: {s1d} ")
                ndict = {}
                for i in s3d:
                    print(i,'%%%**** $$$ ')
                    if s1d[i] <= s2d[i] <= s3d[i]:
                        ndict[i]=s1d[i]
                print(ndict,'****')
                rez = min(ndict, key = lambda k: ndict[k],default=0)
                print(rez,'@@@****__::__')
                if rez==0:
                    rez = min(s3d)
            
        #rez = 0
        # print(f"rezNOW <1 !! : {rez} len: {len(rez)}")
        # print(f"rezNOW <1 !@@@! : {rez[0]['id']}")
        # rezx = rez[0]['id']
        return rez




#####################################################################
##### get id with min weight in j3  w/o doubles (op id j3)
#####  -> id, one id with min weight in j3
def get_id_min_w_j3(exclude_id=0):
#    if exclude_id is None:
#        exclude_id=-1    
    if exclude_id>0:
        print('*** EXCLUDE j3 OP ID: [ ', exclude_id, ' ]')
        ma = att.alias()
        rez = {}
        j3d,j2d,j1d = {},{},{}
        i=0
        subq = ma.select(fn.MIN(ma.j3)).where((ma.id!=exclude_id) & ma.j3ig.is_null(True))
        query = (att.select(att.id, att.j3).where(
            (att.j3ig.is_null(True)) &
            (att.id != exclude_id) &
            (att.j3 == subq)))
        for item in query.dicts().execute():
            rez[i]=item
            i+=1
        print(f"rezNOW: >1>1>1 {rez} len: {len(rez)}")
    # if 1 min weight in s3:
        if not rez:
            print("------==")
            rez = 0
        if (isinstance(rez, dict)):
            if len(rez)==1:
                print("11111 ONLY ONE!")
                clear_nop()
                clear_op()
                rez = rez[0]['id']
                print(f"11111 ONLY ONE! {rez} ::: setOP ID: [ {rez} ]")
                set_op(rez)
                
            # sel_op_id
            # set_op(rez)
            # print(rez, "SET OP")
            # exit(1)
            #
    # if more than 1 min weight in s3:
    #print(f"LEN: {rez}, {len(rez)}, {type(rez)}")
        if (isinstance(rez, dict)):
            if len(rez)>=2:
                print(":::(2) >2222222")
                for key in rez:
                    j3d[rez[key]['id']] = rez[key]['j3']
                    j2d[rez[key]['id']] = get_w_j2_ex(rez[key]['id'])
                    j1d[rez[key]['id']] = get_w_j1_ex(rez[key]['id'])
                # rez = rez[0]['id']
                print(f" j3: {j3d}, j2: {j2d}, j1: {j1d} ")
                ndict = {}
                for i in j3d:
                    print(i,'%%%****!!!!-> ')
                    if j1d[i] <= j2d[i] <= j3d[i]:
                        ndict[i]=j1d[i]
                print(ndict,'****')
                rez = min(ndict, key = lambda k: ndict[k],default=0)
                rez_max = max(ndict, key = lambda k: ndict[k],default=0)
                print(rez,'@@@****=::==')
                print(rez_max,'@@@****=::==')
                


                # clear_op()
    # ????????????????????
    # ????????????????????
    # НАДО ПРАВИТЬ ТУТ ??? ⤵ ⤵ ⤵
    # ПИЗДЕЦ
    # ДОБАВИЛИ СТРОЧКУ:
                set_nop(rez)
    # ????????????????????                
    # ????????????????????

                if rez==0:
                    rez = min(j3d)
            
        #rez = 0
        return rez
    else:
        ma = att.alias()
        rez = {}
        j3d,j2d,j1d = {},{},{}
        i=0
        subq = ma.select(fn.MIN(ma.j3)).where(ma.j3ig.is_null(True))
        query = (att.select(att.id, att.j3).where(
            (att.j3ig.is_null(True)) &
            (att.j3 == subq)))
        for item in query.dicts().execute():
            rez[i]=item
            i+=1
        print(f"rezNOW: {rez} len: {len(rez)}")
    # if 1 min weight in s3:
        if not rez:
            print("------==")
            rez = 0
        if (isinstance(rez, dict)):
            if len(rez)==1:
                print("11111")
                rez = rez[0]['id']
            # sel_op_id
            # set_op(rez)
            # print(rez, "SET OP")
            # exit(1)
            #
    # if more than 1 min weight in s3:
    #print(f"LEN: {rez}, {len(rez)}, {type(rez)}")
        if (isinstance(rez, dict)):
            if len(rez)>=2:
                print(":::(3) >2222222")
                for key in rez:
                    j3d[rez[key]['id']] = rez[key]['j3']
                    j2d[rez[key]['id']] = get_w_j2(rez[key]['id'])
                    j1d[rez[key]['id']] = get_w_j1(rez[key]['id'])
                # rez = rez[0]['id']
                print(f" j3: {j3d}, j2: {j2d}, j1: {j1d} ")
                ndict = {}
                for i in j3d:
                    print(i,'%%%**********=> ')
                    if j1d[i] <= j2d[i] <= j3d[i]:
                        ndict[i]=j1d[i]
                print(ndict,'****')
                rez = min(ndict, key = lambda k: ndict[k],default=0)
                print(rez,'@@@****:::')

                # Берем ДВА ID с одинаковым весом и удаляем уже установленный OP:ID
                # и оставшимуся ОДНОМУ из ДВУХ ID (из словаря ndict)
                # посылаем ПРИГЛАШЕНИЕ на помост ( SET_NOP() )
                # OM TAT SAT
                # 🙏 🙏 🙏 🙏 🙏
                print(f'---- 🙏 🙏 🙏 🙏 🙏 ----------------------::::: {ndict}')
    
    # НАДО ПРАВИТЬ ТУТ ТО ⤵ ⤵ ⤵
    # ПИЗДЕЦ                
    # надо ПРОВЕРИТЬ ndict, keys[0]
    # начали bugzFIFing!!!
    
    # 26.03.22 @ 08:09:10
                # if():
                keys =list(ndict.keys())
                print(f' KURPACHO JI EST #####: { keys } [] = key0: {keys[0]}, key1: {keys[1]}')
                # if(get_min_w_j1(keys[0]) <= get_min_w_j1(keys[1])):
                    # get_min_w_j1()
                # print(f' %% ANGARADJA KARNA %%, keys[0]<=keys[1]: {get_min_w_j1(keys[0])} <= {get_min_w_j1(keys[1])}')
                # print(f' %% ANGARADJA KARNA %%, keys[0]<=keys[1]: {get_min_w_j1(} <= {get_min_w_j1}')
                # j1mn_x0 = get_id_min_w_j1(keys[0])
                # j1mn_x1 = get_id_min_w_j1(keys[1])
                j1mn_x0=get_min_w_j1_all(keys[0])
                j1mn_x1=get_min_w_j1_all(keys[1])

                j1w_all_x0 = get_w_j1_by_id(keys[0])
                j1w_all_x1 = get_w_j1_by_id(keys[1])


                # !!
            
                print(f' %% ANGARADJA KARNA %%, keys[0]<=keys[1]: {j1mn_x0} <= {j1mn_x1}')
                print(f' %% WEIGHT = KARNA %%, keys[0]<=keys[1]: {j1w_all_x0} & {j1w_all_x1}')
                if(j1w_all_x1<=j1w_all_x0):
                    print(f' -=%% j1w_all_x1 <= j1w_all_x0 %%=-, {keys[1]}::{j1w_all_x1} <= {keys[0]}::{j1w_all_x0}')
                    clear_op()
                    clear_nop()
                    set_op(keys[1])
                    set_nop(keys[0])
                    print('commit!!!')
                    
                if(j1w_all_x0<j1w_all_x1):
                    print(f' -=%% j1w_all_x0 < j1w_all_x1 %%=-,  {j1w_all_x0} < {j1w_all_x1}')                





                # ndict.pop(rez)
                # keys = list(ndict.keys())
                ## // Теперь первый ключ можно получить так
                ## keys[0]
                # print(ndict,'**** (DONE NOP ID) ID: ',keys[0])
                # set_nop(keys[0])
                
    # НАДО ПРАВИТЬ ТУТ ТО ⤵ ⤵ ⤵
    # ПИЗДЕЦ                


                if rez==0:
                    rez = min(j3d)
            
        #rez = 0
        return rez







print("v7 c0rE job! MAIN !!!!!!!")
# start_time = time()


# artist = Artist.get(Artist.artist_id == 1)
# attget = dm.att.get(dm.att.id == 19)
# query = att.select()
# print(query)
# att_selected = query.dicts().execute()
#print(att_selected)

# for att in att_selected:
#     print('att: ', att)

# ic(dm.clear_op())
# ic(dm.set_nop(22))
# ic(dm.get_min_w_s1())
# asd=dm.get_min_w_s1()
# ssd=dm.get_id_w_min_s1()
# s1 = get_id_min_w_s1(exclude_id=22)
# s1 = get_id_min_w_s1()
# s2 = get_id_min_w_s2()
# s3 = get_id_min_w_s3()

# # ic('####################################################')
# # ic(s1)
# # ic(s2)
# # ic(s3)
# # ic('####################################################')
# ic('# 456 ###################################################')
# seopidz = sel_op_id(s1, s2, s3)
# ic('# 456 ###################################################')
# ic(f'# {s1} ; {s2} ; {s3} ||| seopidz ::: {seopidz}')









# ic(f"Time taken {time() - start_time}")











image_dir = 'v7_UPLOADS_DIR/'
os.makedirs(image_dir, exist_ok=True)


@app.route('/v7_UPLOADS_DIR')
def rootz():
    return app.send_static_file('index.html')

@app.route('/v7_UPLOADS_DIR/download/<image>')
def download(image):
    return app.send_from_directory(image_dir, image)

@app.route('/v7_UPLOADS_DIR/upload', methods=['POST'])
def upload(camera_id):
    millis = int(time.time() * 1000)
    fn = f'{image_dir}/{millis}.jpg'
    data = request.get_data()
    with open(fn, 'wb') as f:
        f.write(data)
    return jsonify({'filename': fn})


# mycursor.close()
db.close()

if __name__ == '__main__':
    # socketio.run(app,host='10.0.0.8', debug=True)
    socketio.run(app,host=appHost,port=appPort, debug=True)

    # while 1:
    #     os.system("python3 api.py")
    #     print ('Restarting...')
    #     #time.sleep(2880.7) # 48sec & 7ms to CTR+C twice
    #     time.sleep(60.7) # 48sec & 7ms to CTR+C twice
    # app.jinja_env.globals.update(f_fname='f_fname')
    # app.jinja_env.globals.update(s_fname='s_fname')

    #app.run(ssl_context=('cert.pem', 'key.pem'))
    #app.run(host='10.0.0.108',debug=True)
    #app.run(port=443, ssl_context=("localhost+3.pem", "localhost+3-key.pem"))