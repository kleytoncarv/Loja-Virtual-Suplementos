from src.domain.customer import Customer


def test_should_create_customer():
    customer: Customer = Customer(name="Kleyton", email="kleyton@gmail.com")
    
    assert customer.name == "Kleyton"
    assert customer.email == "kleyton@gmail.com"
    