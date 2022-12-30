# Terminal Emulator
  
Module to perform actions on a terminal emulator  

*Read this in other languages: [English](Manual_Terminal_emulator.md), [Español](Manual_Terminal_emulator.es.md).*
  
![banner](imgs/Banner_terminal_emulator.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Connect
  
Connect to terminal
|Parameters|Description|example|
| --- | --- | --- |
|Session name|Session name to identify it|Terminal_1|
|Host|Terminal host|localhost|
|Port|Terminal port|23|
|Terminal type|Terminal type to connect|3270|
|Seguridad|Security type to use|SSL|
|Show terminal|Show the terminal when connected|True|
|Result|Assign the connection result to a variable|connected|
|Configuration file|Terminal configuration file|c:/wc3270/conf.ino|

### Disconnect
  
Disconnect terminal
|Parameters|Description|example|
| --- | --- | --- |
|Session name|Terminal session name|Terminal_1|

### End Session
  
Finish terminal session
|Parameters|Description|example|
| --- | --- | --- |
|Session name|Terminal session name|Terminal_1|

### Send Text
  
Send text to Terminal
|Parameters|Description|example|
| --- | --- | --- |
|Session name|Terminal session name|Terminal_1|
|Text|Text to send|User 1|

### Send Key
  
Send key to Terminal
|Parameters|Description|example|
| --- | --- | --- |
|Session name|Terminal session name|Terminal_1|
|Text|Text to send|Hello World|
|Keys|Key to send|BackSpace|

### Move Cursor
  
Move cursor to specific position on Terminal
|Parameters|Description|example|
| --- | --- | --- |
|Session name|Session name to send the key|Terminal_1|
|Move to position|Move cursor to specific position|row,column|
|Direction|Direction to move the cursor|Cursor Down|

### Get Text
  
Get text from Terminal
|Parameters|Description|example|
| --- | --- | --- |
|Session name|Name of the terminal session|Terminal_1|
|Variable|Variable where the result is stored|terminal_text|

### Wait
  
Wait for text on terminal by specific condition
|Parameters|Description|example|
| --- | --- | --- |
|Session name|Terminal session name|Terminal_1|
|Wait time|Wait time in seconds|10|
|Result|Assign the result to a variable|condition|
|Wait by|Wait by the selected condition|Text appears|
|Text|Text to wait|Option|
