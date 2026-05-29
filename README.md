# PrestaFácil

## 1. Integrantes
| Nombre | Tipo de documento | Rol |
| ------------ | ------------ | ------------ |
| Thomas Gomez Orejuela| CC| Lider de equipo|
| Edinton Hincapie algo| CC| Desarrollador/ Documentacion|
| Laura Cardona algo| CC| Desarrollador / Documentacion|
|Juan Jose algo| CC| Desarrollador / Documentacion|

## 2. Vinculos academicos y descripcion

Thomas Gomez Orejuela — Líder del equipo

Programa: Ingeniería Industrial — Universidad de Antioquia

Descripción: Estudiante de Ingeniería Industrial con interés en la optimización de procesos y programación aplicada. Responsable de la coordinación del equipo, la arquitectura del software y la gestión del repositorio GitHub. Habilidades en lógica algorítmica, trabajo en equipo y resolución de problemas.

Edinton Hincapie — Desarrollador/ Documentacion

Programa: Ingeniería Industrial — Universidad de Antioquia

Descripción: Estudiante con enfoque en la mejora de sistemas y automatización de tareas. Encargado del desarrollo de los módulos de préstamos y devoluciones. Fortalezas en programación orientada a objetos, análisis de requisitos y pensamiento lógico estructurado.

Juan Jose (Apellido) — Desarrollador/ Documentacion

Programa: Ingeniería Industrial — Universidad de Antioquia

Descripción: Estudiante con habilidades en manejo de datos y diseño de soluciones computacionales. Responsable de los módulos de registro de ítems, facturación y exportación de datos. Fortalezas en manejo de archivos, validación de datos y documentación técnica.

Laura Cardona — Documentación y pruebas/ Desarrollador

Programa: Ingeniería Industrial — Universidad de Antioquia

Descripción: Estudiante con habilidades en redacción técnica, organización y control de calidad. Encargada del manual de usuario, las pruebas funcionales del sistema y el seguimiento del plan de proyecto. Fortalezas en atención al detalle, comunicación y gestión documental.

## 3. Nombre del proyecto

Prestafacil

PrestaFácil es un sistema de consola desarrollado en Python que permite gestionar de forma organizada el préstamo de objetos personales: videojuegos, herramientas, libros, dinero y más.
Nuestro nombre refleja el propósito central: hacer que prestar y recordar sea fácil, sin depender de la memoria del prestador.

![PrestaFácil](<logo empresa.jpg>)

## 4. Licencia del software

Este software se distribuye bajo la licencia:

Este software se distribuye bajo la licencia **Creative Commons Atribución 4.0 Internacional (CC BY 4.0)**. 

Este mismo permite a cualquier persona compartir, copiar, redistribuir, mezclar, transformar y crear a partir del código de PrestaFácil para cualquier propósito, incluso comercial, siempre y cuando se otorgue el crédito apropiado a los 4 autores originales (Thomas Gomez, Laura Cardona, Juan jose algo, Edinto Hincapie) y se indiquen si se realizaron cambios.

## 5. Reporte de vision

### 5.1 Descripcion general

PrestaFácil es una aplicación de consola desarrollada en Python que funciona como un gestor de inventario y control de préstamos personales. Está diseñado específicamente para resolver problemas de pérdida de artículos y falta de memoria del prestador mediante un sistema estructurado de registro de usuarios, control de fechas límites, alertas de facturación y almacenamiento persistente en archivos planos con capacidad de exportación a CSV.

### 5.2 Objetivo del producto

*  Proporcionar una interfaz basada en texto que sea rápida, amigable e intuitiva para el usuario.

*  Automatizar el control de tiempos de préstamos, identificando de manera exacta los artículos que superen los umbrales de 20 y 30 días establecidos por el cliente.

*  Centralizar la administración del negocio mediante reportes estadísticos accesibles únicamente para usuarios autorizados (administradores).

### 5.3 Beneficios 

* Cero pérdidas por olvido: El sistema mantiene un registro infalible de qué se prestó, a quién y cuándo.

* Transparencia en penalizaciones: Generación automática de facturas de venta con el cobro del 23% de "impuesto por conchudez" tras un mes de retraso.

* Validación robusta: Evita errores humanos al ingresar datos de contacto, nombres o documentos de identidad erróneos.

## 6. Especificación de requisitos 

### 6.1 Requisitos funcionales

* Registro de Usuarios: El sistema debe registrar clientes validando que el nombre y apellido no contengan números ni tengan menos de 3 letras. El documento debe poseer exactamente 10 dígitos puramente numéricos. El correo debe contener un "@" y terminar en ".com". Ademas, se debe asignar obligatoriamente un tiempo de préstamo de 5, 10, 15 o 30 días.

* Registro de Ítems: El sistema debe permitir registrar artículos asignando un nombre (mínimo 3 letras, permite números), un precio de compra, una categoría (Videojuegos, Libros, Música y video, Herramientas, Dinero, Misceláneo) y un ID alfanumérico único derivado de su categoría. Además, se debe registrar su estado de calidad.

* Gestión de Préstamos: El sistema solo debe permitir préstamos a usuarios previamente registrados. En caso que el usuario no exista, se denegará la operación y se solicitará su registro.

* Control de Devoluciones: El sistema verificará si el usuario consultado tiene préstamos activos. Si la devolución es exitosa y a tiempo, generará un certificado de devolución en un archivo (.txt) nombrado con el formato ["Nombre_Prestador" , "Fecha" , "ID_Ítem"].

* Generación de Ventas por Retraso: Para cualquier artículo cuyo préstamo supere los 30 días, el sistema debe generar automáticamente una factura de venta en texto plano que incluya la motivación del cobro, el precio original del ítem y un recargo del 23% del "impuesto por conchudez", calculando subtotal y total.

* Módulo de Administrador: El sistema restringirá el acceso mediante usuario y contraseña administrativa. Al ingresar correctamente, desplegará reportes de: total de préstamos, total de ítems devueltos, total de ventas, total de dinero pagado, lista completa de usuarios y la indicación de qué usuarios tienen la mayor y menor cantidad de préstamos.

### 6.2 Requisitos no funcionales

* Usabilidad: La interfaz de consola debe ser clara y amigable, usando colores, separadores y mensajes descriptivos que guíen al usuario en cada paso.

* Rendimiento: El sistema debe responder a cualquier operación bajo condiciones normales.

* Fiabilidad: El sistema no debe fallar ante entradas incorrectas del usuario; en su lugar, mostrará un mensaje de error claro y permitirá reintentar.

* Seguridad: El módulo de administración requiere autenticación con usuario y contraseña almacenados en un archivo exclusivo para los administradores.

* Portabilidad: El software debe ejecutarse en Windows, Linux y macOS con Python 3.10+ sin necesidad de instalar librerías externas.

* Compatibilidad: Los archivos generados (.txt, .csv, .json) deben ser legibles en cualquier editor de texto.

* Disponibilidad: El sistema opera de forma local y no requiere conexión a internet, estando disponible el 100% del tiempo que el equipo esté encendido.
## 7. Plan de proyecto

### 7.1 Diagrama de gantt

Actividad                     | S1 (11-17/05)| S2 (18-24/05)| S3 (25-31/05) | S4 (01-07/06)| fecha 5     |
------------------------------|:------------:|:------------:|:-------------:|:------------:|:-----------:|
Análisis de requisitos        |   ██████████ |              |               |              |             |
Diseño de las actas           |   ██████████ |              |               |              |             |
Clases y algoritmo            |   ██████████ |   ██████████ |               |              |             |
algoritmo: Registrar Usuario  |              |   ██████████ |               |              |             |
algoritmo: Registrar Ítem     |              |   ██████████ |   ████        |              |             |
algoritmo: Registrar Préstamo |              |              |   ██████████  |              |             |
algoritmo: Devoluciones       |              |              |   ██████████  |              |             |
algoritmo: Ventas/Facturas    |              |              |   ██████████  |   ██████     |             |
algoritmo: Administrador      |              |              |               |   ██████████ |             |
Pruebas y correcciones        |              |              |               |   ██████████ |   ████████  |
Manual de usuario             |              |              |               |   ██████     |             |
README y documentación        |   ████       |   ██████████ |   ████        |              |             |

### 7.2 Presupueto del proyecto

El proyecto es desarrollado por 4 estudiantes que invierten un total de 50 horas de trabajo académico.

Base salarial de referencia: 1 SMLV Colombia 2026 = $1.750.905. COP/mes ---> 1 mes : 192 horas
Valor hora de práctica profesional = $1.750.905. ÷ 192 horas = $9.120 COP/hora

Concepto             | Horas | Valor hora | Total |
---------------------|-------|------------|----------|
Análisis y diseño    |   8   |    $9.120  | $72.960  |                  
Desarrollo de código |  25   |    $9.120  | $228.000 |                  
Pruebas y depuración |   8   |    $9.120  | $72.960  |                 
Documentacion        |   9   |    $9.120  | $82.080  |               
Total                |  50   |    $9.120  | $456.000 |

Este presupuesto representa el costo en tiempo de formación profesional de los 4 integrantes y no implica pago monetario real.