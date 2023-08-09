<template>
    <el-form-item label="选择规格" class="sku-specs">
        <el-select 
            v-model="specs" 
            value-key="id" 
            multiple
            placeholder="请选择规格..." 
            @change="onChange"
            filterable
            clearable
            style="width: 80%;">
            <el-option
                v-for="item in specsData"
                :key="item.id"
                :label="item.name"
                :value="item"
            />
        </el-select>
        <el-button type="primary"  @click="addSpec" style="margin-left: 10px;">添加规格</el-button>
        <div v-if="specs.length" style="display: block;">
            <div class="sku-value" v-for="item, index in specs" :key="item.id">
                <p>{{ item.name }}</p>
                    <el-tag
                        v-for="tag, indexn in item.baykeshopspecvalue_set"
                        :key="tag.id"
                        closable
                        :disable-transitions="false"
                        @close="handleClose(item.baykeshopspecvalue_set, indexn)"
                    >
                        {{ tag.value }}
                    </el-tag>
                    <el-input
                        v-if="item.inputVisible"
                        ref="tagInputRef"
                        v-model="inputValue[index]"
                        size="small"
                        @keyup.enter="handleInputConfirm(index)"
                        @blur="handleInputConfirm(index)"
                        style="width: auto;"
                    />
                <el-button v-else size="small" @click="showInput(index)">
                    + 添加
                </el-button>
            </div>
        </div>

    </el-form-item>
</template>

<script>
export default {
    name: "skuForm",
    components: {},
    data() {
        return {
            specs: [],
            specsData: [],
            inputVisible: false,
            inputValue: []
        }
    },
    created() {
        this.getSpecsData()
    },
    methods: {
        // 获取规格数据
        async getSpecsData(){
            const res = await this.$API.shop.spec.list.get({pageSize: 1000})
            this.specsData = res.data.results
        },

        // 删除规格属性
        handleClose(items, indexn){
            items.splice(indexn, 1)
        },

        // 点击显示输入框
        showInput(index){
            this.specs[index]['inputVisible'] = true
            this.$nextTick(() => {
                this.$refs.tagInputRef[0].input.focus()
            })
            
        },

        // 规格输入完毕回调
        handleInputConfirm(index){
            if (this.inputValue[index]) {
                this.specs[index].baykeshopspecvalue_set.push({value:this.inputValue[index]})
                this.inputValue.splice(index, 1)
            }
            this.specs[index].inputVisible = false
        },

        // 选择下拉菜单change
        onChange(val){
            console.log(val)
        },

        addSpec(){
            console.log("添加规格")
        }
        
    },
}
</script>

<style>
/* .sku-specs{
    display: flex;
} */
.sku-value p {
    margin: 5px 0;
}

.sku-value span {
    margin-right: 5px;
}
</style>