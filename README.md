# Tischreservierung
Ein Beispiel für die Entwicklung einer API mit Flask.

## Situationsbeschreibung
Ein Restaurant möchte ein Buchungssystem für die Reservierung von Tischen einführen. Im besten Fall müssen die Kellner nur noch überprüfen, welche Reservierungen vorliegen. 

## Analyse
Die Situation wird in mehreren Diagrammen genauer analysiert. 

### Anwendungsfalldiagramm
Das nachfolgende UML-Use-Case Diagramm zeigt die Anwendungsfälle, die entwickelt werden sollen.

![UML-UseCase Diagramm](diagramme/UML-UseCase.drawio.svg)

### Sequenzdiagramm
Daraus wurde dieses UML-Sequence Diagramm entwickelt, das die Abläufe der UseCases genauer darstellt. Hieraus lassen sich einzelne Nachrichten ableiten.

![UML-Sequence Diagramm](diagramme/UML-Sequence.drawio.svg)


### Objektdiagramme
Beispiele für die Inhalte der gesendeten Informationsobjekte stelle ich als UML-Object Diagramm dar. 

#### Freie Tische anfragen
![UML-Object 1: Freie Tische anfragen](diagramme/UML-Object_1_FreieTischeAnfragen.drawio.svg)

#### Tisch reservieren
![UML-Object 2: Tisch reservieren](diagramme/UML-Object_2_TischReservieren.drawio.svg)

#### Reservierung stornieren
![UML-Object 3: Reservierung stornieren](diagramme/UML-Object_3_ReservierungStornieren.drawio.svg)