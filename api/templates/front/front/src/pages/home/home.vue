<template>
	<div class="home-preview">



		<!-- 关于我们 -->
		<div id="about" class="animate__animated">
			<div class="about_item">
				<div class="about_title_box">
					<div class="about_title">{{aboutUsDetail.title}}</div>
					<div class="about_subtitle">{{aboutUsDetail.subtitle}}</div>
				</div>
				<div class="about_img">
					<img :src="baseUrl + aboutUsDetail.picture1">
					<img :src="baseUrl + aboutUsDetail.picture2">
					<img :src="baseUrl + aboutUsDetail.picture3">
				</div>
				<div class="about_content ql-snow ql-editor" v-html="aboutUsDetail.content"></div>
				<div class="about_idea1" />
				<div class="about_idea2" />
				<div class="about_idea3" />
				<div class="about_idea4" />
				<div class="about_more" @click="toDetail('aboutusDetail',aboutUsDetail)">
					<span>查看更多</span>
					<span class="icon iconfont icon-jiantou25"></span>
				</div>
			</div>
		</div>
		<!-- 关于我们 -->

		<!-- 新闻资讯 -->
		<div id="animate_newsnews" class="news animate__animated">
			<div class="news_title_box">
				<span class="news_title">公告信息</span>
				<span class="news_subhead">{{'news'.toUpperCase()}}</span>
			</div>
			<div v-if="newsList.length" class="list list20 index-pv1">
				<div v-for="(item,index) in newsList" :key="index"  @click="toDetail('newsDetail', item)" class="list-item animation-box">
					<div class="img-box">
						<img :src="baseUrl + item.picture" class="image">
					</div>
					<div class="infoBox">
						<div class="infoBox-left">
							<div class="name">{{item.title}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{item.addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont icon-touxiang18"></span>
								<span class="label">发布人：</span>
								<span class="text">{{item.name}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{item.thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{item.storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-liulan13"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{item.clicknum}}</span>
							</div>
						</div>
						<div class="desc">{{item.introduction}}</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('news')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 新闻资讯 -->
		<!-- 商品推荐 -->
		<div id="animate_recommendshiyanshi" class="recommend animate__animated">
			<div class="recommend_title_box">
				<span class="recommend_title">实验室推荐</span>
				<span class="recommend_subhead">{{'shiyanshi'.toUpperCase()}} RECOMMEND</span>
			</div>
			<div class="list list18 index-pv1">
				<div class="list-body" v-if="shiyanshiRecommend.length">
					<div class="list-body-left">
						<div class="list-item1" @click="toDetail('shiyanshiDetail', shiyanshiRecommend[0])">
							<div class="infoBox">
								<div class="name">{{shiyanshiRecommend[0].shiyanshimingcheng}}</div>
								<div class="name">{{shiyanshiRecommend[0].shiyanshifenlei}}</div>
								<div class="time_item">
									<span class="icon iconfont icon-shijian21"></span>
									<span class="label">发布时间：</span>
									<span class="text">{{shiyanshiRecommend[0].addtime.split(' ')[0]}}</span>
								</div>
								<div class="collect_item">
									<span class="icon iconfont icon-shoucang10"></span>
									<span class="label">收藏：</span>
									<span class="text">{{shiyanshiRecommend[0].storeupnum}}</span>
								</div>
								<div class="view_item">
									<span class="icon iconfont icon-liulan04"></span>
									<span class="label">浏览次数：</span>
									<span class="text">{{shiyanshiRecommend[0].clicknum}}</span>
								</div>
							</div>
							<div class="img">
								<img v-if="preHttp(shiyanshiRecommend[0].shiyanshitupian)&&preHttp2(shiyanshiRecommend[0].shiyanshitupian)" :src="shiyanshiRecommend[0].shiyanshitupian" alt="" />
								<img v-else-if="preHttp(shiyanshiRecommend[0].shiyanshitupian)" :src="shiyanshiRecommend[0].shiyanshitupian.split(',')[0]" alt="" />
								<img v-else :src="baseUrl + (shiyanshiRecommend[0].shiyanshitupian?shiyanshiRecommend[0].shiyanshitupian.split(',')[0]:'')" alt="" />
							</div>
						</div>
						<div class="list-item2" @click="toDetail('shiyanshiDetail', shiyanshiRecommend[1])">
							<div class="img">
								<img v-if="preHttp(shiyanshiRecommend[1].shiyanshitupian)&&preHttp2(shiyanshiRecommend[1].shiyanshitupian)" :src="shiyanshiRecommend[1].shiyanshitupian" alt="" />
								<img v-else-if="preHttp(shiyanshiRecommend[1].shiyanshitupian)" :src="shiyanshiRecommend[1].shiyanshitupian.split(',')[0]" alt="" />
								<img v-else :src="baseUrl + (shiyanshiRecommend[1].shiyanshitupian?shiyanshiRecommend[1].shiyanshitupian.split(',')[0]:'')" alt="" />
							</div>
							<div class="infoBox">
								<div class="name">{{shiyanshiRecommend[1].shiyanshimingcheng}}</div>
								<div class="name">{{shiyanshiRecommend[1].shiyanshifenlei}}</div>
								<div class="time_item">
									<span class="icon iconfont icon-shijian21"></span>
									<span class="label">发布时间：</span>
									<span class="text">{{shiyanshiRecommend[1].addtime.split(' ')[0]}}</span>
								</div>
								<div class="collect_item">
									<span class="icon iconfont icon-shoucang10"></span>
									<span class="label">收藏：</span>
									<span class="text">{{shiyanshiRecommend[1].storeupnum}}</span>
								</div>
								<div class="view_item">
									<span class="icon iconfont icon-liulan04"></span>
									<span class="label">浏览次数：</span>
									<span class="text">{{shiyanshiRecommend[1].clicknum}}</span>
								</div>
							</div>
						</div>
					</div>
					<div class="list-body-right">
						<div class="swiper-container recommendSwiper18 recommend-list-18shiyanshi">
							<div class="swiper-wrapper">
								<div class="swiper-slide" v-for="(item,index) in shiyanshiRecommend" :key="index" v-if="index>2">
									<div class="list-item" @click="toDetail('shiyanshiDetail', item)">
										<div class="img">
											<img v-if="preHttp(item.shiyanshitupian)&&preHttp2(item.shiyanshitupian)" :src="item.shiyanshitupian" alt="" />
											<img v-else-if="preHttp(item.shiyanshitupian)" :src="item.shiyanshitupian.split(',')[0]" alt="" />
											<img v-else :src="baseUrl + (item.shiyanshitupian?item.shiyanshitupian.split(',')[0]:'')" alt="" />
										</div>
										<div class="infoBox">
											<div class="name">{{item.shiyanshimingcheng}}</div>
											<div class="name">{{item.shiyanshifenlei}}</div>
											<div class="time_item">
												<span class="icon iconfont icon-shijian21"></span>
												<span class="label">发布时间：</span>
												<span class="text">{{item.addtime.split(' ')[0]}}</span>
											</div>
											<div class="collect_item">
												<span class="icon iconfont icon-shoucang10"></span>
												<span class="label">收藏：</span>
												<span class="text">{{item.storeupnum}}</span>
											</div>
											<div class="view_item">
												<span class="icon iconfont icon-liulan04"></span>
												<span class="label">浏览次数：</span>
												<span class="text">{{item.clicknum}}</span>
											</div>
										</div>
									</div>
								</div>
							</div>
							<div class="swiper-button-prev"></div>
							<div class="swiper-button-next"></div>
							<div class="swiper-pagination"></div>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('shiyanshi')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 商品推荐 -->
	</div>
</template>

<script>
import 'animate.css'
import Swiper from "swiper";

	export default {
		//数据集合
		data() {
			return {
				baseUrl: '',
				aboutUsDetail: {},
				newsList: [],
				shiyanshiRecommend: [],



				recommendListSwiper18shiyanshi: null,


			}
		},
		created() {
			this.baseUrl = this.$config.baseUrl;
			this.getNewsList();
			this.getAboutUs();
			this.getList();
		},
		mounted() {
			window.addEventListener('scroll', this.handleScroll)
			setTimeout(()=>{
				this.handleScroll()
			},100)
			
			this.swiperChanges()
		},
		beforeDestroy() {
			window.removeEventListener('scroll', this.handleScroll)
		},
		//方法集合
		methods: {
			swiperChanges() {
				if (this['recommendListSwiper18shiyanshi']) this['recommendListSwiper18shiyanshi'].destroy()
				setTimeout(()=>{
					this['recommendListSwiper18shiyanshi'] = new Swiper(".recommend-list-18shiyanshi", {"navigation":{"nextEl":".swiper-button-next","prevEl":".swiper-button-prev"},"pagination":{"el":".swiper-pagination","clickable":true},"loop":true,"coverflowEffect":{"rotate":10,"stretch":10,"depth":60,"modifier":3,"slideShadows":false},"centeredSlides":true,"slidesPerView":1,"spaceBetween":0,"autoplay":{"delay":3000,"disableOnInteraction":false}})
				},750)
			},
			async recommendIndexClick18(index, name) {
				this['recommendIndex18' + name] = index
				await this.getList()
			},


			handleScroll() {
				let arr = [
					{id:'about',css:'animate__'},
					{id:'system',css:'animate__'},
					{id:'animate_recommendshiyanshi',css:'animate__'},
					{id:'animate_newsnews',css:'animate__'},
				]
			
				for (let i in arr) {
					let doc = document.getElementById(arr[i].id)
					if (doc) {
						let top = doc.offsetTop
						let win_top = window.innerHeight + window.pageYOffset
						// console.log(top,win_top)
						if (win_top > top && doc.classList.value.indexOf(arr[i].css) < 0) {
							// console.log(doc)
							doc.classList.add(arr[i].css)
						}
					}
				}
			},
			preHttp(str) {
				return str && str.substr(0,4)=='http';
			},
			preHttp2(str) {
				return str && str.split(',w').length>1;
			},
			getAboutUs() {
				this.$http.get('aboutus/detail/1', {}).then(res => {
					if(res.data.code == 0) {
						this.aboutUsDetail = res.data.data;
					}
				})
			},
			getNewsList() {
				let data = {
					page: 1,
					limit: 4,
					sort: 'addtime',
					order: 'desc'
				}
				this.$http.get('news/list', {params: data}).then(res => {
					if (res.data.code == 0) {
						this.newsList = res.data.data.list;
					
					}
				});
			},
			getList() {
				let autoSortUrl = "";
				let data = {}
				autoSortUrl = "shiyanshi/autoSort";
				data = {
					page: 1,
					limit: 8,
				}
				this.$http.get(autoSortUrl, {params: data}).then(res => {
					if (res.data.code == 0) {
						this.shiyanshiRecommend = res.data.data.list;
					}
				});
			
			},
			toDetail(path, item) {
				this.$router.push({path: '/index/' + path, query: {id: item.id}});
			},
			moreBtn(path) {
				this.$router.push({path: '/index/' + path});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.home-preview {
		margin: 0px auto;
		flex-direction: column;
		background: #fff;
		display: flex;
		width: 100%;
		#about {
			padding: 20px 0 0;
			margin: 0 auto;
			background: url(http://codegen.caihongy.cn/20241021/513dd95489604aa3bc858f69c015998d.jpg) no-repeat center top;
			width: 100%;
			height: auto;
			order: 1;
			.about_item {
				padding: 0;
				margin: 0px auto;
				z-index: 9;
				overflow: hidden;
				align-content: flex-start;
				background: none;
				display: flex;
				width: 1400px;
				position: relative;
				flex-wrap: wrap;
				height: 780px;
				.about_title_box {
					padding: 0;
					margin: 0;
					background: none;
					width: 100%;
					position: relative;
					text-align: left;
					.about_title {
						margin: 0 auto;
						color: #fff;
						background: none;
						font-weight: 500;
						display: inline-block;
						width: auto;
						font-size: 26px;
						border-color: #fff;
						border-width: 0 0 4px;
						line-height: 50px;
						border-style: solid;
						text-align: left;
					}
					.about_subtitle {
						margin: 0;
						color: #999;
						display: none;
						width: 100%;
						font-size: 18px;
						line-height: 40px;
						text-align: center;
					}
				}
				.about_img {
					padding: 0;
					margin: 0;
					background: none;
					display: flex;
					width: 100%;
					flex-wrap: wrap;
					height: 290px;
					order: 2;
					img:nth-child(1) {
						margin: 0;
						object-fit: cover;
						display: block;
						width: 33%;
						height: 100%;
					}
					img:nth-child(2) {
						margin: 0;
						object-fit: cover;
						display: block;
						width: 34%;
						height: 100%;
					}
					img:nth-child(3) {
						margin: 0;
						object-fit: cover;
						display: block;
						width: 33%;
						height: 100%;
					}
				}
				.about_content {
					padding: 0;
					margin: 20px 0;
					overflow: hidden;
					color: #fff;
					background: none;
					width: 100%;
					font-size: 16px;
					line-height: 30px;
					height: 210px;
				}
				.about_idea1 {
					z-index: -1;
					top: 0;
					background: #d10602;
					display: none;
					width: 50%;
					position: absolute;
					right: 0;
					height: 400px;
				}
				.about_idea2 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.about_idea3 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.about_idea4 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.about_more {
					border: 0px solid #999;
					padding: 0 20px;
					margin: 40px 0 0;
					background: #0673fa;
					display: block;
					width: 230px;
					line-height: 50px;
					text-align: center;
					order: 3;
					span:nth-child(1) {
						color: #fff;
						font-size: 18px;
					}
					span:nth-child(2) {
						color: #fff;
						font-size: 18px;
					}
				}
				.about_more:hover {
					cursor: pointer;
					opacity: 1;
				}
			}
		}
		.news {
			padding: 0;
			margin: 0;
			background: #e7f3ff;
			width: 100%;
			position: relative;
			order: 7;
			.news_title_box {
				padding: 60px calc((100% - 1400px)/2) 0;
				margin: 0;
				background: #fff;
				width: 100%;
				position: relative;
				text-align: left;
				height: 160px;
				.news_title {
					padding: 0 20px 0 103px;
					margin: 0;
					color: #fff;
					background: url(http://codegen.caihongy.cn/20241021/83b76ba643c24f378a5bfd58e665e1f9.png) no-repeat left center,#0674fc;
					font-weight: 600;
					display: inline-block;
					letter-spacing: 4px;
					width: auto;
					font-size: 32px;
					line-height: 100px;
					text-align: left;
					min-width: 300px;
				}
				.news_subhead {
					margin: 0;
					color: #999;
					display: none;
					width: 100%;
					font-size: 18px;
					line-height: 40px;
					text-align: center;
				}
			}
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list20 {
				padding: 80px 0 20px;
				margin: 0 auto;
				background: none;
				display: flex;
				width: 1400px;
				justify-content: space-between;
				flex-wrap: wrap;
				height: auto;
				.list-item {
					cursor: pointer;
					border: 2px solid #0674fc;
					border-radius: 8px;
					padding: 80px 20px 20px;
					margin: 0 0 60px;
					background: #fff;
					display: flex;
					width: 49%;
					position: relative;
					transition: all 0s;
					height: auto;
					.img-box {
						border: 1px solid #eee;
						padding: 10px;
						overflow: hidden;
						background: #fff;
						display: none;
						width: 200px;
						height: 200px;
						img {
							object-fit: cover;
							display: block;
							width: 100%;
							height: 100%;
						}
					}
					.infoBox {
						padding: 0;
						overflow: hidden;
						align-content: flex-start;
						flex: 1;
						display: flex;
						flex-wrap: wrap;
						height: auto;
						.infoBox-left {
							padding: 0;
							margin: 0;
							color: #0674fc;
							width: 100%;
							font-size: 14px;
							order: 2;
							.name {
								padding: 0;
								overflow: hidden;
								color: #333;
								top: 40px;
								white-space: nowrap;
								width: 93%;
								font-size: 15px;
								line-height: 40px;
								text-overflow: ellipsis;
								position: absolute;
							}
							.time_item {
								border-radius: 8px 8px 8px 0;
								padding: 10px;
								top: -20px;
								color: #fff;
								left: -2px;
								background: #0674fc;
								display: inline-block;
								position: absolute;
								.icon {
									margin: 0 2px 0 0;
									line-height: 28px;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.publisher_item {
								margin: 0 10px 0 0;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 28px;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 28px;
								}
							}
							.like_item {
								margin: 0 10px 0 0;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 28px;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 28px;
								}
							}
							.collect_item {
								margin: 0 10px 0 0;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 28px;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 28px;
								}
							}
							.view_item {
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 28px;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 28px;
								}
							}
						}
						.desc {
							margin: 0 0 10px;
							color: #868686;
							display: flex;
							width: 100%;
							font-size: 14px;
							line-height: 1.5;
							align-items: center;
							flex-wrap: wrap;
						}
					}
					
				}
				.list-item:hover {
					box-shadow: 1px 2px 6px #0674fc;
					.infoBox {
						.infoBox-left {
							.name {
							}
							.time_item {
								.icon {
								}
								.label {
								}
								.text {
								}
							}
							.publisher_item {
								.icon {
								}
								.label {
								}
								.text {
								}
							}
							.like_item {
								.icon {
								}
								.label {
								}
								.text {
								}
							}
							.collect_item {
								.icon {
								}
								.label {
								}
								.text {
								}
							}
							.view_item {
								.icon {
								}
								.label {
								}
								.text {
								}
							}
						}
						.desc {
						}
					}
				}
			}
			.moreBtn {
				border: 0px solid #999;
				cursor: pointer;
				padding: 0 20px;
				margin: 10px calc((100% - 1200px)/2)  0 0;
				background: rgba(255,255,255,.9);
				display: none;
				width: auto;
				line-height: 32px;
				float: right;
				text-align: center;
				.text {
					color: #333;
					font-size: 15px;
				}
				.icon {
					color: #333;
					font-size: 15px;
				}
			}
		}
		.recommend {
			padding: 60px 0 96px;
			margin: 0;
			align-content: flex-start;
			background: url(http://codegen.caihongy.cn/20241021/dc5560406d4146e1ada337e5a58f1599.jpg) no-repeat center bottom;
			display: flex;
			width: 100%;
			justify-content: center;
			align-items: flex-start;
			position: relative;
			order: 3;
			.recommend_title_box {
				padding: 20px 0 63px;
				margin: 0;
				background: url(http://codegen.caihongy.cn/20241021/84fcb60c88f446dd90bb6c22d0baf026.png) no-repeat center 102%,#0674fc;
				display: flex;
				width: 100px;
				min-height: 300px;
				position: relative;
				text-align: center;
				.recommend_title {
					margin: 0 auto;
					writing-mode: vertical-rl;
					color: #fff;
					background: none;
					font-weight: 600;
					display: block;
					letter-spacing: 8px;
					width: auto;
					font-size: 32px;
					line-height: 1;
					text-align: center;
				}
				.recommend_subhead {
					margin: 0;
					color: #999;
					display: none;
					width: 100%;
					font-size: 18px;
					line-height: 40px;
					text-align: center;
				}
			}
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list18 {
				padding: 50px 20px;
				margin: 0;
				color: #666;
				background: #fff;
				width: 1300px;
				font-size: 14px;
				.tab_view {
					margin: 10px auto;
					display: none;
					width: 60%;
					justify-content: center;
					.tab {
						cursor: pointer;
						border-radius: 5px;
						margin: 0 5px 10px;
						color: #333;
						background: #eee;
						display: block;
						width: 140px;
						font-size: 14px;
						line-height: 40px;
						text-align: center;
						height: 40px;
					}
					.tab:hover {
						color: #ddd;
						background: #0195df;
					}
					.tab.tabActive {
						color: #fff;
						background: #5555ff;
					}
				}
				.list-body {
					padding: 0 10px;
					display: flex;
					width: 100%;
					.list-body-left {
						margin: 0 auto 0 0;
						width: 49%;
						.list-item1 {
							display: flex;
							width: 100%;
							align-items: center;
							transition: all 0s;
							.infoBox {
								padding: 20px;
								color: #0674fc;
								align-content: center;
								display: flex;
								width: 50%;
								border-color: #929292;
								border-width: 1px 0 0 1px;
								align-items: center;
								border-style: solid;
								flex-wrap: wrap;
								height: 300px;
								.name {
									overflow: hidden;
									color: #000;
									white-space: nowrap;
									width: 100%;
									font-size: 16px;
									line-height: 1.5;
									text-overflow: ellipsis;
								}
								.price {
									padding: 10px 0;
									color: #f00;
									width: 100%;
									font-size: 16px;
									line-height: 1.5;
								}
								.time_item {
									padding: 0;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
								.publisher_item {
									padding: 0;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
								.like_item {
									padding: 0;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
								.collect_item {
									padding: 0;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
								.view_item {
									padding: 0;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
							}
							.img {
								overflow: hidden;
								width: 50%;
								transition: all .3s;
								height: 300px;
								img {
									transform: scale(1);
									object-fit: cover;
									display: block;
									width: 100%;
									transition: all .3s;
									height: 100%;
								}
							}
						}
						.list-item1:hover {
							cursor: pointer;
							transform: translate3d(0px, 0px, 0px);
							.infoBox {
								.name {
								}
								.price {
									color: #f00;
								}
								.time_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
								.publisher_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
								.like_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
								.collect_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
								.view_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
							}
							.img {
								overflow: hidden;
								img {
									transform: scale(1.05);
								}
							}
						}
						.list-item2 {
							display: flex;
							width: 100%;
							align-items: center;
							transition: all 0s;
							.img {
								overflow: hidden;
								width: 50%;
								transition: all .3s;
								height: 300px;
								img {
									transform: scale(1);
									object-fit: cover;
									display: block;
									width: 100%;
									transition: all .3s;
									height: 100%;
								}
							}
							.infoBox {
								padding: 20px;
								color: #0674fc;
								align-content: center;
								display: flex;
								width: 50%;
								border-color: #929292;
								border-width: 0 1px 1px 0;
								align-items: center;
								border-style: solid;
								flex-wrap: wrap;
								height: 300px;
								.name {
									overflow: hidden;
									color: #000;
									white-space: nowrap;
									width: 100%;
									font-size: 16px;
									line-height: 1.5;
									text-overflow: ellipsis;
								}
								.price {
									padding: 10px 0;
									color: #f00;
									width: 100%;
									font-size: 16px;
									line-height: 1.5;
								}
								.time_item {
									padding: 0;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
								.publisher_item {
									padding: 0;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
								.like_item {
									padding: 0;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
								.collect_item {
									padding: 0;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
								.view_item {
									padding: 0;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
							}
						}
						.list-item2:hover {
							cursor: pointer;
							transform: translate3d(0px, 0px, 0px);
							.img {
								overflow: hidden;
								img {
									transform: scale(1.2);
								}
							}
							.infoBox {
								.name {
								}
								.price {
								}
								.time_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
								.publisher_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
								.like_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
								.collect_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
								.view_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
							}
						}
					}
					.list-body-right {
						width: 49%;
						.list-item {
							width: 100%;
							position: relative;
							.img {
								width: 100%;
								height: 600px;
								img {
									cursor: pointer;
									transform: scale(1);
									object-fit: cover;
									display: block;
									width: 100%;
									transition: all .3s;
									height: 100%;
								}
							}
							.infoBox {
								padding: 10px 10px 30px;
								color: #0674fc;
								left: 0;
								bottom: 0;
								background: rgba(0, 0, 0, .3);
								width: 100%;
								font-size: 14px;
								position: absolute;
								.name {
									overflow: hidden;
									color: #fff;
									white-space: nowrap;
									width: 100%;
									font-size: 16px;
									line-height: 30px;
									text-overflow: ellipsis;
								}
								.price {
									padding: 0;
									color: #f00;
									font-size: 16px;
									line-height: 30px;
								}
								.time_item {
									padding: 0;
									margin: 0 10px 0 0;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
								.publisher_item {
									padding: 0;
									margin: 0 10px 0 0;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
								.like_item {
									padding: 0;
									margin: 0 10px 0 0;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
								.collect_item {
									padding: 0;
									margin: 0 10px 0 0;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
								.view_item {
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
							}
						}
						.swiper-button-prev {
							left: 10px;
							display: none;
							right: auto;
						}
						.swiper-button-prev::after {
							color: #d7b830;
						}
						.swiper-button-next {
							left: auto;
							display: none;
							right: 10px;
						}
						.swiper-button-next::after {
							color: #d7b830;
						}
						/deep/.swiper-pagination {
							transform: translate3d(0,0,0);
							z-index: 10;
							left: 0;
							bottom: 8px;
							width: 100%;
							position: absolute;
							transition: .3s opacity;
							text-align: center;
							.swiper-pagination-bullet {
								cursor: pointer;
								border-radius: 100%;
								margin: 0 4px;
								background: #f6f6f6;
								display: inline-block;
								width: 8px;
								opacity: .8;
								height: 8px;
							}
							.swiper-pagination-bullet:hover {
								background: #0674fc;
							}
							.swiper-pagination-bullet.swiper-pagination-bullet-active {
								background: #0674fc;
							}
						}
					}
				}
			}
			.moreBtn {
				border: 0px solid #999;
				cursor: pointer;
				padding: 0 20px;
				margin: 0px calc((100% - 1200px)/2)  0 0;
				background: #475a8310;
				display: none;
				width: auto;
				line-height: 32px;
				float: right;
				text-align: right;
				.text {
					color: #333;
					font-size: 15px;
				}
				.icon {
					color: #333;
					font-size: 15px;
				}
			}
		}
	}
</style>
