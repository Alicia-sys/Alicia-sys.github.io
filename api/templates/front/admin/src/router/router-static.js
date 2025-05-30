import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
	import news from '@/views/modules/news/list'
	import aboutus from '@/views/modules/aboutus/list'
	import quxiaoyuyue from '@/views/modules/quxiaoyuyue/list'
	import yonghu from '@/views/modules/yonghu/list'
	import shiyanshi from '@/views/modules/shiyanshi/list'
	import kaoqinjilu from '@/views/modules/kaoqinjilu/list'
	import syslog from '@/views/modules/syslog/list'
	import yuyueshiyanshi from '@/views/modules/yuyueshiyanshi/list'
	import config from '@/views/modules/config/list'
	import shiyanshifenlei from '@/views/modules/shiyanshifenlei/list'
	import discussshiyanshi from '@/views/modules/discussshiyanshi/list'
	import newstype from '@/views/modules/newstype/list'


//2.配置路由   注意：名字
export const routes = [{
	path: '/',
	name: '系统首页',
	component: Index,
	children: [{
		// 这里不设置值，是把main作为默认页面
		path: '/',
		name: '系统首页',
		component: Home,
		meta: {icon:'', title:'center', affix: true}
	}, {
		path: '/updatePassword',
		name: '修改密码',
		component: UpdatePassword,
		meta: {icon:'', title:'updatePassword'}
	}, {
		path: '/pay',
		name: '支付',
		component: pay,
		meta: {icon:'', title:'pay'}
	}, {
		path: '/center',
		name: '个人信息',
		component: center,
		meta: {icon:'', title:'center'}
	}
	,{
		path: '/news',
		name: '公告信息',
		component: news
	}
	,{
		path: '/aboutus',
		name: '关于我们',
		component: aboutus
	}
	,{
		path: '/quxiaoyuyue',
		name: '取消预约',
		component: quxiaoyuyue
	}
	,{
		path: '/yonghu',
		name: '用户',
		component: yonghu
	}
	,{
		path: '/shiyanshi',
		name: '实验室',
		component: shiyanshi
	}
	,{
		path: '/kaoqinjilu',
		name: '考勤记录',
		component: kaoqinjilu
	}
	,{
		path: '/syslog',
		name: '系统日志',
		component: syslog
	}
	,{
		path: '/yuyueshiyanshi',
		name: '预约实验室',
		component: yuyueshiyanshi
	}
	,{
		path: '/config',
		name: '轮播图管理',
		component: config
	}
	,{
		path: '/shiyanshifenlei',
		name: '实验室分类',
		component: shiyanshifenlei
	}
	,{
		path: '/discussshiyanshi',
		name: '实验室评论',
		component: discussshiyanshi
	}
	,{
		path: '/newstype',
		name: '公告信息分类',
		component: newstype
	}
	]
	},
	{
		path: '/login',
		name: 'login',
		component: Login,
		meta: {icon:'', title:'login'}
	},
	{
		path: '/register',
		name: 'register',
		component: register,
		meta: {icon:'', title:'register'}
	},
	{
		path: '*',
		component: NotFound
	}
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
	mode: 'hash',
	/*hash模式改为history*/
	routes // （缩写）相当于 routes: routes
})
const originalPush = VueRouter.prototype.push
//修改原型对象中的push方法
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}
export default router;
