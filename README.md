# Definitely not Donkey Kong

Das Projekt beinhaltet ein Platformer-Game, bei welchem eine animierte Spielfigur hüpfen kann, sowie nach links und nach rechts laufen.
Ziel des Spiels ist es, die verteilten Sammelobjekte (in unserem Beispiel Kaffeetassen) einzusammeln.

## Get started

Vor dem Start müssen einige Installs (unter requirements aufgeführt) durchgeführt werden.
Danach kann direkt das "main.py" ausgeführt werden.
Dadurch wird das Spiel auf einem Screen gestartet. 

Spielanleitung: Durch die Pfeiltasten (links und rechts) kann die Spielfigur bewegt werden.
Durch das Betätigen der Leertaste hüpft die Spielfigur. 
Mit diesen Tasten kann die Spielfigur zu den Kaffeetasen bewegt werden. Sobald die Spielfigur die Kaffeetassen berührt, werden diese eingesammelt.
Die Anzahl der eingesammelten Kaffeetassen ist oben rechts auf dem Screen zu sehen.
Das Spiel kann durch die Taste "Esc" oder durch das Schliessen des geöffneten Fenster abgebrochen werden.

Weiter wurde, aus Zeitgründen, auf einen Wechsel in ein neues Level verzichtet. Deshalb muss das Spiel selbst abgebrochen werden und wechselt nicht nach dem Einsammeln aller Objekte in das nächste Level.

## Understanding the sources

Es wurde eine objektorientierte Programmierung angewendet und Klassen, Objekte und Funktionen definiert. Dies ermöglicht einerseits eine bessere Übersicht des Codes sowie eine Trennung der Funktionalitäten und Klassen. Weiter ergibt sich dadurch eine gewisse Flexibilität für künftige Erweiterungen. So kann z.B. ein neues game_object relativ simpel ergänzt werden.

Als Framework wurde "pygame" verwendet. Dies bietet eine erleichterte Handhabung von Grafiken bzw. dem Laden von Bildern. Ebenfalls werden Mechanismen zur Kollisionserkennung angeboten, welche in unserem Fall auch angewendet wurden. Zudem bietet das Framework eine einfache Handhabung der Benutzereingabe, welche im Spiel von Bedeutung sind.

Da unser Softwareprojekt simpel gehalten wurde, ist auch die Architektur überschaubar. Es wurden pro Klasse eigene py-Dateien erstellt. Im main.py werden die Klassen abgerufen und die darin definierten Funktionen. Ergänzend zu den Dateien ist der Ordner "images" in welchem alle Grafiken abgelegt wurden sowie das MANUAL, README und requirments File, welche ergänzend zu dem Code geführt wurden.
