<template>
	<el-dialog :title="titleMap[mode]" v-model="visible" :width="500" destroy-on-close @closed="$emit('closed')">
		<el-form :model="form" :rules="rules" :disabled="mode=='show'" ref="dialogForm" label-width="100px">
			<el-form-item label="权限名称" prop="permission.name">
				<el-input v-model="form.permission.name" placeholder="请输入权限名称" clearable></el-input>
			</el-form-item>
			<el-form-item label="权限标识" prop="permission.codename">
				<el-input v-model="form.permission.codename" placeholder="请输入权限标识" clearable></el-input>
			</el-form-item>
			<el-form-item label="归属模型" prop="permission.content_type.model">
				<el-select v-model="form.permission.content_type" value-key="model" filterable placeholder="请选择权限归属模型">
					<el-option v-for="item in content_types" :key="item.model" :label="item.model" :value="item" />
				</el-select>
			</el-form-item>
			<el-form-item label="接口别名" prop="apiname">
				<el-input v-model="form.apiname" placeholder="请输入接口url别名" clearable></el-input>
			</el-form-item>
			<el-form-item label="请求类型" prop="request_method">
				<el-select v-model="form.request_method" value-key="value" filterable placeholder="请选择请求方式">
					<el-option v-for="item in requestMethodOptions" :key="item.value" :label="item.label" :value="item.value" />
				</el-select>
			</el-form-item>
			<el-form-item label="备注" prop="mark">
				<el-input v-model="form.mark" placeholder="请输入接口备注说明" type="textarea" clearable></el-input>
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
					add: '新增',
					edit: '编辑',
					show: '查看'
				},
				visible: false,
				isSaveing: false,
				//表单数据
				form: {
					id:"",
					apiname: "",
					request_method: "GET",
					mark: '',
					permission: {
						id: '',
						name: '',
						codename: '',
						content_type: {
							id: '',
							app_label: '',
							model: ''
						}
					} 
				},
				content_types: [],
				requestMethodOptions: [
					{
						label: "新增[POST]",
						value: "POST",
					},
					{
						label: "查看[GET]",
						value: "GET",
					},
					{
						label: "修改[PUT]",
						value: "PUT",
					},
					{
						label: "局部修改[PATCH]",
						value: "PATCH",
					},
					{
						label: "删除[DELETE]",
						value: "DELETE",
					}
				],
				//验证规则
				rules: {
					apiname: [
						{required: true, message: '请输入接口url别名name', trigger: 'change'}
					],
					request_method: [
						{required: true, message: '请选择请求类型', trigger: 'change'}
					],
					'permission.name': [
						{required: true, message: '请输入权限名称', trigger: 'change'}
					],
					'permission.codename': [
						{required: true, message: '请输入权限标识', trigger: 'change'}
					],
					'permission.content_type.model': [
						{required: true, message: '请选择归属模型', trigger: 'change'}
					]
				},
				//所需数据选项
				groups: [],
				groupsProps: {
					label: "name",
					value: "id",
					emitPath: false,
					checkStrictly: true
				}
			}
		},
		mounted() {
			// this.getGroup()
			this.getContentType()
		},
		methods: {
			//显示
			open(mode='add'){
				this.mode = mode;
				this.visible = true;
				return this
			},
			//加载树数据
			// async getGroup(){
			// 	var res = await this.$API.shop.category.list.get();
			// 	this.groups = res.data.results;
			// },
			
			// 加载应用
			async getContentType(){
				const res = await this.$API.badmin.content_type.list.get()
				if (res.status == 200){
					this.content_types = res.data
				}
			},

			//表单提交方法
			submit(){
				this.$refs.dialogForm.validate(async (valid) => {
					if (valid) {
						console.log(this.form)
						// this.isSaveing = true; 
						this.form['content_type_id'] = this.form.permission.content_type.id
						this.form['permission_dict'] = this.form.permission
						var res = await this.getSubmitApi(this.mode, this.form);
						this.isSaveing = false;
						if(res.status == 200 || res.status == 201){
							this.$emit('success', res.data, this.mode)
							this.visible = false;
							this.$message.success("操作成功")
						}else{
							this.$alert(res.message, "提示", {type: 'error'})
						}
					}
				})
			},
			//表单注入数据
			setData(data){
				// this.form.id = data.id
				// this.form.label = data.label
				// this.form.status = data.status
				// this.form.sort = data.sort
				// this.form.parentId = data.parentId
				// this.form.remark = data.remark

				//可以和上面一样单个注入，也可以像下面一样直接合并进去
				Object.assign(this.form, data)
			},
			getSubmitApi(model, data){
				if (model == 'edit'){
					console.log(data)
					return this.$API.badmin.action.update.put(data['id'], data)
				}else if (model == 'add'){
					return this.$API.badmin.action.create.post(data)
				}
			}
		}
	}
</script>

<style>
</style>
