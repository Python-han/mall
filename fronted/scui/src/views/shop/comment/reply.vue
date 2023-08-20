<template>
    <el-dialog title="回复" v-model="visible" :width="500" destroy-on-close @closed="$emit('closed')">
        <el-form>
            <el-input v-model="form.reply" placeholder="请输入回复内容" type="textarea" clearable></el-input>
        </el-form>
        <template #footer>
			<el-button @click="visible=false" >取 消</el-button>
			<el-button type="primary" :loading="isSaveing" @click="submit()">保 存</el-button>
		</template>
    </el-dialog>
</template>

<script>
export default {
    emits: ['closed'],
    data() {
        return {
            visible: false,
            isSaveing: false,
            form: {
                reply: ""
            }
        }
    },
    methods:{
        //显示
		open(){
			this.visible = true;
			return this
		},
        //表单注入数据
		setData(data){
			//可以和上面一样单个注入，也可以像下面一样直接合并进去
			Object.assign(this.form, data)
		},
        submit(){
            this.$API.comment.comment.partial_update.patch(this.form.id, {'reply': this.form.reply}).then(res => {
                if (res.status == 200) {
                    this.$emit('success', res.data)
					this.visible = false;
					this.$message.success("操作成功")
                }
            })
        }
    }
}
</script>