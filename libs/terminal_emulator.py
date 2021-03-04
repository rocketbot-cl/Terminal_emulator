from p5250 import P5250Client
from p3270.p3270 import P3270Client

terminals = {
    "3270": P3270Client,
    "5250": P5250Client,
}


class TerminalEmulator:

    def __init__(self):
        self.terminals = []
        self.actual_id = "default"

    def new_terminal(self, terminal_type, id_="", **kwargs):
        if terminal_type in ("3270", "5250"):
            path = "../bin/3270"

            terminal = terminals[terminal_type](path=path, **kwargs)

        terminal = {
            "id": id_ if id_ is not "" else self.id,
            "terminal": terminal
        }
        self.actual_id = terminal["id"]
        self.terminals.append(terminal)

    def get_terminal(self, id_="default"):
        terminal = filter(lambda x: x["id"] == id_, self.terminals)
        self.actual_id = id_
        return list(terminal)[0]["terminal"]

    def create_log(self, path):
        terminal = self.get_terminal()
        with open(path + "log.txt", "r") as log:
            log.write(terminal.getScreen())





