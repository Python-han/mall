import config from "@/config"
import http from "@/utils/request"


export default {
    comment: {
		list:{
			url: `${config.API_URL}/comment/comment/`,
			name: "列表",
			get: async function(params={}){
				return await http.get(this.url, params)
			},
		},
		read: {
			url: `${config.API_URL}/comment/comment/`,
			name: "获取",
			get: async function(id, params={}){
				return await http.get(`${this.url}${id}/`, params)
			}
		},
		update: {
			url: `${config.API_URL}/comment/comment/`,
			name: "修改",
			put: async function(id, data){
				return await http.put(`${this.url}${id}/`, data)
			}
		},
		partial_update: {
			url: `${config.API_URL}/comment/comment/`,
			name: "局部修改",
			patch: async function(id, data){
				return await http.patch(`${this.url}${id}/`, data)
			},
		},
		remove: {
			url: `${config.API_URL}/comment/comment/`,
			name: "删除",
			delete: async function(id, data){
				return await http.delete(`${this.url}${id}/`, data)
			},
			batch_delete: async function(data){
				return await http.delete(`${this.url}batch_destroy/`, data)
			}
		}
	},
}