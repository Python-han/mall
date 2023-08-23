<template>
	<el-form ref="loginForm" :model="form" :rules="rules" label-width="0" size="large" @keyup.enter="login">
		<el-form-item prop="user">
			<el-input v-model="form.user" prefix-icon="el-icon-user" clearable :placeholder="$t('login.userPlaceholder')">
				<!-- <template #append>
					<el-select v-model="userType" style="width: 130px;">
						<el-option :label="$t('login.admin')" value="admin"></el-option>
						<el-option :label="$t('login.user')" value="user"></el-option>
					</el-select>
				</template> -->
			</el-input>
		</el-form-item>
		<el-form-item prop="password">
			<el-input v-model="form.password" prefix-icon="el-icon-lock" clearable show-password :placeholder="$t('login.PWPlaceholder')"></el-input>
		</el-form-item>
		<el-form-item style="margin-bottom: 10px;">
				<el-col :span="12">
					<el-checkbox :label="$t('login.rememberMe')" v-model="form.autologin"></el-checkbox>
				</el-col>
				<!-- <el-col :span="12" class="login-forgot">
					<router-link to="/reset_password">{{ $t('login.forgetPassword') }}？</router-link>
				</el-col> -->
		</el-form-item>
		<el-form-item>
			<el-button type="primary" style="width: 100%;" :loading="islogin" round @click="login">{{ $t('login.signIn') }}</el-button>
		</el-form-item>
		<!-- <div class="login-reg">
			{{$t('login.noAccount')}} <router-link to="/user_register">{{$t('login.createAccount')}}</router-link>
		</div> -->
	</el-form>
</template>

<script>
	import { useLocalStorage } from "@vueuse/core";
	export default {
		data() {
			return {
				userType: 'admin',
				form: {
					user: "",
					password: "",
					autologin: false
				},
				rules: {
					username: [
						{required: true, message: this.$t('login.userError'), trigger: 'blur'}
					],
					password: [
						{required: true, message: this.$t('login.PWError'), trigger: 'blur'}
					]
				},
				islogin: false,
			}
		},
		watch:{
			userType(val){
				if(val == 'admin'){
					this.form.user = ''
					this.form.password = ''
				}else if(val == 'user'){
					this.form.user = 'user'
					this.form.password = 'user'
				}
			}
		},
		mounted() {

		},
		methods: {
			async login(){
				var validate = await this.$refs.loginForm.validate().catch(()=>{})
				if(!validate){ return false }

				this.islogin = true
				var data = {
					username: this.form.user,
					// password: this.$TOOL.crypto.MD5(this.form.password)
					password: this.form.password
				}
				//获取token
				console.log(data)
				var token = await this.$API.auth.token.post(data)			
				if(token.status == 200){
					this.$TOOL.cookie.set("TOKEN", token.data.access, {
						expires: this.form.autologin ? 24*60*60 : 0
					})
					const user = await this.$API.badmin.user.get()
					const dashboardGrid = ["welcome", "ver", "time", "progress", "echarts", "about"]
					useLocalStorage("USERINFO", user.data)
					const system = await this.$API.badmin.system.read.get()
					useLocalStorage("SYSTEM", system.data)
					this.$TOOL.data.set("PERMISSIONS", user.data.perms)
					this.$TOOL.data.set("DASHBOARDGRID", dashboardGrid)
					this.$TOOL.data.set("MENU", user.data.menus)
				}else{
					this.islogin = false 
					this.$message.warning(token.data.detail)
					return false
				}
				this.$router.replace({
					path: '/'
				})
				this.$message.success("Login Success 登录成功")
				this.islogin = false
			},
		}
	}
</script>

<style>
</style>
