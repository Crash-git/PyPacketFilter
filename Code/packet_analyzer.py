from filter_packets import *
from packet_parser import *
from compute_metrics import *
# FUNCTIONS -----

# MAIN ------
Ltest = [['1711', '1479.891456', '192.168.200.2', '842', '0', 'seq=114/29184', 'ttl=128'], ['51', '55.444535', '192.168.100.2', '74', '8', 'seq=172/44032', 'ttl=126'], ['52', '55.444582', '192.168.200.1', '74', '0', 'seq=172/44032', 'ttl=128'], ['54', '56.460216', '192.168.100.2', '74', '8', 'seq=173/44288', 'ttl=126'], ['55', '56.460265', '192.168.200.1', '74', '0', 'seq=173/44288', 'ttl=128'], ['596', '646.422390', '192.168.100.1', '74', '8', 'seq=92/23552', 'ttl=126'], ['597', '646.422446', '192.168.200.1', '74', '0', 'seq=92/23552', 'ttl=128']] # test packet for computing metrics
L1 = list()
L2 = list()
L3 = list()
L4 = list()
filter("Node1", L1)
#filter("Node2", L2)
#filter("Node3", L3)
#filter("Node4", L4)
parse(L1)
node1 = parse(L1)[0]
node2 = parse(L1)[1]
node3 = parse(L1)[2]
node4 = parse(L1)[3]
compute("192.168.100.1", node1)
#compute("192.168.100.2,", node2)
#compute("192.168.200.1,", node3)
#compute("192.168.200.2,", node4)