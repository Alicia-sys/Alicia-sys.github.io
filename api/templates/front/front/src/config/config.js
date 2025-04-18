export default {
	baseUrl: 'http://localhost:8080/pythonek97261k/',
	name: '/pythonek97261k',
	indexNav: [
		{
			name: '实验室',
			url: '/index/shiyanshi',
		},
		{
			name: '公告信息',
			url: '/index/news'
		},
	],
	cateList: [
		{
			name: '公告信息',
			refTable: 'newstype',
			refColumn: 'typename',
		},
	]
}
