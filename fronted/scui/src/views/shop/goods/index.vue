<template>
	<el-container>
		<el-header class="header-tabs">
			<el-tabs type="card" v-model="groupId" @tab-change="tabChange">
				<el-tab-pane label="出售中" name="1"></el-tab-pane>
				<el-tab-pane label="仓库中" name="2"></el-tab-pane>
				<el-tab-pane label="已售罄" name="3"></el-tab-pane>
				<el-tab-pane label="警戒库存" name="4"></el-tab-pane>
				<el-tab-pane label="回收站" name="5"></el-tab-pane>
			</el-tabs>
		</el-header>
		<el-header style="height: auto;">
			<sc-select-filter :data="filterData" :label-width="80" @on-change="filterChange"></sc-select-filter>
		</el-header>

		<el-header>
			<div class="left-panel">
				<!-- <el-button type="primary" icon="el-icon-plus" @click="add">新增</el-button> -->
				<el-button type="primary" icon="el-icon-plus" @click="addPage">新增</el-button>
				<el-button type="danger" plain icon="el-icon-delete" :disabled="selection.length==0" @click="batch_del">批量删除</el-button>
			</div>
			<div class="right-panel">
				<div class="right-panel-search">
					<el-input v-model="search.keyword" placeholder="品牌名称" clearable></el-input>
					<el-button type="primary" icon="el-icon-search" @click="upsearch"></el-button>
				</div>
			</div>
		</el-header>
		<el-main class="nopadding">
			<scTable ref="table" :apiObj="apiObj" row-key="id" @selection-change="selectionChange" :params="{'groupId': '1'}">
				<el-table-column type="selection" width="50"></el-table-column>
				<el-table-column label="ID" prop="id" width="50"></el-table-column>
				<el-table-column label="标题" prop="title" width="300"></el-table-column>
				<el-table-column label="商品图" prop="images" width="150">
					<template #default="scope">
						<el-image :src="img(scope.row.images)" style="width: 50px; height: 50px" fit="cover" :preview-src-list="imgs(scope.row.images)" :preview-teleported="true">
							<template #placeholder>
								<div class="image-slot" style="line-height: 50px;">-</div>
							</template>
							<template #error>
								<div class="image-slot" style="line-height: 50px;">-</div>
							</template>
						</el-image>
					</template>
				</el-table-column>
				<el-table-column label="库存" prop="stock" width="80"></el-table-column>
				<el-table-column label="销量" prop="sales" width="80"></el-table-column>
				<el-table-column label="排序" prop="sort" width="100"></el-table-column>
				<el-table-column label="状态" prop="status" width="150">
					<template #default="scope">
						<el-switch v-model="scope.row.status" @change="changeSwitch($event, scope.row)" 
							:loading="scope.row.$switch_status" 
							:active-value="true" :inactive-value="false"
							active-text="上架" inactive-text="下架"
							inline-prompt
							>
						</el-switch>
					</template>
				</el-table-column>
				<el-table-column label="创建时间" prop="add_date" width="180"></el-table-column>
				<el-table-column label="操作" fixed="right" align="right" width="270">
					<template #default="scope">
						<el-button-group>
							<el-button text type="primary" size="small" @click="table_show(scope.row, scope.$index)">查看</el-button>
							<el-button text type="primary" size="small" @click="table_edit_page(scope.row, scope.$index)">编辑</el-button>
							<el-popconfirm title="确定删除吗？" @confirm="table_del(scope.row, scope.$index)">
								<template #reference>
									<el-button text type="primary" size="small">删除</el-button>
								</template>
							</el-popconfirm>
						</el-button-group>
					</template>
				</el-table-column>

			</scTable>
		</el-main>
	</el-container>
</template>

<script>
	// import saveDialog from './save'
	import scSelectFilter from '@/components/scSelectFilter'

	export default {
		name: 'shopGoods',
		components: {
			// saveDialog,
			scSelectFilter
		},
		data() {
			return {
				dialog: {
					save: false
				},
				apiObj: this.$API.shop.spu.list,
				selection: [],
				search: {
					keyword: null
				},
				ids: [],
				groupId: "1",
				filterData: [
					{
						title: "所属分类",
						key: "category",
						multiple: true,
						options: [
							{
								label: "全部",
								value: 0
							}
						]
					},
					{
						title: "所属品牌",
						key: "brand",
						options: [
							{
								label: "全部",
								value: 0
							}
						]
					}
				],
			}
		},
		computed:{
			
		},
		created(){
			this.getGoodsCategory()
			this.getBrands()
		},
		methods: {
			img(images){
				return images.length ? images[0].url : ""
			},
			imgs(images){
				let items = []
				if (images.length){
					images.forEach(el => {
						items.push(el.url)
					})
				}
				return items
			},
			//页面新增
			addPage(){
				this.$router.push({
					path: '/shop/goods/detail',
				})
			},
			//页面编辑
			table_edit_page(row){
				this.$router.push({
					path: '/shop/goods/detail',
					query: {
						id: row.id
					}
				})
			},
			//查看
			table_show(row){
				this.dialog.save = true
				this.$nextTick(() => {
					this.$refs.saveDialog.open('show').setData(row)
				})
			},
			//删除
			async table_del(row){
				// var reqData = {id: row.id}
				var res = await this.$API.shop.spu.remove.delete(row.id);
				if(res.status == 204){
					this.$refs.table.refresh()
					this.$message.success("删除成功")
				}else{
					this.$alert(res.message, "提示", {type: 'error'})
				}
			},
			//批量删除
			async batch_del(){
				this.$confirm(`确定删除选中的 ${this.selection.length} 项吗？如果删除项中含有子集将会被一并删除`, '提示', {
					type: 'warning'
				}).then(() => {
					const loading = this.$loading();
					this.$API.shop.spu.remove.batch_delete({ids:this.ids}).then(res => {
						if (res.status == 204){
							this.$refs.table.refresh()
							loading.close();
							this.$message.success("操作成功")
						}
					})
				}).catch(() => {

				})
			},
			//表格选择后回调事件
			selectionChange(selection){
				this.selection = selection;
				this.selection.forEach(el => {
					this.ids.push(el.id)
				})
			},
			//搜索
			upsearch(){
				this.$refs.table.upData({search: this.search.keyword})
			},
			//标签切换
			tabChange(name){
				var params = {
					groupId: name
				}
				this.$refs.table.reload(params)
			},

			// 筛选
			filterChange(data){
				this.$refs.table.upData(data)
			},
		
			//本地更新数据
			handleSaveSuccess(data, mode){
				if(mode=='add'){
					this.$refs.table.refresh()
				}else if(mode=='edit'){
					this.$refs.table.refresh()
				}
			},

			//表格内上架开关
			changeSwitch(val, row){
				// row.status = row.status
				row.$switch_status = true;
				this.$API.shop.spu.partial_update.patch(row.id, {status:val}).then(res => {
					if (res.status == 200){
						delete row.$switch_status;
						row.status = val;
						this.$refs.table.refresh()
						this.$message.success("操作成功")
					}else{
						delete row.$switch_status;
						row.status = !val;
						this.$message.success("操作失败，请检查！")
					}
				})
			},

			// 获取分类数据
			async getGoodsCategory(){
				const res = await this.$API.shop.category.list.get()
				let options = this.treeToArray(res.data.results) 
				options.forEach(el => {
					this.filterData[0]['options'].push({
						label: el.name,
						value: el.id
					})
				})
			},
			// 获取品牌数据
			async getBrands(){
				const res = await this.$API.shop.brand.list.get()
				// let options = this.treeToArray(res.data.results) 
				res.data.results.forEach(el => {
					this.filterData[1]['options'].push({
						label: el.name,
						value: el.id
					})
				})
			},
			// 扁平化树状结构
			treeToArray(tree) {
				return tree.reduce((res, item) => {
					const { children, ...i } = item
					return res.concat(i, children && children.length ? this.treeToArray(children) : [])
				}, [])
			}
		}
	}
</script>

<style>
</style>
