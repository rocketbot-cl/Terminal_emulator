# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Función que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'Terminal_emulator' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)
from p5250 import P5250Client

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

global terminal_simulator

functions = {
    "backSpace": "sendBackSpace",
    "backTab": "sendBackTab",
    "delChar": "delChar",
    "delField": "delField",
    "enter": "sendEnter",
    "f": "sendF",
    "moveCursorDown": "moveCursorDown",
    "moveCursorLeft": "moveCursorLeft",
    "moveCursorRight": "moveCursorRight",
    "moveCursorUp": "moveCursorUp",
    "moveTo": "moveTo",
    "tab": "sendTab"
}

if module == "connect":
    host = GetParams('host')
    path = GetParams('path')
    port = GetParams('port')
    result = GetParams('result')
    try:
        args = {
            "hostName": host
        }
        if path:
            args["hostPort"] = port
        if path:
            args["path"] = path
        terminal_simulator = P5250Client(**args)
        connected = terminal_simulator.connect()
        if result:
            SetVar(result, connected)
    except Exception as e:
        SetVar(result, False)
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "disconnect":
    try:
        terminal_simulator.disconnect()

    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "send_text":
    try:
        text = GetParams('text')
        terminal_simulator.sendText(text)

    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "send_key":
    try:
        key = GetParams('key')
        number = None
        if key.startswith("f"):
            number = key[1:]
            key = "f"

        function = functions[key]
        if number is None:
            getattr(terminal_simulator, function)()
        else:
            getattr(terminal_simulator, function)(number)
    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e


if module == "move_cursor":
    try:
        position = GetParams('position')
        direction = GetParams('direction')

        if position:
            position = eval(position)
            getattr(terminal_simulator, "moveTo")(*arg)
        if direction:
            function = functions[direction]
            getattr(terminal_simulator, function)()

    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "get_text":
    try:
        var = GetParams('result')
        result = terminal_simulator.getScreen()
        if var:
            SetVar(var, result)

    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

