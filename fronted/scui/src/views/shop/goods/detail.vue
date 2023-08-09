<template>
	<sc-page-header :title="form.id ? '编辑商品':'新增商品'" description="" icon="el-icon-goods">
		<template #main>
			<router-link :to="{name: 'shopGoods'}">
				<el-button size="small" icon="el-icon-back">返回</el-button> 
			</router-link>
		</template>
	</sc-page-header>

	<el-main>
		<el-card shadow="never">
			<el-form ref="form" :model="form" :rules="rules" label-width="100px">
				<el-tabs v-model="activeName" @tab-click="handleTabClick">
					<el-tab-pane label="基础信息" name="base">
						<el-row>
							<el-col :span="12" :xs="24">
								<el-form-item label="商品分类" prop="category">
									<el-tree-select
										v-model="form.category"
										:data="categoryDatas"
										:render-after-expand="false"
										:props="categoryProps"
										:clearable="true"
										multiple
    									filterable
										style="width: 100%;"
										placeholder="请选择..."
									>
									</el-tree-select>
								</el-form-item>
								<el-form-item label="商品品牌">
									<el-select v-model="form.brand" filterable placeholder="请选择..." style="width: 100%;">
										<el-option
											v-for="item in brandOptions"
											:key="item.id"
											:label="item.name"
											:value="item.id"
										/>
									</el-select>
								</el-form-item>
								<el-form-item label="标题" prop="title">
									<el-input v-model="form.title" placeholder="请输入商品标题"></el-input>
								</el-form-item>
								<el-form-item label="副标题">
									<el-input v-model="form.subtitle" placeholder="请输入商品副标题"></el-input>
								</el-form-item>
								<el-form-item label="单位" prop="unit">
									<el-input v-model="form.unit" placeholder="请输入商品单位"></el-input>
								</el-form-item>
								<el-form-item label="商品轮播图" prop="images">
									<sc-upload-multiple
										v-model="form.images" 
										draggable 
										:limit="10"
										tip="最多上传10个文件,单个文件不要超过10M,请上传图像格式文件">
									</sc-upload-multiple>
								</el-form-item>
								<el-form-item label="商品状态">
									<el-radio-group v-model="form.status">
										<el-radio :label="true">上架</el-radio>
										<el-radio :label="false">下架</el-radio>
									</el-radio-group>
								</el-form-item>
								<el-form-item>
									<el-button @click="activeName='sku'" type="primary">下一步</el-button>
								</el-form-item>
							</el-col>
						</el-row>
						
					</el-tab-pane>
					<el-tab-pane label="规格库存" name="sku">
						<el-row>
							<el-col :span="12" :xs="24">
								<el-form-item label="商品规格">
									<el-radio-group v-model="form.skutype">
										<el-radio :label="0">单规格</el-radio>
										<el-radio :label="1">多规格</el-radio>
									</el-radio-group>
								</el-form-item>
								<div v-if="!form.skutype">
									<el-form-item label="图片">
										<sc-upload :autoUpload="false" ref="uploadRef" v-model="form.img" :width="80" :height="80"></sc-upload>
									</el-form-item>
									<el-form-item label="售价">
										<el-input-number v-model="form.price" controls-position="right" :min="0" :precision="2" :step="1" style="width: 100%;"></el-input-number>
									</el-form-item>
									<el-form-item label="成本价">
										<el-input-number v-model="form.cost_price" controls-position="right" :min="0" :precision="2" :step="1" style="width: 100%;"></el-input-number>
									</el-form-item>
									<el-form-item label="原价">
										<el-input-number v-model="form.retail_price" controls-position="right" :min="0" :precision="2" :step="1" style="width: 100%;"></el-input-number>
									</el-form-item>
									<el-form-item label="库存">
										<el-input-number v-model="form.stock" controls-position="right" :min="0" style="width: 100%;"></el-input-number>
									</el-form-item>
									<el-form-item label="销量">
										<el-input-number v-model="form.sales" controls-position="right" :min="0" style="width: 100%;"></el-input-number>
									</el-form-item>
									<el-form-item label="重量">
										<el-input-number v-model="form.weight" controls-position="right" :min="0" :precision="2" :step="1" style="width: 100%;"></el-input-number>
									</el-form-item>
									<el-form-item label="体积">
										<el-input-number v-model="form.vol" controls-position="right" :min="0" :precision="2" :step="1" style="width: 100%;"></el-input-number>
									</el-form-item>
									<el-form-item label="编号">
										<el-input v-model="form.item" placeholder="请输入商品编号"></el-input>
									</el-form-item>
								</div>
								<div v-else>
									<sku-form></sku-form>
								</div>
								<el-form-item>
									<el-button @click="activeName='base'">上一步</el-button>
									<el-button @click="activeName='content'" type="primary">下一步</el-button>
								</el-form-item>
							</el-col>
						</el-row>
					</el-tab-pane>
					<el-tab-pane label="商品详情" name="content">
						<el-form-item label="详情" prop="content">
							<sc-editor v-model="form.content" placeholder="请输入" :templates="templates" :height="800"></sc-editor>
						</el-form-item>
						<el-form-item>
							<el-button @click="activeName='sku'">上一步</el-button>
							<el-button @click="activeName='express'" type="primary">下一步</el-button>
						</el-form-item>
					</el-tab-pane>
					<el-tab-pane label="物流设置" name="express">
						<el-row>
							<el-col :span="12" :xs="24">
								<el-form-item label="物流方式">
									<el-radio-group v-model="form.expresstype">
										<el-radio :label="0">快递</el-radio>
										<!-- <el-radio :label="1">到店核销</el-radio> -->
									</el-radio-group>
								</el-form-item>
								<el-form-item label="运费设置">
									<el-radio-group v-model="form.freighttype">
										<el-radio :label="0">固定运费</el-radio>
										<!-- <el-radio :label="1">运费模板</el-radio> -->
									</el-radio-group>
								</el-form-item>
								<el-form-item v-if="!form.freighttype">
									<el-input-number v-model="form.freight" controls-position="right" :min="0" :precision="2" :step="1" style="width: 100%;"></el-input-number>
								</el-form-item>
								<el-form-item>
									<el-button @click="activeName='content'">上一步</el-button>
									<el-button @click="activeName='other'" type="primary">下一步</el-button>
								</el-form-item>
							</el-col>
						</el-row>
					</el-tab-pane>
					<!-- <el-tab-pane label="营销设置" name="markting">markting</el-tab-pane> -->
					<el-tab-pane label="其他设置" name="other">
						<el-row>
							<el-col :span="12" :xs="24">
								<el-form-item label="商品关键字">
									<el-input v-model="form.keywords" placeholder="请输入商品关键字"></el-input>
								</el-form-item>
								<el-form-item label="商品简介">
									<el-input v-model="form.desc" placeholder="请输入商品简介" 
										:autosize="{ minRows: 2, maxRows: 4 }" type="textarea">
									</el-input>
								</el-form-item>
								<el-form-item>
									<el-button @click="activeName='express'">上一步</el-button>
									<el-button @click="onsubmit" type="primary">保存</el-button>
								</el-form-item>
							</el-col>
						</el-row>
					</el-tab-pane>
				</el-tabs> 
				
			</el-form>
		</el-card>
	</el-main>
</template>

<script>
	import { RouterLink } from "vue-router"
	import { defineAsyncComponent } from 'vue';
	import skuForm from "./skuForm.vue";

	const scEditor = defineAsyncComponent(() => import('@/components/scEditor'));
	
	export default {
		name: 'goodsDetail',
		components:{
			RouterLink,
			scEditor,
			skuForm
		},
		data() {
			return {
				form:{
					id: this.$route.query.id,
					title: "",
					subtitle: "",
					category: [],
					brand: null,
					unit: "",
					status: true,
					images: [],
					stock: 0,
					sales: 0,
					img: null,
					price: 0,
					retail_price: 0,
					cost_price: 0,
					item: "",
					weight: 0,
					vol: 0,
					skutype: 0,
					content: "",
					expresstype: 0,
					freighttype: 0,
					freight: 0
				},
				activeName: "base",
				templates: [],
				brandOptions: [],
				categoryDatas: [],
				categoryProps: {
					label: "name",
					value: "id",
					children: "children"
				},
				rules: {
					category: [
						{ required: true, message: '请选择商品分类',  }
					],
					title: [
						{ required: true, message: '请输入商品标题',  }
					],
					unit: [
						{ required: true, min: 1, max: 5, message: '范围在1至3位' }
					],
					images: [
						{ required: true, message: '请添加商品轮播图' }
					],
					content: [
						{ required: true, message: '请输入商品详情'  }
					],
				}
			}
		},
		created() {
			this.getBrands()
			this.getCategory()
			this.getGoodsSpu()
		},
		mounted() {
			//修改tab名称
			this.$store.commit("updateViewTagsTitle", this.form.id?`商品编辑ID:${this.form.id}`:"商品新增")
		},
		methods: {
			// 获取品牌数据
			async getBrands(){
				const res = await this.$API.shop.brand.list.get({pageSize: 1000})
				this.brandOptions = res.data.results
			},

			// 获取品牌数据
			async getCategory(){
				const res = await this.$API.shop.category.list.get({pageSize: 1000})
				this.categoryDatas = res.data.results
			},

			// 获取详情数据
			async getGoodsSpu(){
				if (this.form.id){
					const res = await this.$API.shop.spu.read.get(this.form.id)
					this.form = res.data
					this.form.freight = parseFloat(res.data.freight)
					if (!res.data.skutype && res.data.baykeshopsku_set.length == 1){
						let sku = res.data.baykeshopsku_set[0]
						this.form.price = parseFloat(sku.price)
						this.form.cost_price = parseFloat(sku.cost_price)
						this.form.retail_price = parseFloat(sku.retail_price)
						this.form.weight = parseFloat(sku.weight)
						this.form.vol = parseFloat(sku.vol)
						this.form.item = sku.item
						this.form.img = sku.img
					}
				}
			},

			// tab切换回调
			handleTabClick(tab){
				console.log(tab)
			},

			// 提交表单
			onsubmit(){
				this.$refs.form.validate(async (valid) => {
					if (valid) {
						this.$API.shop.spu.create.post(this.form).then(spures => {
							if (spures.status == 201){
								if (!this.form.skutype){
									// 组装数据格式
									let _sku = {
										spu: spures.data.id,
										stock: this.form.stock,
										sales: 0,
										price: this.form.price,
										cost_price: this.form.cost_price,
										retail_price: this.form.retail_price,
										item: this.form.item,
										weight: this.form.weight,
										vol: this.form.vol,
										status: true
									}
									const sendData = new FormData()
									if (this.$refs.uploadRef.file){
										sendData.append('img', this.$refs.uploadRef.file.raw)
									}
									for (const key in _sku) {
										sendData.append(key, this.form[key]);
									}
									// 调用sku的保存接口，保存单规格
									sendData.set("spu", Number(spures.data.id))
									this.$API.shop.sku.create.post(sendData).then(skures => {
										if (skures.status == 201){
											console.log(skures)
											this.$message.success("单规格保存成功")
										}
									})
								}
								this.$message.success("全部验证通过,并且已经保存")
							}
						})
						
					}else{
						this.$message.warning("表单填写有误，请检查！")
						return false;
					}
				})
			}
		}
	}
</script>

<style>
.el-upload--picture-card{
	width: 80px !important;
	height: 80px !important;
}
.el-upload-list--picture-card .el-upload-list__item {
	width: 80px !important;
	height: 80px !important;
}
</style>

<style>
</style>
