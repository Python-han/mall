<template>
	<el-main>
		<el-row :gutter="15">
			<el-col :lg="24">
				<el-card shadow="never" class="aboutTop">
					<div class="aboutTop-info">
						<img src="img/logo.png">
						<h2>baykeshop商城系统</h2>
						<p>baykeshop（拜客商城系统）是一款全开源Python栈商城系统，采用最新版django4+Vue3前后端分离开发，代码精炼简洁易于学习及二次开发。</p>
						<p>后台前端框架UI为（SCUI）, 感谢SCUI开源项目作者的辛苦付出。</p>
					</div>
				</el-card>
				<el-card shadow="never" header="dependencies">
					<el-descriptions border :column="3">
						<el-descriptions-item v-for="(value, key) in data.dependencies" :key="key" :label="key">{{value}}</el-descriptions-item>
					</el-descriptions>
				</el-card>
				<el-card shadow="never" header="devDependencies">
					<el-descriptions border :column="3">
						<el-descriptions-item v-for="(value, key) in data.devDependencies" :key="key" :label="key">{{value}}</el-descriptions-item>
					</el-descriptions>
				</el-card>
			</el-col>
		</el-row>
	</el-main>
</template>

<script>
	import packageJson from '../../../package.json'

	export default {
		name: 'about',
		data() {
			return {
				data: packageJson
			}
		},
		mounted() {

		},
		methods: {

		}
	}
</script>

<style scoped>
	.aboutTop {border:0;background: linear-gradient(to right, #8E54E9, #4776E6);color: #fff;}
	.aboutTop-info {text-align: center}
	.aboutTop-info img {width: 100px;}
	.aboutTop-info h2 {font-size: 26px;margin-top: 15px;}
	.aboutTop-info p {font-size: 16px;margin-top: 10px;}
</style>
