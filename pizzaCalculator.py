# Naam: Hamza Hammouti
# Opdracht: Pizza Calculator

print("----------------------------------------------------")
aantalSmall = int(input("| Aantal pizza's small (25cm)    : "))
aantalMedium = int(input("| Aantal pizza's medium (30cm)   : "))
aantalLarge = int(input("| Aantal pizza's large (35cm)    : "))
print("----------------------------------------------------")

prijsSmall = 9.49
prijsMedium = 11.49
prijsLarge = 14.49

totaalprijs = (aantalSmall * prijsSmall) + (aantalMedium * prijsMedium) + (aantalLarge * prijsLarge)
print (f"Je hebt {aantalSmall} pizza small besteld, {aantalMedium} pizza medium en {aantalLarge} pizza large. Totaalprijs: €{totaalprijs}")