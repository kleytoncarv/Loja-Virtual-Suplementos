from src.domain.order import Order, OrderStatus, OrderStatusName


def test_should_create_order():
    status: OrderStatus = OrderStatus()

    assert status.name == OrderStatusName.ACCOMPLISHED

   # order: Order = Order()

   #parei em 8:18