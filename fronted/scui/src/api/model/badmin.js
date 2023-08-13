import config from "@/config"
import http from "@/utils/request"

export default {
    user: {
		url: `${config.API_URL}/badmin/user/`,
		name: "登录当前登录用户信息",
		get: async function(params={}){
			return await http.get(`${this.url}${params.id}/`, params)
		},
		post: async function(data){
			return await http.post(`${this.url}add/`, data)
		}
	},

	users: {
		list:{
			url: `${config.API_URL}/badmin/users/`,
			name: "用户管理",
			get: async function(params={}){
				return await http.get(this.url, params)
			},
		},
		read: {
			url: `${config.API_URL}/badmin/users/`,
			name: "获取菜单详情",
			get: async function(id, params={}){
				return await http.get(`${this.url}${id}/`, params)
			}
		},
		update: {
			url: `${config.API_URL}/badmin/users/`,
			name: "修改菜单",
			put: async function(id, data){
				return await http.put(`${this.url}${id}/`, data)
			}
		},
		partial_update: {
			url: `${config.API_URL}/badmin/users/`,
			name: "局部修改用户",
			patch: async function(id, data){
				return await http.patch(`${this.url}${id}/`, data)
			},
		},
		remove: {
			url: `${config.API_URL}/badmin/users/`,
			name: "删除菜单",
			delete: async function(id, data){
				return await http.delete(`${this.url}${id}/`, data)
			},
			batch_delete: async function(data){
				return await http.delete(`${this.url}batch_destroy/`, data)
			}
		}
	},

	dept: {
		list: {
			url: `${config.API_URL}/badmin/dept/`,
			name: "获取部门列表",
			get: async function(params){
				return await http.get(this.url, params);
			}
		},
		create: {
			url: `${config.API_URL}/badmin/dept/`,
			name: "部门新增",
			post: async function(data){
				return await http.post(this.url, data)
			}
		},
		read: {
			url: `${config.API_URL}/badmin/dept/`,
			name: "获取部门详情",
			get: async function(id, params={}){
				return await http.get(`${this.url}${id}/`, params)
			}
		},
		update: {
			url: `${config.API_URL}/badmin/dept/`,
			name: "部门修改",
			put: async function(id, data){
				return await http.put(`${this.url}${id}/`, data)
			}
		},
		partial_update: {
			url: `${config.API_URL}/badmin/dept/`,
			name: "部门局部修改",
			patch: async function(id, data){
				return await http.patch(`${this.url}${id}/`, data)
			},
		},
		remove: {
			url: `${config.API_URL}/badmin/dept/`,
			name: "删除部门",
			delete: async function(id, data){
				return await http.delete(`${this.url}${id}/`, data)
			},
			batch_delete: async function(data){
				return await http.delete(`${this.url}batch_destroy/`, data)
			}
		}
	},

	menus: {
		list: {
			url: `${config.API_URL}/badmin/menus/`,
			name: "菜单管理",
			get: async function(params={}){
				return await http.get(this.url, params)
			}
		},
		create: {
			url: `${config.API_URL}/badmin/menus/`,
			name: "新增菜单",
			post: async function(data){
				return await http.post(this.url, data)
			}
		},
		read: {
			url: `${config.API_URL}/badmin/menus/`,
			name: "获取菜单详情",
			get: async function(id, params={}){
				return await http.get(`${this.url}${id}/`, params)
			}
		},
		update: {
			url: `${config.API_URL}/badmin/menus/`,
			name: "修改菜单",
			put: async function(id, data){
				return await http.put(`${this.url}${id}/`, data)
			}
		},
		partial_update: {
			url: `${config.API_URL}/badmin/menus/`,
			name: "局部修改菜单",
			patch: async function(id, data){
				return await http.patch(`${this.url}${id}/`, data)
			},
		},
		remove: {
			url: `${config.API_URL}/badmin/menus/`,
			name: "删除菜单",
			delete: async function(id, data){
				return await http.delete(`${this.url}${id}/`, data)
			},
			batch_delete: async function(data){
				return await http.delete(`${this.url}batch_destroy/`, data)
			}
		}
	},

	// 角色接口
	roles: {
		list: {
			url: `${config.API_URL}/badmin/roles/`,
			name: "获取角色列表",
			get: async function(params){
				return await http.get(this.url, params);
			}
		},
		create: {
			url: `${config.API_URL}/badmin/roles/`,
			name: "创建角色",
			post: async function(data){
				return await http.post(this.url, data)
			}
		},
		update: {
			url: `${config.API_URL}/badmin/roles/`,
			name: "修改角色",
			put: async function(id, data){
				return await http.put(`${this.url}${id}/`, data)
			}
		},
		partial_update: {
			url: `${config.API_URL}/badmin/roles/`,
			name: "局部修改角色",
			patch: async function(id, data){
				return await http.patch(`${this.url}${id}/`, data)
			}
		},
		remove: {
			url: `${config.API_URL}/badmin/roles/`,
			name: "删除角色",
			delete: async function(id, data){
				return await http.delete(`${this.url}${id}/`, data)
			},
			batch_delete: async function(data){
				return await http.delete(`${this.url}batch_destroy/`, data)
			}
		}
	},

	perms: {
		list: {
			url: `${config.API_URL}/badmin/perms/`,
			name: "获取权限列表",
			get: async function(params){
				return await http.get(this.url, params);
			}
		}
	},

	action: {
		list: {
			url: `${config.API_URL}/badmin/action/`,
			name: "权限列表",
			get: async function(params){
				return await http.get(this.url, params);
			}
		},
		remove: {
			url: `${config.API_URL}/badmin/action/`,
			name: "删除菜单权限操作",
			delete: async function(id, data){
				return await http.delete(`${this.url}${id}/`, data)
			},
		},

	},

	// 字典键接口
	dictkey: {
		list: {
			url: `${config.API_URL}/badmin/dictkey/`,
			name: "获取字典键列表",
			get: async function(params){
				return await http.get(this.url, params);
			}
		},
		create: {
			url: `${config.API_URL}/badmin/dictkey/`,
			name: "创建新增",
			post: async function(data){
				return await http.post(this.url, data)
			}
		},
		update: {
			url: `${config.API_URL}/badmin/dictkey/`,
			name: "修改",
			put: async function(id, data){
				return await http.put(`${this.url}${id}/`, data)
			}
		},
		partial_update: {
			url: `${config.API_URL}/badmin/dictkey/`,
			name: "局部修改",
			patch: async function(id, data){
				return await http.patch(`${this.url}${id}/`, data)
			}
		},
		remove: {
			url: `${config.API_URL}/badmin/dictkey/`,
			name: "删除及批量删除",
			delete: async function(id, data){
				return await http.delete(`${this.url}${id}/`, data)
			},
			batch_delete: async function(data){
				return await http.delete(`${this.url}batch_destroy/`, data)
			}
		}
	},

	// 字典值接口
	dictvalue: {
		list: {
			url: `${config.API_URL}/badmin/dictvalue/`,
			name: "获取字典键列表",
			get: async function(params){
				return await http.get(this.url, params);
			}
		},
		create: {
			url: `${config.API_URL}/badmin/dictvalue/`,
			name: "创建新增",
			post: async function(data){
				return await http.post(this.url, data)
			}
		},
		update: {
			url: `${config.API_URL}/badmin/dictvalue/`,
			name: "修改",
			put: async function(id, data){
				return await http.put(`${this.url}${id}/`, data)
			}
		},
		partial_update: {
			url: `${config.API_URL}/badmin/dictvalue/`,
			name: "局部修改",
			patch: async function(id, data){
				return await http.patch(`${this.url}${id}/`, data)
			}
		},
		remove: {
			url: `${config.API_URL}/badmin/dictvalue/`,
			name: "删除及批量删除",
			delete: async function(id, data){
				return await http.delete(`${this.url}${id}/`, data)
			},
			batch_delete: async function(data){
				return await http.delete(`${this.url}batch_destroy/`, data)
			}
		}
	},

	// imgs接口
	imgs: {
		list: {
			url: `${config.API_URL}/badmin/imgs/`,
			name: "获取字典键列表",
			get: async function(params){
				return await http.get(this.url, params);
			}
		},
		create: {
			url: `${config.API_URL}/badmin/imgs/`,
			name: "创建新增",
			post: async function(data){
				return await http.post(this.url, data)
			}
		},
		update: {
			url: `${config.API_URL}/badmin/imgs/`,
			name: "修改",
			put: async function(id, data){
				return await http.put(`${this.url}${id}/`, data)
			}
		},
		partial_update: {
			url: `${config.API_URL}/badmin/imgs/`,
			name: "局部修改",
			patch: async function(id, data){
				return await http.patch(`${this.url}${id}/`, data)
			}
		},
		remove: {
			url: `${config.API_URL}/badmin/imgs/`,
			name: "删除及批量删除",
			delete: async function(id, data){
				return await http.delete(`${this.url}${id}/`, data)
			},
			batch_delete: async function(data){
				return await http.delete(`${this.url}batch_destroy/`, data)
			}
		}
	},

	// system接口
	system: {
		read: {
			url: `${config.API_URL}/badmin/system/1/`,
			name: "修改",
			get: async function(params={}){
				return await http.get(this.url, params)
			}
		},
		readsystem: {
			url: `${config.API_URL}/badmin/readsystem/`,
			name: "获取配置的某一个具体的值",
			get: async function(field_name){
				return await http.get(`${this.url}${field_name}/`)
			}
		},
		update: {
			url: `${config.API_URL}/badmin/system/1/`,
			name: "修改",
			put: async function(data){
				return await http.put(this.url, data)
			}
		},
		partial_update: {
			url: `${config.API_URL}/badmin/system/1/`,
			name: "局部修改",
			patch: async function(data){
				return await http.patch(this.url, data)
			}
		},
	},

	// emailconf接口
	emailconf: {
		read: {
			url: `${config.API_URL}/badmin/emailconf/1/`,
			name: "修改",
			get: async function(params={}){
				return await http.get(this.url, params)
			}
		},
		update: {
			url: `${config.API_URL}/badmin/emailconf/1/`,
			name: "修改",
			put: async function(data){
				return await http.put(this.url, data)
			}
		},
		partial_update: {
			url: `${config.API_URL}/badmin/emailconf/1/`,
			name: "局部修改",
			patch: async function(data){
				return await http.patch(this.url, data)
			}
		},
	},

	// system_extend接口
	system_extend: {
		list: {
			url: `${config.API_URL}/badmin/system_extend/`,
			name: "获取字典键列表",
			get: async function(params){
				return await http.get(this.url, params);
			}
		},
		create: {
			url: `${config.API_URL}/badmin/system_extend/`,
			name: "创建新增",
			post: async function(data){
				return await http.post(this.url, data)
			}
		},
		read: {
			url: `${config.API_URL}/badmin/system_extend/`,
			name: "修改",
			get: async function(id, params={}){
				return await http.get(`${this.url}${id}/`, params)
			}
		},
		update: {
			url: `${config.API_URL}/badmin/system_extend/`,
			name: "修改",
			put: async function(id, data){
				return await http.put(`${this.url}${id}/`, data)
			}
		},
		partial_update: {
			url: `${config.API_URL}/badmin/system_extend/`,
			name: "局部修改",
			patch: async function(id, data){
				return await http.patch(`${this.url}${id}/`, data)
			}
		},
		remove: {
			url: `${config.API_URL}/badmin/system_extend/`,
			name: "删除及批量删除",
			delete: async function(id, data){
				return await http.delete(`${this.url}${id}/`, data)
			},
			batch_delete: async function(data){
				return await http.delete(`${this.url}batch_destroy/`, data)
			}
		}
	},
}