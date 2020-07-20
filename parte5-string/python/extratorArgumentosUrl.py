class ExtratorArgumentosUrl:

    def __init__(self, url):
        if self.is_valid_url(url):
            self.url = url.lower()
        else:
            raise LookupError("Url Inválida!")

    def __len__(self):
        return len(self.url)

    def __str__(self):
        moeda_origem, moeda_destino = self.extrai_argumentos()
        return "Valor: {}\nMoeda origem: {}\nMoeda destino: {}".format(
            self.extrai_valor(),
            moeda_origem,
            moeda_destino
        )

        '''
        return f"Valor: { self.extrai_valor() }\n" \
               f"Moeda origem: { moeda_origem }\n" \
               f"Moeda destino: { moeda_destino }"
        '''

    @staticmethod
    def is_valid_url(url):
        if url and url.startswith("https://bytebank.com"):
            return True
        else:
            return False

    def extrai_argumentos(self):
        busca_moeda_origem = "moedaorigem="
        busca_moeda_destino = "moedadestino="

        indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
        indice_final_moeda_origem = self.url.find("&")
        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        if moeda_origem == "moedadestino":
            self.troca_moeda_origem()
            indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
            indice_final_moeda_origem = self.url.find("&")
            moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        indice_inicial_moeda_destino = self.encontra_indice_inicial(busca_moeda_destino)
        indice_final_moeda_origem = self.url.find("&valor")
        moeda_destino = self.url[indice_inicial_moeda_destino:indice_final_moeda_origem]

        return moeda_origem, moeda_destino

    def extrai_valor(self):
        busca_valor = "valor="
        indice_inicial_valor = self.encontra_indice_inicial(busca_valor)

        return self.url[indice_inicial_valor:]

    def encontra_indice_inicial(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada)

    def troca_moeda_origem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)
