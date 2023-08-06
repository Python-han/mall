import config from "@/config"
import http from "@/utils/request"

export default {
    category: {
        list:{
			url: `${config.API_URL}/shop/category/`,
			name: "分类管理",
			get: async function(params={}){
				return await http.get(this.url, params)
			},
		},
		create:{
			url: `${config.API_URL}/shop/category/`,
			name: "分类新增",
			post: async function(data){
				return await http.post(this.url, data)
			},
		},
		read: {
			url: `${config.API_URL}/shop/category/`,
			name: "详情",
			get: async function(id, params={}){
				return await http.get(`${this.url}${id}/`, params)
			}
		},
		update: {
			url: `${config.API_URL}/shop/category/`,
			name: "修改",
			put: async function(id, data){
				return await http.put(`${this.url}${id}/`, data)
			}
		},
		partial_update: {
			url: `${config.API_URL}/shop/category/`,
			name: "局部修改",
			patch: async function(id, data){
				return await http.patch(`${this.url}${id}/`, data)
			},
		},
		remove: {
			url: `${config.API_URL}/shop/category/`,
			name: "删除及批量删除",
			delete: async function(id, data){
				return await http.delete(`${this.url}${id}/`, data)
			},
			batch_delete: async function(data){
				return await http.delete(`${this.url}batch_destroy/`, data)
			}
		}
    }
}