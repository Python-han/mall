<template>
	<sc-page-header :title="$route.query.mode ? '查看商品':'新增/编辑商品'" description="" icon="el-icon-goods">
		<template #main>
			<router-link :to="{name: 'shopGoods'}">
				<el-button size="small" icon="el-icon-back">返回</el-button> 
			</router-link>
		</template>
	</sc-page-header>

	<el-main>
		<el-card shadow="never">
			<el-form ref="form" :model="form" :rules="rules" label-width="100px" :disabled="$route.query.mode == 'show' ? true : false">
				<el-tabs v-model="activeName">
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
								<el-form-item label="商品关键字">
									<el-input v-model="form.keywords" placeholder="请输入商品关键字"></el-input>
								</el-form-item>
								<el-form-item label="商品简介">
									<el-input v-model="form.desc" placeholder="请输入商品简介" 
										:autosize="{ minRows: 2, maxRows: 4 }" type="textarea">
									</el-input>
								</el-form-item>
								<el-form-item label="单位" prop="unit">
									<el-input v-model="form.unit" placeholder="请输入商品单位"></el-input>
								</el-form-item>
								<el-form-item label="商品轮播图" prop="images">
									<sc-upload-multiple
										v-model="form.images" 
										draggable 
										:limit="10"
										:disabled="$route.query.mode == 'show' ? true : false"
										tip="最多上传10个文件,单个文件不要超过10M,请上传图像格式文件">
									</sc-upload-multiple>
								</el-form-item>
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
							<el-col :span="24" :xs="24">
								<el-form-item label="商品规格">
									<el-radio-group v-model="form.skutype">
										<el-radio :label="0">单规格</el-radio>
										<el-radio :label="1">多规格</el-radio>
									</el-radio-group>
								</el-form-item>
								<div v-if="!form.skutype">
									<el-form-item label="图片">
										<sc-upload ref="uploadRef" v-model="form.img" :width="80" :height="80" :disabled="$route.query.mode == 'show' ? true : false"></sc-upload>
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
									<el-form-item label="选择规格">
										<el-select v-model="modelSpec" placeholder="Select" multiple value-key="id" @change="onSpecChange">
											<el-option
												v-for="item in specOptions"
												:key="item.id"
												:label="item.name"
												:value="item"
												/>
										</el-select>
										<el-button @click="onGenter" type="primary">生成</el-button>
									</el-form-item>

									<el-form-item prop="modelSpec" v-for="item, index in modelSpec" :key="item.id">
										<div class="spec-tags">
											<p>{{ item.name }}：</p>
											<div >
												<el-tag
													v-for="tag, indexn in item.baykeshopspecvalue_set"
													:key="tag.id"
													:closable="$route.query.mode == 'show' ? false : true"
													:disable-transitions="false"
													style="margin-right: 5px;"
													:disabled="$route.query.mode == 'show' ? true : false"
													@close="handleClose(item.baykeshopspecvalue_set, tag, indexn)"
												>
													{{ tag.value }}
												</el-tag>
												<el-input
														v-if="item.inputVisible"
														ref="tagInputRef"
														v-model="inputValue[index]"
														size="small"
														:disabled="$route.query.mode == 'show' ? true : false"
														@keyup.enter="handleInputConfirm(index)"
														@blur="handleInputConfirm(index, item)"
														style="width: auto;"
													/>
												<el-button v-else size="small" @click="showInput(index)">
													+ 添加
												</el-button>
											</div>
										</div>
									</el-form-item>

									<el-form-item>
										<el-alert title="注意：如果生成的新sku规格数量小于原有sku数量，需先删除原有sku数量小于生成sku数量，否则会造成规格混乱" type="warning" v-if="form.id" />

										<sc-form-table ref="specTableRef" v-model="skuTableData" placeholder="暂无数据" :hideAdd="true" @rowDel="tabRowdel">
											<el-table-column prop="specops" label="规格" width="180">
												<template #default="scope">
													<el-select v-model="scope.row.spec_values" multiple :disabled="true" size="large" suffix-icon="" style="width:100%">
														<el-option
															v-for="item in scope.row.specops"
															:key="item.id"
															:label="item.value"
															:value="item.id"
															/>
													</el-select>
												</template>
											</el-table-column>
											<el-table-column prop="img" label="图片" width="105">
												<template #default="scope">
													<sc-upload :autoUpload="true" :ref="`skuUploadRef${scope.$index}`" v-model="scope.row.img" :width="80" :height="80"></sc-upload>
												</template>
											</el-table-column>
											<el-table-column prop="price" label="售价" >
												<template #default="scope">
													<el-input v-model="scope.row.price"></el-input>
												</template>
											</el-table-column>
											<el-table-column prop="cost_price" label="成本价">
												<template #default="scope">
													<el-input v-model="scope.row.cost_price"></el-input>
												</template>
											</el-table-column>
											<el-table-column prop="retail_price" label="划线价" >
												<template #default="scope">
													<el-input v-model="scope.row.retail_price"></el-input>
												</template>
											</el-table-column>
											<el-table-column prop="stock" label="库存">
												<template #default="scope">
													<el-input v-model="scope.row.stock"></el-input>
												</template>
											</el-table-column>
											<el-table-column prop="weight" label="重量">
												<template #default="scope">
													<el-input v-model="scope.row.weight"></el-input>
												</template>
											</el-table-column>
											<el-table-column prop="vol" label="体积">
												<template #default="scope">
													<el-input v-model="scope.row.vol"></el-input>
												</template>
											</el-table-column>
											<el-table-column prop="item" label="商品编号">
												<template #default="scope">
													<el-input v-model="scope.row.item"></el-input>
												</template>
											</el-table-column>
										</sc-form-table>
									</el-form-item>
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
							<sc-editor v-model="form.content" placeholder="请输入" :templates="templates" :height="800" ></sc-editor>
						</el-form-item>
						<!-- <el-form-item>
							<el-button @click="activeName='sku'">上一步</el-button>
							<el-button @click="activeName='express'" type="primary">下一步</el-button>
						</el-form-item> -->
						<el-form-item>
							<el-button @click="activeName='sku'">上一步</el-button>
							<el-button @click="onsubmit" type="primary">保存</el-button>
						</el-form-item>
					</el-tab-pane>
					<!-- <el-tab-pane label="物流设置" name="express">
						<el-row>
							<el-col :span="12" :xs="24">
								<el-form-item label="物流方式">
									<el-radio-group v-model="form.expresstype">
										<el-radio :label="0">快递</el-radio>
										<el-radio :label="1">到店核销</el-radio>
									</el-radio-group>
								</el-form-item>
								<el-form-item label="运费设置">
									<el-radio-group v-model="form.freighttype">
										<el-radio :label="0">固定运费</el-radio>
										<el-radio :label="1">运费模板</el-radio>
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
					</el-tab-pane> -->
					<!-- <el-tab-pane label="营销设置" name="markting">markting</el-tab-pane> -->
					<!-- <el-tab-pane label="其他设置" name="other">
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
					</el-tab-pane> -->
				</el-tabs> 
				
			</el-form>
		</el-card>
	</el-main>
</template>

<script>
	import { RouterLink } from "vue-router"
	import { defineAsyncComponent } from 'vue';
	import useTabs from '@/utils/useTabs'
	const scEditor = defineAsyncComponent(() => import('@/components/scEditor'));
	
	export default {
		name: 'goodsDetail',
		components:{
			RouterLink,
			scEditor
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
					freight: 0,
					sku_id: ''
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
				
				// 选择规格,规格的下拉选项
				specOptions: [],
				// 规格选中的响应式数据,应为spec的id数组[]
				modelSpec: [],
				skuTableData: [],
				// 编辑时缓存原有数据
				skuTableDataCache:[],
				// 添加规格输入框值
				inputValue:[],

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
				},
			}
		},
		// computed:{
		// 	sku: () => {
		// 		let _sku = {}
		// 		if (this.form.baykeshopsku_set.length == 1){
		// 			_sku = this.form.baykeshopsku_set[0]
		// 		}
		// 		return _sku
		// 	}
		// },
		created() {
			this.getBrands()
			this.getCategory()
			this.getGoodsSpu()
			this.getSpecsData()
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

			// 获取分类数据
			async getCategory(){
				const res = await this.$API.shop.category.list.get({pageSize: 1000})
				this.categoryDatas = res.data.results
			},

			// 获取规格数据
			async getSpecsData(){
				const res = await this.$API.shop.spec.list.get({pageSize: 1000})
				this.specOptions = res.data.results
			},

			// 获取详情数据
			async getGoodsSpu(){
				if (this.form.id){
					const res = await this.$API.shop.spu.read.get(this.form.id)
					this.form = res.data
					this.form.freight = parseFloat(res.data.freight)
					if (!res.data.skutype && res.data.baykeshopsku_set.length == 1){
						let sku = res.data.baykeshopsku_set[0]
						this.form.sku_id = sku.id
						this.form.price = parseFloat(sku.price)
						this.form.cost_price = parseFloat(sku.cost_price)
						this.form.retail_price = parseFloat(sku.retail_price)
						this.form.weight = parseFloat(sku.weight)
						this.form.vol = parseFloat(sku.vol)
						this.form.item = sku.item
						this.form.img = sku.img
						// this.form.baykeshopsku_set = res.data.baykeshopsku_set
					}

					// 多规格需要的数据
					this.modelSpec = res.data.specs
					this.skuTableData = res.data.skuSpecs
					this.skuTableDataCache = res.data.skuSpecs
				}
			},

			// 提交表单
			onsubmit(){
				this.$refs.form.validate(async (valid) => {
					if (valid) {
						// 组装sku的数据
						if (this.form.skutype){
							this.form['baykeshopsku_set'] = this.skuTableData
						}else{
							this.form['baykeshopsku_set'] = [{
								id: this.form.sku_id,
								price: this.form.price,
								stock: this.form.stock,
								sales: this.form.sales,
								img: this.form.img,
								retail_price: this.form.retail_price,
								cost_price: this.form.cost_price,
								item: this.form.item,
								weight: this.form.weight,
								vol: this.form.vol,
							}]
						}

						// 这个接口后端根据spu的id和每个skuid来自动判断为新增或修改，因此编辑某个spu时必须携带spu的id
						// baykeshopsku_set为sku的数组，如果sku的id存在则修改否则新增
						this.$API.shop.spu.create.post(this.form).then(res => {
							if (res.status == 200){
								this.$message.success('操作成功')
								this.$router.push({name: 'shopGoods'})
								this.$route.is = true
								useTabs.close() // 关闭当前
							}
						})
					}else{
						this.$message.warning("表单填写有误，请检查！")
						return false;
					}
				})
			},

			// 删除
			handleClose(items, tag, indexn){
				items.splice(indexn, 1)
				// this.generateSkuData(this.modelSpec)
			},

			// 笛卡尔积算法
			arrp(arr){
				//编辑原数组格式
				if(arr[0].baykeshopspecvalue_set){
					arr=arr.map((item)=>{
						return item=item.baykeshopspecvalue_set
					})
				}
				if(arr.length == 1){
					//最终合并成一个
					return arr[0];
				}else{	//有两个子数组就合并
					let arrySon = [];
					//将组合放到新数组中
					arr[0].forEach((item,index)=>{
						arr[1].forEach((item1,index1)=>{
							arrySon.push([].concat(arr[0][index],arr[1][index1]));
						})
					})
					// 新数组并入原数组,去除合并的前两个数组
					arr[0] = arrySon;
					arr.splice(1,1);
					// 递归
					return this.arrp(arr);
				}
			},

			// 选择下拉框生成
			onSpecChange(val){
				this.generateSkuData(val)
				// 刷新规格
				this.getSpecsData()
			},
			// 组装下拉框的默认值
			getSpecType(items){
				let ids = []
				items.forEach(element => {
					ids.push(element.id)
				});
				return ids
			},

			// 生成规格函数
			generateSkuData(val){
				let skuDatas = []
				if (val.length){
					this.arrp(val).forEach((items) => {
						skuDatas.push({
							spec_values: items.length ? this.getSpecType(items) : [items.id],
							specops: items.length ? items : [items]
						})
					})
				}
				this.skuTableData = skuDatas
				// 携带原有的sku数据
				if (this.form.id && this.skuTableData.length){
					for(let i=0; i < this.skuTableData.length; i++){
						if (this.skuTableDataCache[i]){
							this.skuTableData[i]["id"] = this.skuTableDataCache[i].id
							this.skuTableData[i]["price"] = this.skuTableDataCache[i].price
							this.skuTableData[i]["cost_price"] = this.skuTableDataCache[i].cost_price
							this.skuTableData[i]["retail_price"] = this.skuTableDataCache[i].retail_price
							this.skuTableData[i]["item"] = this.skuTableDataCache[i].item
							this.skuTableData[i]["weight"] = this.skuTableDataCache[i].weight
							this.skuTableData[i]["stock"] = this.skuTableDataCache[i].stock
							this.skuTableData[i]["vol"] = this.skuTableDataCache[i].vol
							this.skuTableData[i]["status"] = this.skuTableDataCache[i].status
							this.skuTableData[i]["img"] = this.skuTableDataCache[i].img
						}
					}
				}
			},

			// 点击显示输入框
			showInput(index){
				this.modelSpec[index]['inputVisible'] = true
				this.$nextTick(() => {
					this.$refs.tagInputRef[0].input.focus()
				})
			},

			// 规格输入完毕回调
			handleInputConfirm(index, item){
				if (this.inputValue[index]) {
					this.$API.shop.specvalue.create.post({spec: item.id, value:this.inputValue[index]}).then(res => {
						if (res.status == 201) {
							// console.log(res)
							this.modelSpec[index].baykeshopspecvalue_set.push({id: res.data.id, value: res.data.value})
							// this.generateSkuData(this.modelSpec)
						}
					})
					// this.modelSpec[index].baykeshopspecvalue_set.push({id: "", value:this.inputValue[index]})
					// 删除表单值
					this.inputValue.splice(index, 1)
				}
				// 隐藏输入框
				this.modelSpec[index].inputVisible = false
			},

			// 手动onGenter生成规格
			onGenter(){
				this.generateSkuData(this.modelSpec)
				if (this.skuTableData.length < this.skuTableDataCache.length){
					this.$message.warning("当前生成的sku数量少于原有sku数量，请先删除原有sku后再次生成")
					// useTabs.refresh()
				}
			},

			// 删除sku
			tabRowdel(row, index){
				if (row.id){
					this.$API.shop.sku.remove.delete(row.id).then(res => {
						if (res.status == 204){
							this.$message.success("删除成功")
						}	
					})
				}
				this.$refs.specTableRef.deleteRow(index)
			}
		},
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
.spec-tags{
	display: flex;
	flex-direction: column;
}
</style>, stringifyQuery
