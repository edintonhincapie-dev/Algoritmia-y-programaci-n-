# PrestaFácil

## 1. Integrantes
| Nombre | Tipo de documento | Rol |
| ------------ | ------------ | ------------ |
| Thomas Gomez Orejuela| CC| Lider de equipo|
| Edinton Hincapie algo| CC| Desarrollador/ Documentacion|
| Laura Cardona algo| CC| Desarrollador / Documentacion|
|Juan Jose algo| CC| Desarrollador / Documentacion|

## 2. Vinculos academicos y descripcion

* Thomas Gomez Orejuela — Lider del equipo

Programa: Ingeniería Industrial — Universidad de Antioquia

Interes en la optimizacion de procesos y programacion aplicada. Responsable de la coordinacion del equipo, la arquitectura del software. Habilidades en logica algoritmica, trabajo en equipo y resolucion de conflictos, esto mismo en caso de necesitarse.

* Edinton Hincapie algo — Desarrollador/ Documentacion

Programa: Ingeniería Industrial — Universidad de Antioquia

Cuenta con un enfoque en la mejora de sistemas y automatización de tareas. Encargado del desarrollo de los módulos de préstamos y devoluciones, tambien, encargado de la gestión del repositorio GitHub.
Fortalezas en programación orientada a objetos, análisis de requisitos y pensamiento lógico estructurado.

* Juan Jose algo  — Desarrollador/ Documentacion

Programa: Ingeniería Industrial — Universidad de Antioquia

Cuenta con habilidades en manejo de datos y diseño de soluciones computacionales. Responsable de los módulos de registro de ítems, facturación y exportación de datos. Fortalezas en manejo de archivos, validación de datos y documentación técnica.

* Laura Cardona algo — Documentación/ Desarrollador

Programa: Ingeniería Industrial — Universidad de Antioquia

Cuenta con habilidades en redacción técnica, organización y control de calidad. Encargada del manual de usuario, las pruebas funcionales del sistema y el seguimiento del plan de proyecto. Fortalezas en atención al detalle, comunicación y gestión documental.

## 3. Nombre del proyecto

Prestafacil

PrestaFácil es un sistema de consola desarrollado en Python que permite gestionar de forma organizada el préstamo de objetos personales: videojuegos, herramientas, libros, dinero y más.
Nuestro nombre refleja el propósito central: hacer que prestar y recordar sea fácil, sin depender de la memoria del prestador.

![PrestaFácil](<logo empresa.jpg>)

## 4. Licencia del software

Este software se distribuye bajo la licencia:

Este software se distribuye bajo la licencia **Creative Commons Atribución 4.0 Internacional (CC BY 4.0)**. 

Este mismo permite a cualquier persona compartir, copiar, redistribuir, mezclar, transformar y crear a partir del código de PrestaFácil para cualquier propósito, incluso comercial, siempre y cuando se otorgue el crédito apropiado a los 4 autores originales (Thomas Gomez, Laura Cardona, Juan jose algo, Edinto Hincapie) y se indique en caso de realizarse cambios al codigo.

## 5. Reporte de vision

### 5.1 Descripcion general

PrestaFácil es una aplicacion de consola desarrollada en Python que funciona como un gestor de inventario y control de prestamos personales. Esta diseñado específicamente para resolver problemas de perdida de articulos y falta de memoria del prestador mediante un sistema estructurado de registro de usuarios, control de fechas límites, alertas de facturación y almacenamiento persistente en archivos con capacidad de exportación a CSV (tablas).

### 5.2 Objetivo del producto

*  Proporcionar una interfaz basada en texto que sea rapida, amigable e intuitiva para el usuario.

*  Automatizar el control de tiempos de prestamos, identificando de manera exacta los articulos que superen los umbrales de 20 y 30 días establecidos por el cliente.

*  Centralizar la administracion del negocio mediante reportes estadísticos accesibles únicamente para usuarios autorizados (administradores).

### 5.3 Beneficios 

* Cero perdidas por olvido: El sistema mantiene un registro infalible de que se presto, a quien y cuando.

* Transparencia en penalizaciones: Generación automática de facturas de venta con el cobro del 23% de "impuesto por conchudez" tras un mes de retraso.

* Validación robusta: Evita errores humanos al ingresar datos de contacto, nombres o documentos de identidad erróneos.

## 6. Especificación de requisitos 

### 6.1 Requisitos funcionales

* Registro de Usuarios: El sistema debe registrar clientes validando que el nombre y apellido no contengan numeros ni tengan menos de 3 letras. El documento debe poseer exactamente 10 dígitos puramente numericos (Cedula colombiana). El correo debe contener un "@" y terminar en ".com". Ademas, se debe asignar obligatoriamente un tiempo de prestamo de 5, 10, 15 o 30 días.

* Registro de items: El sistema debe permitir registrar artículos asignando un nombre (mínimo 3 letras, permite numeros), un precio de compra, una categoria (Videojuegos, Libros, Música y video, Herramientas, Dinero, Miscelaneo) y un ID alfanumerico único derivado de su categoria. Ademas, se debe registrar su estado de calidad.

* Gestion de Prestamos: El sistema solo debe permitir prestamos a usuarios previamente registrados. En caso que el usuario no exista, se denegara la operación y se solicitara su registro.

* Control de Devoluciones: El sistema verificara si el usuario consultado tiene prestamos activos. Si la devolución es exitosa y a tiempo, generara un certificado de devolucion en un archivo del tipo (.txt) nombrado con el formato ["Nombre_Prestador" , "Fecha" , "ID_Ítem"].

* Generacion de Ventas por Retraso: Para cualquier articulo cuyo prestamo supere los 30 días, el sistema debe generar automáticamente una factura de venta en texto plano que incluya la motivación del cobro, el precio original del item y un recargo del 23% del "impuesto por conchudez", calculando subtotal y total.

* Modulo de Administrador: El sistema restringirá el acceso mediante usuario y contraseña administrativa. Al ingresar correctamente, desplegará reportes de: total de préstamos, total de ítems devueltos, total de ventas, total de dinero pagado, lista completa de usuarios y la indicación de qué usuarios tienen la mayor y menor cantidad de prestamos.

### 6.2 Requisitos no funcionales

* Usabilidad: La interfaz de consola debe ser clara y amigable, usando colores, separadores y mensajes descriptivos que guíen al usuario en cada paso.

* Rendimiento: El sistema debe responder a cualquier operación bajo condiciones normales.

* Fiabilidad: El sistema no debe fallar ante entradas incorrectas del usuario; en su lugar, mostrara un mensaje de error claro y permitira reintentar.

* Seguridad: El modulo de administracion requiere autenticación con usuario y contraseña almacenados en un archivo exclusivo para los administradores.

* Portabilidad: El software debe ejecutarse en Windows, Linux y macOS con Python 3.10+ sin necesidad de instalar librerias externas.

* Compatibilidad: Los archivos generados deben ser legibles en cualquier editor de texto.

* Disponibilidad: El sistema opera de forma local y no requiere conexion a internet, estando disponible el 100% del tiempo que el equipo esté encendido.
## 7. Plan de proyecto

### 7.1 Diagrama de gantt

Actividad                     | S1 (11-17/05)| S2 (18-24/05)| S3 (25-31/05) | S4 (01-07/06)| S5 (08-14/06)|
------------------------------|:------------:|:------------:|:-------------:|:------------:|:------------:|
Analisis de requisitos        |   ██████████ |              |               |              |              |
Diseño de las actas           |   ██████████ |              |               |              |              |
Clases y algoritmo            |   ██████████ | ████████████ |               |              |              |
algoritmo: Registrar Usuario  |              | ████████████ |               |              |              |
algoritmo: Registrar Ítem     |              | ████████████ | ██████        |              |              |
algoritmo: Registrar Prestamo |              |              | ████████████  |              |              |
algoritmo: Devoluciones       |              |              | ████████████  |              |              |
algoritmo: Ventas/Facturas    |              |              | ████████████  | ███████      |              |
algoritmo: Administrador      |              |              |               | ████████████ |              |
Pruebas y correcciones        |              |              |               | ████████████ | ████████████ |
Manual de usuario             |              |              |               | █████████    |              |
README y documentacion        | ██████████   | ████████████ | ██████        |              |              |

### 7.2 Presupueto del proyecto

El proyecto es desarrollado por 4 estudiantes que invierten un total de 50 horas de trabajo academico.

1 SMLV Colombia 2026 = $1.750.905. COP/mes ---> 1 mes : 192 horas
Valor hora de práctica profesional = $1.750.905. ÷ 192 horas = $9.120 COP/hora

Concepto             | Horas | Valor hora | Total |
---------------------|-------|------------|----------|
Analisis y diseño    |   8   |    $9.120  | $72.960  |                  
Desarrollo de codigo |  25   |    $9.120  | $228.000 |                  
Pruebas              |   8   |    $9.120  | $72.960  |                 
Documentacion        |   9   |    $9.120  | $82.080  |               
Total                |  50   |    $9.120  | $456.000 |

Este presupuesto representa el costo en tiempo de formación profesional de los 4 integrantes y no implica pago monetario real.