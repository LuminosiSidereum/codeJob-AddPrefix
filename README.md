# Dateinamen mit Präfix versehen oder ändern

## Funktionsweise
Dieses Skript ermöglicht das automatische Hinzufügen oder Ändern eines Präfixes für Dateien im aktuellen Verzeichnis. Es bietet zwei Betriebsmodi:
- **Modus 0:** Ein Präfix wird zu den Dateinamen hinzugefügt.
- **Modus 1:** Ein bestehendes Präfix wird durch ein neues ersetzt.

Python- (`.py`) und ausführbare Dateien (`.exe`) werden nicht umbenannt.

## Nutzung des Skripts

### Eingabedaten
- Dateien müssen sich im gleichen Verzeichnis befinden wie das Skript.
- Nicht umbenannt werden `.py`- und `.exe`-Dateien.
- Das Präfix darf keine der folgenden Zeichen enthalten: `/ \ : * ? < > | . ! ; #`.

### Ausführung
1. Das Skript starten.
2. Einen Modus auswählen:
   - `0` - Präfix zu den Dateinamen hinzufügen.
   - `1` - Bestehendes Präfix ändern.
3. Ein gültiges Präfix eingeben.
4. Das Skript benennt die Dateien automatisch um.

### Ausgabe
- Dateien erhalten das neue Präfix oder ein vorhandenes wird ersetzt.
- Konsolenausgabe mit den durchgeführten Änderungen.
