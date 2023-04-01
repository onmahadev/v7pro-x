# import configparser
from peewee import *
# from collections import Counter
import logging
from logging.handlers import RotatingFileHandler

#######################################################################
##### logging config
logging.disable(level=50) # OFF INFO level

logging.basicConfig(
    filename='app.log',
    filemode='a',
    encoding='utf-8',
    level=logging.DEBUG,
    format="%(asctime)s %(process)d %(levelname)s %(funcName)s %(filename)s %(lineno)d %(message)s"
    )
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler("app.log", maxBytes=3145728, backupCount=5)
logger.addHandler(handler)
logging.info("STARTed *****")





#from mysql.connector import connect, Error
#######################################################################
##### get config
# cfg = configparser.ConfigParser()
# cfg.read('theapp.cfg')
# mylHost=cfg.get('mysql', 'host')
# mylUser=cfg.get('mysql', 'user')
# mylPwd=cfg.get('mysql', 'passwd')
# mylDb=cfg.get('mysql', 'database')
#######################################################################

db = MySQLDatabase(
    host="127.0.0.1",
    user="v7user",
    password="v7password",
    database="v7",
    port=8889,
)



#is Snatch|Jerk apps now
SN = True
CJ = False
idOPZzz = -1


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
    s_place = IntegerField(column_name='snatch_place')
    j_place = IntegerField(column_name='cleanjerk_place')
    place = IntegerField(column_name='place')
    country = TextField(column_name='country_')

    nr = IntegerField(column_name='newrank')
    sc = IntegerField(column_name='score')
    pos = IntegerField(column_name='position')
    isend = IntegerField(column_name='actionend')
    sname = TextField(column_name='secondname')
    fname = TextField(column_name='firstname')
    exnow = TextField(column_name='exnow')
    wnow = TextField(column_name='weightnow')
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
            "country_id": self.country_id,
            "country": self.country,
            "city_id": self.city_id,
            "city": self.city,
            "wcat_id": self.wcat_id,
            "wcat": self.wcat,
            "ow": self.ow,
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
    #cntr = ForeignKeyField(att, column_name='id')
    
    def obj_to_dict(self):  # for build json format
        return {
            "id": self.country_id,
            "name": self.name,
            "flag": self.flag,
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
##### f7v att  METHODS

#####################################################################
##### clear op, set all att.op = 0
def clear_op():
    clear = att.update(op=0).where(att.id > 0)
    response = clear.execute()
    return response

#####################################################################
##### clear nop, set all att.nextop = 0
def clear_nop():
    clear = att.update(nop=0).where(att.id > 0)
    response = clear.execute()
    return response

#####################################################################
##### set op, set att.op=1, by gets ID
def set_op(opid):
    setop = att.update(op=1).where(att.id == opid)
    response = setop.execute()
    return response

#####################################################################
##### set nextop, set att.nexiop=1, by gets ID
def set_nop(nopid):
    setnop = att.update(nop=1).where(att.id == nopid)
    response = setnop.execute()
    return response
#####################################################################
#####################################################################
#####################################################################


#####################################################################
##### get s1 weight by id
#####  -> weight
def get_w_s1(id):
    req = att.get(att.id == id).s1
    return req

#####################################################################
##### get s2 weight by id
#####  -> weight
def get_w_s2(id):
    req = att.get(att.id == id).s2
    return req

#####################################################################
##### get s3 weight by id
#####  -> weight
def get_w_s3(id):
    req = att.get(att.id == id).s3
    return req

#####################################################################
#####################################################################
#####################################################################
##### select from (s1&s2&s3) by arg:id min weight and sep op id
#####  -> id (op id)
def sel_op_id(s1,s2,s3):

    nowid = -1
    #print(f"{s1} {s2} {s3} ____3")
############################## only s1
    if(s1>0 and s2==0 and s3==0):
        print(f"op= s1*, id:{s1} weight:{get_w_s1(s1)}")
        clear_op()
        set_op(s1)
        nowid = s1
############################## only s2
    if(s1==0 and s2>0 and s3==0):
        print(f"op= s2, id:{s2} weight:{get_w_s2(s2)}")
        clear_op()
        set_op(s2)
        nowid = s2
############################## only s3
    if(s1==0 and s2==0 and s3>0):
        print(f"op= s3, id:{s3} weight:{get_w_s3(s3)}")
        clear_op()
        set_op(s3)        
        nowid = s3
############################## s1 && s2
    if(s1>0 and s2>0 and s3==0):
        if(get_w_s1(s1))<=(get_w_s2(s2)):
            print(f"op= s1!, id:{s1} weight:{get_w_s1(s1)}")
            clear_op()
            set_op(s1)
            nowid = s1
        elif(get_w_s1(s1))>(get_w_s2(s2)):
            print(f"op= s2, id:{s2} weight:{get_w_s2(s2)}")
            clear_op()
            set_op(s2)
            nowid = s2
############################## s1 && s3
    if(s1>0 and s2==0 and s3>0):
        if(get_w_s1(s1))<=(get_w_s3(s3)):
            print(f"op= s1**, id:{s1} weight:{get_w_s1(s1)}")
            clear_op()
            set_op(s1)
            nowid = s1
        elif(get_w_s1(s1))>(get_w_s3(s3)):
            print(f"op= s3, id:{s3} weight:{get_w_s3(s3)}")
            clear_op()
            set_op(s3)
            nowid = s3
############################## s2 && s3
    if(s1==0 and s2>0 and s3>0):
        if(get_w_s2(s2))<=(get_w_s3(s3)):
            print(f"op= s2, id:{s2} weight:{get_w_s2(s2)}")
            clear_op()
            set_op(s2)
            nowid = s2
        elif(get_w_s1(s2))>(get_w_s3(s3)):
            print(f"op= s3, id:{s3} weight:{get_w_s3(s3)}")
            clear_op()
            set_op(s3)
            nowid = s3
############################## s1 && s2 && s3
    if(s1>0 and s2>0 and s3>0):
        s1w,s2w,s3w = get_w_s1(s1),get_w_s2(s2),get_w_s3(s3)
        clear_op()
        minest = 0
        app = [] # approach=подход s1 ? s2 ? s3
        if s1w <= s2w and s1w <= s3w:
            minest = s1w
            set_op(s1)
            nowid = s1
            print(f"op= s1* id:{s1} w:{s1w}")
        elif s2w <= s3w:
            minest = s2w
            set_op(s2)
            nowid = s2
            print(f"op= s2 id:{s2} w:{s2w}")
        else:
            minest = s3w
            set_op(s3)
            nowid = s3
            print(f"op= s3_ id:{s3} w:{s3w}")

### If all weight = 0 - The END of flow!            
    if(s1==0 and s2==0 and s3==0):
        print(f"THE END!!! ids: {s1}, {s2}, {s3}")
        SN,CJ= False, True
        print(f"Snatch is:  {SN}")
        print(f"Clear&Jerk is:  {CJ}")
    else:

    #print(f"a1={s1w} s2={s2w} s3={s3w}, min={minest} app={app}")
    #get_w_s2(s2) = 0
        print(f"input id's: {s1}, {s2}, {s3},[ lastID: {nowid} ]")
        return nowid



# NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP
#####  -> id (op id)
def sel_nop_id(s1,s2,s3):

    nowid = -1
    #print(f"{s1} {s2} {s3} ____3")
############################## only s1
    if(s1>0 and s2==0 and s3==0):
        print(f"NOP= s1^*, id:{s1} weight:{get_w_s1(s1)}")
        clear_nop()
        set_nop(s1)
        nowid = s1
############################## only s2
    if(s1==0 and s2>0 and s3==0):
        print(f"NOP= s2, id:{s2} weight:{get_w_s2(s2)}")
        clear_nop()
        set_nop(s2)
        nowid = s2
############################## only s3
    if(s1==0 and s2==0 and s3>0):
        print(f"NOP= s3, id:{s3} weight:{get_w_s3(s3)}")
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
        elif(get_w_s1(s1))>(get_w_s2(s2)):
            print(f"NOP= s2, id:{s2} weight:{get_w_s2(s2)}")
            clear_nop()
            set_nop(s2)
            nowid = s2
############################## s1 && s3
    if(s1>0 and s2==0 and s3>0):
        if(get_w_s1(s1))<=(get_w_s3(s3)):
            print(f"NOP= s1**, id:{s1} weight:{get_w_s1(s1)}")
            clear_nop()
            set_nop(s1)
            nowid = s1
        elif(get_w_s1(s1))>(get_w_s3(s3)):
            print(f"NOP= s3, id:{s3} weight:{get_w_s3(s3)}")
            clear_nop()
            set_nop(s3)
            nowid = s3
############################## s2 && s3
    if(s1==0 and s2>0 and s3>0):
        if(get_w_s2(s2))<=(get_w_s3(s3)):
            print(f"NOP= s2, id:{s2} weight:{get_w_s2(s2)}")
            clear_nop()
            set_nop(s2)
            nowid = s2
        elif(get_w_s1(s2))>(get_w_s3(s3)):
            print(f"NOP= s3, id:{s3} weight:{get_w_s3(s3)}")
            clear_nop()
            set_nop(s3)
            nowid = s3
############################## s1 && s2 && s3
    if(s1>0 and s2>0 and s3>0):
        s1w,s2w,s3w = get_w_s1(s1),get_w_s2(s2),get_w_s3(s3)
        clear_nop()
        minest = 0
        app = [] # approach=подход s1 ? s2 ? s3
        if s1w <= s2w and s1w <= s3w:
            minest = s1w
            set_nop(s1)
            nowid = s1
            print(f"NOP= s1*^^^ id:{s1} w:{s1w}")
        elif s2w <= s3w:
            minest = s2w
            set_nop(s2)
            nowid = s2
            print(f"NOP= s2 id:{s2} w:{s2w}")
        else:
            minest = s3w
            set_nop(s3)
            nowid = s3
            print(f"NOP= s3*_ id:{s3} w:{s3w}")

### If all weight = 0 - The END of flow!            
    if(s1==0 and s2==0 and s3==0):
        print(f"THE END!!! ids: {s1}, {s2}, {s3}")
        SN,CJ= False, True
        print(f"Snatch is:  {SN}")
        print(f"Clear&Jerk is:  {CJ}")
    else:

    #print(f"a1={s1w} s2={s2w} s3={s3w}, min={minest} app={app}")
    #get_w_s2(s2) = 0
        print(f"input id's: {s1}, {s2}, {s3},[ lastID: {nowid} ]")
        return nowid



#####################################################################
##### get min s1 with double weigh
#####  -> 1:{id,weight}..n{id,weight}
def get_min_w_s1():
    ma = att.alias()
    rez = {}
    i=0
    subq = ma.select(fn.MIN(ma.s1))
    query = (att.select(att.id, att.s1).where(att.s1 == subq))
    for item in query.dicts().execute():
        i+=1
        rez[i]=item
    return rez

#####################################################################
##### get id with min weight in s1 w/o doubles (op id s1)
#####  -> id, one id with min weight in s1
def get_id_min_w_s1(exclude_id=0):
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
            (att.s1ig.is_null(True)))
        )
        for item in query.dicts().execute():
            print(item,'*****')
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
##### get id with min weight in s2  w/o doubles (op id s2)
#####  -> id, one id with min weight in s2
def get_id_min_w_s2(exclude_id=0):
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
        return rez
    else:
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
        return rez


#####################################################################
##### get id with min weight in s3  w/o doubles (op id s3)
#####  -> id, one id with min weight in s3
def get_id_min_w_s3(exclude_id=0):
    if exclude_id>0:
        print('*** EXCLUDE s3 OP ID: [ ', exclude_id, ' ]')
        ma = att.alias()
        rez = {}
        s3d,s2d,s1d = {},{},{}
        i=0
        subq = ma.select(fn.MIN(ma.s3)).where((ma.id!=exclude_id) & ma.s3ig.is_null(True))
        query = (att.select(att.id, att.s3).where(
            (att.s3ig.is_null(True)) &
            (att.id != exclude_id) &
            (att.s3 == subq)))
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
                print("::: >2222222")
                for key in rez:
                    s3d[rez[key]['id']] = rez[key]['s3']
                    s2d[rez[key]['id']] = get_w_s2(rez[key]['id'])
                    s1d[rez[key]['id']] = get_w_s1(rez[key]['id'])
                # rez = rez[0]['id']
                print(f" s3: {s3d}, s2: {s2d}, s1: {s1d} ")
                ndict = {}
                for i in s3d:
                    print(i,'%%%****')
                    if s1d[i] <= s2d[i] <= s3d[i]:
                        ndict[i]=s1d[i]
                print(ndict,'****')
                rez = min(ndict, key = lambda k: ndict[k],default=0)
                print(rez,'@@@****')
                if rez==0:
                    rez = min(s3d)
            
        #rez = 0
        return rez
    else:
        ma = att.alias()
        rez = {}
        s3d,s2d,s1d = {},{},{}
        i=0
        subq = ma.select(fn.MIN(ma.s3)).where(ma.s3ig.is_null(True))
        query = (att.select(att.id, att.s3).where(
            (att.s3ig.is_null(True)) &
            (att.s3 == subq)))
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
                print("::: >2222222")
                for key in rez:
                    s3d[rez[key]['id']] = rez[key]['s3']
                    s2d[rez[key]['id']] = get_w_s2(rez[key]['id'])
                    s1d[rez[key]['id']] = get_w_s1(rez[key]['id'])
                # rez = rez[0]['id']
                print(f" s3: {s3d}, s2: {s2d}, s1: {s1d} ")
                ndict = {}
                for i in s3d:
                    print(i,'%%%****')
                    if s1d[i] <= s2d[i] <= s3d[i]:
                        ndict[i]=s1d[i]
                print(ndict,'****')
                rez = min(ndict, key = lambda k: ndict[k],default=0)
                print(rez,'@@@****')
                if rez==0:
                    rez = min(s3d)
            
        #rez = 0
        return rez









        # the smallest key 
        # key1 = min(ndict) 
        # print("The smallest key:", key1)
        # key2 = min(ndict, key = lambda k: ndict[k])
        # print("The key with the smallest value:", key2) 
        # print("The smallest value:", ndict[key2])



    #logging.info('len(s2_dict_lst_val)>2')
        #logging.warning("This is a Warning")
    
#def tezto(a:list):
#    print(a)

    
    #tst_dict = {17:60, 22:60, 21:67}
    #tst_dict = {}
    #values = tst_dict.values()
    #counter = Counter(values)
    #print('$$$',dict(counter))
    #zaza = sum(tst_dict.values()) 


    # len_s2 = len(s2_dict)
    # list_s2_id = []
    # list_s2_w = []
    # for ii in s2_dict:
    #     list_s2_id.append(ii)
    #     list_s2_w.append(get_w_s2(ii))
    # print(list_s2_id, list_s2_w[0])

    # #? отчего суда заходим?
    # s1_dict = {}
    # for i in s2_dict:
    #     print('========',s2_dict[i])
    #     #print('========',s2_dict.items[i])
    #     s1_dict[i]=get_w_s1(i)
    # min_val_s1 = min(s1_dict.values(),default=0)
    # z1 = {key:value for key, value in s1_dict.items() if value == min_val_s1}
    # rez = min(z1.keys(),default=0)
    # print(min_val_s1,'+++++++')
    # print(z1,'+++++++',rez)

    # print('###',s1_dict)
    # print('s3',min_w_dict)
    # print('s2',s2_dict)
    # print('rez=',rez)
    # print('miv_val',min_val)






    ###q = att.select(att.id,att.s1).where(att.s1ig.is_null(True))
    #q = att.select(att.id,att.s1).where(att.s1).select(att.id,att.s1)
    #for item in q.dicts().execute():
    #    print('att: ', item)
      


#SELECT id,snatch1 FROM f7anow_tmp
#WHERE snatch1 = (SELECT MIN(snatch1) FROM f7anow_tmp)

# SELECT id,snatch1 FROM f7anow_tmp WHERE snatch1 = (SELECT MIN(snatch1) FROM f7anow_tmp WHERE snatch1isget IS NULL)

# # SELECT id,snatch2,snatch2isget FROM f7anow_tmp
# WHERE snatch2 = (
#     SELECT MIN(snatch2) FROM f7anow_tmp 
# WHERE snatch2isget IS NULL) AND snatch2isget IS NULL




try:
    db.connect()
    #Category.create_table()
except InternalError as px:
    print(str(px))
    logging.inerrorfo(f'DB connect ERROR: { str(px) } ')


logging.info('FINISHed *****')

#######################!!!
######### CPOYNG!
######### NEW BRANCH!
#######################!!!