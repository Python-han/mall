<template>
	<!-- <el-alert title="异步组件动态加载使用了正处于试验阶段的<Suspense>组件, 其API和使用方式可能会改变. <Suspense> is an experimental feature and its API will likely change." type="warning" show-icon style="margin-bottom: 15px;"/> -->

	<el-card shadow="never" header="个人信息">
		<el-form ref="form" :model="form" label-width="120px" style="margin-top:20px;" v-loading="loading">
			<el-form-item label="账号">
				<el-input v-model="form.username" disabled></el-input>
				<div class="el-form-item-msg">账号信息用于登录，系统不允许修改</div>
			</el-form-item>
			<el-form-item label="头像">
				<sc-upload v-model="form.avatar" title="avatar" :cropper="true" :compress="1" :aspectRatio="1/1" round icon="el-icon-avatar"></sc-upload>
			</el-form-item>
			<el-form-item label="姓名">
				<el-input v-model="form.name"></el-input>
			</el-form-item>
			<el-form-item label="性别">
				<el-select v-model="form.sex" placeholder="请选择">
					<el-option
						v-for="item in options"
						:key="item.value"
						:label="item.label"
						:value="item.value"
						/>
				</el-select>
			</el-form-item>
			<el-form-item label="个性签名">
				<el-input v-model="form.about" type="textarea"></el-input>
			</el-form-item>
			<el-form-item>
				<el-button type="primary" @click="onSubmit">保存</el-button>
			</el-form-item>
		</el-form>
	</el-card>
</template>

<script>
	export default {
		data() {
			return {
				form: {
					id: "",
					username: "",
					name: "",
					sex: "1",
					about: "",
					avatar: ""
				},
				options: [
					{
						label: "保密",
						value: 0
					},
					{
						label: "男",
						value: 1
					},
					{
						label: "女",
						value: 2
					}
				],
				loading: false
			}
		},
		created(){
			// 异步组件刷新后进来需要重新请求一次接口获取数据
			this.loading = true
			this.$API.badmin.user.get().then(res => {
				if (res.status == 200){
					this.form.id = res.data.id
					this.form.username = res.data.owner.username
					this.form.name = res.data.name
					this.form.sex = res.data.sex
					this.form.about = res.data.about
					this.form.avatar = res.data.avatar
					this.loading = false
				}
			})	
		},
		methods: {
			onSubmit(){
				const data = {
					name: this.form.name,
					sex: this.form.sex,
					about: this.form.about,
					avatar: this.form.avatar
				}
				this.loading = true
				this.$API.badmin.users.partial_update.patch(this.form.id, data).then(res => {
					if (res.status == 200){
						this.form.id = res.data.id
						this.form.username = res.data.owner.username
						this.form.name = res.data.name
						this.form.sex = res.data.sex
						this.form.about = res.data.about
						this.form.avatar = res.data.avatar
						this.loading = false
						this.$message.success("修改成功")
					}
					
				})
			}
		}
	}
</script>

<style>
</style>
