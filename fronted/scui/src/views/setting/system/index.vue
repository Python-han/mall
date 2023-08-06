<template>
	<el-main>
		<el-card shadow="never">
			<el-tabs tab-position="top">

				<el-tab-pane label="系统设置">
					<el-form ref="form" :model="sys" label-width="100px" style="margin-top: 20px;">
						<el-form-item label="系统名称">
							<el-input v-model="sys.site_title"></el-input>
						</el-form-item>
						<el-form-item label="LogoUrl">
							<sc-upload v-model="sys.logo_url" title="logo" :cropper="true" :compress="1" :aspectRatio="1/1" round icon="el-icon-avatar"></sc-upload>
							<!-- <el-input v-model="sys.logo_url"></el-input> -->
							<!-- <div class="el-form-item-msg" data-v-b33b3cf8="">必须为http://或https://开头的完整url地址</div> -->
						</el-form-item>
						<!-- <el-form-item label="登录开关">
							<el-switch v-model="sys.login"></el-switch>
							<div class="el-form-item-msg" data-v-b33b3cf8="">关闭后普通用户无法登录，仅允许管理员角色登录</div>
						</el-form-item>
						<el-form-item label="密码验证规则">
							<el-input v-model="sys.passwordRules"></el-input>
						</el-form-item> -->
						<el-form-item label="版权信息">
							<el-input type="textarea" :autosize="{minRows: 4}" v-model="sys.copyright"></el-input>
						</el-form-item>
						<el-form-item>
							<el-button type="primary" @click="onSysSubmit">保存</el-button>
						</el-form-item>
					</el-form>
				</el-tab-pane>

				<!-- <el-tab-pane label="短信配置">
					<el-form ref="form" :model="msg" label-width="100px" style="margin-top: 20px;">
						<el-form-item label="短信开关">
							<el-switch v-model="msg.open"></el-switch>
							<div class="el-form-item-msg" data-v-b33b3cf8="">关闭后用户无法收到短信，但日志中将记录</div>
						</el-form-item>
						<el-form-item label="appKey">
							<el-input v-model="msg.appKey"></el-input>
						</el-form-item>
						<el-form-item label="secretKey">
							<el-input v-model="msg.secretKey"></el-input>
						</el-form-item>
						<el-form-item>
							<el-button type="primary">保存</el-button>
						</el-form-item>
					</el-form>
				</el-tab-pane> -->

				<el-tab-pane label="邮箱配置">
					<el-form ref="form" :model="msg" label-width="100px" style="margin-top: 20px;">
						
						<el-form-item label="主机">
							<el-input v-model="msg.email_host"></el-input>
						</el-form-item>
						<el-form-item label="邮箱">
							<el-input v-model="msg.email_host_user" type="email"></el-input>
						</el-form-item>
						<el-form-item label="密码">
							<el-input v-model="msg.email_host_password" type="password" show-password></el-input>
							<div class="el-form-item-msg" data-v-b33b3cf8="">自己的邮箱密码，或授权码，一般现在的邮箱都需要授权码</div>
						</el-form-item>
						<el-form-item label="端口">
							<el-input v-model="msg.email_port"></el-input>
						</el-form-item>
						<el-form-item label="默认发件箱">
							<el-input v-model="msg.default_from_email" type="email"></el-input>
						</el-form-item>
						<el-form-item label="SSL">
							<el-switch v-model="msg.email_use_ssl"></el-switch>
							<div class="el-form-item-msg" data-v-b33b3cf8="">是否为隐式安全连接</div>
						</el-form-item>
						<el-form-item label="邮箱开关">
							<el-switch v-model="msg.status"></el-switch>
							<div class="el-form-item-msg" data-v-b33b3cf8="">关闭后用户无法收到邮件，但日志中将记录</div>
						</el-form-item>
						<el-form-item>
							<el-button type="primary" @click="onMsgSubmit">保存</el-button>
						</el-form-item>
					</el-form>
				</el-tab-pane>

				<el-tab-pane label="扩展配置">
					<el-alert title="扩展配置为系统业务所有的配置，应该由系统管理员操作，如需用户配置应另起业务配置页面。" type="warning" style="margin-bottom: 15px;"></el-alert>

					<el-table :data="setting" stripe>
						<el-table-column label="#" type="index" width="50"></el-table-column>
						<el-table-column label="KEY" prop="key" width="150">
							<template #default="scope">
								<el-input v-if="scope.row.isSet" v-model="scope.row.key" placeholder="请输入内容"></el-input>
								<span v-else>{{scope.row.key}}</span>
							</template>
						</el-table-column>
						<el-table-column label="VALUE" prop="value" width="350">
							<template #default="scope">
								<template v-if="scope.row.isSet">
									<el-switch v-if="typeof scope.row.value==='boolean'" v-model="scope.row.value"></el-switch>
									<el-input v-else v-model="scope.row.value" placeholder="请输入内容"></el-input>
								</template>
								<span v-else>{{scope.row.value}}</span>
							</template>
						</el-table-column>
						<!-- <el-table-column label="CATEGORY" prop="category" width="150">
							<template #default="scope">
								<el-input v-if="scope.row.isSet" v-model="scope.row.category" placeholder="请输入内容"></el-input>
								<span v-else>{{scope.row.category}}</span>
							</template>
						</el-table-column> -->
						<el-table-column label="TITLE" prop="title" width="350">
							<template #default="scope">
								<el-input v-if="scope.row.isSet" v-model="scope.row.title" placeholder="请输入内容"></el-input>
								<span v-else>{{scope.row.title}}</span>
							</template>
						</el-table-column>
						<el-table-column min-width="1"></el-table-column>
						<el-table-column label="操作" fixed="right" width="120">
							<template #default="scope">
								<el-button-group>
									<el-button @click="table_edit(scope.row, scope.$index)" text type="primary" size="small">{{scope.row.isSet?'保存':"修改"}}</el-button>
									<el-button v-if="scope.row.isSet" @click="scope.row.isSet=false" text type="primary" size="small">取消</el-button>
									<el-popconfirm v-if="!scope.row.isSet" title="确定删除吗？" @confirm="table_del(scope.row, scope.$index)">
										<template #reference>
											<el-button text type="primary" size="small">删除</el-button>
										</template>
									</el-popconfirm>
								</el-button-group>
							</template>
						</el-table-column>
					</el-table>
					<el-button type="primary" icon="el-icon-plus" @click="table_add" style="margin-top: 20px;"></el-button>
				</el-tab-pane>

			</el-tabs>
		</el-card>
	</el-main>
</template>

<script>
	import { useLocalStorage } from "@vueuse/core"
	export default {
		name: 'system',
		data() {
			return {
				sys: {},
				msg: {},
				setting: []
			}
		},
		created(){
			this.getSystem()
			this.getEmailConf()
			this.getSystemExtend()
		},
		methods: {
			table_add(){
				var newRow = {
					key: "",
					value: "",
					title: "",
					isSet: true
				}
				this.setting.push(newRow)
			},
			table_edit(row){
				if(row.isSet){
					row.isSet = false
					if (row.id) {
						this.$API.badmin.system_extend.partial_update.patch(row.id, row).then(res => {
						if (res.status == 200){
								this.$message.success("修改成功")
							}
						})
						
					}else{
						this.$API.badmin.system_extend.create.post(row).then(res => {
							if (res.status == 201){
								this.$message.success("保存成功")
							}
						})
					}
				}else{
					row.isSet = true
				}
			},
			table_del(row, index){
				this.$API.badmin.system_extend.remove.delete(row.id).then(res => {
					if (res.status == 204) {
						this.setting.splice(index, 1)
						this.$message.success("删除成功")
					}
				})
			},

			// 获取站配置
			async getSystem(){
				const res = await this.$API.badmin.system.read.get()
				this.sys = res.data
			},

			// 获取邮箱配置
			async getEmailConf(){
				const res = await this.$API.badmin.emailconf.read.get()
				this.msg = res.data
			},

			// 获取扩展配置
			async getSystemExtend(){
				const res = await this.$API.badmin.system_extend.list.get()
				this.setting = res.data
			},

			// 站点配置保存
			onSysSubmit(){
				this.$API.badmin.system.partial_update.patch(this.sys).then(res => {
					if (res.status == 200) {
						this.sys = res.data
						useLocalStorage("SYSTEM").value = JSON.stringify(res.data)
						this.$message.success("修改成功")
					}
				})
			},
			// 邮箱配置保存
			onMsgSubmit(){
				this.$API.badmin.emailconf.partial_update.patch(this.msg).then(res => {
					if (res.status == 200) {
						this.msg = res.data
						this.$message.success("修改成功")
					}
				})
			}
		}
	}
</script>

<style>
</style>
