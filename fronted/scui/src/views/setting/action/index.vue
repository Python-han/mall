<template>
	<el-container>
		<el-header>
			<div class="left-panel">
				<el-button type="primary" icon="el-icon-plus" @click="add">新增</el-button>
				<el-button type="danger" plain icon="el-icon-delete" :disabled="selection.length==0" @click="batch_del">批量删除</el-button>
			</div>
			<div class="right-panel">
				<div class="right-panel-search">
					<el-input v-model="search.keyword" placeholder="权限名称" clearable></el-input>
					<el-button type="primary" icon="el-icon-search" @click="upsearch"></el-button>
				</div>
			</div>
		</el-header>
		<el-main class="nopadding">
			<scTable ref="table" :apiObj="apiObj" row-key="id" @selection-change="selectionChange">
				<el-table-column type="selection" width="50"></el-table-column>
				<el-table-column label="ID" prop="id" width="50"></el-table-column>
				<el-table-column label="权限名称" prop="permission">
					<template #default="scope">
						{{ scope.row.permission.name }}
					</template>
				</el-table-column>
				<el-table-column label="权限标识" prop="permission">
					<template #default="scope">
						{{ scope.row.permission.codename }}
					</template>
				</el-table-column>

				<el-table-column label="归属应用" prop="permission">
					<template #default="scope">
						{{ scope.row.permission.content_type.app_label }}
					</template>
				</el-table-column>
				<el-table-column label="归属模型" prop="permission">
					<template #default="scope">
						{{ scope.row.permission.content_type.model }}
					</template>
				</el-table-column>
				<el-table-column label="接口别名" prop="apiname"></el-table-column>
				<el-table-column label="请求类型" prop="request_method"></el-table-column>
				<el-table-column label="备注" prop="mark"></el-table-column>
				<el-table-column label="创建时间" prop="add_date" width="180"></el-table-column>
				<el-table-column label="操作" fixed="right" align="right" width="170">
					<template #default="scope">
						<el-button-group>
							<el-button text type="primary" size="small" @click="table_show(scope.row, scope.$index)">查看</el-button>
							<el-button text type="primary" size="small" @click="table_edit(scope.row, scope.$index)">编辑</el-button>
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

	<save-dialog v-if="dialog.save" ref="saveDialog" @success="handleSaveSuccess" @closed="dialog.save=false"></save-dialog>
</template>

<script>
	import saveDialog from './save'

	export default {
		name: 'action',
		components: {
			saveDialog
		},
		data() {
			return {
				dialog: {
					save: false
				},
				apiObj: this.$API.badmin.action.list,
				selection: [],
				search: {
					keyword: null
				},
				ids: []
			}
		},
		methods: {
			//添加
			add(){
				this.dialog.save = true
				this.$nextTick(() => {
					this.$refs.saveDialog.open()
				})
			},
			//编辑
			table_edit(row){
				this.dialog.save = true
				this.$nextTick(() => {
					this.$refs.saveDialog.open('edit').setData(row)
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
				var res = await this.$API.badmin.action.remove.delete(row.id);
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
					this.$API.badmin.action.remove.batch_delete({ids:this.ids}).then(res => {
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
			//根据ID获取树结构
			filterTree(id){
				var target = null;
				function filter(tree){
					tree.forEach(item => {
						if(item.id == id){
							target = item
						}
						if(item.children){
							filter(item.children)
						}
					})
				}
				filter(this.$refs.table.tableData)
				return target
			},
			//本地更新数据
			handleSaveSuccess(data, mode){
				if(mode=='add'){
					this.$refs.table.refresh()
				}else if(mode=='edit'){
					this.$refs.table.refresh()
				}
			}
		}
	}
</script>

<style>
</style>
