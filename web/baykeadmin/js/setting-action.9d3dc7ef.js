"use strict";(self["webpackChunkbaykeshop"]=self["webpackChunkbaykeshop"]||[]).push([[2606],{6496:function(e,a,l){l.r(a),l.d(a,{default:function(){return u}});var t=l(6252),i=l(3577);const s={class:"left-panel"},n={class:"right-panel"},o={class:"right-panel-search"};function r(e,a,l,r,d,c){const p=(0,t.up)("el-button"),h=(0,t.up)("el-input"),u=(0,t.up)("el-header"),m=(0,t.up)("el-table-column"),f=(0,t.up)("el-popconfirm"),b=(0,t.up)("el-button-group"),w=(0,t.up)("scTable"),k=(0,t.up)("el-main"),g=(0,t.up)("el-container"),_=(0,t.up)("save-dialog");return(0,t.wg)(),(0,t.iD)(t.HY,null,[(0,t.Wm)(g,null,{default:(0,t.w5)((()=>[(0,t.Wm)(u,null,{default:(0,t.w5)((()=>[(0,t._)("div",s,[(0,t.Wm)(p,{type:"primary",icon:"el-icon-plus",onClick:c.add},{default:(0,t.w5)((()=>[(0,t.Uk)("新增")])),_:1},8,["onClick"]),(0,t.Wm)(p,{type:"danger",plain:"",icon:"el-icon-delete",disabled:0==d.selection.length,onClick:c.batch_del},{default:(0,t.w5)((()=>[(0,t.Uk)("批量删除")])),_:1},8,["disabled","onClick"])]),(0,t._)("div",n,[(0,t._)("div",o,[(0,t.Wm)(h,{modelValue:d.search.keyword,"onUpdate:modelValue":a[0]||(a[0]=e=>d.search.keyword=e),placeholder:"权限名称",clearable:""},null,8,["modelValue"]),(0,t.Wm)(p,{type:"primary",icon:"el-icon-search",onClick:c.upsearch},null,8,["onClick"])])])])),_:1}),(0,t.Wm)(k,{class:"nopadding"},{default:(0,t.w5)((()=>[(0,t.Wm)(w,{ref:"table",apiObj:d.apiObj,"row-key":"id",onSelectionChange:c.selectionChange},{default:(0,t.w5)((()=>[(0,t.Wm)(m,{type:"selection",width:"50"}),(0,t.Wm)(m,{label:"ID",prop:"id",width:"50"}),(0,t.Wm)(m,{label:"权限名称",prop:"permission"},{default:(0,t.w5)((e=>[(0,t.Uk)((0,i.zw)(e.row.permission.name),1)])),_:1}),(0,t.Wm)(m,{label:"权限标识",prop:"permission"},{default:(0,t.w5)((e=>[(0,t.Uk)((0,i.zw)(e.row.permission.codename),1)])),_:1}),(0,t.Wm)(m,{label:"归属应用",prop:"permission"},{default:(0,t.w5)((e=>[(0,t.Uk)((0,i.zw)(e.row.permission.content_type.app_label),1)])),_:1}),(0,t.Wm)(m,{label:"归属模型",prop:"permission"},{default:(0,t.w5)((e=>[(0,t.Uk)((0,i.zw)(e.row.permission.content_type.model),1)])),_:1}),(0,t.Wm)(m,{label:"接口别名",prop:"apiname"}),(0,t.Wm)(m,{label:"请求类型",prop:"request_method"}),(0,t.Wm)(m,{label:"备注",prop:"mark"}),(0,t.Wm)(m,{label:"创建时间",prop:"add_date",width:"180"}),(0,t.Wm)(m,{label:"操作",fixed:"right",align:"right",width:"170"},{default:(0,t.w5)((e=>[(0,t.Wm)(b,null,{default:(0,t.w5)((()=>[(0,t.Wm)(p,{text:"",type:"primary",size:"small",onClick:a=>c.table_show(e.row,e.$index)},{default:(0,t.w5)((()=>[(0,t.Uk)("查看")])),_:2},1032,["onClick"]),(0,t.Wm)(p,{text:"",type:"primary",size:"small",onClick:a=>c.table_edit(e.row,e.$index)},{default:(0,t.w5)((()=>[(0,t.Uk)("编辑")])),_:2},1032,["onClick"]),(0,t.Wm)(f,{title:"确定删除吗？",onConfirm:a=>c.table_del(e.row,e.$index)},{reference:(0,t.w5)((()=>[(0,t.Wm)(p,{text:"",type:"primary",size:"small"},{default:(0,t.w5)((()=>[(0,t.Uk)("删除")])),_:1})])),_:2},1032,["onConfirm"])])),_:2},1024)])),_:1})])),_:1},8,["apiObj","onSelectionChange"])])),_:1})])),_:1}),d.dialog.save?((0,t.wg)(),(0,t.j4)(_,{key:0,ref:"saveDialog",onSuccess:c.handleSaveSuccess,onClosed:a[1]||(a[1]=e=>d.dialog.save=!1)},null,8,["onSuccess"])):(0,t.kq)("",!0)],64)}l(7658);var d=l(2358),c={name:"action",components:{saveDialog:d["default"]},data(){return{dialog:{save:!1},apiObj:this.$API.badmin.action.list,selection:[],search:{keyword:null},ids:[]}},methods:{add(){this.dialog.save=!0,this.$nextTick((()=>{this.$refs.saveDialog.open()}))},table_edit(e){this.dialog.save=!0,this.$nextTick((()=>{this.$refs.saveDialog.open("edit").setData(e)}))},table_show(e){this.dialog.save=!0,this.$nextTick((()=>{this.$refs.saveDialog.open("show").setData(e)}))},async table_del(e){var a=await this.$API.badmin.action.remove.delete(e.id);204==a.status?(this.$refs.table.refresh(),this.$message.success("删除成功")):this.$alert(a.message,"提示",{type:"error"})},async batch_del(){this.$confirm(`确定删除选中的 ${this.selection.length} 项吗？如果删除项中含有子集将会被一并删除`,"提示",{type:"warning"}).then((()=>{const e=this.$loading();this.$API.badmin.action.remove.batch_delete({ids:this.ids}).then((a=>{204==a.status&&(this.$refs.table.refresh(),e.close(),this.$message.success("操作成功"))}))})).catch((()=>{}))},selectionChange(e){this.selection=e,this.selection.forEach((e=>{this.ids.push(e.id)}))},upsearch(){this.$refs.table.upData({search:this.search.keyword})},filterTree(e){var a=null;function l(t){t.forEach((t=>{t.id==e&&(a=t),t.children&&l(t.children)}))}return l(this.$refs.table.tableData),a},handleSaveSuccess(e,a){("add"==a||"edit"==a)&&this.$refs.table.refresh()}}},p=l(3744);const h=(0,p.Z)(c,[["render",r]]);var u=h}}]);