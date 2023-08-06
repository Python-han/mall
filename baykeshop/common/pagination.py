from rest_framework import pagination


class PageNumberPagination(pagination.PageNumberPagination):
    
    page_size = 50
    page_size_query_param = "pageSize"

    