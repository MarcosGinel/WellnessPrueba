# WellnessPrueba
Prueba técnica para Wellness

Este proyecto Django es el proyecto que implementa la parte del servidor.

Consiste en una API rest par almacenar datos sobre los precios diarios de la "luz", el consumo diario de cada usuario y alguna información.

Se implementa una api rest y una autenticación mediante TokenREST sin usar el sistema de django de logging nativo (que también se puede usar).

Requiere:

* Django 1.10.3
* django-cors-headers 1.2.2
* djangorestframework 3.5.2

Viene configurado con datos en la BD y con un usuario que es 
  Username: admin
  Password: wellness
  
Si se visita el sitio desde http://127.0.0.1:8000, se ofrecen las siguientes apis (que se pueden ver mediante ApiView):
  * /users/api/v1/users/
  * /facturas/api/v1/consumodiario
  * /facturas/api/v1/preciodiario
  
Los usuarios pueden consultar, pero no escribir, actualizar o borrar. Sólo el usuario admin-wellness puede hacerlo.
