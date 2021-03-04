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

BASE_PATH = tmp_global_obj["basepath"]
cur_path = BASE_PATH + 'modules' + os.sep + 'Terminal_emulator' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)


from p5250 import P5250Client
from terminal_emulator import TerminalEmulator

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

global emulators
global terminal_simulator

LOG_PATH = cur_path = BASE_PATH + 'modules' + os.sep + 'Terminal_emulator' + os.sep + 'logs' + os.sep

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
    port = GetParams('port')
    terminal_type = GetParams('type')
    protocol = GetParams('protocol')
    show = GetParams('show')
    config = GetParams('config')
    id_ = GetParams('id')

    result = GetParams('result')
    try:
        try:
            emulators
        except NameError:
            emulators = TerminalEmulator()

        if not port:
            port = '23'
        if not config:
            config = None

        args = {
            "hostName": host,
            "hostPort": port,
            "configFile": conf
        }

        terminal_simulator = emulators.new_terminal(terminal_type, id_, **args)
        connected = terminal_simulator.connect()
        emulators.create_log(LOG_PATH)
        if result:
            SetVar(result, connected)

    except Exception as e:
        SetVar(result, False)
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

try:

    if module == "disconnect":
        try:
            terminal_simulator = emulators.get_terminal(emulators.actual_id)
            terminal_simulator.disconnect()
            emulators.create_log(LOG_PATH)
        except NameError:
            pass

    if module == "send_text":

        text = GetParams('text')

        try:
            terminal_simulator = emulators.get_terminal(emulators.actual_id)
        except NameError:
            raise Exception("No terminals connected")

        terminal_simulator.waitForField()
        terminal_simulator.sendText(text)
        emulators.create_log(LOG_PATH)

    if module == "send_key":
        key = GetParams('key')

        try:
            terminal_simulator = emulators.get_terminal(emulators.actual_id)
        except NameError:
            raise Exception("No terminals connected")

        number = None
        if key.startswith("f"):
            number = key[1:]
            key = "f"
        function = functions[key]

        terminal_simulator.waitForField()
        if number is None:
            getattr(terminal_simulator, function)()
        else:
            getattr(terminal_simulator, function)(number)

        emulators.create_log(LOG_PATH)

    if module == "move_cursor":
        position = GetParams('position')
        direction = GetParams('direction')

        try:
            terminal_simulator = emulators.get_terminal(emulators.actual_id)
        except NameError:
            raise Exception("No terminals connected")

        terminal_simulator.waitForField()

        if position:
            position = eval(position)
            getattr(terminal_simulator, "moveTo")(*arg)
        if direction:
            function = functions[direction]
            getattr(terminal_simulator, function)()

        emulators.create_log(LOG_PATH)

    if module == "get_text":
        var = GetParams('result')

        try:
            terminal_simulator = emulators.get_terminal(emulators.actual_id)
        except NameError:
            raise Exception("No terminals connected")

        terminal_simulator.waitForField()
        result = terminal_simulator.getScreen()
        emulators.create_log(LOG_PATH)
        if var:
            SetVar(var, result)

    if module == "end_session":
        try:
            terminal_simulator = emulators.get_terminal(emulators.actual_id)
        except NameError:
            raise Exception("No terminals connected")

        terminal_simulator.endSession()
        emulators.create_log(LOG_PATH)

    if module == "change_terminal":
        id_ = GetParams("id")
        try:
            terminal_simulator = emulators.get_terminal(id_)
            emulators.create_log(LOG_PATH)
        except NameError:
            raise Exception("No terminals connected")

    if module == "wait":
        from time import sleep

        option = GetParams("condition")
        text = GetParams("text")
        result = GetParams("result")

        try:
            terminal_simulator = emulators.get_terminal(emulators.actual_id)
        except NameError:
            raise Exception("No terminals connected")

        screen = terminal_simulator.getScreen
        cursor = terminal_simulator.p3270.s3270.statusMsg.cursorPosition
        connected = False
        if option == "appears":
            while text not in screen():
                sleep(1)

        if option == "disappears":
            while text in screen():
                sleep(1)
        if option == "position_cursor":
            while text != cursor():
                sleep(1)

        if result:
            SetVar(result, connected)

except Exception as e:
    print("\x1B[" + "31;40mError\x1B[" + "0m")
    PrintException()
    raise e

