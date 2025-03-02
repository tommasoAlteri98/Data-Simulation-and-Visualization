class Cioccolato:
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
            unità = 2
            
    def produce(self, fabbrica):
        if fabbrica.cioccolato_disponibile >= 2:
            fabbrica.cioccolato_disponibile -= 2
            super().produce()  
            print(f"Forma: {self.forma}, Ripieno: {self.ripieno}")
        else:
            print("Cioccolato esaurito per oggi.")
        fabbrica.mostra_cioccolato_rimanente()

class Tavoletta(Cioccolato):
    def __init__(self, tipo, percentuale_cacao, peso, quantità, aggiunta):
        super().__init__(tipo, percentuale_cacao)
        self.peso = peso
        self.quantità = quantità
        if quantità < 4:
            self.quantità = 4
        elif quantità <= 24:
            self.quantità = quantità
        else:
            quantità = 24
        self.aggiunta = aggiunta
        
    def produce(self, fabbrica):
        super().produce()
        print(f" il peso è: {self.peso}")
        print(f" aggiunte: {self.aggiunta}")
        print(f" ha utilizzato queste unita' di cioccolato: {self.quantità}")
        fabbrica.cioccolato_disponibile -= self.quantità
        fabbrica.mostra_cioccolato_rimanente()
        
class CioccolataCalda(Cioccolato):
    def __init__(self, tipo, percentuale, temperatura, densità, quantità):
        super().__init__(tipo, percentuale)
        self.temperatura = temperatura
        self.densità = densità
        if quantità >= 20:
            self.quantità = quantità
        else: 
            self.quantità = 20
        
    def produce(self):
        print(" Il tipo di cioccolato è: " + self.tipo + " ed usa " + str(self.quantità) + " unità")
        if fabbrica.cioccolato_disponibile >= 20:
            fabbrica.cioccolato_disponibile -= self.quantità
            print("Produzione di cioccolata calda a " + str(self.temperatura) + " °C con densità " + str(self.densità) + ", usando " + str(self.quantità) + " unità di cioccolato.")
        else:
            print("Cioccolato esaurito per oggi.")
        fabbrica.mostra_cioccolato_rimanente()

class FabbricaDiCioccolato:
    quantitaGiornalieraCioccolato = 100
    
    def __init__(self):
        self.cioccolato_disponibile = self.quantitaGiornalieraCioccolato
    
    def reset_giornata(self):
        self.cioccolato_disponibile = self.quantitaGiornalieraCioccolato
        print("Reset della giornata: il cioccolato disponibile è stato ripristinato.")
    
    def mostra_cioccolato_rimanente(self):
        print("Cioccolato rimanente: " + str(self.cioccolato_disponibile) + " unità.")



fabbrica = FabbricaDiCioccolato()
cioccolatino = Cioccolatino("Fondente", 70, "rotondo", "nocciola")
tavoletta = Tavoletta("Latte", 50, 10, 10, "mandorle")
cioccolata_calda = CioccolataCalda("Bianco", 30, 75, "densa", 30)

cioccolatino.produce(fabbrica)
tavoletta.produce(fabbrica)
cioccolata_calda.produce()