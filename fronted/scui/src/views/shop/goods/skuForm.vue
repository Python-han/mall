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
            style="width: 40%;"
        >
            <el-option
                v-for="item in specsData"
                :key="item.id"
                :label="item.name"
                :value="item"
            />
        </el-select>
        <!-- <el-button type="primary"  @click="addSpec" style="margin-left: 10px;">生成</el-button> -->
        <!-- <div v-if="specs.length" style="display: block;">
            <div class="sku-value" v-for="item, index in specs" :key="item.id">
                <p>{{ item.name }}</p>
                    <el-tag
                        v-for="tag, indexn in item.baykeshopspecvalue_set"
                        :key="tag.id"
                        closable
                        :disable-transitions="false"
                        @close="handleClose(item.baykeshopspecvalue_set, tag, indexn)"
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
        </div> -->
    </el-form-item>

    <el-form-item prop="specs">
        <div v-if="specs.length" style="display: block;">
            <div class="sku-value" v-for="item, index in specs" :key="item.id">
                <p>{{ item.name }}</p>
                    <el-tag
                        v-for="tag, indexn in item.baykeshopspecvalue_set"
                        :key="tag.id"
                        closable
                        :disable-transitions="false"
                        @close="handleClose(item.baykeshopspecvalue_set, tag, indexn)"
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

    <el-form-item prop="skuSpecs" v-if="skuSpecs.length">
        <sc-form-table ref="skuFormTableRef" v-model="skuSpecs" :addTemplate="addTemplate" placeholder="暂无数据" :hideAdd="true" :hideDelete="true" @rowDel="deleteRow">
            <el-table-column prop="spectype" label="商品规格" width="240">
				<template #default="scope">
					<el-select v-model="scope.row.spectype" placeholder="请选择" multiple :disabled="true">
						<el-option v-for="item in specvalues" :key="item.id" :label="item.value" :value="item.id"></el-option>
					</el-select>
				</template>
			</el-table-column>

            <el-table-column prop="img" label="图片" width="105">
				<template #default="scope">
                    <sc-upload :autoUpload="false" :ref="`skuUploadRef${scope.$index}`" v-model="scope.row.img" :width="80" :height="80" :before-upload="onUpload"></sc-upload>
                </template>
			</el-table-column>

            <el-table-column prop="price" label="售价" width="180">
				<template #default="scope">
                    <el-input-number v-model="scope.row.price" controls-position="right" :min="0"></el-input-number>
				</template>
			</el-table-column>
            <el-table-column prop="cost_price" label="成本价" width="180">
				<template #default="scope">
                    <el-input-number v-model="scope.row.cost_price" controls-position="right" :min="0"></el-input-number>
				</template>
			</el-table-column>
            <el-table-column prop="retail_price" label="零售价" width="180">
				<template #default="scope">
                    <el-input-number v-model="scope.row.retail_price" controls-position="right" :min="0"></el-input-number>
				</template>
			</el-table-column>
            <el-table-column prop="stock" label="库存" width="180">
				<template #default="scope">
                    <el-input-number v-model="scope.row.stock" controls-position="right" :min="0"></el-input-number>
				</template>
			</el-table-column>
            <el-table-column prop="sales" label="销量" width="180">
				<template #default="scope">
                    <el-input-number v-model="scope.row.sales" controls-position="right" :min="0"></el-input-number>
				</template>
			</el-table-column>
            <el-table-column prop="weight" label="重量" width="180">
				<template #default="scope">
                    <el-input-number v-model="scope.row.weight" controls-position="right" :min="0"></el-input-number>
				</template>
			</el-table-column>
            <el-table-column prop="vol" label="体积" width="180">
				<template #default="scope">
                    <el-input-number v-model="scope.row.vol" controls-position="right" :min="0"></el-input-number>
				</template>
			</el-table-column>
            <el-table-column prop="item" label="商品编号" width="180">
				<template #default="scope">
                    <el-input v-model="scope.row.item"></el-input>
				</template>
			</el-table-column>
            <el-table-column prop="status" label="状态" width="80" align="center">
				<template #default="scope">
					<el-switch v-model="scope.row.status"></el-switch>
				</template>
			</el-table-column>
        </sc-form-table>
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
            inputValue: [],
            addTemplate: {
                spectype: [],
				price: 0,
                cost_price: 0,
                retail_price: 0,
                stock: 0,
                item: '',
                weight: 0,
                vol: 0,
                sales: 0,
                status: true
			},
            skuSpecs: [],
            specvalues: [],
        }
    },
    created() {
        this.getSpecsData()
    },

    watch: {
        skuSpecs: {
            handler(val){
                console.log(val)
            },
            immediate: true,
            deep: true
        },
    },

    methods: {
        // 获取规格数据
        async getSpecsData(){
            const res = await this.$API.shop.spec.list.get({pageSize: 1000})
            this.specsData = res.data.results
        },

        // 删除规格属性
        handleClose(items, tag, indexn){
            items.splice(indexn, 1)
            this.specvalues.forEach((el, i) => {
                if (el.id == tag.id){
                    // 从数据库删除，这里不建议直接操作数据库，可能会影响其他商品的规格完整性
                    // this.$API.shop.specvalue.remove.delete(tag.id).then(res => {
					// 	if (res.status == 204){
                    //         this.specvalues.splice(i, 1)
					// 		this.$message.success("删除成功")
					// 	}	
					// })

                    // 前端删除
                    this.specvalues.splice(i, 1)  
                }
            })
            // 生成规格
            this.addSpec()
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
                // 动态push进去
                this.specs[index].baykeshopspecvalue_set.push({value:this.inputValue[index]})
                // 通过接口保存到数据库,这个接口后端会自动判断存在就修改，不存在则添加
                this.$API.shop.spec.update.put(
                    this.specs[index].id, 
                    {
                        name:this.specs[index].name, 
                        baykeshopspecvalue_set: this.specs[index].baykeshopspecvalue_set
                    }
                ).then(res => {
                    this.specs[index].baykeshopspecvalue_set = res.data.baykeshopspecvalue_set
                    // 动态添加到specvalues
                    this.specs[index].baykeshopspecvalue_set.forEach(item => {
                        if (!this.specvalues.includes(item)){
                            this.specvalues.push(item)
                        }
                    })
                    // 自动生成
                    this.addSpec()
                })
                // 删除表单值
                this.inputValue.splice(index, 1)
            }
            // 隐藏输入框
            this.specs[index].inputVisible = false
        },

        // 选择下拉菜单change
        onChange(){
            this.specs.forEach(el => {
                el.baykeshopspecvalue_set.forEach(item => {
                    if (!this.specvalues.includes(item)){
                        this.specvalues.push(item)
                    }
                })
            })
            // 生成规格
            this.addSpec()
        },

        // 生成规格
        addSpec(){
            let _values = []
            if (this.specs.length){
                this.arrp(this.specs).forEach(sp => {
                    if (sp.id) {
                        _values.push({
                            spectype: [sp.id],
                            price: 0,
                            cost_price: 0,
                            retail_price: 0,
                            stock: 0,
                            item: '',
                            weight: 0,
                            vol: 0,
                            sales: 0,
                            img: '',
                            status: true
                        })
                    }else if (sp.length){
                        _values.push({
                            spectype: this.getSpecType(sp),
                            price: 0,
                            cost_price: 0,
                            retail_price: 0,
                            stock: 0,
                            item: '',
                            weight: 0,
                            vol: 0,
                            sales: 0,
                            img: '',
                            status: true
                        })
                    }
                    
                })
            }
            this.skuSpecs = _values
        },

        // 删除表格表单
        deleteRow(row, index){
			this.$refs.skuFormTableRef.deleteRow(index)
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

        // 组装下拉框的默认值
        getSpecType(items){
            let ids = []
            items.forEach(element => {
                ids.push(element.id)
            });
            return ids
        },

        onUpload(val){
            console.log(val)
        }

    },
}
</script>

<style>

.sku-value span {
    margin-right: 5px;
}
</style>