** Selection models
clear all

use "data_p1.dta"

* b
heckprobit parcial edad edad2 escolaridad casada n0_5 n6_17 d2_5 d6_9 d10_49 d50_199 d200 dminas dmanu dega dconstru dcomercio dtransporte dservfin dservicios log_salario nlingreso if mujer == 1, select(parti = edad edad2 escolaridad casada n0_5 n6_17 n18 nlingreso)

* c

heckman horas edad edad2 escolaridad casada n0_5 n6_17 d2_5 d6_9 d10_49 d50_199 d200 dminas dmanu dega dconstru dcomercio dtransporte dservfin dservicios log_salario nlingreso if mujer == 1, select(parti = edad edad2 escolaridad casada n0_5 n6_17 n18 nlingreso) twostep

* d

heckman horas edad edad2 escolaridad casada n0_5 n6_17 d2_5 d6_9 d10_49 d50_199 d200 dminas dmanu dega dconstru dcomercio dtransporte dservfin dservicios log_salario nlingreso if mujer == 1, select(parti = edad edad2 escolaridad casada n0_5 n6_17 n18 nlingreso)

