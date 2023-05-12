*** Duration model
clear all
* data
use "caso.dta"

gen female = 1 
replace female = 0 if sex==1

gen capacit = 1
replace capacit = 0 if treatment == "FALSE"
replace capacit = 0 if treatment == "NA"

gen cen_dummy = 1
replace cen_dummy = 0 if censored == "FALSE"

gen dummy_quit = 0
replace dummy_quit = 1 if quit== "TRUE"

gen educ2 = educ^2

* a

reg productivity female test_skill educ educ2 capacit dummy_quit

* b
* En principio puedo estimar por probit o logit

probit dummy_quit productivity female test_skill educ educ2
predict prob_quit

logit dummy_quit productivity female test_skill educ educ2
predict logit_quit

* c

twoway scatter logit_quit educ || fpfit logit_quit educ

* d

xtile test_tertile = test_skill,n(3)

gen educ_lvl = "superior" 
replace educ_lvl = "media" if educ == 12
replace educ_lvl = "incompleta" if educ<12

stset job_tenure, failure(cen_dummy==1)

sts graph, by(female)

sts graph, by(educ_lvl)

sts graph, by(test_tertile)

* f

stcox female productivity educ educ2 test_skill

* g

streg female productivity educ educ2 test_skill, distribution(weibull) 








