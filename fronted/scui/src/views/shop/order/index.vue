<template>
    <el-container>
        <div style="padding: 10px;">
            <el-card shadow="never" header="订单筛选">
                <sc-select-filter :data="data" :selected-values="selectedValues" :label-width="80"
                    @on-change="change"></sc-select-filter>
            </el-card>
        </div>
        <el-header>
            <div class="left-panel">
                <!-- <el-button type="primary" icon="el-icon-plus" @click="add">新增</el-button> -->
                <el-button type="danger" plain icon="el-icon-delete" @click="batch_del" :disabled="!ids.length">批量删除</el-button>
            </div>
            <div class="right-panel">
                <div class="right-panel-search">
                    <el-input v-model="search.keyword" placeholder="订单号、收件人、手机号" clearable></el-input>
                    <el-button type="primary" icon="el-icon-search" @click="upsearch"></el-button>
                </div>
            </div>
        </el-header>
        <el-main class="nopadding">
            <scTable ref="table" :apiObj="apiObj" row-key="id" @selection-change="selectionChange">
                <el-table-column type="selection" width="50"></el-table-column>
                <el-table-column label="订单号" prop="order_sn" width="180"></el-table-column>
                <el-table-column label="用户" prop="owner_data" width="180"></el-table-column>
                <el-table-column label="商品信息" prop="baykeshopordersku_set">
                    <template #default="scope">
                        <el-row v-for="sku in scope.row.baykeshopordersku_set" :key="sku.id">
                            <el-col :xs="24" :md="6" :sm="4">
                                <el-image style="width: 50px; height: 50px" :src="sku.sku_json.img" fit="cover" />
                            </el-col>
                            <el-col :xs="24" :md="13" :sm="15">
                                {{ sku.sku_json.title }}
                                <span v-for="spec in sku.sku_json.spec_values" :key="spec.id">
                                    |{{ spec.value }}
                                </span>
                            </el-col>
                            <el-col :md="5"><span>¥{{ sku.sku_json.price }}x{{ sku.count }} </span></el-col>
                            <el-divider border-style="dashed" style="margin: 0;" />
                        </el-row>
                    </template>
                </el-table-column>
                <el-table-column label="实际支付" prop="total_price">
                    <template #default="scope">
                        <span v-if="scope.row.status > 1">{{ scope.row.total_price }}</span>
                        <span v-else-if="scope.row.status == 7">退款中</span>
                        <span v-else>未支付</span>
                    </template>
                </el-table-column>
                <el-table-column label="支付方式" prop="paymethod">
                    <template #default="scope">
                        <span v-if="scope.row.paymethod == 1">支付宝支付</span>
                        <span v-if="scope.row.paymethod == 2">微信支付</span>
                        <span v-if="scope.row.paymethod == 3">余额支付</span>
                    </template>
                </el-table-column>
                <el-table-column label="支付时间" prop="pay_time"></el-table-column>
                <el-table-column label="订单状态" prop="status">
                    <template #default="scope">
                        <span v-if="scope.row.status == 1">待付款</span>
                        <span v-if="scope.row.status == 2">待发货</span>
                        <span v-if="scope.row.status == 3">待收货</span>
                        <span v-if="scope.row.status == 4">待评价</span>
                        <span v-if="scope.row.status == 5">已完成</span>
                        <span v-if="scope.row.status == 6">已关闭</span>
                        <span v-if="scope.row.status == 7">退款中</span>
                    </template>
                </el-table-column>
                <el-table-column label="操作" fixed="right" align="right" width="170">
                    <template #default="scope">
                        <el-button-group>
                            <el-button text type="primary" size="small"
                                @click="table_show(scope.row, scope.$index)">查看</el-button>
                            <el-button text type="primary" size="small" v-if="scope.row.status == 1"
                                @click="table_edit(scope.row, scope.$index)">编辑</el-button>
                            <el-button text type="primary" size="small" v-if="scope.row.status == 2"
                                @click="send_goods(scope.row, scope.$index)">发货</el-button>
                            <el-popconfirm title="确定删除吗？" @confirm="table_del(scope.row, scope.$index)" v-if="scope.row.status == 1">
                                <template #reference>
                                    <el-button text type="primary" size="small" >删除</el-button>
                                </template>
                            </el-popconfirm>
                        </el-button-group>
                    </template>
                </el-table-column>
            </scTable>
        </el-main>
    </el-container>
    <save-dialog v-if="dialog.save" ref="saveDialog" @success="handleSaveSuccess" @closed="dialog.save = false"></save-dialog>
    
    <el-drawer v-model="drawer" size="40%"  title="订单信息" destroy-on-close>
        <template #default>
            <!-- <el-divider content-position="left">收货信息</el-divider> -->
            <div style="padding: 0 15px;">
                <div style="font-weight: bold; color: rgb(44, 44, 44);">收货信息</div>
                <el-row>
                    <el-col :span="12">用户：{{ drawerData.owner_data }}</el-col>
                    <el-col :span="12">收货人：{{ drawerData.name }}</el-col>
                    <el-col :span="12">联系电话：{{ drawerData.phone }}</el-col>
                    <el-col :span="12">收货地址：{{ drawerData.address }}</el-col>
                </el-row>
            </div>
            <el-divider border-style="dashed" />
            <div style="padding: 0 15px;">
                <div style="font-weight: bold; color: rgb(44, 44, 44);">订单信息</div>
                <el-row>
                    <el-col :span="12">订单号：{{ drawerData.order_sn }}</el-col>
                    <el-col :span="12">订单状态：
                        <span v-if="drawerData.status == 1">待付款</span>
                        <span v-if="drawerData.status == 2">待发货</span>
                        <span v-if="drawerData.status == 3">待收货</span>
                        <span v-if="drawerData.status == 4">待评价</span>
                        <span v-if="drawerData.status == 5">已完成</span>
                        <span v-if="drawerData.status == 6">已关闭</span>
                        <span v-if="drawerData.status == 7">退款中</span>
                    </el-col>
                    <el-col :span="12">商品总数：{{ orderSkuCount(drawerData.baykeshopordersku_set) }}</el-col>
                    <el-col :span="12">商品总价：{{ orderSkuTotalPrice(drawerData.baykeshopordersku_set) }}</el-col>
                    <el-col :span="12">实际支付：{{ drawerData.total_price }}</el-col>
                    <el-col :span="12">创建时间：{{ drawerData.add_date }}</el-col>
                    <el-col :span="12">支付方式：
                        <span v-if="drawerData.paymethod == 1">支付宝支付</span>
                        <span v-else-if="drawerData.paymethod == 2">微信支付</span>
                        <span v-else-if="drawerData.paymethod == 3">余额支付</span>
                        <span v-else>未支付</span>
                    </el-col>
                    <el-col :span="12">支付时间：{{ drawerData.pay_time }}</el-col>
                </el-row>
            </div>
            <el-divider border-style="dashed" />
            <div style="padding: 0 15px;">
                <div style="font-weight: bold; color: rgb(44, 44, 44);">商品信息</div>
                <el-row v-for="sku in drawerData.baykeshopordersku_set" :key="sku.id">
                    <el-col :span="5">
                        <el-image style="width: 50px; height: 50px" :src="sku.sku_json.img" fit="cover" />
                    </el-col>
                    <el-col :span="15">
                        {{ sku.sku_json.title }}
                        <span v-for="spec in sku.sku_json.spec_values" :key="spec.id">
                        |{{ spec.value }}
                        </span>
                    </el-col>
                    <el-col :md="4"><span>¥{{ sku.sku_json.price }}x{{ sku.count }} </span></el-col>
                </el-row>
            </div>
        </template>
	</el-drawer>
</template>

<script>
import saveDialog from './save'
import scSelectFilter from '@/components/scSelectFilter'

export default {
    name: "shopOrder",
    components: {
        scSelectFilter,
        saveDialog
    },
    data() {
        return {
            data: [
                {
                    title: "订单状态",
                    key: "status",
                    options: [
                        {
                            label: "全部",
                            value: ""
                        },
                        {
                            label: "待付款",
                            value: "1",
                        },
                        {
                            label: "待发货",
                            value: "2",
                        },
                        {
                            label: "待收货",
                            value: "3",
                        },
                        {
                            label: "待评价",
                            value: "4",
                        },
                        {
                            label: "已完成",
                            value: "5",
                        },
                        {
                            label: "已关闭",
                            value: "6",
                        },
                        {
                            label: "退款中",
                            value: "7",
                        },
                    ]
                },
                {
                    title: "支付方式",
                    key: "paymethod",
                    multiple: false,
                    options: [
                        {
                            label: "全部",
                            value: ""
                        },
                        {
                            label: "支付宝支付",
                            value: "1"
                        },
                        {
                            label: "微信支付",
                            value: "2"
                        },
                        {
                            label: "余额支付",
                            value: "3"
                        }
                    ]
                }
            ],
            selectedValues: {
                state: [""],
                type: [""]
            },
            filterData: {},
            // table
            dialog: {
                save: false
            },
            apiObj: this.$API.shop.order.list,
            selection: [],
            search: {
                keyword: null
            },
            ids: [],
            drawer: false,
            drawerData: ""
        }
    },
    methods: {
        change(selected) {
            this.filterData = selected
            this.$refs.table.upData(this.filterData)
        },
        // 新增
        add() {
            console.log('add')
        },
        table_show(row){
            this.drawer = true
            this.drawerData = row
        },
        //编辑
        table_edit(row) {
            this.dialog.save = true
            this.$nextTick(() => {
                this.$refs.saveDialog.open('edit').setData(row)
            })
        },
        // 发货
        send_goods(row) {
            // console.log(row)
            this.$API.shop.order.partial_update.patch(row.id, {status:3}).then(res => {
                if (res.status == 200) {
                    this.$message.success("发货成功")
                    this.$refs.table.refresh()
                }
            })
        },
        //删除
        async table_del(row) {
            var res = await this.$API.shop.order.remove.delete(row.id);
            if (res.status == 204) {
                this.$refs.table.refresh()
                this.$message.success("删除成功")
            } else {
                this.$alert(res.message, "提示", { type: 'error' })
            }
        },
        // 批量删除
        batch_del() {
            this.$confirm(`确定删除选中的 ${this.selection.length} 项吗？如果删除项中含有子集将会被一并删除`, '提示', {
                type: 'warning'
            }).then(() => {
                const loading = this.$loading();
                this.$API.shop.order.remove.batch_delete({ ids: this.ids }).then(res => {
                    if (res.status == 204) {
                        this.$refs.table.refresh()
                        loading.close();
                        this.$message.success("操作成功")
                    }
                })
            }).catch(() => {

            })
        },
        // 搜索
        upsearch() {
            let params = Object.assign(this.filterData, { serarch: this.search.keyword })
            this.$refs.table.upData(params)
        },
        // 选中回调
        selectionChange(selection) {
            this.selection = selection;
            this.selection.forEach(el => {
                this.ids.push(el.id)
            })
        },

        //本地更新数据
        handleSaveSuccess(data, mode) {
            if (mode == 'add') {
                this.$refs.table.refresh()
            } else if (mode == 'edit') {
                this.$refs.table.refresh()
            }
        },
        // 计算商品总数
        orderSkuCount(skus){
            let count = 0
            skus.forEach(el => {
                count += el.count
            })
            return count
        },
        // 计算商品总价
        orderSkuTotalPrice(skus){
            let total_price = 0
            skus.forEach(el => {
                total_price += parseFloat(el.sku_json.price)
            })
            return total_price
        }
    }
}
</script>

<style>
.el-drawer__header{
    border-bottom: solid 1px #eee;
    padding-bottom: 15px;
    margin-bottom: 0;
}
.el-drawer__body{
    padding: 10px;
    font-size: 14px;
    color: #737373;
    line-height: 35px;
}
/* .order-show-body{

} */
</style>


