"use strict";(self["webpackChunkbaykeshop"]=self["webpackChunkbaykeshop"]||[]).push([[5738],{4955:function(e,l,a){a.r(l),a.d(l,{default:function(){return w}});var t=a(6252),o=a(3577),s=a(9963);const u={key:0},i={key:1},d={class:"spec-tags"};function m(e,l,a,m,r,p){const n=(0,t.up)("el-button"),h=(0,t.up)("router-link"),c=(0,t.up)("sc-page-header"),f=(0,t.up)("el-tree-select"),w=(0,t.up)("el-form-item"),b=(0,t.up)("el-option"),g=(0,t.up)("el-select"),k=(0,t.up)("el-input"),V=(0,t.up)("sc-upload-multiple"),_=(0,t.up)("el-radio"),W=(0,t.up)("el-radio-group"),y=(0,t.up)("el-input-number"),U=(0,t.up)("el-col"),D=(0,t.up)("el-row"),v=(0,t.up)("el-tab-pane"),C=(0,t.up)("sc-upload"),T=(0,t.up)("el-tag"),$=(0,t.up)("el-alert"),S=(0,t.up)("el-table-column"),q=(0,t.up)("sc-form-table"),I=(0,t.up)("sc-editor"),R=(0,t.up)("el-tabs"),x=(0,t.up)("el-form"),z=(0,t.up)("el-card"),P=(0,t.up)("el-main");return(0,t.wg)(),(0,t.iD)(t.HY,null,[(0,t.Wm)(c,{title:e.$route.query.mode?"查看商品":"新增/编辑商品",description:"",icon:"el-icon-goods"},{main:(0,t.w5)((()=>[(0,t.Wm)(h,{to:{name:"shopGoods"}},{default:(0,t.w5)((()=>[(0,t.Wm)(n,{size:"small",icon:"el-icon-back"},{default:(0,t.w5)((()=>[(0,t.Uk)("返回")])),_:1})])),_:1})])),_:1},8,["title"]),(0,t.Wm)(P,null,{default:(0,t.w5)((()=>[(0,t.Wm)(z,{shadow:"never"},{default:(0,t.w5)((()=>[(0,t.Wm)(x,{ref:"form",model:r.form,rules:r.rules,"label-width":"100px",disabled:"show"==e.$route.query.mode},{default:(0,t.w5)((()=>[(0,t.Wm)(R,{modelValue:r.activeName,"onUpdate:modelValue":l[29]||(l[29]=e=>r.activeName=e)},{default:(0,t.w5)((()=>[(0,t.Wm)(v,{label:"基础信息",name:"base"},{default:(0,t.w5)((()=>[(0,t.Wm)(D,null,{default:(0,t.w5)((()=>[(0,t.Wm)(U,{span:12,xs:24},{default:(0,t.w5)((()=>[(0,t.Wm)(w,{label:"商品分类",prop:"category"},{default:(0,t.w5)((()=>[(0,t.Wm)(f,{modelValue:r.form.category,"onUpdate:modelValue":l[0]||(l[0]=e=>r.form.category=e),data:r.categoryDatas,"render-after-expand":!1,props:r.categoryProps,clearable:!0,multiple:"",filterable:"",style:{width:"100%"},placeholder:"请选择..."},null,8,["modelValue","data","props"])])),_:1}),(0,t.Wm)(w,{label:"商品品牌"},{default:(0,t.w5)((()=>[(0,t.Wm)(g,{modelValue:r.form.brand,"onUpdate:modelValue":l[1]||(l[1]=e=>r.form.brand=e),filterable:"",placeholder:"请选择...",style:{width:"100%"}},{default:(0,t.w5)((()=>[((0,t.wg)(!0),(0,t.iD)(t.HY,null,(0,t.Ko)(r.brandOptions,(e=>((0,t.wg)(),(0,t.j4)(b,{key:e.id,label:e.name,value:e.id},null,8,["label","value"])))),128))])),_:1},8,["modelValue"])])),_:1}),(0,t.Wm)(w,{label:"标题",prop:"title"},{default:(0,t.w5)((()=>[(0,t.Wm)(k,{modelValue:r.form.title,"onUpdate:modelValue":l[2]||(l[2]=e=>r.form.title=e),placeholder:"请输入商品标题"},null,8,["modelValue"])])),_:1}),(0,t.Wm)(w,{label:"副标题"},{default:(0,t.w5)((()=>[(0,t.Wm)(k,{modelValue:r.form.subtitle,"onUpdate:modelValue":l[3]||(l[3]=e=>r.form.subtitle=e),placeholder:"请输入商品副标题"},null,8,["modelValue"])])),_:1}),(0,t.Wm)(w,{label:"商品关键字"},{default:(0,t.w5)((()=>[(0,t.Wm)(k,{modelValue:r.form.keywords,"onUpdate:modelValue":l[4]||(l[4]=e=>r.form.keywords=e),placeholder:"请输入商品关键字"},null,8,["modelValue"])])),_:1}),(0,t.Wm)(w,{label:"商品简介"},{default:(0,t.w5)((()=>[(0,t.Wm)(k,{modelValue:r.form.desc,"onUpdate:modelValue":l[5]||(l[5]=e=>r.form.desc=e),placeholder:"请输入商品简介",autosize:{minRows:2,maxRows:4},type:"textarea"},null,8,["modelValue"])])),_:1}),(0,t.Wm)(w,{label:"单位",prop:"unit"},{default:(0,t.w5)((()=>[(0,t.Wm)(k,{modelValue:r.form.unit,"onUpdate:modelValue":l[6]||(l[6]=e=>r.form.unit=e),placeholder:"请输入商品单位"},null,8,["modelValue"])])),_:1}),(0,t.Wm)(w,{label:"商品轮播图",prop:"images"},{default:(0,t.w5)((()=>[(0,t.Wm)(V,{modelValue:r.form.images,"onUpdate:modelValue":l[7]||(l[7]=e=>r.form.images=e),draggable:"",limit:10,disabled:"show"==e.$route.query.mode,tip:"最多上传10个文件,单个文件不要超过10M,请上传图像格式文件"},null,8,["modelValue","disabled"])])),_:1}),(0,t.Wm)(w,{label:"物流方式"},{default:(0,t.w5)((()=>[(0,t.Wm)(W,{modelValue:r.form.expresstype,"onUpdate:modelValue":l[8]||(l[8]=e=>r.form.expresstype=e)},{default:(0,t.w5)((()=>[(0,t.Wm)(_,{label:0},{default:(0,t.w5)((()=>[(0,t.Uk)("快递")])),_:1})])),_:1},8,["modelValue"])])),_:1}),(0,t.Wm)(w,{label:"运费设置"},{default:(0,t.w5)((()=>[(0,t.Wm)(W,{modelValue:r.form.freighttype,"onUpdate:modelValue":l[9]||(l[9]=e=>r.form.freighttype=e)},{default:(0,t.w5)((()=>[(0,t.Wm)(_,{label:0},{default:(0,t.w5)((()=>[(0,t.Uk)("固定运费")])),_:1})])),_:1},8,["modelValue"])])),_:1}),r.form.freighttype?(0,t.kq)("",!0):((0,t.wg)(),(0,t.j4)(w,{key:0},{default:(0,t.w5)((()=>[(0,t.Wm)(y,{modelValue:r.form.freight,"onUpdate:modelValue":l[10]||(l[10]=e=>r.form.freight=e),"controls-position":"right",min:0,precision:2,step:1,style:{width:"100%"}},null,8,["modelValue"])])),_:1})),(0,t.Wm)(w,{label:"商品状态"},{default:(0,t.w5)((()=>[(0,t.Wm)(W,{modelValue:r.form.status,"onUpdate:modelValue":l[11]||(l[11]=e=>r.form.status=e)},{default:(0,t.w5)((()=>[(0,t.Wm)(_,{label:!0},{default:(0,t.w5)((()=>[(0,t.Uk)("上架")])),_:1}),(0,t.Wm)(_,{label:!1},{default:(0,t.w5)((()=>[(0,t.Uk)("下架")])),_:1})])),_:1},8,["modelValue"])])),_:1}),(0,t.Wm)(w,null,{default:(0,t.w5)((()=>[(0,t.Wm)(n,{onClick:l[12]||(l[12]=e=>r.activeName="sku"),type:"primary"},{default:(0,t.w5)((()=>[(0,t.Uk)("下一步")])),_:1})])),_:1})])),_:1})])),_:1})])),_:1}),(0,t.Wm)(v,{label:"规格库存",name:"sku"},{default:(0,t.w5)((()=>[(0,t.Wm)(D,null,{default:(0,t.w5)((()=>[(0,t.Wm)(U,{span:24,xs:24},{default:(0,t.w5)((()=>[(0,t.Wm)(w,{label:"商品规格"},{default:(0,t.w5)((()=>[(0,t.Wm)(W,{modelValue:r.form.skutype,"onUpdate:modelValue":l[13]||(l[13]=e=>r.form.skutype=e)},{default:(0,t.w5)((()=>[(0,t.Wm)(_,{label:0},{default:(0,t.w5)((()=>[(0,t.Uk)("单规格")])),_:1}),(0,t.Wm)(_,{label:1},{default:(0,t.w5)((()=>[(0,t.Uk)("多规格")])),_:1})])),_:1},8,["modelValue"])])),_:1}),r.form.skutype?((0,t.wg)(),(0,t.iD)("div",i,[(0,t.Wm)(w,{label:"选择规格"},{default:(0,t.w5)((()=>[(0,t.Wm)(g,{modelValue:r.modelSpec,"onUpdate:modelValue":l[23]||(l[23]=e=>r.modelSpec=e),placeholder:"Select",multiple:"","value-key":"id",onChange:p.onSpecChange},{default:(0,t.w5)((()=>[((0,t.wg)(!0),(0,t.iD)(t.HY,null,(0,t.Ko)(r.specOptions,(e=>((0,t.wg)(),(0,t.j4)(b,{key:e.id,label:e.name,value:e},null,8,["label","value"])))),128))])),_:1},8,["modelValue","onChange"]),(0,t.Wm)(n,{onClick:p.onGenter,type:"primary"},{default:(0,t.w5)((()=>[(0,t.Uk)("生成")])),_:1},8,["onClick"])])),_:1}),((0,t.wg)(!0),(0,t.iD)(t.HY,null,(0,t.Ko)(r.modelSpec,((l,a)=>((0,t.wg)(),(0,t.j4)(w,{prop:"modelSpec",key:l.id},{default:(0,t.w5)((()=>[(0,t._)("div",d,[(0,t._)("p",null,(0,o.zw)(l.name)+"：",1),(0,t._)("div",null,[((0,t.wg)(!0),(0,t.iD)(t.HY,null,(0,t.Ko)(l.baykeshopspecvalue_set,((a,s)=>((0,t.wg)(),(0,t.j4)(T,{key:a.id,closable:"show"!=e.$route.query.mode,"disable-transitions":!1,style:{"margin-right":"5px"},disabled:"show"==e.$route.query.mode,onClose:e=>p.handleClose(l.baykeshopspecvalue_set,a,s)},{default:(0,t.w5)((()=>[(0,t.Uk)((0,o.zw)(a.value),1)])),_:2},1032,["closable","disabled","onClose"])))),128)),l.inputVisible?((0,t.wg)(),(0,t.j4)(k,{key:0,ref_for:!0,ref:"tagInputRef",modelValue:r.inputValue[a],"onUpdate:modelValue":e=>r.inputValue[a]=e,size:"small",disabled:"show"==e.$route.query.mode,onKeyup:(0,s.D2)((e=>p.handleInputConfirm(a)),["enter"]),onBlur:e=>p.handleInputConfirm(a,l),style:{width:"auto"}},null,8,["modelValue","onUpdate:modelValue","disabled","onKeyup","onBlur"])):((0,t.wg)(),(0,t.j4)(n,{key:1,size:"small",onClick:e=>p.showInput(a)},{default:(0,t.w5)((()=>[(0,t.Uk)(" + 添加 ")])),_:2},1032,["onClick"]))])])])),_:2},1024)))),128)),(0,t.Wm)(w,null,{default:(0,t.w5)((()=>[r.form.id?((0,t.wg)(),(0,t.j4)($,{key:0,title:"注意：如果生成的新sku规格数量小于原有sku数量，需先删除原有sku数量小于生成sku数量，否则会造成规格混乱",type:"warning"})):(0,t.kq)("",!0),(0,t.Wm)(q,{ref:"specTableRef",modelValue:r.skuTableData,"onUpdate:modelValue":l[24]||(l[24]=e=>r.skuTableData=e),placeholder:"暂无数据",hideAdd:!0,onRowDel:p.tabRowdel},{default:(0,t.w5)((()=>[(0,t.Wm)(S,{prop:"specops",label:"规格",width:"180"},{default:(0,t.w5)((e=>[(0,t.Wm)(g,{modelValue:e.row.spec_values,"onUpdate:modelValue":l=>e.row.spec_values=l,multiple:"",disabled:!0,size:"large","suffix-icon":"",style:{width:"100%"}},{default:(0,t.w5)((()=>[((0,t.wg)(!0),(0,t.iD)(t.HY,null,(0,t.Ko)(e.row.specops,(e=>((0,t.wg)(),(0,t.j4)(b,{key:e.id,label:e.value,value:e.id},null,8,["label","value"])))),128))])),_:2},1032,["modelValue","onUpdate:modelValue"])])),_:1}),(0,t.Wm)(S,{prop:"img",label:"图片",width:"105"},{default:(0,t.w5)((e=>[(0,t.Wm)(C,{autoUpload:!0,ref:`skuUploadRef${e.$index}`,modelValue:e.row.img,"onUpdate:modelValue":l=>e.row.img=l,width:80,height:80},null,8,["modelValue","onUpdate:modelValue"])])),_:1}),(0,t.Wm)(S,{prop:"price",label:"售价"},{default:(0,t.w5)((e=>[(0,t.Wm)(k,{modelValue:e.row.price,"onUpdate:modelValue":l=>e.row.price=l},null,8,["modelValue","onUpdate:modelValue"])])),_:1}),(0,t.Wm)(S,{prop:"cost_price",label:"成本价"},{default:(0,t.w5)((e=>[(0,t.Wm)(k,{modelValue:e.row.cost_price,"onUpdate:modelValue":l=>e.row.cost_price=l},null,8,["modelValue","onUpdate:modelValue"])])),_:1}),(0,t.Wm)(S,{prop:"retail_price",label:"划线价"},{default:(0,t.w5)((e=>[(0,t.Wm)(k,{modelValue:e.row.retail_price,"onUpdate:modelValue":l=>e.row.retail_price=l},null,8,["modelValue","onUpdate:modelValue"])])),_:1}),(0,t.Wm)(S,{prop:"stock",label:"库存"},{default:(0,t.w5)((e=>[(0,t.Wm)(k,{modelValue:e.row.stock,"onUpdate:modelValue":l=>e.row.stock=l},null,8,["modelValue","onUpdate:modelValue"])])),_:1}),(0,t.Wm)(S,{prop:"weight",label:"重量"},{default:(0,t.w5)((e=>[(0,t.Wm)(k,{modelValue:e.row.weight,"onUpdate:modelValue":l=>e.row.weight=l},null,8,["modelValue","onUpdate:modelValue"])])),_:1}),(0,t.Wm)(S,{prop:"vol",label:"体积"},{default:(0,t.w5)((e=>[(0,t.Wm)(k,{modelValue:e.row.vol,"onUpdate:modelValue":l=>e.row.vol=l},null,8,["modelValue","onUpdate:modelValue"])])),_:1}),(0,t.Wm)(S,{prop:"item",label:"商品编号"},{default:(0,t.w5)((e=>[(0,t.Wm)(k,{modelValue:e.row.item,"onUpdate:modelValue":l=>e.row.item=l},null,8,["modelValue","onUpdate:modelValue"])])),_:1})])),_:1},8,["modelValue","onRowDel"])])),_:1})])):((0,t.wg)(),(0,t.iD)("div",u,[(0,t.Wm)(w,{label:"图片"},{default:(0,t.w5)((()=>[(0,t.Wm)(C,{ref:"uploadRef",modelValue:r.form.img,"onUpdate:modelValue":l[14]||(l[14]=e=>r.form.img=e),width:80,height:80,disabled:"show"==e.$route.query.mode},null,8,["modelValue","disabled"])])),_:1}),(0,t.Wm)(w,{label:"售价"},{default:(0,t.w5)((()=>[(0,t.Wm)(y,{modelValue:r.form.price,"onUpdate:modelValue":l[15]||(l[15]=e=>r.form.price=e),"controls-position":"right",min:0,precision:2,step:1,style:{width:"100%"}},null,8,["modelValue"])])),_:1}),(0,t.Wm)(w,{label:"成本价"},{default:(0,t.w5)((()=>[(0,t.Wm)(y,{modelValue:r.form.cost_price,"onUpdate:modelValue":l[16]||(l[16]=e=>r.form.cost_price=e),"controls-position":"right",min:0,precision:2,step:1,style:{width:"100%"}},null,8,["modelValue"])])),_:1}),(0,t.Wm)(w,{label:"原价"},{default:(0,t.w5)((()=>[(0,t.Wm)(y,{modelValue:r.form.retail_price,"onUpdate:modelValue":l[17]||(l[17]=e=>r.form.retail_price=e),"controls-position":"right",min:0,precision:2,step:1,style:{width:"100%"}},null,8,["modelValue"])])),_:1}),(0,t.Wm)(w,{label:"库存"},{default:(0,t.w5)((()=>[(0,t.Wm)(y,{modelValue:r.form.stock,"onUpdate:modelValue":l[18]||(l[18]=e=>r.form.stock=e),"controls-position":"right",min:0,style:{width:"100%"}},null,8,["modelValue"])])),_:1}),(0,t.Wm)(w,{label:"销量"},{default:(0,t.w5)((()=>[(0,t.Wm)(y,{modelValue:r.form.sales,"onUpdate:modelValue":l[19]||(l[19]=e=>r.form.sales=e),"controls-position":"right",min:0,style:{width:"100%"}},null,8,["modelValue"])])),_:1}),(0,t.Wm)(w,{label:"重量"},{default:(0,t.w5)((()=>[(0,t.Wm)(y,{modelValue:r.form.weight,"onUpdate:modelValue":l[20]||(l[20]=e=>r.form.weight=e),"controls-position":"right",min:0,precision:2,step:1,style:{width:"100%"}},null,8,["modelValue"])])),_:1}),(0,t.Wm)(w,{label:"体积"},{default:(0,t.w5)((()=>[(0,t.Wm)(y,{modelValue:r.form.vol,"onUpdate:modelValue":l[21]||(l[21]=e=>r.form.vol=e),"controls-position":"right",min:0,precision:2,step:1,style:{width:"100%"}},null,8,["modelValue"])])),_:1}),(0,t.Wm)(w,{label:"编号"},{default:(0,t.w5)((()=>[(0,t.Wm)(k,{modelValue:r.form.item,"onUpdate:modelValue":l[22]||(l[22]=e=>r.form.item=e),placeholder:"请输入商品编号"},null,8,["modelValue"])])),_:1})])),(0,t.Wm)(w,null,{default:(0,t.w5)((()=>[(0,t.Wm)(n,{onClick:l[25]||(l[25]=e=>r.activeName="base")},{default:(0,t.w5)((()=>[(0,t.Uk)("上一步")])),_:1}),(0,t.Wm)(n,{onClick:l[26]||(l[26]=e=>r.activeName="content"),type:"primary"},{default:(0,t.w5)((()=>[(0,t.Uk)("下一步")])),_:1})])),_:1})])),_:1})])),_:1})])),_:1}),(0,t.Wm)(v,{label:"商品详情",name:"content"},{default:(0,t.w5)((()=>[(0,t.Wm)(w,{label:"详情",prop:"content"},{default:(0,t.w5)((()=>[(0,t.Wm)(I,{modelValue:r.form.content,"onUpdate:modelValue":l[27]||(l[27]=e=>r.form.content=e),placeholder:"请输入",templates:r.templates,height:800},null,8,["modelValue","templates"])])),_:1}),(0,t.Wm)(w,null,{default:(0,t.w5)((()=>[(0,t.Wm)(n,{onClick:l[28]||(l[28]=e=>r.activeName="sku")},{default:(0,t.w5)((()=>[(0,t.Uk)("上一步")])),_:1}),(0,t.Wm)(n,{onClick:p.onsubmit,type:"primary"},{default:(0,t.w5)((()=>[(0,t.Uk)("保存")])),_:1},8,["onClick"])])),_:1})])),_:1})])),_:1},8,["modelValue"])])),_:1},8,["model","rules","disabled"])])),_:1})])),_:1})],64)}a(7658);var r=a(2201),p=a(907);const n=(0,t.RC)((()=>Promise.all([a.e(8285),a.e(6054),a.e(1517)]).then(a.bind(a,1517))));var h={name:"goodsDetail",components:{RouterLink:r.rH,scEditor:n},data(){return{form:{id:this.$route.query.id,title:"",subtitle:"",category:[],brand:null,unit:"",status:!0,images:[],stock:0,sales:0,img:null,price:0,retail_price:0,cost_price:0,item:"",weight:0,vol:0,skutype:0,content:"",expresstype:0,freighttype:0,freight:0,sku_id:""},activeName:"base",templates:[],brandOptions:[],categoryDatas:[],categoryProps:{label:"name",value:"id",children:"children"},specOptions:[],modelSpec:[],skuTableData:[],skuTableDataCache:[],inputValue:[],rules:{category:[{required:!0,message:"请选择商品分类"}],title:[{required:!0,message:"请输入商品标题"}],unit:[{required:!0,min:1,max:5,message:"范围在1至3位"}],images:[{required:!0,message:"请添加商品轮播图"}],content:[{required:!0,message:"请输入商品详情"}]}}},created(){this.getBrands(),this.getCategory(),this.getGoodsSpu(),this.getSpecsData()},mounted(){this.$store.commit("updateViewTagsTitle",this.form.id?`商品编辑ID:${this.form.id}`:"商品新增")},methods:{async getBrands(){const e=await this.$API.shop.brand.list.get({pageSize:1e3});this.brandOptions=e.data.results},async getCategory(){const e=await this.$API.shop.category.list.get({pageSize:1e3});this.categoryDatas=e.data.results},async getSpecsData(){const e=await this.$API.shop.spec.list.get({pageSize:1e3});this.specOptions=e.data.results},async getGoodsSpu(){if(this.form.id){const e=await this.$API.shop.spu.read.get(this.form.id);if(this.form=e.data,this.form.freight=parseFloat(e.data.freight),!e.data.skutype&&1==e.data.baykeshopsku_set.length){let l=e.data.baykeshopsku_set[0];this.form.sku_id=l.id,this.form.price=parseFloat(l.price),this.form.cost_price=parseFloat(l.cost_price),this.form.retail_price=parseFloat(l.retail_price),this.form.weight=parseFloat(l.weight),this.form.vol=parseFloat(l.vol),this.form.item=l.item,this.form.img=l.img}this.modelSpec=e.data.specs,this.skuTableData=e.data.skuSpecs,this.skuTableDataCache=e.data.skuSpecs}},onsubmit(){this.$refs.form.validate((async e=>{if(!e)return this.$message.warning("表单填写有误，请检查！"),!1;this.form.skutype?this.form["baykeshopsku_set"]=this.skuTableData:this.form["baykeshopsku_set"]=[{id:this.form.sku_id,price:this.form.price,stock:this.form.stock,sales:this.form.sales,img:this.form.img,retail_price:this.form.retail_price,cost_price:this.form.cost_price,item:this.form.item,weight:this.form.weight,vol:this.form.vol}],this.$API.shop.spu.create.post(this.form).then((e=>{200==e.status&&(this.$message.success("操作成功"),this.$router.push({name:"shopGoods"}),this.$route.is=!0,p.Z.close())}))}))},handleClose(e,l,a){e.splice(a,1)},arrp(e){if(e[0].baykeshopspecvalue_set&&(e=e.map((e=>e.baykeshopspecvalue_set))),1==e.length)return e[0];{let l=[];return e[0].forEach(((a,t)=>{e[1].forEach(((a,o)=>{l.push([].concat(e[0][t],e[1][o]))}))})),e[0]=l,e.splice(1,1),this.arrp(e)}},onSpecChange(e){this.generateSkuData(e),this.getSpecsData()},getSpecType(e){let l=[];return e.forEach((e=>{l.push(e.id)})),l},generateSkuData(e){let l=[];if(e.length&&this.arrp(e).forEach((e=>{l.push({spec_values:e.length?this.getSpecType(e):[e.id],specops:e.length?e:[e]})})),this.skuTableData=l,this.form.id&&this.skuTableData.length)for(let a=0;a<this.skuTableData.length;a++)this.skuTableDataCache[a]&&(this.skuTableData[a]["id"]=this.skuTableDataCache[a].id,this.skuTableData[a]["price"]=this.skuTableDataCache[a].price,this.skuTableData[a]["cost_price"]=this.skuTableDataCache[a].cost_price,this.skuTableData[a]["retail_price"]=this.skuTableDataCache[a].retail_price,this.skuTableData[a]["item"]=this.skuTableDataCache[a].item,this.skuTableData[a]["weight"]=this.skuTableDataCache[a].weight,this.skuTableData[a]["stock"]=this.skuTableDataCache[a].stock,this.skuTableData[a]["vol"]=this.skuTableDataCache[a].vol,this.skuTableData[a]["status"]=this.skuTableDataCache[a].status,this.skuTableData[a]["img"]=this.skuTableDataCache[a].img)},showInput(e){this.modelSpec[e]["inputVisible"]=!0,this.$nextTick((()=>{this.$refs.tagInputRef[0].input.focus()}))},handleInputConfirm(e,l){this.inputValue[e]&&(this.$API.shop.specvalue.create.post({spec:l.id,value:this.inputValue[e]}).then((l=>{201==l.status&&this.modelSpec[e].baykeshopspecvalue_set.push({id:l.data.id,value:l.data.value})})),this.inputValue.splice(e,1)),this.modelSpec[e].inputVisible=!1},onGenter(){this.generateSkuData(this.modelSpec),this.skuTableData.length<this.skuTableDataCache.length&&this.$message.warning("当前生成的sku数量少于原有sku数量，请先删除原有sku后再次生成")},tabRowdel(e,l){e.id&&this.$API.shop.sku.remove.delete(e.id).then((e=>{204==e.status&&this.$message.success("删除成功")})),this.$refs.specTableRef.deleteRow(l)}}},c=a(3744);const f=(0,c.Z)(h,[["render",m]]);var w=f}}]);