-- Dieses Skript erzeugt eine SQLite Testdatenbank.

DROP TABLE IF EXISTS reservierungen;
DROP TABLE IF EXISTS tische;

CREATE TABLE tische(
    tischnummer              INTEGER NOT NULL UNIQUE
,   anzahlPlaetze   INTEGER 
,   PRIMARY KEY (tischnummer)
);

CREATE TABLE reservierungen(
    reservierungsnummer          INTEGER NOT NULL UNIQUE
,   zeitpunkt   TEXT
,   tischnummer     INTEGER
,   pin         INTEGER
,   storniert   BOOLEAN NOT NULL CHECK (storniert IN ('True', 'False'))
-- SQLite unterstützt keine Boolschen Werte. 
-- Dieser Workaround lässt nur zwei Einträge zu
,   PRIMARY KEY (reservierungsnummer)
,   FOREIGN KEY (tischnummer) REFERENCES tische(tischnummer)
);

INSERT INTO tische (tischnummer, anzahlPlaetze) VALUES
    (1, 4)
,   (2, 6)
,   (3, 6)
,   (4, 5)
;

INSERT INTO reservierungen (reservierungsnummer, zeitpunkt, tischnummer, pin, storniert) VALUES
    (1, '2022-02-02 17:30:00', 1, 1331, 'False') -- PIN wurde garantiert zufällig erzeugt...
,   (2, '2022-02-02 18:30:00', 1, 1332, 'False')
,   (3, '2022-02-02 19:30:00', 1, 1333, 'False')
,   (4, '2022-02-02 18:30:00', 3, 1334, 'False')
,   (5, '2022-02-02 19:30:00', 3, 1335, 'False')
,   (6, '2022-02-02 20:30:00', 3, 1336, 'False')
;