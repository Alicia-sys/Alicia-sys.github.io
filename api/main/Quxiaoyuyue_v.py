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
@main_bp.route("/pythonek97261k/quxiaoyuyue/register", methods=['POST'])
def pythonek97261k_quxiaoyuyue_register():
    if request.method == 'POST':#post请求
        msg = {'code': normal_code, 'message': 'success', 'data': [{}]}
        req_dict = session.get("req_dict")


        #创建新用户数据
        error = quxiaoyuyue.createbyreq(quxiaoyuyue, quxiaoyuyue, req_dict)
        if error!=None and error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = "注册用户已存在"
        else:
            msg['data'] = error
        #返回结果
        return jsonify(msg)

# 登录接口
@main_bp.route("/pythonek97261k/quxiaoyuyue/login", methods=['GET','POST'])
def pythonek97261k_quxiaoyuyue_login():
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
        datas = quxiaoyuyue.getbyparams(quxiaoyuyue, quxiaoyuyue, req_model)
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
        return Auth.authenticate(Auth, quxiaoyuyue, req_dict)


# 登出接口
@main_bp.route("/pythonek97261k/quxiaoyuyue/logout", methods=['POST'])
def pythonek97261k_quxiaoyuyue_logout():
    if request.method == 'POST':#post请求
        msg = {
            "msg": "退出成功",
            "code": 0
        }
        req_dict = session.get("req_dict")

        return jsonify(msg)

# 重置密码接口
@main_bp.route("/pythonek97261k/quxiaoyuyue/resetPass", methods=['POST'])
def pythonek97261k_quxiaoyuyue_resetpass():
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success"}
        #获取传递的参数
        req_dict = session.get("req_dict")

        if req_dict.get('mima') != None:
            req_dict['mima'] = '123456'
        #更新重置后的密码
        error = quxiaoyuyue.updatebyparams(quxiaoyuyue, quxiaoyuyue, req_dict)

        if error != None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            msg['msg'] = '密码已重置为：123456'
        return jsonify(msg)

# 获取会话信息接口
@main_bp.route("/pythonek97261k/quxiaoyuyue/session", methods=['GET'])
def pythonek97261k_quxiaoyuyue_session():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "data": {}}
        #获取token里的id，查找对应的用户数据返回
        req_dict={"id":session.get('params').get("id")}
        msg['data']  = quxiaoyuyue.getbyparams(quxiaoyuyue, quxiaoyuyue, req_dict)[0]

        return jsonify(msg)

# 分类接口（后端）
@main_bp.route("/pythonek97261k/quxiaoyuyue/page", methods=['GET'])
def pythonek97261k_quxiaoyuyue_page():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success",  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        #获取传递的参数
        req_dict = session.get("req_dict")
        userinfo = session.get("params")
        try:#判断是否有消息
            __hasMessage__=quxiaoyuyue.__hasMessage__
        except:
            __hasMessage__=None
        if __hasMessage__ and __hasMessage__!="否":
            tablename=session.get("tablename")
            if tablename!="users" and session.get("params")!=None and quxiaoyuyue!='chat':
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
            if  __isAdmin__ == "是" and 'quxiaoyuyue' != 'forum':
                if req_dict.get("userid") and 'quxiaoyuyue' != 'chat':
                    del req_dict["userid"]
            else:
                #非管理员权限的表,判断当前表字段名是否有userid
                if tablename!="users" and 'quxiaoyuyue'[:7]!='discuss'and "userid" in quxiaoyuyue.getallcolumn(quxiaoyuyue,quxiaoyuyue):
                    req_dict["userid"] = session.get("params").get("id")

        # 判断用户权限对应字段
        tablename = session.get("tablename")
        if tablename == 'yonghu':
            req_dict['yonghuzhanghao'] = userinfo['yonghuzhanghao']
            if 'userid' in req_dict.keys():
                del req_dict["userid"]
        clause_args = []
        or_clauses = or_(*clause_args)
        #查询列表数据
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = quxiaoyuyue.page(quxiaoyuyue, quxiaoyuyue, req_dict, or_clauses)
        return jsonify(msg)

# 排序接口
@main_bp.route("/pythonek97261k/quxiaoyuyue/autoSort", methods=['GET'])
def pythonek97261k_quxiaoyuyue_autosort():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success",  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        #获取传递的参数
        req_dict = session.get("req_dict")
        req_dict['sort']='clicktime'
        req_dict['order']='desc'

        try:#获取需要排序的内容
            __browseClick__= quxiaoyuyue.__browseClick__
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
        msg['data']['pageSize']  = quxiaoyuyue.page(quxiaoyuyue, quxiaoyuyue, req_dict)

        return jsonify(msg)

#查询单条数据
@main_bp.route("/pythonek97261k/quxiaoyuyue/query", methods=['GET'])
def pythonek97261k_quxiaoyuyue_query():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success",  "data":{}}
        #获取传递的参数，根据参数获取单条结果
        req_dict = session.get("req_dict")
        query = db.session.query(quxiaoyuyue)
        for key, value in req_dict.items():
            query = query.filter(getattr(quxiaoyuyue, key) == value)
        query_result = query.first()
        query_result.__dict__.pop('_sa_instance_state', None)
        msg['data'] = query_result.__dict__
        return jsonify(msg)

# 分页接口（前端）
@main_bp.route("/pythonek97261k/quxiaoyuyue/list", methods=['GET'])
def pythonek97261k_quxiaoyuyue_list():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success",  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        #获取传递的参数
        req_dict = session.get("req_dict")
        if req_dict.__contains__('vipread'):
            del req_dict['vipread']
            
        userinfo = session.get("params")

        try:#判断是否有列表权限
            __foreEndListAuth__=quxiaoyuyue.__foreEndListAuth__
        except:
            __foreEndListAuth__=None
        #不需要权限判断就去掉userid
        if __foreEndListAuth__ and __foreEndListAuth__!="否":
            tablename=session.get("tablename")
            if tablename!="users" and session.get("params")!=None:
                req_dict['userid']=session.get("params").get("id")

        tablename=session.get("tablename")

        if 'luntan' in 'quxiaoyuyue':
            if 'userid' in req_dict.keys():
                del req_dict["userid"]

        if 'discuss' in 'quxiaoyuyue':
            if 'userid' in req_dict.keys():
                del req_dict["userid"]
        #根据封装的req_dict字典去筛选获取列表数据
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = quxiaoyuyue.page(quxiaoyuyue, quxiaoyuyue, req_dict)
        return jsonify(msg)

# 保存接口（后端）
@main_bp.route("/pythonek97261k/quxiaoyuyue/save", methods=['POST'])
def pythonek97261k_quxiaoyuyue_save():
    request.operation = "新增取消预约"#封装日志内容
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        #获取传递的参数
        req_dict = session.get("req_dict")
        for key in req_dict:#将空值转为None
            if req_dict[key] == '':
                req_dict[key] = None

        #保存数据
        error= quxiaoyuyue.createbyreq(quxiaoyuyue, quxiaoyuyue, req_dict)
        if error!=None and error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            msg['data'] = error
        return jsonify(msg)

# 添加接口（前端）
@main_bp.route("/pythonek97261k/quxiaoyuyue/add", methods=['POST'])
def pythonek97261k_quxiaoyuyue_add():
    request.operation = "新增取消预约"#封装日志内容
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        #获取参数
        req_dict = session.get("req_dict")
        #判断用户权限
        try:
            __foreEndListAuth__=quxiaoyuyue.__foreEndListAuth__
        except:
            __foreEndListAuth__=None
        #不需要权限则去掉userid
        if __foreEndListAuth__ and __foreEndListAuth__!="否":
            tablename=session.get("tablename")
            if tablename!="users":
                req_dict['userid']=session.get("params").get("id")

        #保存数据
        error= quxiaoyuyue.createbyreq(quxiaoyuyue, quxiaoyuyue, req_dict)
        if error!=None and error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = error
            return jsonify(msg)
        else:
            msg['data'] = error
        return jsonify(msg)

# 踩、赞接口
@main_bp.route("/pythonek97261k/quxiaoyuyue/thumbsup/<id_>", methods=['GET'])
def pythonek97261k_quxiaoyuyue_thumbsup(id_):
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        id_=int(id_)
        type_=int(req_dict.get("type",0))
        #获取要踩赞的记录
        rets=quxiaoyuyue.getbyid(quxiaoyuyue, quxiaoyuyue,id_)
        update_dict={
            "id":id_,
        }
        #加减数据
        if type_==1:#赞
            update_dict["thumbsupnum"]=int(rets[0].get('thumbsupnum'))+1
        elif type_==2:#踩
            update_dict["crazilynum"]=int(rets[0].get('crazilynum'))+1
        #更新记录
        error = quxiaoyuyue.updatebyparams(quxiaoyuyue, quxiaoyuyue, update_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return jsonify(msg)

# 获取详情信息（后端）
@main_bp.route("/pythonek97261k/quxiaoyuyue/info/<id_>", methods=['GET'])
def pythonek97261k_quxiaoyuyue_info(id_):
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        #根据id获取对应记录
        data = quxiaoyuyue.getbyid(quxiaoyuyue, quxiaoyuyue, int(id_))
        if len(data)>0:
            msg['data']=data[0]
        #浏览点击次数
        try:
            __browseClick__= quxiaoyuyue.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__  and  "clicknum"  in quxiaoyuyue.__table__.columns:
            click_dict={"id":int(id_),"clicknum":str(int(data[0].get("clicknum") or 0)+1)}#增加点击次数
            ret=quxiaoyuyue.updatebyparams(quxiaoyuyue,quxiaoyuyue,click_dict)#更新记录
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return jsonify(msg)

# 获取详情信息（前端）
@main_bp.route("/pythonek97261k/quxiaoyuyue/detail/<id_>", methods=['GET'])
def pythonek97261k_quxiaoyuyue_detail(id_):
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        #根据id获取对应记录
        data = quxiaoyuyue.getbyid(quxiaoyuyue, quxiaoyuyue, int(id_))
        if len(data)>0:
            msg['data']=data[0]

        #浏览点击次数
        try:
            __browseClick__= quxiaoyuyue.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__ and "clicknum" in quxiaoyuyue.__table__.columns:
            click_dict={"id":int(id_),"clicknum":str(int(data[0].get("clicknum") or 0)+1)}#增加点击次数
            ret=quxiaoyuyue.updatebyparams(quxiaoyuyue,quxiaoyuyue,click_dict)#更新记录
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return jsonify(msg)

# 更新接口
@main_bp.route("/pythonek97261k/quxiaoyuyue/update", methods=['POST'])
def pythonek97261k_quxiaoyuyue_update():
    request.operation = "更新取消预约"#填充日志内容
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        #如果存在密码或点击次数则不更新
        if req_dict.get("mima") and "mima" not in quxiaoyuyue.__table__.columns :
            del req_dict["mima"]
        if req_dict.get("password") and "password" not in quxiaoyuyue.__table__.columns :
            del req_dict["password"]
        try:
            del req_dict["clicknum"]
        except:
            pass

        #更新记录
        error = quxiaoyuyue.updatebyparams(quxiaoyuyue, quxiaoyuyue, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error

        return jsonify(msg)

# 删除接口
@main_bp.route("/pythonek97261k/quxiaoyuyue/delete", methods=['POST'])
def pythonek97261k_quxiaoyuyue_delete():
    request.operation = "删除取消预约"#更新日志记录
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        #删除记录
        error=quxiaoyuyue.delete(
            quxiaoyuyue,
            req_dict
        )
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return jsonify(msg)

# 投票接口
@main_bp.route("/pythonek97261k/quxiaoyuyue/vote/<int:id_>", methods=['POST'])
def pythonek97261k_quxiaoyuyue_vote(id_):
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success"}
        #根据id获取记录
        data= quxiaoyuyue.getbyid(quxiaoyuyue, quxiaoyuyue, int(id_))
        for i in data:
            #增加投票数并更新记录
            votenum=i.get('votenum')
            if votenum!=None:
                params={"id":int(id_),"votenum":votenum+1}
                error=quxiaoyuyue.updatebyparams(quxiaoyuyue,quxiaoyuyue,params)
                if error!=None:
                    msg['code'] = crud_error_code
                    msg['msg'] = error
        return jsonify(msg)




#获取所有记录列表
@main_bp.route("/pythonek97261k/quxiaoyuyue/lists", methods=['GET'])
def pythonek97261k_quxiaoyuyue_lists():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": []}
        list,_,_,_,_ = quxiaoyuyue.page(quxiaoyuyue,quxiaoyuyue,{})
        msg['data'] = list
        return jsonify(msg)

