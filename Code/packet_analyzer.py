from filter_packets import *
from packet_parser import *
from compute_metrics import *
# FUNCTIONS -----

# MAIN ------
L1 = list()
L2 = list()
L3 = list()
L4 = list()
filter("Node1", L1)
filter("Node2", L2)
filter("Node3", L3)
filter("Node4", L4)
parse()
compute("192.168.100.1", L1)
compute("192.168.200.2,", L2)
compute("192.168.300.3,", L3)
compute("192.168.400.4,", L4)
