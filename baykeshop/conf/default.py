import datetime
from django.conf import settings


INSTALLED_APPS = [
    'baykeshop.conf.apps.BaykeAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'corsheaders',
    'baykeshop',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': f'{settings.BASE_DIR}/mysql.cnf',
            'charset': 'utf8mb4',
        },
    }
}


DEFAULTS_CONF = {
    # 后台站点标题
    "SITE_HEADER": "BaykeShop",
    "SITE_TITLE": "BaykeShop",
    
    # 是否开启后台自定义管理菜单
    "ADMIN_MENUS": True,
    
    # 设置后台自定义管理菜单
    "ADMIN_MENUS_DATAS": None,
    
    # 是否开启邮件通知
    "HAS_MESSAGE_EAMIL": False,
    
    # 是否开启关联分类搜索
    "HAS_SEARCH_CATEGORY": False,
    
    "PC_LOGO": "baykeshop",
    
    "SEARCH_VALUE": "请输入搜索关键字",
    
    # 首页楼层数量及分类显示数量
    "HOME_NAV_COUNT": 5,
    
    # 手机号验证正则
    "REGEX_PHONE": "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$",
    # 邮箱验证正则
    "REGEX_EMAIL": "^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$",
    
    # 邮箱验证码过期时间
    "EMAIL_CODE_EXP": datetime.timedelta(seconds=300),
    # 验证码随机范围
    "CODE_CHAR": "1234567890",
    # 验证码长度
    "CODE_LENGTH": 4,
    # 分页长度
    "PAGE_SIZE": 20,
    
    # 支付宝支付相关配置
    "ALIPAY_APPID": "2021000122666025",
    "ALIPAY_NOTIFY_URL": "baykeshop:alipay-api",
    "ALIPAY_RETURN_URL": "baykeshop:alipaypc",
    "ALIPAY_PRIVATE_KEY":"baykeshop/payment/alipay/keys/app_private_key.pem",
    "ALIPAY_PUBLIC_KEY": "baykeshop/payment/alipay/keys/alipay_public_key.pem",
    "ALIPAY_SIGN_TYPE": "RSA2",  # RSA 或者 RSA2
    
     # tinymce富文本编辑器默认配置
    # https://www.tiny.cloud/docs/tinymce/6/basic-setup/
    
    "FILE_PATH": "upload/",
    # <script src="https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js" referrerpolicy="origin"></script>
    "TINYMCE_CDN": False,
    "TINYMCE_API_KEY": "no-api-key",   # 当TINYMCE_CDN为True时，必须设置该项为你的api-key,否则不能正确加载
    "TINYMCE_DEFAULTS": {
        # 向用户展开展示的工具栏
        'toolbar': 'undo redo | styles | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | print preview media | forecolor backcolor emoticons',
        # 选择要在加载时包含的插件
        'plugins': [
            'advlist', 'autolink', 'link', 'image', 'lists', 'charmap', 'preview', 'anchor', 'pagebreak',
            'searchreplace', 'wordcount', 'visualblocks', 'visualchars', 'code', 'fullscreen', 'insertdatetime',
            'media', 'table', 'emoticons', 'template', 'help'
        ],
        "browser_spellcheck": True,
        "contextmenu": False,
        'image_title': False,
        'automatic_uploads': True,
        'images_file_types': 'jpg,svg,webp,png,gif',
        'file_picker_types': 'file image media',
        'images_upload_url': '/upload/tinymce/',
        'images_reuse_filename': True,   # 是否开启每次为文件生成唯一名称
    },
}
