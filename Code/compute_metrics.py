def compute(srcIp, L) : # Computing 13 different metrics per node
    reqRecNum = 0
    reqSentNum = 0
    reqRecByte = 0
    reqRecData = 0
    reqSentByte = 0
    reqSentData = 0

    repRecNum = 0
    repSentNum = 0
    repRecByte = 0
    repRecData = 0
    repSentByte = 0
    repSentData = 0

    for iter in L:
	    # Data size metrics
        if L[iter][4] = 8: # tracking metrics for echo requests
            if L[iter][1] = srcIp:
                reqNumSent += 1 # Number of echo requests sent
                reqSentByte = reqSentByte + L[iter][3] # echo request bytes sent- based on the total size of the frame
                reqSentData = # echo request bytes sent sent - based on the payload size of the ICMP packet
            if L[iter][2] = srcIp:
                reqRecNum += 1 # Number of echo requests received
                reqRecByte = reqRecByte + L[iter][3] # echo request bytes received
                reqRecData =  # echo request data received

        if L[iter][4] = 1: # tracking metrics for echo replies
            if L[iter][1] = srcIp:
                repNumSent += 1 # Number of echo replies sent
                repSentByte = repSentByte + L[iter][3] # echo reply bytes sent
                repSentData =  # echo reply data
            if L[iter][2] = srcIp:
                repRecNum += 1 # Number of echo replies received
                repRecByte = repRecByte + L[iter][3] # echo reply bytes received
                repRecData =  # echo reply data received

	# Time based metrics
		# Average Round-Trip-Time, the time between sending an Echo-Req and receiving an Echo-Rep, measured in MS
		# Echo Request Throughput (in kB/s), the sum of the frame sizes of all the Echo-Reqs sent divided by the sum of RTTs
        # Echo Request Goodput (in kB/s) the sum of the ICMP payloads of all Echo-Reqs sent divided by the sum of the RTTs
        # Avg. reply delay (in microseconds so *1000), the time between a node receiving an Echo-Req and sending an Echo-Rep

	# Distance metrics
        # Avg. number of hops per Echo-Req (one hop per change of network, min. one hop)


