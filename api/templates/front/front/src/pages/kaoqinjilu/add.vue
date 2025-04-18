<template>
	<div class="add-update-preview">
		<el-form
			class="add-update-form"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="180px"
			>
			<el-form-item class="add-item" label="实验室编号" prop="shiyanshibianhao">
				<el-input v-model="ruleForm.shiyanshibianhao" 
					placeholder="实验室编号" clearable :disabled=" false  ||ro.shiyanshibianhao"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="实验室名称" prop="shiyanshimingcheng">
				<el-input v-model="ruleForm.shiyanshimingcheng" 
					placeholder="实验室名称" clearable :disabled=" false  ||ro.shiyanshimingcheng"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="实验室分类" prop="shiyanshifenlei">
				<el-input v-model="ruleForm.shiyanshifenlei" 
					placeholder="实验室分类" clearable :disabled=" false  ||ro.shiyanshifenlei"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="实验室规模" prop="shiyanshiguimo">
				<el-input v-model="ruleForm.shiyanshiguimo" 
					placeholder="实验室规模" clearable :disabled=" false  ||ro.shiyanshiguimo"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="头像" v-if="type!='cross' || (type=='cross' && !ro.touxiang)" prop="touxiang">
				<img class="upload-img" v-if="ruleForm.touxiang" :src="ruleForm.touxiang?baseUrl + ruleForm.touxiang:''">
				<div class="faceBtn" @click="imgAddClick">人脸识别</div>
			</el-form-item>
			<el-form-item class="add-item" v-else label="头像" prop="touxiang">
				<img v-if="ruleForm.touxiang.substring(0,4)=='http'" class="upload-img" v-bind:key="index" :src="ruleForm.touxiang.split(',')[0]">
				<img v-else class="upload-img" v-bind:key="index" v-for="(item,index) in ruleForm.touxiang.split(',')" :src="baseUrl+item">
			</el-form-item>
			<el-form-item class="add-item" label="签到时间" prop="qiandaoshijian">
				<el-date-picker
					:disabled=" false  ||ro.qiandaoshijian"
					value-format="yyyy-MM-dd HH:mm:ss"
					v-model="ruleForm.qiandaoshijian" 
					type="datetime"
					placeholder="签到时间">
				</el-date-picker>
			</el-form-item>
			<el-form-item class="add-item" label="用户账号" prop="yonghuzhanghao">
				<el-input v-model="ruleForm.yonghuzhanghao" 
					placeholder="用户账号" clearable :disabled=" false  ||ro.yonghuzhanghao"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="用户姓名" prop="yonghuxingming">
				<el-input v-model="ruleForm.yonghuxingming" 
					placeholder="用户姓名" clearable :disabled=" false  ||ro.yonghuxingming"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="用户类型" prop="yonghuleixing">
				<el-input v-model="ruleForm.yonghuleixing" 
					placeholder="用户类型" clearable :disabled=" false  ||ro.yonghuleixing"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="签到备注" prop="qiandaobeizhu">
				<el-input
					type="textarea"
					:rows="8"
					placeholder="签到备注"
					v-model="ruleForm.qiandaobeizhu">
					</el-input>
			</el-form-item>

			<el-form-item class="add-btn-item">
				<el-button class="submitBtn" v-if="!faceMatchFlag" type="primary" @click="onSubmit">
					<span class="icon iconfont icon-renlian07"></span>
					<span class="text">人脸校验</span>
				</el-button>
				<el-button class="submitBtn" v-if="faceMatchFlag" type="primary" @click="onSubmit">
					<span class="icon iconfont "></span>
					<span class="text">提交</span>
				</el-button>
				<el-button class="closeBtn" @click="back()">
					<span class="icon iconfont "></span>
					<span class="text">取消</span>
				</el-button>
			</el-form-item>
		</el-form>
		<imgAdd ref="imgAdd" @imgChange="imgChange"></imgAdd>
	</div>
</template>

<script>
import imgAdd from "@/components/img";
	export default {
		data() {
			return {
				id: '',
				baseUrl: '',
				ro:{
					shiyanshibianhao : false,
					shiyanshimingcheng : false,
					shiyanshifenlei : false,
					shiyanshiguimo : false,
					touxiang : false,
					qiandaoshijian : false,
					qiandaobeizhu : false,
					yonghuzhanghao : false,
					yonghuxingming : false,
					yonghuleixing : false,
				},
				type: '',
				userface : '',
				faceMatchFlag: false,
				userTableName: localStorage.getItem('UserTableName'),
				ruleForm: {
					shiyanshibianhao: '',
					shiyanshimingcheng: '',
					shiyanshifenlei: '',
					shiyanshiguimo: '',
					touxiang: '',
					qiandaoshijian: '',
					qiandaobeizhu: '',
					yonghuzhanghao: '',
					yonghuxingming: '',
					yonghuleixing: '',
				},


				rules: {
					shiyanshibianhao: [
					],
					shiyanshimingcheng: [
					],
					shiyanshifenlei: [
					],
					shiyanshiguimo: [
					],
					touxiang: [
					],
					qiandaoshijian: [
					],
					qiandaobeizhu: [
					],
					yonghuzhanghao: [
					],
					yonghuxingming: [
					],
					yonghuleixing: [
					],
				},
				centerType: false,
			};
		},
		computed: {



		},
		components: {
			imgAdd
		},
		created() {
			if(this.$route.query.centerType){
				this.centerType = true
			}
			//this.bg();
			let type = this.$route.query.type ? this.$route.query.type : '';
			this.init(type);
			this.baseUrl = this.$config.baseUrl;
			this.ruleForm.qiandaoshijian = this.getCurDateTime()
		},
		methods: {
			getMakeZero(s) {
				return s < 10 ? '0' + s : s;
			},
			imgAddClick(){
				this.$refs.imgAdd.onTake()
			},
			imgChange(e){
				this.ruleForm.touxiang = 'upload/' + e
			},
			// 下载
			download(file){
				window.open(`${file}`)
			},
			// 初始化
			init(type) {
				this.type = type;
				if(type=='cross'){
					var obj = JSON.parse(localStorage.getItem('crossObj'));
					for (var o in obj){
						if(o=='shiyanshibianhao'){
							this.ruleForm.shiyanshibianhao = obj[o];
							this.ro.shiyanshibianhao = true;
							continue;
						}
						if(o=='shiyanshimingcheng'){
							this.ruleForm.shiyanshimingcheng = obj[o];
							this.ro.shiyanshimingcheng = true;
							continue;
						}
						if(o=='shiyanshifenlei'){
							this.ruleForm.shiyanshifenlei = obj[o];
							this.ro.shiyanshifenlei = true;
							continue;
						}
						if(o=='shiyanshiguimo'){
							this.ruleForm.shiyanshiguimo = obj[o];
							this.ro.shiyanshiguimo = true;
							continue;
						}
						if(o=='touxiang'){
							this.ruleForm.touxiang = obj[o].split(",")[0];
							this.ro.touxiang = true;
							continue;
						}
						if(o=='qiandaoshijian'){
							this.ruleForm.qiandaoshijian = obj[o];
							this.ro.qiandaoshijian = true;
							continue;
						}
						if(o=='qiandaobeizhu'){
							this.ruleForm.qiandaobeizhu = obj[o];
							this.ro.qiandaobeizhu = true;
							continue;
						}
						if(o=='yonghuzhanghao'){
							this.ruleForm.yonghuzhanghao = obj[o];
							this.ro.yonghuzhanghao = true;
							continue;
						}
						if(o=='yonghuxingming'){
							this.ruleForm.yonghuxingming = obj[o];
							this.ro.yonghuxingming = true;
							continue;
						}
						if(o=='yonghuleixing'){
							this.ruleForm.yonghuleixing = obj[o];
							this.ro.yonghuleixing = true;
							continue;
						}
					}
				}else if(type=='edit'){
					this.info()
				}
				// 获取用户信息
				this.$http.get(this.userTableName + '/session', {emulateJSON: true}).then(res => {
					if (res.data.code == 0) {
						var json = res.data.data;
						this.userface = res.data.data.touxiang;
						if((json.yonghuzhanghao!=''&&json.yonghuzhanghao) || json.yonghuzhanghao==0){
							this.ruleForm.yonghuzhanghao = json.yonghuzhanghao;
							this.ro.yonghuzhanghao = true;
						}
						if((json.yonghuxingming!=''&&json.yonghuxingming) || json.yonghuxingming==0){
							this.ruleForm.yonghuxingming = json.yonghuxingming;
							this.ro.yonghuxingming = true;
						}
						if((json.yonghuleixing!=''&&json.yonghuleixing) || json.yonghuleixing==0){
							this.ruleForm.yonghuleixing = json.yonghuleixing;
							this.ro.yonghuleixing = true;
						}
					}
				});

				if (localStorage.getItem('raffleType') && localStorage.getItem('raffleType') != null) {
					localStorage.removeItem('raffleType')
					setTimeout(() => {
						this.onSubmit()
					}, 300)
				}
			},

			// 多级联动参数
			// 多级联动参数
			info() {
				this.$http.get(`kaoqinjilu/detail/${this.$route.query.id}`, {emulateJSON: true}).then(res => {
					if (res.data.code == 0) {
						this.ruleForm = res.data.data;
					}
				});
			},
			// 提交
			async onSubmit() {
				if(!this.faceMatchFlag) {
					//人脸校验
					if(!this.ruleForm.touxiang) {
						this.$message({
						  message: "请上传人脸图片",
						  type: 'error',
						  duration: 1500
						});
						return;
					}
					if(this.ruleForm.touxiang!=null) {
						this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$config.baseUrl,"g"),"");
					}
					let params = {
						face1:this.userface.replace("upload/",""),
						face2:this.ruleForm.touxiang.replace("upload/",""),
					}
					this.$http.get('matchFace', {params: params}).then(res => {
						if (res.data && res.data.code == 0) {
							if(res.data.score>60) {
								this.faceMatchFlag = true;
								this.$message({
									message: "匹配成功",
									type: "success",
									duration: 1500,
								});
							} else {
								this.faceMatchFlag = false;
								this.$message.error("匹配失败");
								return;
							}
						} else {
							this.faceMatchFlag = false;
							this.$message.error("匹配失败");
							return;
						}
					});
					return;
				}
				await this.$refs["ruleForm"].validate(async valid => {
					if(valid) {
						if(this.type=='cross'){
							var statusColumnName = localStorage.getItem('statusColumnName');
							var statusColumnValue = localStorage.getItem('statusColumnValue');
							if(statusColumnName && statusColumnName!='') {
								var obj = JSON.parse(localStorage.getItem('crossObj'));
								if(!statusColumnName.startsWith("[")) {
									for (var o in obj){
										if(o==statusColumnName){
											obj[o] = statusColumnValue;
										}
									}
									var table = localStorage.getItem('crossTable');
									await this.$http.post(table+'/update', obj).then(res => {});
								}
							}
						}


						await this.$http.post(`kaoqinjilu/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(async res => {
							if (res.data.code == 0) {
								this.$message({
									message: '操作成功',
									type: 'success',
									duration: 1500,
									onClose: () => {
										this.$router.go(-1);
										
									}
								});
							} else {
								this.$message({
									message: res.data.msg,
									type: 'error',
									duration: 1500
								});
							}
						});
					}
				});
			},
			// 获取uuid
			getUUID () {
				return new Date().getTime();
			},
			// 返回
			back() {
				this.$router.go(-1);
			},
			touxiangUploadChange(fileUrls) {
				this.ruleForm.touxiang = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
			},
		}
	};
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.add-update-preview {
		padding: 0 0 20px;
		margin: 0px auto;
		color: #666;
		background: #f6f6f6;
		width: 1400px;
		font-size: 16px;
		position: relative;
		.add-update-form {
			border: 0px solid #fcbb78;
			padding: 20px;
			margin: 20px 0;
			background: #fff;
			width: 100%;
			position: relative;
			.add-item.el-form-item {
				border-radius: 0px;
				padding: 6px 0 0;
				margin: 0 0 20px 0;
				background: none;
				border-color: #475a8310;
				border-width:  0 0 0px;
				border-style: solid;
				/deep/ .el-form-item__label {
					padding: 0 10px 0 0;
					color: #666;
					font-weight: 500;
					width: 180px;
					font-size: inherit;
					line-height: 40px;
					text-align: right;
				}
				/deep/ .el-form-item__content {
					margin-left: 180px;
				}
				.el-input {
					width: auto;
				}
				.el-input /deep/ .el-input__inner {
					border: 1px solid #ddd;
					border-radius: 4px;
					padding: 0 12px;
					box-shadow: none;
					color: inherit;
					width: auto;
					font-size: 16px;
					height: 40px;
				}
				.el-input /deep/ .el-input__inner[readonly="readonly"] {
					border: 0;
					cursor: not-allowed;
					border-radius: 0px;
					padding: 0 12px;
					box-shadow: none;
					color: rgba(85, 85, 127, 1.0);
					background: none;
					width: auto;
					font-size: 16px;
					height: 40px;
				}
				.el-input-number /deep/ .el-input__inner {
					text-align: left;
					border: 1px solid #ddd;
					border-radius: 4px;
					padding: 0 12px;
					box-shadow: none;
					color: inherit;
					width: auto;
					font-size: 16px;
					height: 40px;
				}
				.el-input-number /deep/ .is-disabled .el-input__inner {
					text-align: left;
					border: 0;
					cursor: not-allowed;
					border-radius: 0px;
					padding: 0 12px;
					box-shadow: none;
					color: rgba(85, 85, 127, 1.0);
					background: none;
					width: auto;
					font-size: 16px;
					height: 40px;
				}
				.el-input-number /deep/ .el-input-number__decrease {
					display: none;
				}
				.el-input-number /deep/ .el-input-number__increase {
					display: none;
				}
				.el-select {
					width: auto;
				}
				.el-select /deep/ .el-input__inner {
					border: 1px solid #ddd;
					border-radius: 4px;
					padding: 0 10px;
					color: inherit;
					width: 100%;
					font-size: 16px;
					min-width: inherit !important;
					height: 40px;
				}
				.el-select /deep/ .is-disabled .el-input__inner {
					border: 0;
					cursor: not-allowed;
					border-radius: 0px;
					padding: 0 10px;
					box-shadow: none;
					color: inherit;
					background: none;
					width: 100%;
					font-size: 16px;
					height: 40px;
				}
				.el-date-editor {
					width: auto;
				}
				.el-date-editor /deep/ .el-input__inner {
					border: 1px solid #ddd;
					border-radius: 4px;
					padding: 0 10px 0 30px;
					box-shadow: none;
					color: inherit;
					width: auto;
					font-size: 16px;
					height: 40px;
				}
				.el-date-editor /deep/ .el-input__inner[readonly="readonly"] {
					border: 0;
					cursor: not-allowed;
					border-radius: 0px;
					padding: 0 10px 0 30px;
					box-shadow: none;
					color: inherit;
					background: none;
					width: auto;
					font-size: 16px;
					height: 40px;
				}
				/deep/ .el-upload--picture-card {
					background: transparent;
					border: 0;
					border-radius: 0;
					width: auto;
					height: auto;
					line-height: initial;
					vertical-align: middle;
				}
				/deep/ .upload .upload-img {
					border: 1px solid #ddd;
					cursor: pointer;
					border-radius: 4px;
					color: #999;
					background: #fff;
					width: 80px;
					font-size: 26px;
					line-height: 60px;
					text-align: center;
					height: 60px;
				}
				/deep/ .el-upload-list .el-upload-list__item {
					border: 1px solid #ddd;
					cursor: pointer;
					border-radius: 4px;
					color: #999;
					background: #fff;
					width: 80px;
					font-size: 26px;
					line-height: 60px;
					text-align: center;
					height: 60px;
					font-size: 14px;
					line-height: 1.8;
				}
				/deep/ .el-upload .el-icon-plus {
					border: 1px solid #ddd;
					cursor: pointer;
					border-radius: 4px;
					color: #999;
					background: #fff;
					width: 80px;
					font-size: 26px;
					line-height: 60px;
					text-align: center;
					height: 60px;
				}
				/deep/ .el-upload__tip {
					color: #888;
					font-size: 16px;
				}
				.el-textarea /deep/ .el-textarea__inner {
					border: 1px solid #ddd;
					border-radius: 4px;
					padding: 12px;
					box-shadow: none;
					color: inherit;
					width: auto;
					font-size: 16px;
					min-height: 150px;
					min-width: 48%;
					height: auto;
				}
				.el-textarea /deep/ .el-textarea__inner[readonly="readonly"] {
					border: 0px solid #ddd;
					cursor: not-allowed;
					border-radius: 0px;
					padding: 12px;
					box-shadow: none;
					color: inherit;
					background: none;
					width: auto;
					font-size: 16px;
					min-height: 150px;
					min-width: 50%;
					height: auto;
				}
				/deep/ .el-input__inner::placeholder {
					color: inherit;
					font-size: inherit;
				}
				/deep/ textarea::placeholder {
					color: inherit;
					font-size: inherit;
				}
				.editor {
					background-color: #fff;
					border-radius: 0;
					padding: 0;
					box-shadow: none;
					margin: 0;
					width: 100%;
					min-height: 350px;
					border-color: #ccc;
					border-width: 1px;
					border-style: solid;
					height: auto;
				}
				.faceBtn {
					border: 0;
					cursor: pointer;
					border-radius: 4px;
					padding: 0 10px;
					margin: 0;
					color: #fff;
					background: #0674fc60;
					display: inline-block;
					width: auto;
					font-size: 16px;
					line-height: 34px;
					height: 34px;
				}
				.faceBtn:hover {
				}
				.upload-img {
					object-fit: cover;
					width: 100px;
					height: 100px;
				}
				.viewBtn {
					border: 0;
					cursor: pointer;
					border-radius: 4px;
					padding: 0 20px;
					margin: 0;
					color: #fff;
					background: #0674fc60;
					display: inline-block;
					width: auto;
					font-size: 14px;
					line-height: 34px;
					height: 34px;
				}
				.viewBtn:hover {
				}
				.unviewBtn {
					border: 0;
					cursor: pointer;
					padding: 0 20px;
					margin: 0;
					color: #333;
					display: inline-block;
					font-size: 14px;
					line-height: 34px;
					border-radius: 4px;
					outline: none;
					background: #eee;
					width: auto;
					height: 34px;
				}
				.unviewBtn:hover {
				}
			}
			.add-btn-item {
				padding: 0;
				margin: 20px 0;
				.submitBtn {
					border: 0;
					cursor: pointer;
					padding: 0 24px;
					margin: 0 20px 0 0;
					display: inline-block;
					font-size: 16px;
					line-height: 44px;
					border-radius: 4px;
					background: #0674fc;
					width: auto;
					text-align: center;
					min-width: 120px;
					height: 44px;
					.icon {
						color: #fff;
					}
					.text {
						color: #fff;
					}
				}
				.submitBtn:hover {
					.icon {
					}
					.text {
					}
				}
				.closeBtn {
					border: 0px solid #ddd;
					cursor: pointer;
					padding: 0 24px;
					margin: 0 20px 0 0;
					color: #fff;
					display: inline-block;
					font-size: 16px;
					line-height: 44px;
					border-radius: 4px;
					background: #858585;
					width: auto;
					text-align: center;
					min-width: 120px;
					height: 44px;
					.icon {
						color: #fff;
					}
					.text {
						color: #fff;
					}
				}
				.closeBtn:hover {
					.icon {
					}
					.text {
					}
				}
			}
		}
	}
	.el-date-editor.el-input {
		width: auto;
	}
</style>
