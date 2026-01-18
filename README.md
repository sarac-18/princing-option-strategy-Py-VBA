# princing-option-strategy-py

**INTRODUZIONE**

- linguaggi di programmazione usati: Python e VBA.
  
Questo progetto ha l'obiettivo di prezzare una stategia di opzioni, detta _“Bull Put Spread”_. In questa caso, la tipologia di opzioni che formano la strategia sono _asiatiche_. 
Il payoff di un'opzione asiatica è il seguente:
- CALL= MAX(S(T)- K, 0)
- PUT= MAX (K- S(T),0)

Dove K è la media dei valori che il sottostante durante la durata del derivato, mentre S(T) è il valore del sottostante al momento dell'esercizio del diritto costituito dall'acquisto del prodotto.

Il metodo utilizzato per la determinazione del pricing è il metodo Montecarlo con N simulazione e S scenari diversi. La costruzione della strategia _“Bull Put Spread”_ è la seguente:
- Comprare una Put OTM -> PUT= MAX (K- S(T),0)
- Vendere una Put ITM -> PUT= MIN (K- S(T),0)

La strategia viene composta sommando, strike per strike, i valori delle opzioni.

**DATI DI INPUT**
- Data operazione: 20-12-2021
- Prezzo sottostante: 4.568.02 pt
- Data scadenza opzione: 21-12-2018
- Tasso interesse privo di rischio: 0,19%
- Volatilità Implicita: 24% (lasciare costante per il momento)
- Valore di un punto (future): 50$
- I prezzi del sottostante su cui creare il Risk-Graph sono intervallati ogni 10 punti. I limiti inferiore e superiore vanno calcolati al 20% del prezzo attuale.

**RISULTATO**

Il progetto avrà come risultato finale:
- il prezzo a scadenza della strategia
- il grafico che mostra il payoff della strategia a scadenza

NB: il progetto può essere facilmente adattato per il calcolo di ogni tipo di strategia di opzioni 


 

