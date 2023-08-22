import config from "@/config"
import http from "@/utils/request"


export default {
	token: {
		url: `${config.API_URL}/auth/token/`,
		name: "登录获取TOKEN",
		post: async function(data={}){
			return await http.post(this.url, data);
		}
	},
	refresh: {
		url: `${config.API_URL}/auth/refresh/`,
		name: "刷新TOKEN",
		post: async function(data={}){
			return await http.post(this.url, data);
		}
	},
	verify: {
		url: `${config.API_URL}/auth/refresh/`,
		name: "验证TOKEN",
		post: async function(data={}){
			return await http.post(this.url, data);
		}
	},
	logout: {
		url: `${config.API_URL}/auth/logout/`,
		name: "验证TOKEN",
		post: async function(){
			return await http.post(this.url);
		}
	},
	user: {
		url: `${config.API_URL}/auth/user/changepassword/`,
		name: "修改自己的密码",
		post: async function(data){
			return await http.post(this.url, data)
		}
	},
	owner: {
		url: `${config.API_URL}/auth/owner/changepassword/`,
		name: "修改指定用户的密码",
		post: async function(data){
			return await http.post(this.url, data)
		}
	},
}
