from dataclasses import dataclass
from importlib.abc import MetaPathFinder
from typing import List, Optional

from models.dimensions import Dimensions
from models.review import Review

@dataclass
class Product:
    id: int
    title: str
    description: str
    category: str
    price: float
    discount_percentage: float
    rating: float
    stock: int
    tags: List[str]
    sku: str
    weight: int
    dimensions: str
    warranty_information: str
    shipping_information: str
    availability_status: str
    reviews: List[Review]
    return_policy: str
    minimum_order_quantity: int
    meta: str
    images: List[str]
    thumbnail: str
    brand: Optional[str] = None

