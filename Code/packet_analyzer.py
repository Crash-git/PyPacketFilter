#Claire Lavergne, Victor Hermes, Deajah Barbour, Rowan Keller
from filter_packets import *
from packet_parser import *
from compute_metrics import *
# FUNCTIONS -----

# MAIN ------
L1 = list()
L2 = list()
L3 = list()
L4 = list()
filter("Node1")
filter("Node2")
filter("Node3")
filter("Node4")

L1 = parse("1")
L2 = parse("2")
L3 = parse("3")
L4 = parse("4")


#output attempt to call compute metrics
compute("192.168.100.1", L1, "Node 1")
compute("192.168.100.2", L2,"Node 2")
compute("192.168.200.1", L3,"Node 3")
compute("192.168.200.2", L4,"Node 4")


