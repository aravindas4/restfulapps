from rest_framework.pagination import LimitOffsetPagination


class NewPagination(LimitOffsetPagination):
    max_limit = 4