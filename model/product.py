from dataclasses import dataclass

@dataclass
class Product:
    id: int
    product_name: str
    brand_id: int
    category_id: int
    model_year: int
    list_price : float


    def __repr__(self):
        return f"{self.id}"

    # Serve per poter usare l'oggetto come nodo del grafo
    def __hash__(self):
        return hash(self.id)