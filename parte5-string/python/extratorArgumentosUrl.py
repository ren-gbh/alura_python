class ExtratorArgumentosUrl:

    def __init__(self, url):
        if self.is_valid_url(url):
            self.url = url
        else:
            raise LookupError("Url Inválida!")

    @staticmethod
    def is_valid_url(url):
        if url:
            return True
        else:
            return False
