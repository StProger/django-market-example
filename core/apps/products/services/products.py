from abc import ABC, abstractmethod
from typing import Iterable

from core.apps.products.entities.products import Product
from core.apps.products.models.products import Product as ProductModel

class BaseProductService(ABC):
    
    @abstractmethod
    def get_product_list(self) -> Iterable[Product]:
        ...


    @abstractmethod
    def get_product_count(self) -> int:
        ...
    

class ORMProductService(BaseProductService):

    def get_product_list(self) -> Iterable[Product]:
        
        qs = ProductModel.objects.filter(is_visible=True)
        return [product_dto.to_entity() for product_dto in qs]

    def get_product_count(self) -> int:

        procuct_count = ProductModel.objects.filter(is_visible=True).count()
        return procuct_count