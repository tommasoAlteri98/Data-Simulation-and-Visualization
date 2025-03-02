class Cioccolato:
    cioccolato_disponibile = 100 
    
    def __init__(self, tipo, percentuale_cacao):
        self.tipo = tipo
        self.percentuale_cacao = percentuale_cacao
    
    def produce(self):
        print("Produzione di cioccolato: " + self.tipo + ", con " + str(self.percentuale_cacao) + " percentuale di cacao.")

class Cioccolatino(Cioccolato):
    def __init__(self, tipo, percentuale_cacao, forma, ripieno):
        super().__init__(tipo, percentuale_cacao)
        self.forma = forma
        self.ripieno = ripieno
    
    def produce(self):
        if Cioccolato.cioccolato_disponibile >= 2:
            Cioccolato.cioccolato_disponibile -= 2
            print("Produzione di un cioccolatino " + self.forma + " con ripieno di " + self.ripieno + ", usando 2 unità di cioccolato.")
        else:
            print("Cioccolato esaurito per oggi.")

class Tavoletta(Cioccolato):
    def __init__(self, tipo, percentuale_cacao, peso, aggiunta):
        super().__init__(tipo, percentuale_cacao)
        self.peso = peso
        self.aggiunta = aggiunta
    
    def produce(self):
        if Cioccolato.cioccolato_disponibile >= self.peso:
            Cioccolato.cioccolato_disponibile -= self.peso
            print("Produzione di una tavoletta da " + str(self.peso) + "g con aggiunta di " + self.aggiunta + ", usando " + str(self.peso) + " unità di cioccolato.")
        else:
            print("Cioccolato esaurito per oggi.")

class CioccolataCalda(Cioccolato):
    def __init__(self, tipo, percentuale_cacao, temperatura, densità):
        super().__init__(tipo, percentuale_cacao)
        self.temperatura = temperatura
        self.densità = densità
    
    def produce(self):
        if Cioccolato.cioccolato_disponibile >= 20:
            Cioccolato.cioccolato_disponibile -= 20
            print("Produzione di cioccolata calda a " + str(self.temperatura) + " °C con densità " + str(self.densità) + ", usando 20 unità di cioccolato.")
        else:
            print("Cioccolato esaurito per oggi.")

class FabbricaDiCioccolato:
    MAX_CIOCCOLATO_GIORNALIERO = 100
    
    def __init__(self):
        self.cioccolato_disponibile = self.MAX_CIOCCOLATO_GIORNALIERO
    
    def produce(self, prodotto, costo):
        if self.cioccolato_disponibile >= costo:
            self.cioccolato_disponibile -= costo
            prodotto.produce()
            print(f"Cioccolato rimanente: {self.cioccolato_disponibile}")
        else:
            print("Cioccolato esaurito per oggi.")
    
    def reset_giornata(self):
        self.cioccolato_disponibile = self.MAX_CIOCCOLATO_GIORNALIERO