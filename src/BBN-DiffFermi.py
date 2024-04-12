import time 
import numpy as np
from scipy.integrate import quad
from scipy.special import kv
import PRyM.PRyM_init as PRyMini
import PRyM.PRyM_main as PRyMm
import importlib.util

# the code adds the scientific notation

user_input_str = input("Please enter your value for GF:\nGF = 1.1663787*10**-5*1.e-6 (Fermi coupling constant in [MeV-2])")
user_input = float(user_input_str)

PRyMini.GF = user_input*10**-5*1.e-6
PRyMini.aTid_flag = True
PRyMini.compute_bckg_flag = True
PRyMini.compute_nTOp_flag = True
PRyMini.compute_nTOp_thermal_flag = False
PRyMini.save_bckg_flag = False
PRyMini.save_nTOp_flag = False
PRyMini.save_nTOp_thermal_flag = False
PRyMini.verbose_flag = False

#start the simulation :0
print("#################       running       ###################")
PRyMini.smallnet_flag = False
PRyMini.julia_flag = False
stime = time.time()
res = PRyMm.PRyMclass().PRyMresults()
TVal = res[5] #the calculated value
EVal = 2.527 # the experimental value (Cooke, et al. 2018)
print ("D/H x 10^5:",res[5])
print("run time: ", time.time() - stime)
print("percent change", abs(((EVal - TVal)/TVal)*100))
print("#################        done         ###################")
