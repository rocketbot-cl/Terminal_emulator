# coding: utf-8
"""Module for terminal emulator.

Base para desarrollo de modulos externos.
Para obtener el modulo/Función que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

__version__ = "2.1.1"
__author__ = "Danilo Toro"
__update_by__ = "Danilo Toro"

# ignore warning for rocketbot functions
tmp_global_obj = tmp_global_obj #type:ignore
GetParams = GetParams #type: ignore
PrintException = PrintException #type: ignore
SetVar = SetVar #type: ignore

# Python modules
import os
import sys
import platform
import subprocess


PLATFORM = platform.platform(terse=True)

# Define path
BASE_PATH = tmp_global_obj["basepath"]
MODULE_PATH = BASE_PATH + 'modules' + os.sep + 'Terminal_emulator' + os.sep
LOG_PATH = MODULE_PATH + "logs" + os.sep

platform_ = PLATFORM.split("-")[0]
APP_PATH = MODULE_PATH + 'bin' + os.sep + platform_ + os.sep + "fileview" + os.sep + "fileview.exe"

# Import module libs
cur_path = MODULE_PATH + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from p5250 import P5250Client #type:ignore
from terminal_emulator import create_terminal, create_log

# Globals declared here
global mod_terminal_emulator_sessions
# Default declared here
SESSION_DEFAULT = "default"
# Initialize settings for the module here
try:
    if not mod_terminal_emulator_sessions: #type:ignore
        mod_terminal_emulator_sessions = {SESSION_DEFAULT: {}}
except NameError:
    mod_terminal_emulator_sessions = {SESSION_DEFAULT: {}}

FUNCTIONS_ = {
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

module = GetParams("module")
session = GetParams('id')

if not session:
    session = SESSION_DEFAULT

if session in mod_terminal_emulator_sessions:
    terminal_simulator = mod_terminal_emulator_sessions[session].get("terminal")
    terminal_log_path = mod_terminal_emulator_sessions[session].get("log_path")

if module == "connect":
    host = GetParams('host')
    port = GetParams('port')
    terminal_type = GetParams('type')
    protocol = GetParams('protocol')
    show = GetParams('show')
    config = GetParams('config')

    result = GetParams('result')
    try:

        if not port:
            port = '23'
        if not config:
            config = None

        path = path = BASE_PATH + 'modules' + os.sep + 'Terminal_emulator' + os.sep + 'bin' + os.sep + "3270" + os.sep
        args = {
            "hostName": host,
            "hostPort": port,
            "configFile": config,
            "path": path
        }
        
        if protocol == "tls":
            args["enableTLS"] = "yes"
           
        terminal_simulator = create_terminal(terminal_type, **args)
        terminal_log_path = LOG_PATH + session + ".txt"
        mod_terminal_emulator_sessions[session] = {
            "terminal": terminal_simulator,
            "log_path": terminal_log_path,
            "process": None
        }

        connected = terminal_simulator.connect()

        if show and show == "True":
            print([APP_PATH, "-l=" + terminal_log_path])
            process = subprocess.Popen([APP_PATH, "-l=" + terminal_log_path])
            mod_terminal_emulator_sessions[session]["process"] = process
        if result:
            SetVar(result, connected)

    except Exception as e:
        SetVar(result, False)
        PrintException()
        raise e

try:

    if module == "disconnect":
        process = mod_terminal_emulator_sessions[session]["process"]

        terminal_simulator.endSession()
        terminal_simulator.disconnect()

        if process is not None:
            import psutil

            for p in psutil.process_iter(attrs=["pid", "name"]):
                if p.info["pid"] == process.pid:
                    p.kill()

        terminal_simulator = None

    if module == "send_text":

        text = GetParams('text')

        terminal_simulator.waitForField()

        terminal_simulator.sendText(text)

    if module == "send_key":
        params_key = GetParams('key') or ""
        params_keys = GetParams("keys")
        params_only_pf = GetParams("only_PF")
        number = []
        key = params_key

        if not session:
            session = SESSION_DEFAULT

        if key.startswith("f"):
            number = [int(params_key[1:])]
            key = "f"

        function = FUNCTIONS_.get(key)

        # terminal_simulator.waitForField()
        if params_key and params_only_pf=="True":
            terminal_simulator.p3270.s3270.do("PF({})".format(number[0]))
        elif params_key:
            print(terminal_simulator, function)
            getattr(terminal_simulator, function)(*number)        
        
        elif params_keys:
            for key in params_keys:
                terminal_simulator.p3270.s3270.do("Key({})".format(key[0]))



    if module == "move_cursor":
        position = GetParams('position')
        direction = GetParams('direction')

        terminal_simulator.waitForField()

        if position:
            position = eval(position)
            getattr(terminal_simulator, "moveTo")(*position)
        if direction:
            function = FUNCTIONS_[direction]
            getattr(terminal_simulator, function)()

    if module == "get_text":
        var = GetParams('result')

        result = terminal_simulator.getScreen()
        if var:
            SetVar(var, result)

    if module == "end_session":

        terminal_simulator.endSession()


    if module == "wait":
        from time import sleep, perf_counter

        ProcessTime = perf_counter
        ProcessTime()
        start = ProcessTime()

        wait = GetParams("time")
        option = GetParams("condition")
        text = GetParams("text")
        result = GetParams("result")

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

    if terminal_log_path and terminal_simulator is not None:
        create_log(terminal_simulator, terminal_log_path)

except Exception as e:
    PrintException()
    raise e

