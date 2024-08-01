from src.domain.product import Product


def test_should_create_product():
    product: Product = Product(
        name="Creatina", 
        description="Creatina monohidrata, 100% pura",
        price=100)
    
   
    assert product.name == "Creatina"
    assert product.description == "Creatina monohidrata, 100% pura"
    assert product.price == 100.0