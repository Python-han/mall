"use strict";(self["webpackChunkbaykeshop"]=self["webpackChunkbaykeshop"]||[]).push([[8782],{7550:function(a,e,t){t.r(e),t.d(e,{default:function(){return s}});var l=t(6252);const o=(0,l._)("div",{class:"el-form-item-msg"},"账号信息用于登录，系统不允许修改",-1);function m(a,e,t,m,u,r){const d=(0,l.up)("el-input"),s=(0,l.up)("el-form-item"),n=(0,l.up)("sc-upload"),i=(0,l.up)("el-option"),f=(0,l.up)("el-select"),h=(0,l.up)("el-button"),p=(0,l.up)("el-form"),b=(0,l.up)("el-card"),c=(0,l.Q2)("loading");return(0,l.wg)(),(0,l.j4)(b,{shadow:"never",header:"个人信息"},{default:(0,l.w5)((()=>[(0,l.wy)(((0,l.wg)(),(0,l.j4)(p,{ref:"form",model:u.form,"label-width":"120px",style:{"margin-top":"20px"}},{default:(0,l.w5)((()=>[(0,l.Wm)(s,{label:"账号"},{default:(0,l.w5)((()=>[(0,l.Wm)(d,{modelValue:u.form.username,"onUpdate:modelValue":e[0]||(e[0]=a=>u.form.username=a),disabled:""},null,8,["modelValue"]),o])),_:1}),(0,l.Wm)(s,{label:"头像"},{default:(0,l.w5)((()=>[(0,l.Wm)(n,{modelValue:u.form.avatar,"onUpdate:modelValue":e[1]||(e[1]=a=>u.form.avatar=a),title:"avatar",cropper:!0,compress:1,aspectRatio:1,round:"",icon:"el-icon-avatar"},null,8,["modelValue"])])),_:1}),(0,l.Wm)(s,{label:"姓名"},{default:(0,l.w5)((()=>[(0,l.Wm)(d,{modelValue:u.form.name,"onUpdate:modelValue":e[2]||(e[2]=a=>u.form.name=a)},null,8,["modelValue"])])),_:1}),(0,l.Wm)(s,{label:"性别"},{default:(0,l.w5)((()=>[(0,l.Wm)(f,{modelValue:u.form.sex,"onUpdate:modelValue":e[3]||(e[3]=a=>u.form.sex=a),placeholder:"请选择"},{default:(0,l.w5)((()=>[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(u.options,(a=>((0,l.wg)(),(0,l.j4)(i,{key:a.value,label:a.label,value:a.value},null,8,["label","value"])))),128))])),_:1},8,["modelValue"])])),_:1}),(0,l.Wm)(s,{label:"个性签名"},{default:(0,l.w5)((()=>[(0,l.Wm)(d,{modelValue:u.form.about,"onUpdate:modelValue":e[4]||(e[4]=a=>u.form.about=a),type:"textarea"},null,8,["modelValue"])])),_:1}),(0,l.Wm)(s,null,{default:(0,l.w5)((()=>[(0,l.Wm)(h,{type:"primary",onClick:r.onSubmit},{default:(0,l.w5)((()=>[(0,l.Uk)("保存")])),_:1},8,["onClick"])])),_:1})])),_:1},8,["model"])),[[c,u.loading]])])),_:1})}var u={data(){return{form:{id:"",username:"",name:"",sex:"1",about:"",avatar:""},options:[{label:"保密",value:0},{label:"男",value:1},{label:"女",value:2}],loading:!1}},created(){this.loading=!0,this.$API.badmin.user.get().then((a=>{200==a.status&&(this.form.id=a.data.id,this.form.username=a.data.owner.username,this.form.name=a.data.name,this.form.sex=a.data.sex,this.form.about=a.data.about,this.form.avatar=a.data.avatar?a.data.avatar:"img/avatar2.gif",this.loading=!1)}))},methods:{onSubmit(){const a={name:this.form.name,sex:this.form.sex,about:this.form.about,avatar:this.form.avatar};this.loading=!0,this.$API.badmin.users.partial_update.patch(this.form.id,a).then((a=>{200==a.status&&(this.form.id=a.data.id,this.form.username=a.data.owner.username,this.form.name=a.data.name,this.form.sex=a.data.sex,this.form.about=a.data.about,this.form.avatar=a.data.avatar,this.loading=!1,this.$message.success("修改成功"))}))}}},r=t(3744);const d=(0,r.Z)(u,[["render",m]]);var s=d}}]);