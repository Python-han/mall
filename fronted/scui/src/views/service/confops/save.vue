<template>
	<el-dialog :title="titleMap[mode]" v-model="visible" :width="500" destroy-on-close @closed="$emit('closed')">
		<el-form :model="form" :rules="rules" :disabled="mode=='show'" ref="dialogForm" label-width="100px">
			<!-- <el-form-item label="分类" prop="category">
				<el-cascader v-model="form.category" :options="groups" :props="groupsProps" :show-all-levels="false" clearable style="width: 100%;"></el-cascader>
			</el-form-item> -->
			<el-form-item label="字段类型" prop="field_type">
				<!-- <el-input v-model="form.name" placeholder="请输入分类名称" clearable></el-input> -->
				<el-select v-model="form.field_type" class="m-2" placeholder="Select">
					<el-option
						v-for="item in options"
						:key="item.value"
						:label="item.label"
						:value="item.value"
					/>
				</el-select>
			</el-form-item>
			<el-form-item label="配置名称" prop="name">
				<el-input v-model="form.name" placeholder="请输入分类名称" clearable></el-input>
			</el-form-item>
			<el-form-item label="别名" prop="slug">
				<el-input v-model="form.slug" placeholder="请输入分类别名" clearable></el-input>
			</el-form-item>
			<el-form-item label="值" prop="value">
				<el-input v-model="form.value" placeholder="默认值" clearable></el-input>
			</el-form-item>
			<el-form-item label="备注" prop="remark">
				<el-input v-model="form.remark" placeholder="备注" clearable></el-input>
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
					category: "",
					name: "",
					sort: 1,
					status: true,
					slug: "",
					value: "",
					remark: "",
					field_type: "input"
				},
				//验证规则
				rules: {
					sort: [
						{required: true, message: '请输入排序', trigger: 'change'}
					],
					name: [
						{required: true, message: '请输入分类名称'}
					],
					slug: [
						{required: true, message: '请输入分类别名'}
					],
					value: [
						{required: true, message: '请输入默认值'}
					],
				},
				//所需数据选项
				groups: [],
				groupsProps: {
					label: "name",
					value: "id",
					emitPath: false,
					checkStrictly: true
				},
				activeName:"input",
				options: [
					{
						label: "文本框",
						value: "input"
					},
					{
						label: "switch开关",
						value: "switch"
					},
					{
						label: "上传",
						value: "upload"
					},
					{
						label: "单选",
						value: "radio"
					},
					{
						label: "复选框",
						value: "checkbox"
					},
					{
						label: "时间",
						value: "date"
					},
					{
						label: "颜色",
						value: "color"
					},
					{
						label: "滑块",
						value: "slider"
					},
				]
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
			//加载树数据
			async getGroup(){
				var res = await this.$API.badmin.confcategory.list.get();
				this.groups = res.data.results;
			},
			//表单提交方法
			submit(){
				this.$refs.dialogForm.validate(async (valid) => {
					if (valid) {
						this.isSaveing = true; 
						// var res = await this.$API.demo.post.post(this.form);
						this.form.category = this.$route.params.id
						var res = await this.getSubmitApi(this.mode, this.form);
						this.isSaveing = false;
						if(res.status == 200 || res.status == 201){
							console.log(res.data)
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
				//可以和上面一样单个注入，也可以像下面一样直接合并进去
				Object.assign(this.form, data)
			},
			getSubmitApi(model, data){
				if (model == 'edit'){
					return this.$API.badmin.confoptions.update.put(data.id, data)
				}else if (model == 'add'){
					return this.$API.badmin.confoptions.create.post(data)
				}
			},

			// 标签页切换回调
			handleClick(tab, event){
				console.log(tab, event)
			}
		}
	}
</script>

<style>
.el-dialog__body{
	padding-top: 0;
}
</style>
