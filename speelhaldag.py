print("----------------------------------------------------")
prijsTickets = float(input("|  Toegangsticket kosten      : "))
aantalTickets = int(input("|  Aantal personen        : "))
kostenGameseat = float(input("|  Gameseat kosten per minuut     : "))
aantalMinuten = int(input("|  Totaal aantal minuten       : "))
aantalGameseat = int(input("|  Totaal aantal Gameseat personen     : "))
print("----------------------------------------------------")

totaalprijs = (prijsTickets * aantalTickets) + ((kostenGameseat * aantalMinuten) * aantalGameseat)

print(totaalprijs)