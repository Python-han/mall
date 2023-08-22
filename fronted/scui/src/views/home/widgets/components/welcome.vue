<template>
	<el-card shadow="hover" header="欢迎">
		<div class="welcome">
			<div class="logo">
				<img :src="config.logo_url">
				<h2>欢迎体验 {{ config.site_title }}</h2>
			</div>
			<div class="tips">
				<div class="tips-item">
					<div class="tips-item-icon"><el-icon><el-icon-menu/></el-icon></div>
					<div class="tips-item-message">这里是项目控制台，你可以点击右上方的“自定义”按钮来添加移除或者移动部件。</div>
				</div>
				<div class="tips-item">
					<div class="tips-item-icon"><el-icon><el-icon-promotion/></el-icon></div>
					<div class="tips-item-message">在提高前端算力、减少带宽请求和代码执行力上多次优化，并且持续着。</div>
				</div>
				<div class="tips-item">
					<div class="tips-item-icon"><el-icon><el-icon-milk-tea/></el-icon></div>
					<div class="tips-item-message">项目目的：让后端也能搞前端，前端也能搞后端，大家都成全栈工程师</div>
				</div>
			</div>
			<div class="actions">
				<el-button type="primary" icon="el-icon-check" size="large" @click="godoc">文档</el-button>
			</div>
		</div>
	</el-card>
</template>

<script>
	import { useLocalStorage } from '@vueuse/core' 

	export default {
		title: "欢迎",
		icon: "el-icon-present",
		description: "项目特色以及文档链接",
		data() {
			return {
				config: {}
			}
		},
		methods: {
			godoc(){
				window.open("http://bayke.shop")
			},
		},
		created(){
			let system = JSON.parse(useLocalStorage("SYSTEM").value)
			if (!system.logo_url){
				system.logo_url = 'img/logo.png'
			}
			this.config = system
		}
	}
</script>

<style scoped>
	.welcome {}
	.welcome .logo {text-align: center;}
	.welcome .logo img {vertical-align: bottom;width: 100px;height: 100px;margin-bottom: 20px;}
	.welcome .logo h2 {font-size: 30px;font-weight: normal;display: flex;align-items: center;justify-content: center;}

	.tips {margin-top: 20px;padding:0 40px;}
	.tips-item {display: flex;align-items: center;justify-content: center;padding:7.5px 0;}
	.tips-item-icon {width: 40px;height:40px;display: flex;align-items: center;justify-content: center;border-radius: 50%;font-size: 18px;margin-right: 20px;color: var(--el-color-primary);background: rgba(180,180,180,0.1);}
	.tips-item-message {flex: 1;font-size: 14px;}

	.actions {text-align: center;margin: 40px 0 20px 0;}
</style>
