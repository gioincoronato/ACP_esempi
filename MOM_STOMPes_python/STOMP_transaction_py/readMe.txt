Le transazioni garantiscono atomicità ovvero che un gruppo di messaggi 
venga inviato tutto insieme o non venga inviato per nulla, 
per una questione di sicurezza.

COMANDI STOMP:
- conn.begin() -> inzia la transazione e restituisce un ID univoco (txid)

- transaction = txid ->  par che va aggiunto ad ogni send inclusa nel pacchetto
                         il broker conserva questi messaggi in un limbo

- conn.commit(txid) ->  sblocca tutto permettendo al broker di conseganre il pacchetto
- conn.abort(txid)  ->  annulla tutta la transazione