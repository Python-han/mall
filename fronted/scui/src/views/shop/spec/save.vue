<template>
	<el-dialog :title="titleMap[mode]" v-model="visible" :width="500" destroy-on-close @closed="$emit('closed')">
		<el-form :model="form" :rules="rules" :disabled="mode=='show'" ref="dialogForm" label-width="100px">
			<el-form-item label="规格名称" prop="name">
				<el-input v-model="form.name" placeholder="请输入规格名称" clearable></el-input>
			</el-form-item>
			<el-form-item label="规格选项" prop="baykeshopspecvalue_set">
				<sc-form-table ref="table" v-model="form.baykeshopspecvalue_set" :addTemplate="addTemplate" placeholder="暂无数据" @rowDel="deleteRow">
					<!-- <el-table-column prop="value" label="ID" width="50">
						<template #default="scope">
							{{ scope.row.id }}
						</template>
					</el-table-column> -->
					<el-table-column prop="value" label="规格值" width="280">
						<template #default="scope">
							<el-input v-model="scope.row.value" placeholder="请输入规格值" :minlength="1"></el-input>
						</template>
					</el-table-column>
				</sc-form-table>
			</el-form-item>
			<el-form-item label="排序" prop="sort">
				<el-input-number v-model="form.sort" controls-position="right" :min="1" style="width: 100%;"></el-input-number>
			</el-form-item>
			<el-form-item label="是否有效" prop="status">
				<el-switch v-model="form.status" :active-value="true" :inactive-value="false"></el-switch>
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
					name: "",
					sort: 1,
					status: true,
					baykeshopspecvalue_set: [
						{	
							id: "",
							value: ""
						}
					]
				},
				addTemplate: {
					value:""
				},
				//验证规则
				rules: {
					sort: [
						{required: true, message: '请输入排序', trigger: 'change'}
					],
					name: [
						{required: true, message: '请输入规格名称'}
					],
					baykeshopspecvalue_set: [
						{required: true, message: '请输入规格值'}
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
		},
		methods: {
			//显示
			open(mode='add'){
				this.mode = mode;
				this.visible = true;
				return this
			},
			// 删除规格值
			deleteRow(row, index){
				if (row.id){
					this.$API.shop.specvalue.remove.delete(row.id).then(res => {
						if (res.status == 204){
							this.$message.success("删除成功")
						}	
					})
				}
				this.$refs.table.deleteRow(index)
			},
			//加载树数据
			// async getGroup(){
			// 	var res = await this.$API.shop.category.list.get();
			// 	this.groups = res.data.results;
			// },
			//表单提交方法
			submit(){
				this.$refs.dialogForm.validate(async (valid) => {
					if (valid) {
						this.isSaveing = true; 
						if (this.form.baykeshopspecvalue_set.length == 1 && !this.form.baykeshopspecvalue_set[0].value){
							this.$alert("规格值至少应该有一个", "提示", {type: 'error'})
							this.isSaveing = false;
							return
						}
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
					return this.$API.shop.spec.update.put(data.id, data)
				}else if (model == 'add'){
					return this.$API.shop.spec.create.post(data)
				}
			}
		}
	}
</script>

<style>
</style>
