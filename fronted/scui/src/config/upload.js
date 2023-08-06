import API from "@/api";

//上传配置

export default {
	apiObj: API.badmin.imgs.create,			//上传请求API对象
	filename: "img",					//form请求时文件的key
	successCode: 201,					//请求完成代码
	maxSize: 10,						//最大文件大小 默认10MB
	parseData: function (res) {
		return {
			code: res.status,				//分析状态字段结构
			fileName: res.data.img, 		//分析文件名称
			src: res.data.img,				//分析图片远程地址结构
			msg: res.statusText				//分析描述字段结构
		}
	},
	apiObjFile: API.common.uploadFile,	//附件上传请求API对象
	maxSizeFile: 10						//最大文件大小 默认10MB
}
