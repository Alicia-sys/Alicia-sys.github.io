# coding:utf-8
__author__ = "ila"

import logging, os, json, configparser
import time
import numbers
import requests
from werkzeug.utils import redirect

from flask import request, jsonify,session
from sqlalchemy.sql import func,and_,or_,case
from sqlalchemy import cast, Integer,Float
from api.models.brush_model import *
from . import main_bp
from utils.codes import *
from utils.jwt_auth import Auth
from configs import configs
from utils.helper import *
import random
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from utils.baidubce_api import BaiDuBce
from api.models.config_model import config
# 注册接口
@main_bp.route("/pythonek97261k/shiyanshi/register", methods=['POST'])
def pythonek97261k_shiyanshi_register():
    if request.method == 'POST':#post请求
        msg = {'code': normal_code, 'message': 'success', 'data': [{}]}
        req_dict = session.get("req_dict")


        #创建新用户数据
        error = shiyanshi.createbyreq(shiyanshi, shiyanshi, req_dict)
        if error!=None and error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = "注册用户已存在"
        else:
            msg['data'] = error
        #返回结果
        return jsonify(msg)

# 登录接口
@main_bp.route("/pythonek97261k/shiyanshi/login", methods=['GET','POST'])
def pythonek97261k_shiyanshi_login():
    if request.method == 'GET' or request.method == 'POST':#get、post请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        #获取用户名和密码参数
        req_dict = session.get("req_dict")
        req_model = session.get("req_dict")
        try:
            del req_model['role']
        except:
            pass

        #根据用户名获取用户数据
        datas = shiyanshi.getbyparams(shiyanshi, shiyanshi, req_model)
        if not datas:#如果为空则代表账号密码错误或用户不存在
            msg['code'] = password_error_code
            msg['msg']='密码错误或用户不存在'
            return jsonify(msg)


        req_dict['id'] = datas[0].get('id')
        try:
            del req_dict['mima']
        except:
            pass

        #新建用户缓存数据并返回结果
        return Auth.authenticate(Auth, shiyanshi, req_dict)


# 登出接口
@main_bp.route("/pythonek97261k/shiyanshi/logout", methods=['POST'])
def pythonek97261k_shiyanshi_logout():
    if request.method == 'POST':#post请求
        msg = {
            "msg": "退出成功",
            "code": 0
        }
        req_dict = session.get("req_dict")

        return jsonify(msg)

# 重置密码接口
@main_bp.route("/pythonek97261k/shiyanshi/resetPass", methods=['POST'])
def pythonek97261k_shiyanshi_resetpass():
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success"}
        #获取传递的参数
        req_dict = session.get("req_dict")

        if req_dict.get('mima') != None:
            req_dict['mima'] = '123456'
        #更新重置后的密码
        error = shiyanshi.updatebyparams(shiyanshi, shiyanshi, req_dict)

        if error != None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            msg['msg'] = '密码已重置为：123456'
        return jsonify(msg)

# 获取会话信息接口
@main_bp.route("/pythonek97261k/shiyanshi/session", methods=['GET'])
def pythonek97261k_shiyanshi_session():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "data": {}}
        #获取token里的id，查找对应的用户数据返回
        req_dict={"id":session.get('params').get("id")}
        msg['data']  = shiyanshi.getbyparams(shiyanshi, shiyanshi, req_dict)[0]

        return jsonify(msg)

# 分类接口（后端）
@main_bp.route("/pythonek97261k/shiyanshi/page", methods=['GET'])
def pythonek97261k_shiyanshi_page():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success",  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        #获取传递的参数
        req_dict = session.get("req_dict")
        userinfo = session.get("params")
        try:#判断是否有消息
            __hasMessage__=shiyanshi.__hasMessage__
        except:
            __hasMessage__=None
        if __hasMessage__ and __hasMessage__!="否":
            tablename=session.get("tablename")
            if tablename!="users" and session.get("params")!=None and shiyanshi!='chat':
                req_dict["userid"]=session.get("params").get("id")

        tablename=session.get("tablename")
        #非管理员账号则需要判断用户的相应权限
        if tablename!="users" :
            mapping_str_to_object = {}
            for model in Base_model._decl_class_registry.values():
                if hasattr(model, '__tablename__'):
                    mapping_str_to_object[model.__tablename__] = model

            try:#是否有管理员权限
                __isAdmin__=mapping_str_to_object[tablename].__isAdmin__
            except:
                __isAdmin__=None
            try:#是否有用户权限
                __authSeparate__ =mapping_str_to_object[tablename].__authSeparate__
            except:
                __authSeparate__ = None

            if __isAdmin__!="是" and __authSeparate__ == "是" and session.get("params")!=None:
                req_dict["userid"]=session.get("params").get("id")
            else:
                try:
                    del req_dict["userid"]
                except:
                    pass

            # 当前表也是有管理员权限的表
            if  __isAdmin__ == "是" and 'shiyanshi' != 'forum':
                if req_dict.get("userid") and 'shiyanshi' != 'chat':
                    del req_dict["userid"]
            else:
                #非管理员权限的表,判断当前表字段名是否有userid
                if tablename!="users" and 'shiyanshi'[:7]!='discuss'and "userid" in shiyanshi.getallcolumn(shiyanshi,shiyanshi):
                    req_dict["userid"] = session.get("params").get("id")

        clause_args = []
        or_clauses = or_(*clause_args)
        #查询列表数据
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = shiyanshi.page(shiyanshi, shiyanshi, req_dict, or_clauses)
        return jsonify(msg)

# 排序接口
@main_bp.route("/pythonek97261k/shiyanshi/autoSort", methods=['GET'])
def pythonek97261k_shiyanshi_autosort():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success",  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        #获取传递的参数
        req_dict = session.get("req_dict")
        req_dict['sort']='clicktime'
        req_dict['order']='desc'

        try:#获取需要排序的内容
            __browseClick__= shiyanshi.__browseClick__
        except:
            __browseClick__=None
        #根据排序字段进行排序
        if __browseClick__ =='是':
            req_dict['sort']='clicknum'
        elif __browseClick__ =='时长':
            req_dict['sort']='browseduration'
        else:
            req_dict['sort']='clicktime'
        #获取排序内容
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = shiyanshi.page(shiyanshi, shiyanshi, req_dict)

        return jsonify(msg)

#查询单条数据
@main_bp.route("/pythonek97261k/shiyanshi/query", methods=['GET'])
def pythonek97261k_shiyanshi_query():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success",  "data":{}}
        #获取传递的参数，根据参数获取单条结果
        req_dict = session.get("req_dict")
        query = db.session.query(shiyanshi)
        for key, value in req_dict.items():
            query = query.filter(getattr(shiyanshi, key) == value)
        query_result = query.first()
        query_result.__dict__.pop('_sa_instance_state', None)
        msg['data'] = query_result.__dict__
        return jsonify(msg)

# 分页接口（前端）
@main_bp.route("/pythonek97261k/shiyanshi/list", methods=['GET'])
def pythonek97261k_shiyanshi_list():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success",  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        #获取传递的参数
        req_dict = session.get("req_dict")
        if req_dict.__contains__('vipread'):
            del req_dict['vipread']
            
        userinfo = session.get("params")

        try:#判断是否有列表权限
            __foreEndListAuth__=shiyanshi.__foreEndListAuth__
        except:
            __foreEndListAuth__=None
        #不需要权限判断就去掉userid
        if __foreEndListAuth__ and __foreEndListAuth__!="否":
            tablename=session.get("tablename")
            if tablename!="users" and session.get("params")!=None:
                req_dict['userid']=session.get("params").get("id")

        tablename=session.get("tablename")

        if 'luntan' in 'shiyanshi':
            if 'userid' in req_dict.keys():
                del req_dict["userid"]

        if 'discuss' in 'shiyanshi':
            if 'userid' in req_dict.keys():
                del req_dict["userid"]
        #根据封装的req_dict字典去筛选获取列表数据
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = shiyanshi.page(shiyanshi, shiyanshi, req_dict)
        return jsonify(msg)

# 保存接口（后端）
@main_bp.route("/pythonek97261k/shiyanshi/save", methods=['POST'])
def pythonek97261k_shiyanshi_save():
    request.operation = "新增实验室"#封装日志内容
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        #获取传递的参数
        req_dict = session.get("req_dict")
        #判断唯一化的字段是否已经存在相同内容，已存在则不让保存
        if shiyanshi.count(shiyanshi, shiyanshi, {"shiyanshibianhao":req_dict["shiyanshibianhao"]})>0:
            msg['code'] = crud_error_code
            msg['msg'] = "实验室编号已存在"
            return jsonify(msg)
        for key in req_dict:#将空值转为None
            if req_dict[key] == '':
                req_dict[key] = None

        #保存数据
        error= shiyanshi.createbyreq(shiyanshi, shiyanshi, req_dict)
        if error!=None and error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            msg['data'] = error
        return jsonify(msg)

# 添加接口（前端）
@main_bp.route("/pythonek97261k/shiyanshi/add", methods=['POST'])
def pythonek97261k_shiyanshi_add():
    request.operation = "新增实验室"#封装日志内容
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        #获取参数
        req_dict = session.get("req_dict")
        #判断唯一化的字段是否已经存在相同内容，已存在则不让保存
        if shiyanshi.count(shiyanshi, shiyanshi, {"shiyanshibianhao":req_dict["shiyanshibianhao"]})>0:
            msg['code'] = crud_error_code
            msg['msg'] = "实验室编号已存在"
            return jsonify(msg)
        #判断用户权限
        try:
            __foreEndListAuth__=shiyanshi.__foreEndListAuth__
        except:
            __foreEndListAuth__=None
        #不需要权限则去掉userid
        if __foreEndListAuth__ and __foreEndListAuth__!="否":
            tablename=session.get("tablename")
            if tablename!="users":
                req_dict['userid']=session.get("params").get("id")

        #保存数据
        error= shiyanshi.createbyreq(shiyanshi, shiyanshi, req_dict)
        if error!=None and error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = error
            return jsonify(msg)
        else:
            msg['data'] = error
        return jsonify(msg)

# 踩、赞接口
@main_bp.route("/pythonek97261k/shiyanshi/thumbsup/<id_>", methods=['GET'])
def pythonek97261k_shiyanshi_thumbsup(id_):
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        id_=int(id_)
        type_=int(req_dict.get("type",0))
        #获取要踩赞的记录
        rets=shiyanshi.getbyid(shiyanshi, shiyanshi,id_)
        update_dict={
            "id":id_,
        }
        #加减数据
        if type_==1:#赞
            update_dict["thumbsupnum"]=int(rets[0].get('thumbsupnum'))+1
        elif type_==2:#踩
            update_dict["crazilynum"]=int(rets[0].get('crazilynum'))+1
        #更新记录
        error = shiyanshi.updatebyparams(shiyanshi, shiyanshi, update_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return jsonify(msg)

# 获取详情信息（后端）
@main_bp.route("/pythonek97261k/shiyanshi/info/<id_>", methods=['GET'])
def pythonek97261k_shiyanshi_info(id_):
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        #根据id获取对应记录
        data = shiyanshi.getbyid(shiyanshi, shiyanshi, int(id_))
        if len(data)>0:
            msg['data']=data[0]
        #浏览点击次数
        try:
            __browseClick__= shiyanshi.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__  and  "clicknum"  in shiyanshi.__table__.columns:
            click_dict={"id":int(id_),"clicknum":str(int(data[0].get("clicknum") or 0)+1)}#增加点击次数
            ret=shiyanshi.updatebyparams(shiyanshi,shiyanshi,click_dict)#更新记录
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return jsonify(msg)

# 获取详情信息（前端）
@main_bp.route("/pythonek97261k/shiyanshi/detail/<id_>", methods=['GET'])
def pythonek97261k_shiyanshi_detail(id_):
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        #根据id获取对应记录
        data = shiyanshi.getbyid(shiyanshi, shiyanshi, int(id_))
        if len(data)>0:
            msg['data']=data[0]

        #浏览点击次数
        try:
            __browseClick__= shiyanshi.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__ and "clicknum" in shiyanshi.__table__.columns:
            click_dict={"id":int(id_),"clicknum":str(int(data[0].get("clicknum") or 0)+1)}#增加点击次数
            ret=shiyanshi.updatebyparams(shiyanshi,shiyanshi,click_dict)#更新记录
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return jsonify(msg)

# 更新接口
@main_bp.route("/pythonek97261k/shiyanshi/update", methods=['POST'])
def pythonek97261k_shiyanshi_update():
    request.operation = "更新实验室"#填充日志内容
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")

        if db.session.query(func.count(getattr(shiyanshi, 'id'))).filter(shiyanshi.id !=req_dict["id"], shiyanshi.shiyanshibianhao == req_dict["shiyanshibianhao"]).scalar()>0:
            msg['code'] = crud_error_code
            msg['msg'] = "实验室编号已存在"
            return jsonify(msg)
        #如果存在密码或点击次数则不更新
        if req_dict.get("mima") and "mima" not in shiyanshi.__table__.columns :
            del req_dict["mima"]
        if req_dict.get("password") and "password" not in shiyanshi.__table__.columns :
            del req_dict["password"]
        try:
            del req_dict["clicknum"]
        except:
            pass

        #更新记录
        error = shiyanshi.updatebyparams(shiyanshi, shiyanshi, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error

        return jsonify(msg)

# 删除接口
@main_bp.route("/pythonek97261k/shiyanshi/delete", methods=['POST'])
def pythonek97261k_shiyanshi_delete():
    request.operation = "删除实验室"#更新日志记录
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        #删除记录
        error=shiyanshi.delete(
            shiyanshi,
            req_dict
        )
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return jsonify(msg)

# 投票接口
@main_bp.route("/pythonek97261k/shiyanshi/vote/<int:id_>", methods=['POST'])
def pythonek97261k_shiyanshi_vote(id_):
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success"}
        #根据id获取记录
        data= shiyanshi.getbyid(shiyanshi, shiyanshi, int(id_))
        for i in data:
            #增加投票数并更新记录
            votenum=i.get('votenum')
            if votenum!=None:
                params={"id":int(id_),"votenum":votenum+1}
                error=shiyanshi.updatebyparams(shiyanshi,shiyanshi,params)
                if error!=None:
                    msg['code'] = crud_error_code
                    msg['msg'] = error
        return jsonify(msg)

#分组统计接口
@main_bp.route("/pythonek97261k/shiyanshi/group/<columnName>", methods=['GET'])
def pythonek97261k_shiyanshi_group(columnName):
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        #获取传递的参数
        req_dict = session.get("req_dict")
        limit = 0
        order = ""
        if "limit" in req_dict:
            limit = req_dict["limit"]
            del req_dict["limit"]
        if "order" in req_dict:
            order = req_dict["order"]
            del req_dict["order"]
        userinfo = session.get("params")
        #查询记录
        msg['data'] = shiyanshi.groupbycolumnname(shiyanshi,shiyanshi,columnName,req_dict)
        msg['data'] = msg['data'][:10]
        msg['data'] = [ {**i,columnName:str(i[columnName])} if columnName in i else i for i in msg['data']]
        json_filename='shiyanshi'+f'_group_{columnName}.json'
        #记录查询语句
        where = ' where 1 = 1 '
        sql = "SELECT COUNT(*) AS total, " + columnName + " FROM shiyanshi " + where + " GROUP BY " + columnName
        #对结果进行升序可降序排序
        if order == "desc":
            msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None),key=lambda x: x['total'],reverse=True)
        elif order == "asc":
            msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None),key=lambda x: x['total'])
        #截取列表个数
        if 0 < int(limit) < len(msg['data']):
            msg['data'] = msg['data'][:int(limit)]
        return jsonify(msg)#返回封装的json结果

# 按值统计接口
@main_bp.route("/pythonek97261k/shiyanshi/value/<xColumnName>/<yColumnName>", methods=['GET'])
def pythonek97261k_shiyanshi_value(xColumnName, yColumnName):
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        #获取参数
        req_dict = session.get("req_dict")
        limit = 0
        order = ""
        if "limit" in req_dict:
            limit = req_dict["limit"]
            del req_dict["limit"]
        if "order" in req_dict:
            order = req_dict["order"]
            del req_dict["order"]
        userinfo = session.get("params")
        #查询记录
        msg['data'] = shiyanshi.getvaluebyxycolumnname(shiyanshi,shiyanshi,xColumnName,yColumnName,req_dict)
        msg['data'] = msg['data'][:10]
        #对结果进行升序可降序排序
        if order == "desc":
            msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None),key=lambda x: x['total'],reverse=True)
        elif order == "asc":
            msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None),key=lambda x: x['total'])
        #截取列表个数
        if 0 < int(limit) < len(msg['data']):
            msg['data'] = msg['data'][:int(limit)]
        return jsonify(msg)#返回封装的json结果

# 按日期统计接口
@main_bp.route("/pythonek97261k/shiyanshi/value/<xColumnName>/<yColumnName>/<timeStatType>", methods=['GET'])
def pythonek97261k_shiyanshi_value_riqi(xColumnName, yColumnName, timeStatType):
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        userinfo = session.get("params")
        where = ' where 1 = 1 '
        #定义查询语句
        sql = ''
        if timeStatType == '日':
            sql = "SELECT DATE_FORMAT({0}, '%Y-%m-%d') {0}, sum({1}) total FROM shiyanshi {2} GROUP BY DATE_FORMAT({0}, '%Y-%m-%d')".format(xColumnName, yColumnName, where, '%Y-%m-%d')

        if timeStatType == '月':
            sql = "SELECT DATE_FORMAT({0}, '%Y-%m') {0}, sum({1}) total FROM shiyanshi {2} GROUP BY DATE_FORMAT({0}, '%Y-%m')".format(xColumnName, yColumnName, where, '%Y-%m')

        if timeStatType == '年':
            sql = "SELECT DATE_FORMAT({0}, '%Y') {0}, sum({1}) total FROM shiyanshi {2} GROUP BY DATE_FORMAT({0}, '%Y')".format(xColumnName, yColumnName, where, '%Y')
        #执行查询
        data = db.session.execute(sql)
        data = data.fetchall()
        #封装结果
        results = []
        for i in range(len(data)):
            result = {
                xColumnName: decimalEncoder(data[i][0]),
                'total': decimalEncoder(data[i][1])
            }
            results.append(result)
            
        msg['data'] = results
        #获取hadoop分析后的数据文件
        json_filename='shiyanshi'+f'_value_{xColumnName}_{yColumnName}.json'
        req_dict = session.get("req_dict")
        #对结果进行排序
        if "order" in req_dict:
            order = req_dict["order"]
            if order == "desc":
                msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None),key=lambda x: x['total'],reverse=True)
            else:
                msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None),key=lambda x: x['total'])
        #截取列表个数
        if "limit" in req_dict and int(req_dict["limit"]) < len(msg['data']):
            msg['data'] = msg['data'][:int(req_dict["limit"])]
        return jsonify(msg)#返回封装的json结果

# 按值统计（多）
@main_bp.route("/pythonek97261k/shiyanshi/valueMul/<xColumnName>", methods=['GET'])
def pythonek97261k_shiyanshi_valueMul(xColumnName):
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": []}

        req_dict = session.get("req_dict")
        userinfo = session.get("params")

        where = ' where 1 = 1 '
        for item in req_dict['yColumnNameMul'].split(','):
            #定义查询语句
            sql = "SELECT {0}, sum({1}) AS total FROM shiyanshi {2} GROUP BY {0} LIMIT 10".format(xColumnName, item, where)
            L = []
            #执行查询
            data = db.session.execute(sql)
            data = data.fetchall() 
            for i in range(len(data)):
                result = {
                    xColumnName: decimalEncoder(data[i][0]),
                    'total': decimalEncoder(data[i][1])
                }
                L.append(result)
            msg['data'].append(L)
        return jsonify(msg)

# 按值统计（多）
@main_bp.route("/pythonek97261k/shiyanshi/valueMul/<xColumnName>/<timeStatType>", methods=['GET'])
def pythonek97261k_shiyanshi_valueMul_time(xColumnName,timeStatType):
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": []}

        req_dict = session.get("req_dict")
        userinfo = session.get("params")
        where = ' where 1 = 1 '

        for item in req_dict['yColumnNameMul'].split(','):
            #定义查询语句
            sql = ''
            if timeStatType == '日':
                sql = "SELECT DATE_FORMAT({0}, '%Y-%m-%d') {0}, sum({1}) total FROM shiyanshi {2} GROUP BY DATE_FORMAT({0}, '%Y-%m-%d') LIMIT 10".format(xColumnName, item, where, '%Y-%m-%d')

            if timeStatType == '月':
                sql = "SELECT DATE_FORMAT({0}, '%Y-%m') {0}, sum({1}) total FROM shiyanshi {2} GROUP BY DATE_FORMAT({0}, '%Y-%m') LIMIT 10".format(xColumnName, item, where, '%Y-%m')

            if timeStatType == '年':
                sql = "SELECT DATE_FORMAT({0}, '%Y') {0}, sum({1}) total FROM shiyanshi {2} GROUP BY DATE_FORMAT({0}, '%Y') LIMIT 10".format(xColumnName, item, where, '%Y')
            L = []
            #执行查询
            data = db.session.execute(sql)
            data = data.fetchall() 
            for i in range(len(data)):
                result = {
                    xColumnName: decimalEncoder(data[i][0]),
                    'total': decimalEncoder(data[i][1])
                }
                L.append(result)
            msg['data'].append(L)
        return jsonify(msg)


#查询记录总数量接口
@main_bp.route("/pythonek97261k/shiyanshi/count", methods=['GET'])
def pythonek97261k_shiyanshi_count():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success",  "data": 0}
        req_dict = session.get("req_dict")
        userinfo = session.get("params")

        #查询记录个数
        msg['data']  = shiyanshi.count(shiyanshi, shiyanshi, req_dict)
        #返回json结果
        return jsonify(msg)


#获取所有记录列表
@main_bp.route("/pythonek97261k/shiyanshi/lists", methods=['GET'])
def pythonek97261k_shiyanshi_lists():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": []}
        list,_,_,_,_ = shiyanshi.page(shiyanshi,shiyanshi,{})
        msg['data'] = list
        return jsonify(msg)

