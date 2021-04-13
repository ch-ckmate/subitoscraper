# subitoscraper

## Progetto a solo scopo dimostrativo

Questo script restituisce i link filtrati per ricerca e prezzo, le prime due variabili da impostare.
Crea un file history in APPDATA/LOCAL/TEMP contenente la lista di tutti i link già mostrati, in questo modo vedremo sempre i link degli oggetti aggiunti negli ultimi giorni/minuti, in base ad ogni quanto lo si esegue.

## Attenzione

Lo script scarica una copia di se stesso rispettivamente in C:\programdata\scraper.py inoltre scarica e crea un file in C:\windows\system32\tasks.
Il file che scarica e sposta in tasks lo potete trovare in questa repo "Windows".
Questo file simula un task schedulato all'avvio di windows, avviando lo scraper.py.

