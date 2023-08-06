from django.contrib.admin.apps import AdminConfig


class BaykeAdminConfig(AdminConfig):
    
    default_site = "baykeshop.admin.sites.AdminSite"
    