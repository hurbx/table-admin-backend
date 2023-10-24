# table-admin-backend
## Proyecto en desarrollo...

El proyecto tiene como objetivo crear una aplicacion
web para la administracion de las mesas de un restaurant,
su consumo total, productos agregados a las mesas,
trabajador encargado de la mesa, etc, luego ser
capaces de generar una boleta, con el monto total,
propina y detalle de los productos consumidos. 

---
MER
---
```mermaid
  erDiagram
      Mesa ||--o{ Productos : has
      Mesa ||--o{ Empleado : has
      Mesa ||--o{ Boleta : has
      Boleta ||--o{ Poprina: has
      Empleado ||--o{ Tipo : has
      Productos ||--o{ Categoria : has
      Categoria ||--o{ Descuento : has
      Boleta ||--o{ Empleado : has
      Boleta ||--o{ Mesa : has
      Boleta ||--o{ Productos : has
      
```
