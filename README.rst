El Módulo que vemos aquí se ha hecho de la siguiente manera:
1. Se ha lanzado una consulta a ChatGPT para acelerar la construcción de modelos y vistas.
2. Se han añadido ficheros necesarios para el funcionamiento del módulo que el chat no incluía
 Como son ir.model.access.csv, una vista de menús y los datos dentro de los __init__.py
3. Se ha desarrollado camputes para los campos que lo necesitaban.
4. Se Envía de nuevo la consulta a chatgPT para resolver el ejercicio,
Comprobando que el código sea funcional, y siga los estándares.

Resultado:
Modelo ResPartner:
Este modelo representa a los socios comerciales (clientes, proveedores, etc.).
Tiene una relación One2many con el modelo SaleOrder llamada sale_order_ids, que representa las órdenes de venta relacionadas con este socio comercial.

Modelo SaleOrder:
Este modelo representa las órdenes de venta.
Tiene una relación Many2one con el modelo ResPartner llamada partner_id, que indica el socio comercial asociado con la orden de venta.

Modelo SaleOrderLine:
Este modelo representa las líneas de las órdenes de venta.
Tiene una relación Many2one con el modelo SaleOrder llamada order_id, que indica la orden de venta a la que pertenece esta línea.
Calcula el subtotal de la línea en euros en el campo price_subtotal mediante el método _compute_subtotal.

Modelo ProductProduct:
Este modelo representa los productos.
Es utilizado en el modelo StockHistory para indicar el producto asociado a un historial de stock.
También se utiliza en el modelo SaleOrderLine para representar el producto vendido en una línea de orden de venta.

Modelo StockHistory:
Este modelo representa el historial de stock de productos.
Tiene una relación Many2one con el modelo ProductProduct llamada product_id, que indica el producto relacionado con el historial de stock.