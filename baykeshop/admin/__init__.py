from django.contrib.admin.apps import AdminConfig


class BaykeAdminConfig(AdminConfig):
    
    default_site = "baykeshop.apps.admin.sites.AdminSite"