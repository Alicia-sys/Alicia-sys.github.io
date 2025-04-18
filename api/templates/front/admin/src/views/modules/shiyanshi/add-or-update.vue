<template>
	<div class="addEdit-block">
		<el-form
			class="add-update-preview"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="180px"
		>
			<template >
				<el-form-item class="input" v-if="type!='info'"  label="实验室编号" prop="shiyanshibianhao" >
					<el-input v-model="ruleForm.shiyanshibianhao" placeholder="实验室编号" clearable  :readonly="ro.shiyanshibianhao"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="实验室编号" prop="shiyanshibianhao" >
					<el-input v-model="ruleForm.shiyanshibianhao" placeholder="实验室编号" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="实验室名称" prop="shiyanshimingcheng" >
					<el-input v-model="ruleForm.shiyanshimingcheng" placeholder="实验室名称" clearable  :readonly="ro.shiyanshimingcheng"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="实验室名称" prop="shiyanshimingcheng" >
					<el-input v-model="ruleForm.shiyanshimingcheng" placeholder="实验室名称" readonly></el-input>
				</el-form-item>
				<el-form-item class="select" v-if="type!='info'"  label="实验室分类" prop="shiyanshifenlei" >
					<el-select :disabled="ro.shiyanshifenlei" v-model="ruleForm.shiyanshifenlei" placeholder="请选择实验室分类" >
						<el-option
							v-for="(item,index) in shiyanshifenleiOptions"
							v-bind:key="index"
							:label="item"
							:value="item">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item v-else class="input" label="实验室分类" prop="shiyanshifenlei" >
					<el-input v-model="ruleForm.shiyanshifenlei"
						placeholder="实验室分类" readonly></el-input>
				</el-form-item>
				<el-form-item class="select" v-if="type!='info'"  label="实验室规模" prop="shiyanshiguimo" >
					<el-select :disabled="ro.shiyanshiguimo" v-model="ruleForm.shiyanshiguimo" placeholder="请选择实验室规模" >
						<el-option
							v-for="(item,index) in shiyanshiguimoOptions"
							v-bind:key="index"
							:label="item"
							:value="item">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item v-else class="input" label="实验室规模" prop="shiyanshiguimo" >
					<el-input v-model="ruleForm.shiyanshiguimo"
						placeholder="实验室规模" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="容纳人数" prop="rongnarenshu" >
					<el-input v-model.number="ruleForm.rongnarenshu" placeholder="容纳人数" clearable  :readonly="ro.rongnarenshu"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="容纳人数" prop="rongnarenshu" >
					<el-input v-model="ruleForm.rongnarenshu" placeholder="容纳人数" readonly></el-input>
				</el-form-item>
				<el-form-item class="select" v-if="type!='info'"  label="安全等级" prop="anquandengji" >
					<el-select :disabled="ro.anquandengji" v-model="ruleForm.anquandengji" placeholder="请选择安全等级" >
						<el-option
							v-for="(item,index) in anquandengjiOptions"
							v-bind:key="index"
							:label="item"
							:value="item">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item v-else class="input" label="安全等级" prop="anquandengji" >
					<el-input v-model="ruleForm.anquandengji"
						placeholder="安全等级" readonly></el-input>
				</el-form-item>
				<el-form-item class="select" v-if="type!='info'"  label="实验室状态" prop="shiyanshizhuangtai" >
					<el-select :disabled="ro.shiyanshizhuangtai" v-model="ruleForm.shiyanshizhuangtai" placeholder="请选择实验室状态" >
						<el-option
							v-for="(item,index) in shiyanshizhuangtaiOptions"
							v-bind:key="index"
							:label="item"
							:value="item">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item v-else class="input" label="实验室状态" prop="shiyanshizhuangtai" >
					<el-input v-model="ruleForm.shiyanshizhuangtai"
						placeholder="实验室状态" readonly></el-input>
				</el-form-item>
				<el-form-item class="upload" v-if="type!='info' && !ro.shiyanshitupian" label="实验室图片" prop="shiyanshitupian" >
					<file-upload
						tip="点击上传实验室图片"
						action="file/upload"
						:limit="3"
						:multiple="true"
						:fileUrls="ruleForm.shiyanshitupian?ruleForm.shiyanshitupian:''"
						@change="shiyanshitupianUploadChange"
					></file-upload>
				</el-form-item>
				<el-form-item class="upload" v-else-if="ruleForm.shiyanshitupian" label="实验室图片" prop="shiyanshitupian" >
					<img v-if="ruleForm.shiyanshitupian.substring(0,4)=='http'&&ruleForm.shiyanshitupian.split(',w').length>1" class="upload-img" style="margin-right:20px;" v-bind:key="index" :src="ruleForm.shiyanshitupian" width="100" height="100">
					<img v-else-if="ruleForm.shiyanshitupian.substring(0,4)=='http'" class="upload-img" style="margin-right:20px;" v-bind:key="index" :src="ruleForm.shiyanshitupian.split(',')[0]" width="100" height="100">
					<img v-else class="upload-img" style="margin-right:20px;" v-bind:key="index" v-for="(item,index) in ruleForm.shiyanshitupian.split(',')" :src="$base.url+item" width="100" height="100">
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="实验室位置" prop="shiyanshiweizhi" >
					<el-input v-model="ruleForm.shiyanshiweizhi" placeholder="实验室位置" clearable  :readonly="ro.shiyanshiweizhi"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="实验室位置" prop="shiyanshiweizhi" >
					<el-input v-model="ruleForm.shiyanshiweizhi" placeholder="实验室位置" readonly></el-input>
				</el-form-item>
			</template>
			<el-form-item v-if="type!='info'"  label="实验室详情" prop="shiyanshixiangqing" >
				<editor 
					style="min-width: 200px; max-width: 600px;"
					v-model="ruleForm.shiyanshixiangqing" 
					class="editor" 
					action="file/upload">
				</editor>
			</el-form-item>
			<el-form-item v-else-if="ruleForm.shiyanshixiangqing" label="实验室详情" prop="shiyanshixiangqing" >
				<span class="text ql-snow ql-editor" v-html="ruleForm.shiyanshixiangqing"></span>
			</el-form-item>
			<el-form-item class="btn">
				<el-button class="btn3"  v-if="type!='info'" type="success" @click="onSubmit">
					<span class="icon iconfont icon-xihuan"></span>
					提交
				</el-button>
				<el-button class="btn4" v-if="type!='info'" type="success" @click="back()">
					<span class="icon iconfont icon-xihuan"></span>
					取消
				</el-button>
				<el-button class="btn5" v-if="type=='info'" type="success" @click="back()">
					<span class="icon iconfont icon-xihuan"></span>
					返回
				</el-button>
			</el-form-item>
		</el-form>
    

	</div>
</template>
<script>
	import { 
		isIntNumer,
	} from "@/utils/validate";
	export default {
		data() {
			var validateIntNumber = (rule, value, callback) => {
				if(!value){
					callback();
				} else if (!isIntNumer(value)) {
					callback(new Error("请输入整数"));
				} else {
					callback();
				}
			};
			return {
				id: '',
				type: '',
			
			
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
			
				ruleForm: {
					shiyanshibianhao: '',
					shiyanshimingcheng: '',
					shiyanshifenlei: '',
					shiyanshiguimo: '',
					rongnarenshu: '',
					anquandengji: '',
					shiyanshizhuangtai: '空闲中',
					shiyanshitupian: '',
					shiyanshiweizhi: '',
					shiyanshixiangqing: '',
					clicktime: '',
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
						{ validator: validateIntNumber, trigger: 'blur' },
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
						{ validator: validateIntNumber, trigger: 'blur' },
					],
					discussnum: [
						{ validator: validateIntNumber, trigger: 'blur' },
					],
					storeupnum: [
						{ validator: validateIntNumber, trigger: 'blur' },
					],
				},
			};
		},
		props: ["parent"],
		computed: {



		},
		components: {
		},
		created() {
		},
		methods: {
			// 下载
			download(file){
				window.open(`${file}`)
			},
			// 初始化
			init(id,type) {
				if (id) {
					this.id = id;
					this.type = type;
				}
				if(this.type=='info'||this.type=='else'||this.type=='msg'){
					this.info(id);
				}else if(this.type=='logistics'){
					for(let x in this.ro) {
						this.ro[x] = true
					}
					this.logistics=false;
					this.info(id);
				}else if(this.type=='cross'){
					var obj = this.$storage.getObj('crossObj');
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
							this.ruleForm.shiyanshitupian = obj[o];
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
					this.ruleForm.shiyanshizhuangtai = '空闲中'; 				}
				// 获取用户信息
				this.$http({
					url: `${this.$storage.get('sessionTable')}/session`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						var json = data.data;
						if(this.$storage.get("role")!="管理员") {
							this.ro.shiyanshizhuangtai = true;
						}
					} else {
						this.$message.error(data.msg);
					}
				});
				this.$http({
					url: `option/shiyanshifenlei/shiyanshifenlei`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.shiyanshifenleiOptions = data.data;
					} else {
						this.$message.error(data.msg);
					}
				});
				this.shiyanshiguimoOptions = "大型,中型,小型".split(',')
				this.anquandengjiOptions = "红,橙,黄,蓝".split(',')
				this.shiyanshizhuangtaiOptions = "使用中,空闲中".split(',')
			
			},
			// 多级联动参数

			info(id) {
				this.$http({
					url: `shiyanshi/info/${id}`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.ruleForm = data.data;
						//解决前台上传图片后台不显示的问题
						let reg=new RegExp('../../../upload','g')//g代表全部
						this.ruleForm.shiyanshixiangqing = this.ruleForm.shiyanshixiangqing.replace(reg,'../../../pythonek97261k/upload');
					} else {
						this.$message.error(data.msg);
					}
				});
			},

			// 提交
			async onSubmit() {
					if(this.ruleForm.shiyanshitupian!=null) {
						this.ruleForm.shiyanshitupian = this.ruleForm.shiyanshitupian.replace(new RegExp(this.$base.url,"g"),"");
					}
					var objcross = this.$storage.getObj('crossObj');
					await this.$refs["ruleForm"].validate(async valid => {
						if (valid) {
							if(this.type=='cross'){
								var statusColumnName = this.$storage.get('statusColumnName');
								var statusColumnValue = this.$storage.get('statusColumnValue');
								if(statusColumnName!='') {
									var obj = this.$storage.getObj('crossObj');
									if(statusColumnName && !statusColumnName.startsWith("[")) {
										for (var o in obj){
											if(o==statusColumnName){
												obj[o] = statusColumnValue;
											}
										}
										var table = this.$storage.get('crossTable');
										await this.$http({
											url: `${table}/update`,
											method: "post",
											data: obj
										}).then(({ data }) => {});
									}
								}
							}
							
							await this.$http({
								url: `shiyanshi/${!this.ruleForm.id ? "save" : "update"}`,
								method: "post",
								data: this.ruleForm
							}).then(async ({ data }) => {
								if (data && data.code === 0) {
									this.$message({
										message: "操作成功",
										type: "success",
										duration: 1500,
										onClose: () => {
											this.parent.showFlag = true;
											this.parent.addOrUpdateFlag = false;
											this.parent.shiyanshiCrossAddOrUpdateFlag = false;
											this.parent.search();
											this.parent.contentStyleChange();
										}
									});
								} else {
									this.$message.error(data.msg);
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
				this.parent.showFlag = true;
				this.parent.addOrUpdateFlag = false;
				this.parent.shiyanshiCrossAddOrUpdateFlag = false;
				this.parent.contentStyleChange();
			},
			shiyanshitupianUploadChange(fileUrls) {
				this.ruleForm.shiyanshitupian = fileUrls;
			},
		}
	};
</script>
<style lang="scss" scoped>
	.addEdit-block {
		padding: 30px 20px 20px 20px;
	}
	.add-update-preview {
		border: 1px solid #BFBFBF;
		padding: 40px 30% 20px 10%;
		background: #FFFFFF;
	}
	.amap-wrapper {
		width: 100%;
		height: 500px;
	}
	
	.search-box {
		position: absolute;
	}
	
	.el-date-editor.el-input {
		width: auto;
	}
	.add-update-preview /deep/ .el-form-item {
		border: 0px solid #eee;
		padding: 0;
		margin: 0 0 26px 0;
		display: inline-block;
		width: 100%;
	}
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
		padding: 0 10px 0 0;
		color: #666;
		font-weight: 600;
		width: 180px;
		font-size: 16px;
		line-height: 40px;
		text-align: right;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
		margin-left: 180px;
	}
	.add-update-preview .el-form-item span.text {
		border: 0px solid #E8E8E8;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 15px;
		margin: 0 20px 0 0;
		color: #666;
		background: #fff;
		width: 360px;
		font-size: 15px;
		line-height: 34px;
		text-align: left;
		height: 34px;
	}
	
	.add-update-preview .el-input {
		width: 100%;
	}
	.add-update-preview .el-input /deep/ .el-input__inner {
		border: 1px dashed #bfbfbf;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		width: 100%;
		font-size: 16px;
		min-width: 360px;
		height: 40px;
	}
	.add-update-preview .el-input /deep/ .el-input__inner[readonly="readonly"] {
		border: 1px dashed #bfbfbf;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		background: none;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-input-number {
		text-align: left;
		width: 100%;
	}
	.add-update-preview .el-input-number /deep/ .el-input__inner {
		text-align: left;
		border: 1px dashed #bfbfbf;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		width: 100%;
		font-size: 16px;
		min-width: 360px;
		height: 40px;
	}
	.add-update-preview .el-input-number /deep/ .is-disabled .el-input__inner {
		text-align: left;
		border: 1px dashed #bfbfbf;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		background: none;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__decrease {
		display: none;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__increase {
		display: none;
	}
	.add-update-preview .el-select {
		width: 100%;
	}
	.add-update-preview .el-select /deep/ .el-input__inner {
		border: 1px dashed #bfbfbf;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		background: none;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-select /deep/ .is-disabled .el-input__inner {
		border: 1px dashed #bfbfbf;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		background: none;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-date-editor {
		width: 100%;
	}
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
		border: 1px dashed #bfbfbf;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 30px;
		color: #666;
		background: none;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-date-editor /deep/ .el-input__inner[readonly="readonly"] {
		border: 1px dashed #bfbfbf;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 30px;
		color: #666;
		background: none;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .viewBtn {
		border: 1px dashed #bfbfbf;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 30px;
		margin: 0 20px 0 0;
		color: #666;
		background: #fff;
		width: auto;
		font-size: 15px;
		line-height: 34px;
		text-align: left;
		height: 34px;
		.iconfont {
			margin: 0 2px;
			color: #666;
			font-size: 16px;
			height: 34px;
		}
	}
	.add-update-preview .viewBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview .downBtn {
		border: 1px dashed #bfbfbf;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 30px;
		margin: 0 20px 0 0;
		color: #666;
		background: #fff;
		width: auto;
		font-size: 15px;
		line-height: 34px;
		height: 34px;
		.iconfont {
			margin: 0 2px;
			color: #666;
			font-size: 16px;
			height: 34px;
		}
	}
	.add-update-preview .downBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview .unBtn {
		border: 1px dashed #bfbfbf;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 30px;
		margin: 0 20px 0 0;
		color: #666;
		background: #fff;
		width: auto;
		font-size: 15px;
		line-height: 34px;
		text-align: left;
		height: 34px;
		.iconfont {
			margin: 0 2px;
			color: #fff;
			display: none;
			font-size: 14px;
			height: 34px;
		}
	}
	.add-update-preview .unBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview /deep/ .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview /deep/ .upload .upload-img {
		border: 1px dashed #bfbfbf;
		cursor: pointer;
		border-radius: 0px;
		color: #666;
		background: #fff;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
		border: 1px dashed #bfbfbf;
		cursor: pointer;
		border-radius: 0px;
		color: #666;
		background: #fff;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
		border: 1px dashed #bfbfbf;
		cursor: pointer;
		border-radius: 0px;
		color: #666;
		background: #fff;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	.add-update-preview /deep/ .el-upload__tip {
		color: #666;
		font-size: 15px;
	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
		border: 1px dashed #bfbfbf;
		border-radius: 0px;
		padding: 12px;
		color: #666;
		background: #fff;
		width: 100%;
		font-size: 14px;
		min-width: 400px;
		height: 120px;
	}
	.add-update-preview .el-textarea /deep/ .el-textarea__inner[readonly="readonly"] {
				border: 1px dashed #bfbfbf;
				border-radius: 0px;
				padding: 12px;
				color: #666;
				background: #fff;
				width: 100%;
				font-size: 14px;
				min-width: 400px;
				height: 120px;
			}
	.add-update-preview .el-form-item.btn {
		padding: 0;
		margin: 20px 0 0;
		.btn1 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: linear-gradient( 135deg, #097499 0%, #A5DDFD 100%);
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn1:hover {
			opacity: 0.8;
		}
		.btn2 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: linear-gradient( 135deg, #097499 0%, #A5DDFD 100%);
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 34px;
			}
		}
		.btn2:hover {
			opacity: 0.8;
		}
		.btn3 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: linear-gradient( 135deg, #097499 0%, #A5DDFD 100%);
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn3:hover {
			opacity: 0.8;
		}
		.btn4 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: linear-gradient( 135deg, #097499 0%, #A5DDFD 100%);
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn4:hover {
			opacity: 0.8;
		}
		.btn5 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: linear-gradient( 135deg, #097499 0%, #A5DDFD 100%);
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn5:hover {
			opacity: 0.8;
		}
	}
</style>
