from logger import logger


class PyRanj:
    def __init__(self, function=None):
        self.function = function

    def __enter__(self):
        try:
            self.function()
        except Exception as e:
            logger.log("[EXCEPTION] :: {}".format(e))

    def __exit__(self, *ext):
        pass

    def __call__(self):
        try:
            self.function()
        except Exception as e:
            logger.log("[EXCEPTION] :: {}".format(e))


with PyRanj:
    raise Exception("error")
