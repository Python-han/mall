"use strict";(self["webpackChunkbaykeshop"]=self["webpackChunkbaykeshop"]||[]).push([[6560],{826:function(e,t,a){a.r(t),a.d(t,{default:function(){return w}});var l=a(6252);const s=e=>((0,l.dD)("data-v-00984cfa"),e=e(),(0,l.Cn)(),e),i={class:"left-panel"},o={class:"right-panel"},n={class:"right-panel-search"},r=s((()=>(0,l._)("div",{class:"image-slot"},"-",-1)));function d(e,t,a,s,d,c){const h=(0,l.up)("el-button"),p=(0,l.up)("el-input"),u=(0,l.up)("el-header"),w=(0,l.up)("el-table-column"),m=(0,l.up)("el-image"),f=(0,l.up)("el-tag"),g=(0,l.up)("el-popconfirm"),b=(0,l.up)("el-button-group"),k=(0,l.up)("scTable"),_=(0,l.up)("el-main"),y=(0,l.up)("el-container"),v=(0,l.up)("save-dialog");return(0,l.wg)(),(0,l.iD)(l.HY,null,[(0,l.Wm)(y,null,{default:(0,l.w5)((()=>[(0,l.Wm)(u,null,{default:(0,l.w5)((()=>[(0,l._)("div",i,[(0,l.Wm)(h,{type:"primary",icon:"el-icon-plus",onClick:c.add},{default:(0,l.w5)((()=>[(0,l.Uk)("新增")])),_:1},8,["onClick"]),(0,l.Wm)(h,{type:"danger",plain:"",icon:"el-icon-delete",disabled:0==d.selection.length,onClick:c.batch_del},{default:(0,l.w5)((()=>[(0,l.Uk)("批量删除")])),_:1},8,["disabled","onClick"])]),(0,l._)("div",o,[(0,l._)("div",n,[(0,l.Wm)(p,{modelValue:d.search.keyword,"onUpdate:modelValue":t[0]||(t[0]=e=>d.search.keyword=e),placeholder:"分类名称",clearable:""},null,8,["modelValue"]),(0,l.Wm)(h,{type:"primary",icon:"el-icon-search",onClick:c.upsearch},null,8,["onClick"])])])])),_:1}),(0,l.Wm)(_,{class:"nopadding"},{default:(0,l.w5)((()=>[(0,l.Wm)(k,{ref:"table",apiObj:d.apiObj,"row-key":"id",onSelectionChange:c.selectionChange},{default:(0,l.w5)((()=>[(0,l.Wm)(w,{type:"selection",width:"50"}),(0,l.Wm)(w,{label:"ID",prop:"id",width:"250"}),(0,l.Wm)(w,{label:"分类名称",prop:"name",width:"250"}),(0,l.Wm)(w,{label:"分类图标",prop:"icon",width:"250"},{default:(0,l.w5)((e=>[(0,l.Wm)(m,{src:e.row.icon,style:{width:"30px",height:"30px"},fit:"cover","preview-src-list":[e.row.icon],"preview-teleported":!0},{placeholder:(0,l.w5)((()=>[r])),_:2},1032,["src","preview-src-list"])])),_:1}),(0,l.Wm)(w,{label:"排序",prop:"sort",width:"150"}),(0,l.Wm)(w,{label:"状态",prop:"status",width:"150"},{default:(0,l.w5)((e=>[e.row.status?((0,l.wg)(),(0,l.j4)(f,{key:0,type:"success"},{default:(0,l.w5)((()=>[(0,l.Uk)("启用")])),_:1})):(0,l.kq)("",!0),e.row.status?(0,l.kq)("",!0):((0,l.wg)(),(0,l.j4)(f,{key:1,type:"danger"},{default:(0,l.w5)((()=>[(0,l.Uk)("停用")])),_:1}))])),_:1}),(0,l.Wm)(w,{label:"创建时间",prop:"add_date",width:"180"}),(0,l.Wm)(w,{label:"操作",fixed:"right",align:"right",width:"170"},{default:(0,l.w5)((e=>[(0,l.Wm)(b,null,{default:(0,l.w5)((()=>[(0,l.Wm)(h,{text:"",type:"primary",size:"small",onClick:t=>c.table_show(e.row,e.$index)},{default:(0,l.w5)((()=>[(0,l.Uk)("查看")])),_:2},1032,["onClick"]),(0,l.Wm)(h,{text:"",type:"primary",size:"small",onClick:t=>c.table_edit(e.row,e.$index)},{default:(0,l.w5)((()=>[(0,l.Uk)("编辑")])),_:2},1032,["onClick"]),(0,l.Wm)(g,{title:"确定删除吗？",onConfirm:t=>c.table_del(e.row,e.$index)},{reference:(0,l.w5)((()=>[(0,l.Wm)(h,{text:"",type:"primary",size:"small"},{default:(0,l.w5)((()=>[(0,l.Uk)("删除")])),_:1})])),_:2},1032,["onConfirm"])])),_:2},1024)])),_:1})])),_:1},8,["apiObj","onSelectionChange"])])),_:1})])),_:1}),d.dialog.save?((0,l.wg)(),(0,l.j4)(v,{key:0,ref:"saveDialog",onSuccess:c.handleSaveSuccess,onClosed:t[1]||(t[1]=e=>d.dialog.save=!1)},null,8,["onSuccess"])):(0,l.kq)("",!0)],64)}a(7658);var c=a(1631),h={name:"dept",components:{saveDialog:c["default"]},data(){return{dialog:{save:!1},apiObj:this.$API.shop.category.list,selection:[],search:{keyword:null},ids:[]}},methods:{add(){this.dialog.save=!0,this.$nextTick((()=>{this.$refs.saveDialog.open()}))},table_edit(e){this.dialog.save=!0,this.$nextTick((()=>{this.$refs.saveDialog.open("edit").setData(e)}))},table_show(e){this.dialog.save=!0,this.$nextTick((()=>{this.$refs.saveDialog.open("show").setData(e)}))},async table_del(e){var t=await this.$API.shop.category.remove.delete(e.id);204==t.status?(this.$refs.table.refresh(),this.$message.success("删除成功")):this.$alert(t.message,"提示",{type:"error"})},async batch_del(){this.$confirm(`确定删除选中的 ${this.selection.length} 项吗？如果删除项中含有子集将会被一并删除`,"提示",{type:"warning"}).then((()=>{const e=this.$loading();this.$API.shop.category.remove.batch_delete({ids:this.ids}).then((t=>{204==t.status&&(this.$refs.table.refresh(),e.close(),this.$message.success("操作成功"))}))})).catch((()=>{}))},selectionChange(e){this.selection=e,this.selection.forEach((e=>{this.ids.push(e.id)}))},upsearch(){this.$refs.table.upData({search:this.search.keyword})},filterTree(e){var t=null;function a(l){l.forEach((l=>{l.id==e&&(t=l),l.children&&a(l.children)}))}return a(this.$refs.table.tableData),t},handleSaveSuccess(e,t){("add"==t||"edit"==t)&&this.$refs.table.refresh()}}},p=a(3744);const u=(0,p.Z)(h,[["render",d],["__scopeId","data-v-00984cfa"]]);var w=u}}]);