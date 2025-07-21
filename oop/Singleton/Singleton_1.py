from datetime import datetime


class Logger:
    _logs = []
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        print(self.__class__)

    def log(self, msg: str):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__class__._logs.append(f"[{date}]| {msg}")

    def get_logs(self):
        return self.__class__._logs

    def show(self):
        print("\n".join(self.__class__._logs))


log1 = Logger()

log2 = Logger()

log2.log("Error")
log1.log("Error2")

log2.show()
