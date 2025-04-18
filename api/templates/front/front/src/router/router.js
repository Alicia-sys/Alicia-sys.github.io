import VueRouter from 'vue-router'
//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Storeup from '../pages/storeup/list'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import payList from '../pages/pay'

import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import shiyanshifenleiList from '../pages/shiyanshifenlei/list'
import shiyanshifenleiDetail from '../pages/shiyanshifenlei/detail'
import shiyanshifenleiAdd from '../pages/shiyanshifenlei/add'
import shiyanshiList from '../pages/shiyanshi/list'
import shiyanshiDetail from '../pages/shiyanshi/detail'
import shiyanshiAdd from '../pages/shiyanshi/add'
import yuyueshiyanshiList from '../pages/yuyueshiyanshi/list'
import yuyueshiyanshiDetail from '../pages/yuyueshiyanshi/detail'
import yuyueshiyanshiAdd from '../pages/yuyueshiyanshi/add'
import quxiaoyuyueList from '../pages/quxiaoyuyue/list'
import quxiaoyuyueDetail from '../pages/quxiaoyuyue/detail'
import quxiaoyuyueAdd from '../pages/quxiaoyuyue/add'
import kaoqinjiluList from '../pages/kaoqinjilu/list'
import kaoqinjiluDetail from '../pages/kaoqinjilu/detail'
import kaoqinjiluAdd from '../pages/kaoqinjilu/add'
import syslogList from '../pages/syslog/list'
import syslogDetail from '../pages/syslog/detail'
import syslogAdd from '../pages/syslog/add'
import newstypeList from '../pages/newstype/list'
import newstypeDetail from '../pages/newstype/detail'
import newstypeAdd from '../pages/newstype/add'
import aboutusList from '../pages/aboutus/list'
import aboutusDetail from '../pages/aboutus/detail'
import aboutusAdd from '../pages/aboutus/add'
import discussshiyanshiList from '../pages/discussshiyanshi/list'
import discussshiyanshiDetail from '../pages/discussshiyanshi/detail'
import discussshiyanshiAdd from '../pages/discussshiyanshi/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'pay',
					component: payList,
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'shiyanshifenlei',
					component: shiyanshifenleiList
				},
				{
					path: 'shiyanshifenleiDetail',
					component: shiyanshifenleiDetail
				},
				{
					path: 'shiyanshifenleiAdd',
					component: shiyanshifenleiAdd
				},
				{
					path: 'shiyanshi',
					component: shiyanshiList
				},
				{
					path: 'shiyanshiDetail',
					component: shiyanshiDetail
				},
				{
					path: 'shiyanshiAdd',
					component: shiyanshiAdd
				},
				{
					path: 'yuyueshiyanshi',
					component: yuyueshiyanshiList
				},
				{
					path: 'yuyueshiyanshiDetail',
					component: yuyueshiyanshiDetail
				},
				{
					path: 'yuyueshiyanshiAdd',
					component: yuyueshiyanshiAdd
				},
				{
					path: 'quxiaoyuyue',
					component: quxiaoyuyueList
				},
				{
					path: 'quxiaoyuyueDetail',
					component: quxiaoyuyueDetail
				},
				{
					path: 'quxiaoyuyueAdd',
					component: quxiaoyuyueAdd
				},
				{
					path: 'kaoqinjilu',
					component: kaoqinjiluList
				},
				{
					path: 'kaoqinjiluDetail',
					component: kaoqinjiluDetail
				},
				{
					path: 'kaoqinjiluAdd',
					component: kaoqinjiluAdd
				},
				{
					path: 'syslog',
					component: syslogList
				},
				{
					path: 'syslogDetail',
					component: syslogDetail
				},
				{
					path: 'syslogAdd',
					component: syslogAdd
				},
				{
					path: 'newstype',
					component: newstypeList
				},
				{
					path: 'newstypeDetail',
					component: newstypeDetail
				},
				{
					path: 'newstypeAdd',
					component: newstypeAdd
				},
				{
					path: 'aboutus',
					component: aboutusList
				},
				{
					path: 'aboutusDetail',
					component: aboutusDetail
				},
				{
					path: 'aboutusAdd',
					component: aboutusAdd
				},
				{
					path: 'discussshiyanshi',
					component: discussshiyanshiList
				},
				{
					path: 'discussshiyanshiDetail',
					component: discussshiyanshiDetail
				},
				{
					path: 'discussshiyanshiAdd',
					component: discussshiyanshiAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
