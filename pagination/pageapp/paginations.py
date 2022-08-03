from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

# class MyPagination(PageNumberPagination):
#     page_size = 5
#     page_query_param = 'p'          #default  'page'
#     page_size_query_param = 'user'
#     max_page_size = 7
#     last_page_strings = 'end'         #default value  'last'
    
    
# class MylimitoffsetPagination(LimitOffsetPagination):
#     default_limit = 5
#     limit_query_param = 'mylimit'
#     offset_query_param = 'myoffset'
#     max_limit = 6 


class MyCursorPaginaion(CursorPagination):
    page_size = 4
    ordering = 'name'
    cursor_query_param = 'cu'