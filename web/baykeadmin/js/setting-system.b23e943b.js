"use strict";(self["webpackChunkbaykeshop"]=self["webpackChunkbaykeshop"]||[]).push([[4835],{6728:function(e,l,t){t.r(l),t.d(l,{default:function(){return g}});var a=t(6252),s=t(3577);const m=(0,a._)("div",{class:"el-form-item-msg","data-v-b33b3cf8":""},"自己的邮箱密码，或授权码，一般现在的邮箱都需要授权码",-1),o=(0,a._)("div",{class:"el-form-item-msg","data-v-b33b3cf8":""},"是否为隐式安全连接",-1),d=(0,a._)("div",{class:"el-form-item-msg","data-v-b33b3cf8":""},"关闭后用户无法收到邮件，但日志中将记录",-1),i={key:1},u={key:1},n={key:1};function p(e,l,t,p,r,w){const _=(0,a.up)("el-input"),y=(0,a.up)("el-form-item"),g=(0,a.up)("sc-upload"),c=(0,a.up)("el-button"),f=(0,a.up)("el-form"),h=(0,a.up)("el-tab-pane"),b=(0,a.up)("el-switch"),V=(0,a.up)("el-alert"),W=(0,a.up)("el-table-column"),k=(0,a.up)("el-popconfirm"),S=(0,a.up)("el-button-group"),U=(0,a.up)("el-table"),v=(0,a.up)("el-tabs"),x=(0,a.up)("el-card"),C=(0,a.up)("el-main");return(0,a.wg)(),(0,a.j4)(C,null,{default:(0,a.w5)((()=>[(0,a.Wm)(x,{shadow:"never"},{default:(0,a.w5)((()=>[(0,a.Wm)(v,{"tab-position":"top"},{default:(0,a.w5)((()=>[(0,a.Wm)(h,{label:"系统设置"},{default:(0,a.w5)((()=>[(0,a.Wm)(f,{ref:"form",model:r.sys,"label-width":"100px",style:{"margin-top":"20px"}},{default:(0,a.w5)((()=>[(0,a.Wm)(y,{label:"系统名称"},{default:(0,a.w5)((()=>[(0,a.Wm)(_,{modelValue:r.sys.site_title,"onUpdate:modelValue":l[0]||(l[0]=e=>r.sys.site_title=e)},null,8,["modelValue"])])),_:1}),(0,a.Wm)(y,{label:"LogoUrl"},{default:(0,a.w5)((()=>[(0,a.Wm)(g,{modelValue:r.sys.logo_url,"onUpdate:modelValue":l[1]||(l[1]=e=>r.sys.logo_url=e),title:"logo",cropper:!1,compress:1,aspectRatio:1,round:"",icon:"el-icon-avatar"},null,8,["modelValue"])])),_:1}),(0,a.Wm)(y,{label:"版权信息"},{default:(0,a.w5)((()=>[(0,a.Wm)(_,{type:"textarea",autosize:{minRows:4},modelValue:r.sys.copyright,"onUpdate:modelValue":l[2]||(l[2]=e=>r.sys.copyright=e)},null,8,["modelValue"])])),_:1}),(0,a.Wm)(y,null,{default:(0,a.w5)((()=>[(0,a.Wm)(c,{type:"primary",onClick:w.onSysSubmit},{default:(0,a.w5)((()=>[(0,a.Uk)("保存")])),_:1},8,["onClick"])])),_:1})])),_:1},8,["model"])])),_:1}),(0,a.Wm)(h,{label:"邮箱配置"},{default:(0,a.w5)((()=>[(0,a.Wm)(f,{ref:"form",model:r.msg,"label-width":"100px",style:{"margin-top":"20px"}},{default:(0,a.w5)((()=>[(0,a.Wm)(y,{label:"主机"},{default:(0,a.w5)((()=>[(0,a.Wm)(_,{modelValue:r.msg.email_host,"onUpdate:modelValue":l[3]||(l[3]=e=>r.msg.email_host=e)},null,8,["modelValue"])])),_:1}),(0,a.Wm)(y,{label:"邮箱"},{default:(0,a.w5)((()=>[(0,a.Wm)(_,{modelValue:r.msg.email_host_user,"onUpdate:modelValue":l[4]||(l[4]=e=>r.msg.email_host_user=e),type:"email"},null,8,["modelValue"])])),_:1}),(0,a.Wm)(y,{label:"密码"},{default:(0,a.w5)((()=>[(0,a.Wm)(_,{modelValue:r.msg.email_host_password,"onUpdate:modelValue":l[5]||(l[5]=e=>r.msg.email_host_password=e),type:"password","show-password":""},null,8,["modelValue"]),m])),_:1}),(0,a.Wm)(y,{label:"端口"},{default:(0,a.w5)((()=>[(0,a.Wm)(_,{modelValue:r.msg.email_port,"onUpdate:modelValue":l[6]||(l[6]=e=>r.msg.email_port=e)},null,8,["modelValue"])])),_:1}),(0,a.Wm)(y,{label:"默认发件箱"},{default:(0,a.w5)((()=>[(0,a.Wm)(_,{modelValue:r.msg.default_from_email,"onUpdate:modelValue":l[7]||(l[7]=e=>r.msg.default_from_email=e),type:"email"},null,8,["modelValue"])])),_:1}),(0,a.Wm)(y,{label:"SSL"},{default:(0,a.w5)((()=>[(0,a.Wm)(b,{modelValue:r.msg.email_use_ssl,"onUpdate:modelValue":l[8]||(l[8]=e=>r.msg.email_use_ssl=e)},null,8,["modelValue"]),o])),_:1}),(0,a.Wm)(y,{label:"邮箱开关"},{default:(0,a.w5)((()=>[(0,a.Wm)(b,{modelValue:r.msg.status,"onUpdate:modelValue":l[9]||(l[9]=e=>r.msg.status=e)},null,8,["modelValue"]),d])),_:1}),(0,a.Wm)(y,null,{default:(0,a.w5)((()=>[(0,a.Wm)(c,{type:"primary",onClick:w.onMsgSubmit},{default:(0,a.w5)((()=>[(0,a.Uk)("保存")])),_:1},8,["onClick"])])),_:1})])),_:1},8,["model"])])),_:1}),(0,a.Wm)(h,{label:"扩展配置"},{default:(0,a.w5)((()=>[(0,a.Wm)(V,{title:"扩展配置为系统业务所有的配置，应该由系统管理员操作，如需用户配置应另起业务配置页面。",type:"warning",style:{"margin-bottom":"15px"}}),(0,a.Wm)(U,{data:r.setting,stripe:""},{default:(0,a.w5)((()=>[(0,a.Wm)(W,{label:"#",type:"index",width:"50"}),(0,a.Wm)(W,{label:"KEY",prop:"key",width:"300"},{default:(0,a.w5)((e=>[e.row.isSet?((0,a.wg)(),(0,a.j4)(_,{key:0,modelValue:e.row.key,"onUpdate:modelValue":l=>e.row.key=l,placeholder:"请输入内容"},null,8,["modelValue","onUpdate:modelValue"])):((0,a.wg)(),(0,a.iD)("span",i,(0,s.zw)(e.row.key),1))])),_:1}),(0,a.Wm)(W,{label:"VALUE",prop:"value"},{default:(0,a.w5)((e=>[e.row.isSet?((0,a.wg)(),(0,a.iD)(a.HY,{key:0},["boolean"===typeof e.row.value?((0,a.wg)(),(0,a.j4)(b,{key:0,modelValue:e.row.value,"onUpdate:modelValue":l=>e.row.value=l},null,8,["modelValue","onUpdate:modelValue"])):((0,a.wg)(),(0,a.j4)(_,{key:1,modelValue:e.row.value,"onUpdate:modelValue":l=>e.row.value=l,placeholder:"请输入内容"},null,8,["modelValue","onUpdate:modelValue"]))],64)):((0,a.wg)(),(0,a.iD)("span",u,(0,s.zw)(e.row.value),1))])),_:1}),(0,a.Wm)(W,{label:"TITLE",prop:"title",width:"350"},{default:(0,a.w5)((e=>[e.row.isSet?((0,a.wg)(),(0,a.j4)(_,{key:0,modelValue:e.row.title,"onUpdate:modelValue":l=>e.row.title=l,placeholder:"请输入内容"},null,8,["modelValue","onUpdate:modelValue"])):((0,a.wg)(),(0,a.iD)("span",n,(0,s.zw)(e.row.title),1))])),_:1}),(0,a.Wm)(W,{"min-width":"1"}),(0,a.Wm)(W,{label:"操作",fixed:"right",width:"120"},{default:(0,a.w5)((e=>[(0,a.Wm)(S,null,{default:(0,a.w5)((()=>[(0,a.Wm)(c,{onClick:l=>w.table_edit(e.row,e.$index),text:"",type:"primary",size:"small"},{default:(0,a.w5)((()=>[(0,a.Uk)((0,s.zw)(e.row.isSet?"保存":"修改"),1)])),_:2},1032,["onClick"]),e.row.isSet?((0,a.wg)(),(0,a.j4)(c,{key:0,onClick:l=>e.row.isSet=!1,text:"",type:"primary",size:"small"},{default:(0,a.w5)((()=>[(0,a.Uk)("取消")])),_:2},1032,["onClick"])):(0,a.kq)("",!0),e.row.isSet?(0,a.kq)("",!0):((0,a.wg)(),(0,a.j4)(k,{key:1,title:"确定删除吗？",onConfirm:l=>w.table_del(e.row,e.$index)},{reference:(0,a.w5)((()=>[(0,a.Wm)(c,{text:"",type:"primary",size:"small"},{default:(0,a.w5)((()=>[(0,a.Uk)("删除")])),_:1})])),_:2},1032,["onConfirm"]))])),_:2},1024)])),_:1})])),_:1},8,["data"]),(0,a.Wm)(c,{type:"primary",icon:"el-icon-plus",onClick:w.table_add,style:{"margin-top":"20px"}},null,8,["onClick"])])),_:1})])),_:1})])),_:1})])),_:1})}t(7658);var r=t(8743),w={name:"system",data(){return{sys:{},msg:{},setting:[]}},created(){this.getSystem(),this.getEmailConf(),this.getSystemExtend()},methods:{table_add(){var e={key:"",value:"",title:"",isSet:!0};this.setting.push(e)},table_edit(e){e.isSet?(e.isSet=!1,e.id?this.$API.badmin.system_extend.partial_update.patch(e.id,e).then((e=>{200==e.status&&this.$message.success("修改成功")})):this.$API.badmin.system_extend.create.post(e).then((e=>{201==e.status&&this.$message.success("保存成功")}))):e.isSet=!0},table_del(e,l){this.$API.badmin.system_extend.remove.delete(e.id).then((e=>{204==e.status&&(this.setting.splice(l,1),this.$message.success("删除成功"))}))},async getSystem(){const e=await this.$API.badmin.system.read.get();this.sys=e.data},async getEmailConf(){const e=await this.$API.badmin.emailconf.read.get();this.msg=e.data},async getSystemExtend(){const e=await this.$API.badmin.system_extend.list.get();this.setting=e.data},onSysSubmit(){this.$API.badmin.system.partial_update.patch(this.sys).then((e=>{200==e.status&&(this.sys=e.data,(0,r._aR)("SYSTEM").value=JSON.stringify(e.data),this.$message.success("修改成功"))}))},onMsgSubmit(){this.$API.badmin.emailconf.partial_update.patch(this.msg).then((e=>{200==e.status&&(this.msg=e.data,this.$message.success("修改成功"))}))}}},_=t(3744);const y=(0,_.Z)(w,[["render",p]]);var g=y}}]);