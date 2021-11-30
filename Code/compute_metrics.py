def compute(srcIp, L) : # Computing 13 different metrics per node
    reqRecNum = 0
    reqSentNum = 0
    reqRecByte = 0
    reqRecData = 0
    reqSentByte = 0
    reqSentData = 0

    recRecNum = 0
    recSentNum = 0
    recRecByte = 0
    recRecData = 0
    recSentByte = 0
    recSentData = 0

    for iter in L:
	    # Data size metrics
		# Number of echo requests sent
        if L[iter][4] = 8:
            if L[iter][1] = srcIp:
                reqNumSent += 1
                reqSentByte = reqSentByte + L[iter][3]
                reqSentData =
            if L[iter][2] = srcIp:
                reqRecNum += 1
                reqRecByte = reqRecByte + L[iter][3]
                reqRecData =
		# Total number of echo request bytes sent - based on the total size of the frame
		# Total echo request data sent - based on the payload size of the ICMP packet

		# Number of echo requests received
		# Total number of echo request bytes received - based on the total size of the frame
		# Total echo request data received  - based on the payload size of the ICMP packet

		# Number of echo replies sent
		# Number of echo replies received

	# Time based metrics
		# Average Round-Trip-Time, the time between sending an Echo-Req and receiving an Echo-Rep, measured in MS
		# Echo Request Throughput (in kB/s), the sum of the frame sizes of all the Echo-Reqs sent divided by the sum of RTTs
        # Echo Request Goodput (in kB/s) the sum of the ICMP payloads of all Echo-Reqs sent divided by the sum of the RTTs
        # Avg. reply delay (in microseconds so *1000), the time between a node receiving an Echo-Req and sending an Echo-Rep

	# Distance metrics
        # Avg. number of hops per Echo-Req (one hop per change of network, min. one hop)


