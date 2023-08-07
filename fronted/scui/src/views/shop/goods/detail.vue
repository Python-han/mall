<template>
	<sc-page-header :title="form.id ? '编辑':'新增'" description="" icon="el-icon-goods">
		<template #main>
			<router-link :to="{name: 'shopGoods'}">
				<el-button size="small" icon="el-icon-back">返回</el-button> 
			</router-link>
		</template>
	</sc-page-header>

	<el-main>
		<el-card shadow="never">
			<el-form ref="form" label-width="100px">
				<el-tabs v-model="activeName" @tab-click="handleTabClick">
					<el-tab-pane label="基础信息" name="base">
						<el-row>
							<el-col :span="12" :xs="24">
								<el-form-item label="标题">
									<el-input v-model="form.title" placeholder="请输入商品标题"></el-input>
								</el-form-item>
								<el-form-item label="副标题">
									<el-input v-model="form.subtitle" placeholder="请输入商品副标题"></el-input>
								</el-form-item>
								<el-form-item label="单位">
									<el-input v-model="form.unit" placeholder="请输入商品单位"></el-input>
								</el-form-item>
								<el-form-item label="商品轮播图">
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
										<sc-upload v-model="form.img" :width="80" :height="80"></sc-upload>
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

								<el-form-item>
									<el-button @click="activeName='base'">上一步</el-button>
									<el-button @click="activeName='content'" type="primary">下一步</el-button>
								</el-form-item>
							</el-col>
						</el-row>
					</el-tab-pane>
					<el-tab-pane label="商品详情" name="content">
						<el-form-item label="详情">
							<sc-editor v-model="form.content" placeholder="请输入" :templates="templates" :height="800"></sc-editor>
						</el-form-item>
						<el-form-item>
							<el-button @click="activeName='sku'">上一步</el-button>
							<el-button @click="activeName='express'" type="primary">下一步</el-button>
						</el-form-item>
					</el-tab-pane>
					<el-tab-pane label="物流设置" name="express">express</el-tab-pane>
					<el-tab-pane label="营销设置" name="markting">markting</el-tab-pane>
					<el-tab-pane label="其他设置" name="other">
						<el-form-item>
							<el-button @click="onsubmit" type="primary">保存</el-button>
						</el-form-item>
					</el-tab-pane>
				</el-tabs> 
				
			</el-form>
		</el-card>
	</el-main>
</template>

<script>
	import { RouterLink } from "vue-router"
	import { defineAsyncComponent } from 'vue';
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
					unit: "",
					status: true,
					images: [],
					stock: 0,
					sales: 0,
					img: "",
					price: 0,
					retail_price: 0,
					cost_price: 0,
					item: "",
					weight: 0,
					vol: 0,
					skutype: 0,
					content: ""
				},
				activeName: "base",
				templates: []
			}
		},
		created() {

		},
		mounted() {
			//修改tab名称
			this.$store.commit("updateViewTagsTitle", this.form.id?`商品编辑ID:${this.form.id}`:"商品新增")
		},
		methods: {
			// tab切换回调
			handleTabClick(tab){
				console.log(tab)
			},

			onsubmit(){
				console.log(this.form)
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
