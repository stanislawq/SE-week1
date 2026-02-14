"""
Varasto module.
"""

class Varasto:
    """
    Varasto class for managing inventory.
    """
    def __init__(self, tilavuus, alku_saldo=0):
        """
        Initialize the inventory.
        """
        self.tilavuus = tilavuus if tilavuus > 0.0 else 0.0

        if alku_saldo < 0.0:
            self.saldo = 0.0
        elif alku_saldo <= self.tilavuus:
            self.saldo = alku_saldo
        else:
            self.saldo = self.tilavuus

    def paljonko_mahtuu(self):
        """
        Return available space.
        """
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """
        Add item to inventory.
        """
        if maara < 0:
            return

        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """
        Take item from inventory.
        """
        if maara < 0:
            return 0.0

        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        """
        Return string representation.
        """
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
