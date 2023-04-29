*** Pregunta 3
clear all
* c

use "peru.dta"

* parameters

local Ga atan({G=0})/_pi + 0.5
local Qa atan({Q=0})/_pi + 0.5
local Ka atan({K=0})/_pi + 0.5
local Ra atan({R=0})/_pi + 0.5

local PrC (`Ga')*(1 - (`Qa'))
local PcC (`Ka')*(`Ga')
local PrR 0.5*(1 + (`Ga'))*(1 - (`Qa'))
local PcR 0.5*(1 + (`Ka')*(`Ga'))

gen xav = x/7

local Es (`Ra')*(`PrC') + (1 - (`Ra'))*(`PcC')

local Ex (`Ra')*(`PrR') + (1 - (`Ra'))*(`PcR')

local m1 s - (`Es')
local m2 xav - (`Ex')

local Csx (xav-(`Ex'))*(s-(`Es'))

local m3 (`Csx') - (`Ra')*(1 - (`Ra'))*((`PrC') - (`PcC'))*((`PrR') - (`PcR'))

local Cxx (`Ra')*(1 - (`Ra'))*((`PrR') - (`PcR'))^2

local Vx xav^2 - (`Ex')^2

local m4 (`Vx') - ((`Ex')*(1-(`Ex')))/7 - 6*(`Cxx')/7

gmm (`m1')(`m2')(`m3')(`m4'), winitial(identity)

disp atan(/G)/_pi + 0.5
disp atan(/R)/_pi + 0.5
disp atan(/Q)/_pi + 0.5
disp atan(/K)/_pi + 0.5

* replacing m1 with seven moments conditions

local mr1 rr1 - (`Ex')
local mr2 rr2 - (`Ex')
local mr3 rr3 - (`Ex')
local mr5 rr5 - (`Ex')
local mr6 rr6 - (`Ex')
local mr8 rr8 - (`Ex')
local mr10 rr10 - (`Ex')

gmm (`m1')(`mr1')(`mr2')(`mr3')(`mr5')(`mr6')(`mr8')(`mr10')(`m3') /// 
(`m4'), winitial(identity)

disp atan(/G)/_pi + 0.5
disp atan(/R)/_pi + 0.5
disp atan(/Q)/_pi + 0.5
disp atan(/K)/_pi + 0.5

* d 

* estimating max liklehood

*local L (`Ra')*binomialp(s,1,(`Ga')*(1 - (`Qa')))*binomialp(x,7,.5*(1 + (`Ga'))*(1 - (`Qa'))) /// 
*+ (1 - (`Ra'))*binomialp(s,1,(`Ka')*(`Ga'))*binomialp(x,7,.5*(1 +(`Ka')*(`Ga')))

program define objective
	args lnf G R Q K
	tempvar Ga Ra Qa Ka
	quietly gen double `Ga' = atan(`G')/_pi + .5
	quietly gen double `Ra' = atan(`R')/_pi + .5
	quietly gen double `Qa' = atan(`Q')/_pi + .5
	quietly gen double `Ka' = atan(`K')/_pi + .5
	
	quietly replace `lnf' = (`Ra')*binomialp($ML_y1 , 1, (`Ga')*(1 - (`Qa')))*binomialp($ML_y2 ,7,.5*(1 + (`Ga'))*(1 - (`Qa'))) + (1 - (`Ra'))*binomialp($ML_y1 ,1,(`Ka')*(`Ga'))*binomialp($ML_y2 ,7,.5*(1 +(`Ka')*(`Ga')))
end

ml model lf objective (s x=) (s x=) (s x=) (s x=)
ml max
















