from filter_packets import *
from packet_parser import *
from compute_metrics import *
# FUNCTIONS -----

# MAIN ------
L = list()
M1 = list()
M2 = list()
M3 = list()
M4 = list()
filter(L)
parse()
compute("192.168.100.1", M1)
compute("192.168.200.2,", M2)
compute("192.168.300.3,", M3)
compute("192.168.400.4,", M4)
