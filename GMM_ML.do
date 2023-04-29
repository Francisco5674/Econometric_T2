*** Practice GMM and ML

*** GMM
clear all

set seed 3442

set obs 10000

gen y = rnormal() 

local m1 {mu=1}-y
local m2 1 - ({mu=1}-y)^2

gmm (`m1')(`m2'), winitial(identity) 


*** ML
program define obj
	version 1.0
	args lnf mu
	quietly replace `lnf'=ln(normd(($ML_y1 -`mu')/1))
end

ml model lf obj (y=)

ml max



