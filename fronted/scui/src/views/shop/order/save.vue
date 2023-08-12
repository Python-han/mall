<template>
	<el-dialog :title="titleMap[mode]" v-model="visible" :width="500" destroy-on-close @closed="$emit('closed')">
		<el-form :model="form" :rules="rules" :disabled="mode=='show'" ref="dialogForm" label-width="100px">
			
			<el-form-item label="订单号" prop="order_sn">
				<el-input v-model="form.order_sn" :disabled="true" clearable></el-input>
			</el-form-item>
			<el-form-item label="商品总价" prop="total_price">
				<el-input-number v-model="form.total_price" controls-position="right" :precision="2" :min="1" style="width: 100%;"></el-input-number>
			</el-form-item>
			<el-form-item label="收货地址" prop="address">
				<el-input v-model="form.address" clearable></el-input>
			</el-form-item>
			<el-form-item label="订单备注" prop="mark">
				<el-input v-model="form.mark" clearable type="textarea"></el-input>
			</el-form-item>
		</el-form>
		<template #footer>
			<el-button @click="visible=false" >取 消</el-button>
			<el-button v-if="mode!='show'" type="primary" :loading="isSaveing" @click="submit">保 存</el-button>
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
					order_sn: "",
					address: "",
					mark: "",
					total_price: 0
				},
				//验证规则
				rules: {
					sort: [
						{required: true, message: '请输入排序', trigger: 'change'}
					],
					name: [
						{required: true, message: '请输入部门名称'}
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
			this.getGroup()
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
				var res = await this.$API.badmin.dept.list.get();
				this.groups = res.data.results;
			},
			//表单提交方法
			submit(){
				this.$refs.dialogForm.validate(async (valid) => {
					if (valid) {
						console.log('asdasd')
						this.isSaveing = true; 
						var res = await this.$API.shop.order.partial_update.patch(this.form.id, this.form);
						this.isSaveing = false;
						if(res.status == 200){
							this.$emit('success', this.form, this.mode)
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
				this.form.id = data.id
				this.form.order_sn = data.order_sn
				this.form.address = data.address
				this.form.total_price = parseFloat(data.total_price)
				this.form.mark = data.mark

				//可以和上面一样单个注入，也可以像下面一样直接合并进去
				// Object.assign(this.form, data)
			},
		}
	}
</script>

<style>
</style>
