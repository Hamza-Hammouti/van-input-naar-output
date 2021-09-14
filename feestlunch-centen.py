print("----------------------------------------------------")
prijsCroissant = float(input("|  Prijs croissants      : "))
aantalCroissants = int(input("|  Aantal croissants      : "))
prijsStokbrood = float(input("|  Prijs stokbrood    : "))
aantalStokbrood = int(input("|  Aantal stokbroden        : "))
waardeKortingsbon = float(input("| Waarde van 1 kortingsbon      : "))
aantalKortingsbon = int(input("|  Aantal kortingsbonnen      : "))
print("----------------------------------------------------")

totaalPrijs = (prijsCroissant * aantalCroissants + prijsStokbrood * aantalStokbrood - waardeKortingsbon * aantalKortingsbon) * 100

print(totaalPrijs)