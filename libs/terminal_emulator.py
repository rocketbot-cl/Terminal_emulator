from p5250 import P5250Client
from p3270.p3270 import P3270Client

terminals = {
    "3270": P3270Client,
    "5250": P5250Client,
}


def create_terminal(terminal_type, **kwargs):
    if terminal_type in ("3270", "5250"):
        return terminals[terminal_type](**kwargs)


def create_log(terminal, path):
    with open(path, "w") as log:
        log.write(terminal.getScreen())


class TerminalEmulator:

    def __init__(self):
        self.terminals = []
        self.actual_id = "default"

    def new_terminal(self, terminal_type, id_="", **kwargs):
        if terminal_type in ("3270", "5250"):
            print(kwargs)

            terminal = terminals[terminal_type](**kwargs)

        terminal_obj = {
            "id": id_ if id_ is not "" else self.actual_id,
            "terminal": terminal
        }
        self.actual_id = terminal_obj["id"]
        self.terminals.append(terminal_obj)
        return terminal

    def get_terminal(self, id_=None):
        if id_ is None:
            id_ = self.actual_id
        for terminal in self.terminals:
            if terminal["id"]== id_:
                return terminal["terminal"]
        

    def create_log(self, path):
        terminal = self.get_terminal()
        with open(path, "w") as log:
            log.write(terminal.getScreen())





