"use strict";(self["webpackChunkbaykeshop"]=self["webpackChunkbaykeshop"]||[]).push([[2798,1200],{3312:function(e,l,t){t.r(l),t.d(l,{default:function(){return k}});var i=t(6252),s=t(3577);const a=e=>((0,i.dD)("data-v-dbf89736"),e=e(),(0,i.Cn)(),e),n=a((()=>(0,i._)("h4",null,"执行类",-1))),d=a((()=>(0,i._)("h4",null,"定时规则",-1))),o={class:"bottom"},u={class:"state"},r={class:"handler"},c=a((()=>(0,i._)("p",null,"添加计划任务",-1)));function m(e,l,t,a,m,p){const f=(0,i.up)("el-tag"),g=(0,i.up)("el-button"),h=(0,i.up)("el-popconfirm"),w=(0,i.up)("el-dropdown-item"),k=(0,i.up)("el-dropdown-menu"),_=(0,i.up)("el-dropdown"),v=(0,i.up)("el-card"),W=(0,i.up)("el-col"),C=(0,i.up)("el-icon-plus"),b=(0,i.up)("el-icon"),y=(0,i.up)("el-row"),D=(0,i.up)("el-main"),x=(0,i.up)("save-dialog"),U=(0,i.up)("logs"),$=(0,i.up)("el-drawer");return(0,i.wg)(),(0,i.iD)(i.HY,null,[(0,i.Wm)(D,null,{default:(0,i.w5)((()=>[(0,i.Wm)(y,{gutter:15},{default:(0,i.w5)((()=>[((0,i.wg)(!0),(0,i.iD)(i.HY,null,(0,i.Ko)(m.list,(e=>((0,i.wg)(),(0,i.j4)(W,{xl:6,lg:6,md:8,sm:12,xs:24,key:e.id},{default:(0,i.w5)((()=>[(0,i.Wm)(v,{class:"task task-item",shadow:"hover"},{default:(0,i.w5)((()=>[(0,i._)("h2",null,(0,s.zw)(e.title),1),(0,i._)("ul",null,[(0,i._)("li",null,[n,(0,i._)("p",null,(0,s.zw)(e.handler),1)]),(0,i._)("li",null,[d,(0,i._)("p",null,(0,s.zw)(e.cron),1)])]),(0,i._)("div",o,[(0,i._)("div",u,["1"==e.state?((0,i.wg)(),(0,i.j4)(f,{key:0,size:"small"},{default:(0,i.w5)((()=>[(0,i.Uk)("准备就绪")])),_:1})):(0,i.kq)("",!0),"-1"==e.state?((0,i.wg)(),(0,i.j4)(f,{key:1,size:"small",type:"info"},{default:(0,i.w5)((()=>[(0,i.Uk)("停用")])),_:1})):(0,i.kq)("",!0)]),(0,i._)("div",r,[(0,i.Wm)(h,{title:"确定立即执行吗？",onConfirm:l=>p.run(e)},{reference:(0,i.w5)((()=>[(0,i.Wm)(g,{type:"primary",icon:"el-icon-caret-right",circle:""})])),_:2},1032,["onConfirm"]),(0,i.Wm)(_,{trigger:"click"},{dropdown:(0,i.w5)((()=>[(0,i.Wm)(k,null,{default:(0,i.w5)((()=>[(0,i.Wm)(w,{onClick:l=>p.edit(e)},{default:(0,i.w5)((()=>[(0,i.Uk)("编辑")])),_:2},1032,["onClick"]),(0,i.Wm)(w,{onClick:l=>p.logs(e)},{default:(0,i.w5)((()=>[(0,i.Uk)("日志")])),_:2},1032,["onClick"]),(0,i.Wm)(w,{onClick:l=>p.del(e),divided:""},{default:(0,i.w5)((()=>[(0,i.Uk)("删除")])),_:2},1032,["onClick"])])),_:2},1024)])),default:(0,i.w5)((()=>[(0,i.Wm)(g,{type:"primary",icon:"el-icon-more",circle:"",plain:""})])),_:2},1024)])])])),_:2},1024)])),_:2},1024)))),128)),(0,i.Wm)(W,{xl:6,lg:6,md:8,sm:12,xs:24},{default:(0,i.w5)((()=>[(0,i.Wm)(v,{class:"task task-add",shadow:"never",onClick:p.add},{default:(0,i.w5)((()=>[(0,i.Wm)(b,null,{default:(0,i.w5)((()=>[(0,i.Wm)(C)])),_:1}),c])),_:1},8,["onClick"])])),_:1})])),_:1})])),_:1}),m.dialog.save?((0,i.wg)(),(0,i.j4)(x,{key:0,ref:"saveDialog",onSuccess:p.handleSuccess,onClosed:l[0]||(l[0]=e=>m.dialog.save=!1)},null,8,["onSuccess"])):(0,i.kq)("",!0),(0,i.Wm)($,{title:"计划任务日志",modelValue:m.dialog.logsVisible,"onUpdate:modelValue":l[1]||(l[1]=e=>m.dialog.logsVisible=e),size:600,direction:"rtl","destroy-on-close":""},{default:(0,i.w5)((()=>[(0,i.Wm)(U)])),_:1},8,["modelValue"])],64)}t(7658);var p=t(9902),f=t(5301),g={name:"task",components:{saveDialog:p["default"],logs:f["default"]},provide(){return{list:this.list}},data(){return{dialog:{save:!1,logsVisible:!1},list:[{id:"1",title:"清理服务器缓存",handler:"cleanUpCacheHandler",cron:"59 59 23 * * ? *",state:"1"},{id:"2",title:"自动审核",handler:"automaticAuditHandler",cron:"0 0 * * * ? *",state:"1"},{id:"3",title:"清理未实名用户",handler:"deleteUserHandler",cron:"0 0 0 * * ? *",state:"-1"}]}},mounted(){},methods:{add(){this.dialog.save=!0,this.$nextTick((()=>{this.$refs.saveDialog.open()}))},edit(e){this.dialog.save=!0,this.$nextTick((()=>{this.$refs.saveDialog.open("edit").setData(e)}))},del(e){this.$confirm(`确认删除 ${e.title} 计划任务吗？`,"提示",{type:"warning",confirmButtonText:"删除",confirmButtonClass:"el-button--danger"}).then((()=>{this.list.splice(this.list.findIndex((l=>l.id===e.id)),1)})).catch((()=>{}))},logs(){this.dialog.logsVisible=!0},run(e){this.$message.success(`已成功执行计划任务：${e.title}`)},handleSuccess(e,l){"add"==l?(e.id=(new Date).getTime(),this.list.push(e)):"edit"==l&&this.list.filter((l=>l.id===e.id)).forEach((l=>{Object.assign(l,e)}))}}},h=t(3744);const w=(0,h.Z)(g,[["render",m],["__scopeId","data-v-dbf89736"]]);var k=w}}]);