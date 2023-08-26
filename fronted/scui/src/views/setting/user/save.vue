<template>
	<el-dialog :title="titleMap[mode]" v-model="visible" :width="500" destroy-on-close @closed="$emit('closed')">
		<el-form :model="form" :rules="rules" :disabled="mode=='show'" ref="dialogForm" label-width="100px" label-position="left">
			<el-form-item label="头像" prop="avatar">
				<sc-upload v-model="form.avatar" title="上传头像" ref="uploadRef"></sc-upload>
				<!-- <sc-upload title="上传头像" :autoUpload="false" ref="uploadRef" v-model="form.avatar" round icon="el-icon-avatar"></sc-upload> -->
			</el-form-item>
			<el-form-item label="登录账号" prop="username">
				<el-input v-model="form.username" placeholder="用于登录系统" :disabled="mode=='edit'" clearable></el-input>
			</el-form-item>
			<el-form-item label="姓名" prop="name">
				<el-input v-model="form.name" placeholder="请输入完整的真实姓名" clearable></el-input>
			</el-form-item>
			<template v-if="mode=='add'">
				<el-form-item label="登录密码" prop="password">
					<el-input type="password" v-model="form.password" clearable show-password></el-input>
				</el-form-item>
				<el-form-item label="确认密码" prop="password1">
					<el-input type="password" v-model="form.password1" clearable show-password></el-input>
				</el-form-item>
			</template>
			<el-form-item label="所属部门" prop="dept">
				<el-cascader v-model="form.dept" :options="depts" :props="deptsProps" ref="deptRef" clearable style="width: 100%;" @change="deptChange"></el-cascader>
			</el-form-item>
			<el-form-item label="所属角色" prop="group">
				<el-select v-model="form.group" multiple filterable style="width: 100%">
					<el-option v-for="item in groups" :key="item.group.id" :label="item.group.name" :value="item.group.id"/>
				</el-select>
			</el-form-item>
		</el-form>
		<template #footer>
			<el-button @click="visible=false" >取 消</el-button>
			<el-button v-if="mode!='show'" type="primary" :loading="isSaveing" @click="submit()">保 存</el-button>
		</template>
	</el-dialog>
</template>

<script>
	export default {
		emits: ['success', 'closed'],
		data() {
			return {
				mode: "add",
				titleMap: {
					add: '新增用户',
					edit: '编辑用户',
					show: '查看'
				},
				visible: false,
				isSaveing: false,
				//表单数据
				form: {
					id:"",
					username: "",
					avatar: "",
					name: "",
					dept: 0,
					group: [],
					password: "",
					password1: ""
				},
				//验证规则
				rules: {
					avatar:[
						{required: true, message: '请上传头像'}
					],
					username: [
						{required: true, message: '请输入登录账号'}
					],
					name: [
						{required: true, message: '请输入真实姓名'}
					],
					password: [
						{required: true, message: '请输入登录密码'},
						{validator: (rule, value, callback) => {
							if (this.form.password1 !== '') {
								this.$refs.dialogForm.validateField('password1');
							}
							callback();
						}}
					],
					password1: [
						{required: true, message: '请再次输入密码'},
						{validator: (rule, value, callback) => {
							if (value !== this.form.password) {
								callback(new Error('两次输入密码不一致!'));
							}else{
								callback();
							}
						}}
					],
					dept: [
						{required: false, message: '请选择所属部门'}
					],
					group: [
						{required: false, message: '请选择所属角色', trigger: 'change'}
					]
				},
				//所需数据选项
				groups: [],
				groupsProps: {
					label: "name",
					value: "id",
					multiple: true,
					checkStrictly: true
				},
				depts: [],
				deptsProps: {
					label: 'name',
					value: "id",
					checkStrictly: true
				}
			}
		},
		mounted() {
			this.getGroup()
			this.getDept()
		},
		methods: {
			//显示
			open(mode='add'){
				this.mode = mode;
				this.visible = true;
				return this
			},
			//加载树数据
			async getGroup(){
				var res = await this.$API.badmin.roles.list.get();
				this.groups = res.data.results;
			},
			async getDept(){
				var res = await this.$API.badmin.dept.list.get();
				this.depts = res.data.results;
			},
			//表单提交方法
			submit(){
				this.$refs.dialogForm.validate(async (valid) => {
					if (valid) {
						// this.isSaveing = true;
						this.form['group_ids'] = this.form.group
						var res = await this.getSubmitApi(this.mode, this.form);
						this.isSaveing = false;
						if(res.status == 200 || res.status == 201){
							this.$emit('success', res.data, this.mode)
							this.visible = false;
							this.$message.success("操作成功")
						}else{
							this.$alert(res.statusText, "提示", {type: 'error'})
						}
					}else{
						return false;
					}
				})
			},
			//表单注入数据
			setData(data){
				this.form.id = data.id
				this.form.username = data.owner.username
				this.form.avatar = data.avatar
				this.form.name = data.name
				this.form.group = data.group
				this.form.dept = data.dept
				this.form.groupName = data.groupName
				//可以和上面一样单个注入，也可以像下面一样直接合并进去
				//Object.assign(this.form, data)
			},
			getSubmitApi(model, data){
				if (model == 'edit'){
					return this.$API.badmin.users.update.put(data.id, data)
				}else if (model == 'add'){
					return this.$API.badmin.user.post(data)
				}
			},
			deptChange(val){
				console.log(val)
				// 响应式改变选择,只能选择最后一级
				const deptref = this.$refs.deptRef
				if (deptref.getCheckedNodes(true).length){
					this.form.dept = this.$refs.deptRef.getCheckedNodes(false)[0].value
					deptref.togglePopperVisible(false)
				}
			}
		}
	}
</script>

<style>
</style>
