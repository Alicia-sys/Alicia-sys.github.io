# coding:utf-8
import random
from datetime import datetime
from sqlalchemy import text,TIMESTAMP

from api.models.models import Base_model
from api.exts import db
from sqlalchemy.dialects.mysql import DOUBLE,LONGTEXT
# 个人信息
class yonghu(Base_model):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='是'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    yonghuzhanghao=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='用户账号' )
    yonghuxingming=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='用户姓名' )
    mima=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='密码' )
    shoujihaoma=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机号码' )
    xingbie=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='性别' )
    nianling=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='年龄' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    yonghuleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户类型' )

class shiyanshifenlei(Base_model):
    __doc__ = u'''shiyanshifenlei'''
    __tablename__ = 'shiyanshifenlei'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    shiyanshifenlei=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室分类' )

class shiyanshi(Base_model):
    __doc__ = u'''shiyanshi'''
    __tablename__ = 'shiyanshi'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='是'
    __browseClick__='是'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    shiyanshibianhao=db.Column( db.VARCHAR(255),  nullable=True,unique=True,comment='实验室编号' )
    shiyanshimingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室名称' )
    shiyanshifenlei=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室分类' )
    shiyanshiguimo=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室规模' )
    rongnarenshu=db.Column( db.Integer, default=0 ,  nullable=True, unique=False,comment='容纳人数' )
    anquandengji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='安全等级' )
    shiyanshizhuangtai=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室状态' )
    shiyanshitupian=db.Column( db.Text,  nullable=True, unique=False,comment='实验室图片' )
    shiyanshiweizhi=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室位置' )
    shiyanshixiangqing=db.Column( db.Text,  nullable=True, unique=False,comment='实验室详情' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    clicknum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='点击次数' )
    discussnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='评论数' )
    storeupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='收藏数' )

class yuyueshiyanshi(Base_model):
    __doc__ = u'''yuyueshiyanshi'''
    __tablename__ = 'yuyueshiyanshi'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    shiyanshibianhao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室编号' )
    shiyanshimingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室名称' )
    shiyanshifenlei=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室分类' )
    shiyanshiguimo=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室规模' )
    shiyanshitupian=db.Column( db.Text,  nullable=True, unique=False,comment='实验室图片' )
    yuyuebeizhu=db.Column( db.Text,  nullable=True, unique=False,comment='预约备注' )
    yonghuzhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户账号' )
    yonghuxingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户姓名' )
    yonghuleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户类型' )
    yuyueshijian=db.Column( db.Date,  nullable=True, unique=False,comment='预约时间' )
    sfsh=db.Column( db.VARCHAR(255),default='待审核', nullable=True, unique=False,comment='是否审核' )
    shhf=db.Column( db.Text,  nullable=True, unique=False,comment='审核回复' )

class quxiaoyuyue(Base_model):
    __doc__ = u'''quxiaoyuyue'''
    __tablename__ = 'quxiaoyuyue'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    shiyanshibianhao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室编号' )
    shiyanshimingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室名称' )
    shiyanshifenlei=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室分类' )
    shiyanshiguimo=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室规模' )
    shiyanshitupian=db.Column( db.Text,  nullable=True, unique=False,comment='实验室图片' )
    quxiaoyuanyin=db.Column( db.Text,  nullable=True, unique=False,comment='取消原因' )
    yonghuzhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户账号' )
    yonghuxingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户姓名' )
    yonghuleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户类型' )
    quxiaoshijian=db.Column( db.Date,  nullable=True, unique=False,comment='取消时间' )

class kaoqinjilu(Base_model):
    __doc__ = u'''kaoqinjilu'''
    __tablename__ = 'kaoqinjilu'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    shiyanshibianhao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室编号' )
    shiyanshimingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室名称' )
    shiyanshifenlei=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室分类' )
    shiyanshiguimo=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='实验室规模' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    qiandaoshijian=db.Column( db.DateTime,  nullable=True, unique=False,comment='签到时间' )
    qiandaobeizhu=db.Column( db.Text,  nullable=True, unique=False,comment='签到备注' )
    yonghuzhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户账号' )
    yonghuxingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户姓名' )
    yonghuleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户类型' )

class syslog(Base_model):
    __doc__ = u'''syslog'''
    __tablename__ = 'syslog'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    username=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='用户名' )
    operation=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='用户操作' )
    method=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='请求方法' )
    params=db.Column( db.Text,  nullable=True, unique=False,comment='请求参数' )
    time=db.Column( db.BigInteger, default=0 ,  nullable=True, unique=False,comment='请求时长(毫秒)' )
    ip=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='IP地址' )

class newstype(Base_model):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    typename=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='分类名称' )

class news(Base_model):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __thumbsUp__='是'
    __intelRecom__='是'
    __browseClick__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    introduction=db.Column( db.Text,  nullable=True, unique=False,comment='简介' )
    typename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='分类名称' )
    name=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='发布人' )
    headportrait=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    clicknum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='点击次数' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    thumbsupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='踩' )
    storeupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='收藏数' )
    picture=db.Column( db.Text, nullable=False, unique=False,comment='图片' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )

class storeup(Base_model):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='用户id' )
    refid=db.Column( db.BigInteger, default=0 ,  nullable=True, unique=False,comment='商品id' )
    tablename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='表名' )
    name=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='名称' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    type=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='类型' )
    inteltype=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='推荐类型' )
    remark=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='备注' )

class aboutus(Base_model):
    __doc__ = u'''aboutus'''
    __tablename__ = 'aboutus'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    subtitle=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='副标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )
    picture1=db.Column( db.Text,  nullable=True, unique=False,comment='图片1' )
    picture2=db.Column( db.Text,  nullable=True, unique=False,comment='图片2' )
    picture3=db.Column( db.Text,  nullable=True, unique=False,comment='图片3' )

class discussshiyanshi(Base_model):
    __doc__ = u'''discussshiyanshi'''
    __tablename__ = 'discussshiyanshi'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )
    thumbsupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='踩' )
    istop=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='置顶(1:置顶,0:非置顶)' )
    tuserids=db.Column( db.Text,  nullable=True, unique=False,comment='赞用户ids' )
    cuserids=db.Column( db.Text,  nullable=True, unique=False,comment='踩用户ids' )

