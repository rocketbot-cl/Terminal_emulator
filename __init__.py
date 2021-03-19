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
import platform

PLATFORM = platform.platform(terse=True)

# Define path
BASE_PATH = tmp_global_obj["basepath"]
MODULE_PATH = BASE_PATH + 'modules' + os.sep + 'Terminal_emulator' + os.sep
LOG_PATH = MODULE_PATH + "logs" + os.sep

platform = PLATFORM.split("-")[0]
APP_PATH = MODULE_PATH + 'bin' + os.sep + platform + os.sep + "fileview" + os.sep + "fileview.exe"

cur_path = MODULE_PATH + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from p5250 import P5250Client
from terminal_emulator import *

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

# Globals declared here
global mod_terminal_emulator_sessions
# Default declared here
SESSION_DEFAULT = "default"
# Initialize settings for the module here
try:
    if not mod_terminal_emulator_sessions:
        mod_terminal_emulator_sessions = {SESSION_DEFAULT: {}}
except NameError:
    mod_terminal_emulator_sessions = {SESSION_DEFAULT: {}}

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
    session = GetParams('id')

    result = GetParams('result')
    try:

        if not port:
            port = '23'
        if not config:
            config = None
        if not session:
            session = SESSION_DEFAULT

        path = path = BASE_PATH + 'modules' + os.sep + 'Terminal_emulator' + os.sep + 'bin' + os.sep + "3270" + os.sep
        args = {
            "hostName": host,
            "hostPort": port,
            "configFile": config,
            "path": path
        }

        terminal_simulator = create_terminal(terminal_type, **args)
        terminal_log_path = LOG_PATH + session + ".txt"
        mod_terminal_emulator_sessions[session] = {
            "terminal": terminal_simulator,
            "log_path": terminal_log_path,
            "process": None
        }

        connected = terminal_simulator.connect()
        create_log(terminal_simulator, terminal_log_path)

        if show and show == "True":
            print([APP_PATH, "-l=" + terminal_log_path])
            process = subprocess.Popen([APP_PATH, "-l=" + terminal_log_path])
            mod_terminal_emulator_sessions[session]["process"] = process
            print(process.pid)
        if result:
            SetVar(result, connected)

    except Exception as e:
        SetVar(result, False)
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

try:

    if module == "disconnect":

        session = GetParams('id')

        if not session:
            session = SESSION_DEFAULT

        terminal_simulator = mod_terminal_emulator_sessions[session]["terminal"]
        terminal_log_path = mod_terminal_emulator_sessions[session]["log_path"]
        process = mod_terminal_emulator_sessions[session]["process"]

        terminal_simulator.endSession()
        terminal_simulator.disconnect()

        create_log(terminal_simulator, terminal_log_path)

        import psutil

        for p in psutil.process_iter(attrs=["pid", "name"]):
            if p.info["pid"] == process.pid:
                p.kill()

    if module == "send_text":

        text = GetParams('text')
        session = GetParams('id')

        if not session:
            session = SESSION_DEFAULT

        terminal_simulator = mod_terminal_emulator_sessions[session]["terminal"]
        terminal_log_path = mod_terminal_emulator_sessions[session]["log_path"]

        terminal_simulator.waitForField()

        terminal_simulator.sendText(text)
        create_log(terminal_simulator, terminal_log_path)

    if module == "send_key":
        key = GetParams('key')
        session = GetParams('id')

        if not session:
            session = SESSION_DEFAULT

        terminal_simulator = mod_terminal_emulator_sessions[session]["terminal"]
        terminal_log_path = mod_terminal_emulator_sessions[session]["log_path"]

        number = None
        if key.startswith("f"):
            number = key[1:]
            key = "f"
        function = functions[key]

        terminal_simulator.waitForField()
        if number is None:
            getattr(terminal_simulator, function)()
        else:
            getattr(terminal_simulator, function)(int(number))

        create_log(terminal_simulator, terminal_log_path)

    if module == "move_cursor":
        position = GetParams('position')
        direction = GetParams('direction')
        session = GetParams('id')

        if not session:
            session = SESSION_DEFAULT

        terminal_simulator = mod_terminal_emulator_sessions[session]["terminal"]
        terminal_log_path = mod_terminal_emulator_sessions[session]["log_path"]

        terminal_simulator.waitForField()

        if position:
            position = eval(position)
            getattr(terminal_simulator, "moveTo")(*arg)
        if direction:
            function = functions[direction]
            getattr(terminal_simulator, function)()

        create_log(terminal_simulator, terminal_log_path)

    if module == "get_text":
        var = GetParams('result')
        session = GetParams('id')

        if not session:
            session = SESSION_DEFAULT

        terminal_simulator = mod_terminal_emulator_sessions[session]["terminal"]
        terminal_log_path = mod_terminal_emulator_sessions[session]["log_path"]

        result = terminal_simulator.getScreen()

        create_log(terminal_simulator, terminal_log_path)
        if var:
            SetVar(var, result)

    if module == "end_session":

        session = GetParams('id')

        if not session:
            session = SESSION_DEFAULT

        terminal_simulator = mod_terminal_emulator_sessions[session]["terminal"]
        terminal_log_path = mod_terminal_emulator_sessions[session]["log_path"]

        terminal_simulator.endSession()
        create_log(terminal_simulator, terminal_log_path)

    if module == "wait":
        from time import sleep, perf_counter

        ProcessTime = time.perf_counter
        ProcessTime()
        start = ProcessTime()

        wait = GetParams("time")
        option = GetParams("condition")
        text = GetParams("text")
        result = GetParams("result")
        session = GetParams('id')

        if not session:
            session = SESSION_DEFAULT

        terminal_simulator = mod_terminal_emulator_sessions[session]["terminal"]
        terminal_log_path = mod_terminal_emulator_sessions[session]["log_path"]

        screen = terminal_simulator.getScreen
        cursor = terminal_simulator.p3270.s3270.statusMsg.cursorPosition
        connected = False
        now = 0
        if option == "appears":
            while text not in screen() and now - start <= int(wait):
                sleep(1)
                now = ProcessTime()

        if option == "disappears":
            while text in screen() and now - start <= int(wait):
                sleep(1)
                now = ProcessTime()
        if option == "position_cursor":
            while text != cursor() and now - start <= int(wait):
                sleep(1)
                now = ProcessTime()
        if now - start > int(wait):
            connected = True
        if result:
            SetVar(result, connected)

except Exception as e:
    print("\x1B[" + "31;40mError\x1B[" + "0m")
    PrintException()
    raise e

