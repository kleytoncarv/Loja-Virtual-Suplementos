# Loja-Virtual-Suplementos
Modelo de Loja E-commerce para suplementos.



# Sistema de Pedidos

- Customer
  name
  email
  
- Product
  name
  description
  price

- Order
  [OrderStatus]
  [OrderItem]
  total
  
- OrderStatus
  name (REALIZADO, EM PREPARAÇÃO, ENVIADO, ENTREGUE, FINALIZADO)

- OrderItem
  - product_id
  - price
  - quantity
  
  
