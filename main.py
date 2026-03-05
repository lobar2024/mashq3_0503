from dataclasses import dataclass

@dataclass
class Avto:
    marka: str
    model: str
    yil: int
    tezlik: int

    def tezlik_oshir(self):
        self.tezlik += 10

    def tezlik_kamaytirish(self):
            self.tezlik -= 10
