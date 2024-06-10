### Proyecto Urban Grocers 

Este proyecto fue desarrollado como parte del séptimo sprint del bootcamp de QA de TripleTen. 

El objetivo de este proyecto es automatizar las pruebas para la creación de kits de productos en la aplicación Urban Grocers. La aplicación Urban Grocers permite a los usuarios crear kits de productos personalizados que pueden incluir una variedad de artículos. Se ha creado una lista de comprobación específica para el campo `name` en la solicitud de creación de un kit de productos. La tarea es automatizar estas pruebas, cargar el código en GitHub y enviar el repositorio para revisión.

Este proyecto forma parte del bootcamp de QA de TripleTen, donde aprenderemos a automatizar pruebas y garantizar la calidad del software. Para también poner en práctica las habilidades adquiridas durante el bootcamp y aplicar técnicas de automatización de pruebas.

Urban Grocers es una aplicación que permite a los usuarios crear y gestionar kits de productos personalizados. Los usuarios pueden seleccionar diversos productos y agruparlos en kits que se pueden comprar y enviar.

como un solo paquete. La funcionalidad de creación de kits es esencial para la experiencia del usuario y, por lo tanto, es crucial que sea probada exhaustivamente. 

### En el proyecto se utilizaron la siguientes tecnologías:
- pyton 
- pytest
- Requests (para envier solicitudes HTTP)
- Git

### Pruebas Automatizadas 

Se han automatizado las siguientes pruebas para el campo `name` en la solicitud de creación de un kit de productos: 
1. Prueba 1: Nombre con un solo carácter permitido. 
2. Prueba 2: Nombre con 511 caracteres permitidos. 
3. Prueba 3: Nombre con 0 caracteres (menor que la cantidad permitida). 
4. Prueba 4: Nombre con 512 caracteres (mayor que la cantidad permitida). 
5. Prueba 5: Nombre con caracteres especiales permitidos. 
6. Prueba 6: Nombre con espacios permitidos. 
7. Prueba 7: Nombre con números permitidos. 
8. Prueba 8: El parámetro `name` no se pasa en la solicitud. 
9. Prueba 9: El parámetro `name` se pasa como un número en lugar de una cadena. 

### Resultados de las Pruebas 

De las 9 pruebas realizadas, 4 fallaron y 5 fueron exitosas a continuación las pruebas que fallaron:

Prueba 3: Nombre con 0 caracteres 
-Resultado Esperado: 400 
-Resultado Actual: 201 

Prueba 4: Nombre con 512 caracteres 
- Resultado Esperado: 400 
- Resultado Actual: 201 

Prueba 8: El parámetro `name` no se pasa en la solicitud 
-Resultado Esperado: 400 
-Resultado Actual: 500 

Prueba 9: El parámetro `name` se pasa como un número en lugar de una cadena 
-Resultado Esperado: 400 
-Resultado Actual: 201
