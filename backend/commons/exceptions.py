class WebException(Exception):
    def __init__(self, msg:str=None, code:str=None) -> None:
        self.msg = msg
        self.code = code

    def dict(self):
        return {
            'msg': self.msg,
            'code': self.code
        }