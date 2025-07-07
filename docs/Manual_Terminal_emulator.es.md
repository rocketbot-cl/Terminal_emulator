



# Terminal Emulator
  
Este módulo permite realizar acciones en un emulador de terminal, como conectar, enviar texto, enviar teclas, mover el cursor, etc.  

*Read this in other languages: [English](Manual_Terminal_emulator.md), [Português](Manual_Terminal_emulator.pr.md), [Español](Manual_Terminal_emulator.es.md)*
  
![banner](imgs/Banner_Terminal_emulator.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Conectar
  
Conecta con una terminal
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de sesión||Terminal_1|
|Host||localhost|
|Port||23|
|Tipo de terminal|||
|Modelo de terminal|||
|Protocolo de seguridad|||
|Mostrar terminal|Si se marca, se mostrara una terminal para revisar ejecuciones del robot. Herramienta para desarollo.||
|Workstation ID|Opcional. Identificador único de estación de trabajo para la conexión al servidor AS400. Este valor debe estar registrado y autorizado por el sistema. Si se deja en blanco, se generará uno automáticamente.|BOTWKS01|
|Archivo de configuración||c:/wc3270/conf.ini|
|Variable donde guardar el resultado||connected|

### Enviar Texto
  
Envía texto a la terminal
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de sesión||Terminal_1|
|Texto|Texto a envir a la terminal|Usuario 1|

### Enviar Tecla
  
Envía una tecla o secuencia de teclas a la terminal
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de sesión||Terminal_1|
|Keys|Teclas a enviar|Hola Mundo|
|Tecla|Tecla a enviar||
|Cantidad|Cantidad de veces a enviar la tecla|1|
|Enviar tecla F sin comando PA |Enviar tecla de Función de Programa (PF) sin tecla de Atención de Programa (PA).||

### Mover cursor
  
Mueve el cursor 
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de sesión||Terminal_1|
|Mover por posición||fila,columna|
|Dirección|Dirección a donde mover el cursor||
|Cantidad|Cantidad de lugares a mover|1|

### Obtener Texto
  
Obtiene el texto de la terminal
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de sesión||Terminal_1|
|Variable donde guardar el resultado||terminal_text|

### Esperar
  
Espera el texto en la terminal según una condición específica
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de sesión||Terminal_1|
|Tiempo de espera|Tiempo maximo de espera|10|
|Esperar por|||
|Texto|Texto por el cual se esperara|Opción|
|Variable donde guardar el resultado||condition|

### Desconectar
  
Desconecta con la terminal
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de sesión||Terminal_1|

### Cerrar sesión
  
Finaliza la sesión en la terminal
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de sesión||Terminal_1|
