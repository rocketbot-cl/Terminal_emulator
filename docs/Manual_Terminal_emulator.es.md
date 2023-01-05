# Terminal Emulator
  
Módulo para realizar acciones en un emulador de terminal  

*Read this in other languages: [English](Manual_Terminal_emulator.md), [Español](Manual_Terminal_emulator.es.md).*
  
![banner](imgs/Banner_terminal_emulator.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Conectar
  
Conecta con una terminal
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de sesión|Nombre de la sesión para identificarla|Terminal_1|
|Host|Host de la terminal|localhost|
|Port|Puerto de la terminal|23|
|Tipo de terminal|Tipo de terminal a conectar|3270|
|Seguridad|Tipo de seguridad a utilizar|SSL|
|Mostrar terminal|Mostrar la terminal al conectarse|True|
|Asignar a variable|Asigna el resultado de la conexión a una variable|connected|
|Archivo de configuración|Archivo de configuración de la terminal|c:/wc3270/conf.ini|

### Desconectar
  
Desconecta con la terminal
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de sesión|Nombre de la sesión de la terminal|Terminal_1|

### Cerrar sesión
  
Finaliza la sesión en la terminal
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de sesión|Nombre de la sesión de la terminal|Terminal_1|

### Enviar Texto
  
Envía texto a la terminal
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de sesión|Nombre de la sesión de la terminal|Terminal_1|
|Texto|Texto a enviar|Usuario 1|

### Enviar Tecla
  
Envía tecla a la terminal
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de sesión|Nombre de la sesión de la terminal|Terminal_1|
|Texto|Texto a enviar|Hola Mundo|
|Tecla|Tecla a enviar|BackSpace|

### Mover cursor
  
Mueve el cursor a una posición específica en el terminal
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de sesión|Nombre de la sesión a la que se le enviará la tecla|Terminal_1|
|Mover por posición|Mover el cursor a una posición específica|fila,columna|
|Dirección|Dirección a la que se moverá el cursor|Cursor Down|

### Obtener Texto
  
Obtiene el texto de la terminal
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de sesión|Nombre de la sesión de la terminal|Terminal_1|
|Variable donde guardar el resultado|Variable donde se almacena el resultado|terminal_text|

### Esperar
  
Espera el texto en la terminal según una condición específica
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de sesión|Nombre de la sesión de la terminal|Terminal_1|
|Tiempo de espera|Tiempo de espera en segundos|10|
|Asignar a variable|Asigna el resultado a una variable|condition|
|Esperar por|Espera por la condición seleccionada|Text appears|
|Texto|Texto a esperar|Opción|
