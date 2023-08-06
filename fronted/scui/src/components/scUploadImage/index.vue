<template>
    <el-upload class="avatar-uploader" :show-file-list="false" :on-success="handleAvatarSuccess"
        :before-upload="beforeAvatarUpload">
        <img v-if="imageUrl" :src="imageUrl" class="avatar" />
        <el-icon v-else class="avatar-uploader-icon">
            <Plus />
        </el-icon>
    </el-upload>
</template>

<script>
export default {
    name: "scUploadImage",
    components: {},
    data() {
        return {
            imageUrl: ""
        }
    },
    methods: {
        handleAvatarSuccess(response, uploadFile) {
            console.log(response, uploadFile)
            this.imageUrl = URL.createObjectURL(uploadFile.raw)
        },
        beforeAvatarUpload(rawFile) {
            let isType = ['image/jpeg', 'image/png', 'image/gif'].includes(rawFile.type)
            if (!isType) {
                this.$message.error("上传图片格式不正确！")
                return false
            } else if (rawFile.size / 1024 / 1024 > 2) {
                this.$message.error("图片太大！")
                return false
            }
            return true
        }
    }
}
</script>

<style scoped>
.avatar-uploader .avatar {
    width: 178px;
    height: 178px;
    display: block;
}
</style>

<style>
.avatar-uploader .el-upload {
    border: 1px dashed var(--el-border-color);
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
    border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    text-align: center;
}
</style>