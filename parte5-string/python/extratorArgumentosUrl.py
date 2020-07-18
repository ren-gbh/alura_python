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

    def extrai_argumentos(self):
        indice_inicial_moeda_origem = self.url.find("=") + 1
        indice_final_moeda_origem = self.url.find("&")

        indice_inicial_moeda_destino = self.url.find("=", 15) + 1

        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]
        moeda_destino = self.url[indice_inicial_moeda_destino:]

        return moeda_origem, moeda_destino
