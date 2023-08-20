<template>
	<el-container>
		<el-header>
			<div class="left-panel">
				<!-- <el-button type="primary" icon="el-icon-plus" @click="add">新增</el-button> -->
				<el-button type="danger" plain icon="el-icon-delete" :disabled="selection.length==0" @click="batch_del">批量删除</el-button>
			</div>
			<div class="right-panel">
				<div class="right-panel-search">
					<el-input v-model="search.keyword" placeholder="分类名称" clearable></el-input>
					<el-button type="primary" icon="el-icon-search" @click="upsearch"></el-button>
				</div>
			</div>
		</el-header>
		<el-main class="nopadding">
			<scTable ref="table" :apiObj="apiObj" row-key="id" @selection-change="selectionChange">
				<el-table-column type="selection" width="50"></el-table-column>
				<el-table-column label="ID" prop="id" width="250"></el-table-column>
				<el-table-column label="评论用户" prop="owner" width="250">
					<template #default="scope">
						<span>{{ scope.row.owner.username }}</span>
					</template>
				</el-table-column>
				<el-table-column label="评论详情" prop="content" width="250"></el-table-column>
				<el-table-column label="评分" prop="comment_choices" width="150"></el-table-column>
				<el-table-column label="回复" prop="reply" width="250"></el-table-column>
				<el-table-column label="创建时间" prop="add_date" width="180"></el-table-column>
				<el-table-column label="操作" fixed="right" align="right" width="170">
					<template #default="scope">
						<el-button-group>
							<!-- <el-button text type="primary" size="small" @click="table_show(scope.row, scope.$index)">查看</el-button> -->
							<!-- <el-button text type="primary" size="small" @click="table_edit(scope.row, scope.$index)">回复</el-button> -->
							<el-button text type="primary" size="small" @click="reply_edit(scope.row, scope.$index)" v-if="!scope.row.reply">回复</el-button>
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

	<!-- <save-dialog v-if="dialog.save" ref="saveDialog" @success="handleSaveSuccess" @closed="dialog.save=false"></save-dialog> -->
	<reply-dialog v-if="dialog.reply" ref="replyDialog" @success="handleReplySuccess" @closed="dialog.reply=false"></reply-dialog>
</template>

<script>
	import saveDialog from './save'
	import replyDialog from './reply.vue'

	export default {
		name: 'shopComment',
		components: {
			saveDialog,
			replyDialog,
		},
		data() {
			return {
				dialog: {
					save: false,
					reply: false
				},
				apiObj: this.$API.comment.comment.list,
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
				var res = await this.$API.comment.comment.remove.delete(row.id);
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
					this.$API.comment.comment.remove.batch_delete({ids:this.ids}).then(res => {
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
			//本地更新数据
			handleSaveSuccess(data, mode){
				if(mode=='add'){
					this.$refs.table.refresh()
				}else if(mode=='edit'){
					this.$refs.table.refresh()
				}
			},
			// 评论回调
			handleReplySuccess(data){
				this.$refs.table.refresh()
			},
			// 回复
			reply_edit(row){
				this.dialog.reply = true
				this.$nextTick(() => {
					this.$refs.replyDialog.open().setData(row)
				})
			}
		}
	}
</script>

<style scoped>
.image-slot{
	line-height: 30px;
}
</style>
