from rest_framework.pagination import PageNumberPagination
class WFMTPagination(PageNumberPagination):
    page_size=10
    page_size_query_params="page_size"
    max_page_size=15