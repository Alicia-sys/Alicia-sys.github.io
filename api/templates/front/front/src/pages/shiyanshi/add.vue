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
			<el-form-item class="add-item"  label="实验室分类" prop="shiyanshifenlei">
				<el-select v-model="ruleForm.shiyanshifenlei" placeholder="请选择实验室分类" :disabled=" false  ||ro.shiyanshifenlei" >
					<el-option
						v-for="(item,index) in shiyanshifenleiOptions"
						:key="index"
						:label="item"
						:value="item">
					</el-option>
				</el-select>
			</el-form-item>
			<el-form-item class="add-item"  label="实验室规模" prop="shiyanshiguimo">
				<el-select v-model="ruleForm.shiyanshiguimo" placeholder="请选择实验室规模" :disabled=" false  ||ro.shiyanshiguimo" >
					<el-option
						v-for="(item,index) in shiyanshiguimoOptions"
						:key="index"
						:label="item"
						:value="item">
					</el-option>
				</el-select>
			</el-form-item>
			<el-form-item class="add-item" label="容纳人数" prop="rongnarenshu">
				<el-input v-model.number="ruleForm.rongnarenshu" 
					placeholder="容纳人数" clearable :disabled=" false  ||ro.rongnarenshu"></el-input>
			</el-form-item>
			<el-form-item class="add-item"  label="安全等级" prop="anquandengji">
				<el-select v-model="ruleForm.anquandengji" placeholder="请选择安全等级" :disabled=" false  ||ro.anquandengji" >
					<el-option
						v-for="(item,index) in anquandengjiOptions"
						:key="index"
						:label="item"
						:value="item">
					</el-option>
				</el-select>
			</el-form-item>
			<el-form-item class="add-item"  label="实验室状态" prop="shiyanshizhuangtai">
				<el-select v-model="ruleForm.shiyanshizhuangtai" placeholder="请选择实验室状态" :disabled="true  ||ro.shiyanshizhuangtai" >
					<el-option
						v-for="(item,index) in shiyanshizhuangtaiOptions"
						:key="index"
						:label="item"
						:value="item">
					</el-option>
				</el-select>
			</el-form-item>
			<el-form-item class="add-item" label="实验室图片" v-if="type!='cross' || (type=='cross' && !ro.shiyanshitupian)" prop="shiyanshitupian">
				<file-upload
					tip="点击上传实验室图片"
					action="file/upload"
					:limit="3"
					:multiple="true"
					:fileUrls="ruleForm.shiyanshitupian?ruleForm.shiyanshitupian:''"
					@change="shiyanshitupianUploadChange"
					></file-upload>
			</el-form-item>
			<el-form-item class="add-item" v-else label="实验室图片" prop="shiyanshitupian">
				<img v-if="ruleForm.shiyanshitupian.substring(0,4)=='http'" class="upload-img" v-bind:key="index" :src="ruleForm.shiyanshitupian.split(',')[0]">
				<img v-else class="upload-img" v-bind:key="index" v-for="(item,index) in ruleForm.shiyanshitupian.split(',')" :src="baseUrl+item">
			</el-form-item>
			<el-form-item class="add-item" label="实验室位置" prop="shiyanshiweizhi">
				<el-input v-model="ruleForm.shiyanshiweizhi" 
					placeholder="实验室位置" clearable :disabled=" false  ||ro.shiyanshiweizhi"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="实验室详情" prop="shiyanshixiangqing">
				<editor 
					v-model="ruleForm.shiyanshixiangqing" 
					class="editor" 
					action="file/upload">
				</editor>
			</el-form-item>

			<el-form-item class="add-btn-item">
				<el-button class="submitBtn"  type="primary" @click="onSubmit">
					<span class="icon iconfont "></span>
					<span class="text">提交</span>
				</el-button>
				<el-button class="closeBtn" @click="back()">
					<span class="icon iconfont "></span>
					<span class="text">取消</span>
				</el-button>
			</el-form-item>
		</el-form>
	</div>
</template>

<script>
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
					rongnarenshu : false,
					anquandengji : false,
					shiyanshizhuangtai : false,
					shiyanshitupian : false,
					shiyanshiweizhi : false,
					shiyanshixiangqing : false,
					clicktime : false,
					clicknum : false,
					discussnum : false,
					storeupnum : false,
				},
				type: '',
				userTableName: localStorage.getItem('UserTableName'),
				ruleForm: {
					shiyanshibianhao: '',
					shiyanshimingcheng: '',
					shiyanshifenlei: '',
					shiyanshiguimo: '',
					rongnarenshu: '',
					anquandengji: '',
					shiyanshizhuangtai: '空闲中' ,
					shiyanshitupian: '',
					shiyanshiweizhi: '',
					shiyanshixiangqing: '',
					clicktime: '',
					clicknum: '',
					discussnum: '',
					storeupnum: '',
				},
				shiyanshifenleiOptions: [],
				shiyanshiguimoOptions: [],
				anquandengjiOptions: [],
				shiyanshizhuangtaiOptions: [],


				rules: {
					shiyanshibianhao: [
					],
					shiyanshimingcheng: [
					],
					shiyanshifenlei: [
					],
					shiyanshiguimo: [
					],
					rongnarenshu: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
					anquandengji: [
					],
					shiyanshizhuangtai: [
					],
					shiyanshitupian: [
					],
					shiyanshiweizhi: [
					],
					shiyanshixiangqing: [
					],
					clicktime: [
					],
					clicknum: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
					discussnum: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
					storeupnum: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
				},
				centerType: false,
			};
		},
		computed: {



		},
		components: {
		},
		created() {
			if(this.$route.query.centerType){
				this.centerType = true
			}
			//this.bg();
			let type = this.$route.query.type ? this.$route.query.type : '';
			this.init(type);
			this.baseUrl = this.$config.baseUrl;
		},
		methods: {
			getMakeZero(s) {
				return s < 10 ? '0' + s : s;
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
						if(o=='rongnarenshu'){
							this.ruleForm.rongnarenshu = obj[o];
							this.ro.rongnarenshu = true;
							continue;
						}
						if(o=='anquandengji'){
							this.ruleForm.anquandengji = obj[o];
							this.ro.anquandengji = true;
							continue;
						}
						if(o=='shiyanshizhuangtai'){
							this.ruleForm.shiyanshizhuangtai = obj[o];
							this.ro.shiyanshizhuangtai = true;
							continue;
						}
						if(o=='shiyanshitupian'){
							this.ruleForm.shiyanshitupian = obj[o].split(",")[0];
							this.ro.shiyanshitupian = true;
							continue;
						}
						if(o=='shiyanshiweizhi'){
							this.ruleForm.shiyanshiweizhi = obj[o];
							this.ro.shiyanshiweizhi = true;
							continue;
						}
						if(o=='shiyanshixiangqing'){
							this.ruleForm.shiyanshixiangqing = obj[o];
							this.ro.shiyanshixiangqing = true;
							continue;
						}
						if(o=='clicktime'){
							this.ruleForm.clicktime = obj[o];
							this.ro.clicktime = true;
							continue;
						}
						if(o=='clicknum'){
							this.ruleForm.clicknum = obj[o];
							this.ro.clicknum = true;
							continue;
						}
						if(o=='discussnum'){
							this.ruleForm.discussnum = obj[o];
							this.ro.discussnum = true;
							continue;
						}
						if(o=='storeupnum'){
							this.ruleForm.storeupnum = obj[o];
							this.ro.storeupnum = true;
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
					}
				});
				this.$http.get('option/shiyanshifenlei/shiyanshifenlei', {emulateJSON: true}).then(res => {
					if (res.data.code == 0) {
						this.shiyanshifenleiOptions = res.data.data;
					}
				});
				this.shiyanshiguimoOptions = "大型,中型,小型".split(',')
				this.anquandengjiOptions = "红,橙,黄,蓝".split(',')
				this.shiyanshizhuangtaiOptions = "使用中,空闲中".split(',')

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
				this.$http.get(`shiyanshi/detail/${this.$route.query.id}`, {emulateJSON: true}).then(res => {
					if (res.data.code == 0) {
						this.ruleForm = res.data.data;
					}
				});
			},
			// 提交
			async onSubmit() {
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


						await this.$http.post(`shiyanshi/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(async res => {
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
			shiyanshitupianUploadChange(fileUrls) {
				this.ruleForm.shiyanshitupian = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
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
