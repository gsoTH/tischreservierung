# Tischreservierung
Ein Beispiel für die Entwicklung einer API mit Flask.

## Wie man mit diesem Repository arbeitet
Dieses Repository enthält Branches, die unterschiedliche Versionen des gleichen Beispiels enthalten. Einige Beispiele: 
- Der [main-branch](https://github.com/gsoTH/tischreservierung/tree/main) enthält das Lastenheft und Anforderungen des Kunden
- Der [nurSQL-branch](https://github.com/gsoTH/tischreservierung/tree/nurSQL) entält eine Implementierung ohne den Einsatz von Objekt-Rationalen-Mappern, also pures SQL - eine Variante die **nur** für Lehrzwecke geeignet ist.

# Anforderungen

## Auszug aus dem Lastenheft
Ein Restaurant möchte ein Buchungssystem für die Reservierung von Tischen einführen. Das Restaurant hat eine Filiale mit weniger als 20 Tischen. 

### Beschreibung des Ist-Zustands
Derzeit werden Reservierungen via Telefon geregelt. Kunden rufen an und geben einen gewünschten Zeitpunkt und ggf. eine Personenzahl an. Der Kellner überprüft, welche Tische für den jeweiligen Zeitpunkt in Frage kommen. Falls genügend Tische zur Verfügung stehen, wird die Reservierung mit den betroffenen Tischnummern und einem Namen, ggf. mit einer Telefnonummer in einen großen Terminplan eingetragen. 

Es hat sich als praktikabel gezeigt, dass eine Reservierung nur zur halben Stunde (z.B. 16:30 Uhr, 17:30 Uhr) angeboten werden und jeweils für eine Stunde gelten.

In einigen Fällen kommt es vor, dass Reservierungen telefonisch wieder storniert werden. 

### Beschreibung des Soll-Konzepts
Die Reservierung soll zukünftig nur noch über ein Buchungssystem erfolgen. Die Kunden sollen über unsere Webseite die freien Tische zu einem gewünschten Termin anzeigen können. Anschließend sollen sie die Tische reservieren und die Reservierung ggf. stornieren können. 

Vor Ort benötigen die Kellner nur Einblick über alle Reservierungen des aktuellen Tages, um Gäste zu ihren Tischen zu leiten.

Personenbezogene Daten sollen vorerst nicht erhoben werden.

Das System soll zukünftig erweiterbar sein, um z.B. mehrere Filialen einbinden zu können.

## Fachkonzept
Ausgehend von der Situationsbeschreibung wurde die Situation vertieft analysiert. Ergebnis waren mehrere UML-Diagramme.

### Anwendungsfalldiagramm
Das nachfolgende UML-Use-Case Diagramm zeigt die Anwendungsfälle, die das neue System zur Verfügung stellen soll.

![UML-UseCase Diagramm](diagramme/UML-UseCase.drawio.svg)

### Sequenzdiagramm
Daraus wurde dieses UML-Sequence Diagramm entwickelt, das die Abläufe der UseCases genauer darstellt. 

![UML-Sequence Diagramm](diagramme/UML-Sequence.drawio.svg)

**Nachrichtenbezeichnungen anpassen, damit ein Mapping zum Objektdiagramm möglich ist?**

### Objektdiagramme
Aus dem Sequenzdiagramm lassen sich einzelne Nachrichten ableiten.Beispiele für die Inhalte der gesendeten Informationsobjekte stelle ich als UML-Object Diagramm dar. 

#### Freie Tische anfragen
![UML-Object 1: Freie Tische anfragen](diagramme/UML-Object_1_FreieTischeAnfragen.drawio.svg)

#### Tisch reservieren
![UML-Object 2: Tisch reservieren](diagramme/UML-Object_2_TischReservieren.drawio.svg)

#### Reservierung stornieren
![UML-Object 3: Reservierung stornieren](diagramme/UML-Object_3_ReservierungStornieren.drawio.svg)

