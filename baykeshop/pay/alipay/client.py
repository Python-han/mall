import logging

from django.conf import settings
from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient

from baykeshop.apps.badmin.models import BaykeSystemExtend


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a',)

logger = logging.getLogger('')

_server_url = 'https://openapi-sandbox.dl.alipaydev.com/gateway.do' if settings.DEBUG else 'https://openapi.alipay.com/gateway.do'


def client(app_id=None, app_private_key=None, alipay_public_key=None):
    """ 构造一个支付宝请求客户端 """
    alipay_client_config = AlipayClientConfig(sandbox_debug=settings.DEBUG)
    alipay_client_config.app_id = app_id or BaykeSystemExtend.get_system_extend('alipay_app_id').value
    alipay_client_config.app_private_key = app_private_key or BaykeSystemExtend.get_system_extend('alipay_private_key').value
    alipay_public_key = alipay_public_key or BaykeSystemExtend.get_system_extend('alipay_public_key').value
    alipay_client_config.server_url = _server_url
    return DefaultAlipayClient(alipay_client_config=alipay_client_config, logger=logger)
    