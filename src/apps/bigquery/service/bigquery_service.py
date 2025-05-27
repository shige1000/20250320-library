from utils import AsyncSingleton
from apps.bigquery.service.bigquery_service_interface import BigqueryServiceInterface


class BigqueryService(AsyncSingleton, BigqueryServiceInterface):
    pass
