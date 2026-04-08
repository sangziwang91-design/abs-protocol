class BaseTask:
    def prompt(self):
        raise NotImplementedError

    def verify(self, outputs):
        return None
