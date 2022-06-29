# Nutzwertanalyse Backend-Technologie
Diese Nutzwertanalyse soll die Entscheidung hinter der Technologieauswahl nachvollziehbar machen. 

Es gibt zahlreiche Möglichkeiten, ein API im Backend zu realisieren. 

In unserem Fall kamen nur Programmiersprachen in Frage, die auf Python basieren, um auf Vorwissen aus der Unter- und Mittelstufe aufzubauen. 

Ausschlaggebendes Kriterium war schließlich die Menge der Lernanlässe (je mehr wir manuell machen müssen, desto besser; also möglichst wenig out-of-the-box Funktionen) und eine minimalistische Syntax (je weniger erklärt werden muss, desto besser; also möglichst wenig Konzepte wie z.B. async als Schlüsselwort).

Die nachfolgende Tabelle schlüsselt die Elemente der Entscheidung auf.


<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-2b7s{text-align:right;vertical-align:bottom}
.tg .tg-fvtb{background-color:#C6EFCE;color:#006100;font-weight:bold;text-align:right;vertical-align:bottom}
.tg .tg-8d8j{text-align:center;vertical-align:bottom}
.tg .tg-7zrl{text-align:left;vertical-align:bottom}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-8d8j" colspan="4">Kriterien</th>
    <th class="tg-8d8j" colspan="3">Django</th>
    <th class="tg-8d8j" colspan="3">Flask</th>
    <th class="tg-8d8j" colspan="3">FastAPI</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-7zrl">Kriterium</td>
    <td class="tg-7zrl">Erläuterung</td>
    <td class="tg-7zrl">Skala</td>
    <td class="tg-7zrl">Gewichtung</td>
    <td class="tg-8d8j">Bewertung</td>
    <td class="tg-8d8j">Anmerkung</td>
    <td class="tg-8d8j">Punkte</td>
    <td class="tg-8d8j">Bewertung</td>
    <td class="tg-8d8j">Anmerkung</td>
    <td class="tg-8d8j">Punkte</td>
    <td class="tg-8d8j">Bewertung</td>
    <td class="tg-8d8j">Anmerkung</td>
    <td class="tg-8d8j">Punkte</td>
  </tr>
  <tr>
    <td class="tg-7zrl">Dokumentation</td>
    <td class="tg-7zrl">Der Grad der verfügbaren   Dokumentation und wie gut man darin navigieren kann.</td>
    <td class="tg-7zrl">0 - nicht oder nicht vollständig   vorhanden<br>1 - vorhanden<br>2 - umfangreiche Dokumentation, HowTos etc.</td>
    <td class="tg-7zrl">20</td>
    <td class="tg-7zrl">2</td>
    <td class="tg-7zrl"> </td>
    <td class="tg-7zrl">40</td>
    <td class="tg-7zrl">2</td>
    <td class="tg-7zrl"> </td>
    <td class="tg-7zrl">40</td>
    <td class="tg-7zrl">1</td>
    <td class="tg-7zrl"> </td>
    <td class="tg-7zrl">20</td>
  </tr>
  <tr>
    <td class="tg-7zrl">Etabliert</td>
    <td class="tg-7zrl">Je länger ein&nbsp;&nbsp;&nbsp;Produkt (zum Zeitpunkt dieser Entscheidung) am Markt vorhanden ist, desto&nbsp;&nbsp;&nbsp;zuverlässiger und desto mehr gelöste Probleme (z.B. bei StackOverflow)</td>
    <td class="tg-7zrl">0 - nicht   verfügbar<br>1 - relativ neu<br>2 - etabliert</td>
    <td class="tg-7zrl">10</td>
    <td class="tg-7zrl">2</td>
    <td class="tg-7zrl"> </td>
    <td class="tg-7zrl">20</td>
    <td class="tg-7zrl">2</td>
    <td class="tg-7zrl"> </td>
    <td class="tg-7zrl">20</td>
    <td class="tg-7zrl">1</td>
    <td class="tg-7zrl">Neu, aber für&nbsp;&nbsp;&nbsp;hoch-skallierende Projekte anscheinend sehr beliebt.</td>
    <td class="tg-7zrl">10</td>
  </tr>
  <tr>
    <td class="tg-7zrl">OpenSource</td>
    <td class="tg-7zrl">Für den&nbsp;&nbsp;&nbsp;Lehreinsatz sollten keine Hürden für den Einsatz bestehen.</td>
    <td class="tg-7zrl">0 -   propietär<br>1 - OpenSource, keine Entwicklung<br>2 - OpenSource, aktive Entwicklung</td>
    <td class="tg-7zrl">20</td>
    <td class="tg-7zrl">2</td>
    <td class="tg-7zrl"> </td>
    <td class="tg-7zrl">40</td>
    <td class="tg-7zrl">2</td>
    <td class="tg-7zrl"> </td>
    <td class="tg-7zrl">40</td>
    <td class="tg-7zrl">2</td>
    <td class="tg-7zrl"> </td>
    <td class="tg-7zrl">40</td>
  </tr>
  <tr>
    <td class="tg-7zrl">Lernwirksam</td>
    <td class="tg-7zrl">Für den&nbsp;&nbsp;&nbsp;Lehreinsatz sind minimalistische Mittel vorteilhaft: Je weniger automatisch&nbsp;&nbsp;&nbsp;passiert, desto mehr Lernanlässe gibt es.</td>
    <td class="tg-7zrl">0 - Viel Lösung   ohne tatsächliche Entwicklung<br>1 - Es muss viel entwickelt werden, aber die Syntax ist kompliziert<br>2 - Es muss viel entwickelt werden, die Syntax ist minimalistisch</td>
    <td class="tg-7zrl">50</td>
    <td class="tg-7zrl">0</td>
    <td class="tg-7zrl">Front- und&nbsp;&nbsp;&nbsp;BackEnd Lösung; Nimmt viel Arbeit ab.</td>
    <td class="tg-7zrl">0</td>
    <td class="tg-7zrl">2</td>
    <td class="tg-7zrl"> </td>
    <td class="tg-7zrl">100</td>
    <td class="tg-7zrl">1</td>
    <td class="tg-7zrl">async in&nbsp;&nbsp;&nbsp;Minimalbeispiel.</td>
    <td class="tg-7zrl">50</td>
  </tr>
  <tr>
    <td class="tg-2b7s" colspan="3">Summen</td>
    <td class="tg-7zrl">100</td>
    <td class="tg-2b7s" colspan="3">100</td>
    <td class="tg-fvtb" colspan="3">200</td>
    <td class="tg-2b7s" colspan="3">120</td>
  </tr>
</tbody>
</table>


## Hintergrund
Der Sinn einer Nutzwertanalyse ist, mehrere Alternativen miteinander zu vergleichen, die nicht (nur) durch harte Kriterien verglichen werden können. Harte Kriterien sind in diesem Fall meist monetäre Aspekte, also ein Geld- oder Zeitaufwand (der letztlich in Geld umgerechnet werden kann). Die Nutzwertanalyse ist quasi eine Betrachtung des geringsten Bedauerns.

Die Nutzwertanalse kann immer dann eingesetz werden, wenn eine Entscheidung nicht nur auf Basis eines einzelnen Kriteriums gefällt wird bzw. wenn man mehrere Ziele gleichzeitig verfolgt. Wenn es z.B. nicht nur um die Frage, welcher Lieferant am günstigsten ist, sondern gleichzeitig auch um die Qualität des Produkts und die Nachhaltigkeit der Herrstellung geht. 

Solche Analysen können auch eingesetzt werden, um den nicht-monetären (in Geld gemessenen) Nutzen ihres Projekts zu bewerten. Hier kann auch dargestellt werden, inwiefern Ihr Produkt für den Kunden geeigneter ist, als vielleicht bereits bestehende ähnliche Produkte auf dem Markt.

Tolle Hinweise zum Sinn und Unsinn einer Nutzwertanalyse in IT-Projekten: https://it-berufe-podcast.de/nutzwertanalyse-in-der-projektdokumentation/ 


## Vorgehensweise: Nutzwertanalyse erstellen
1.	Auswahl der Kriterien, die für die Entscheidung wichtig sind.
2.	Gewichtung der Kriterien (Spalte „Gewicht“)

    - Das Gewicht kann z.B. in ganzen Zahlen oder Prozenten angegeben werden.
    - Die Summe der Gewichte sollte 10, 100 bzw. 100% ergeben.

3.	Alternativen auflisten (beliebig viele Spalten nach rechts einfügen).

4.	Bewertung der Stärke der Kriterien bei den Alternativen

    Die Skala der Bewertung kann beliebig ausgewählt werden. 
    
    Je schlechter ein Kriterium erfüllt wird, desto geringer muss die Zahl der Bewertung sein (je mehr, desto besser!). Man kann z.B. Werte von 0 (kein Nutzen) bis 4 (sehr hoher) wählen. 
    
    Man kann auch Ziffern von 0 – 10 wählen und zwischen den Kriterien gleich verteilen (Beispiel: Höchster Preis 2.500€ = 0, niedrigster Preis 2.000€ = 10. 2.400€ wäre dann 2, 2.300€ wäre dann 4 etc.).

    In Projektdokumentationen sollten die Bewertungskriterien genau beschrieben werden.

5.	Ergebnisse je Alternative berechnen

    Für jede Alternative und jedes Kriterium wird das Gewicht des Kriteriums mit der Bewertung der Alternative multipliziert.

6.	Beste Alternative auswählen.

    Die Alternative mit der höchsten Punktzahl bietet den höchsten Nutzen und sollte ausgewählt werden.
