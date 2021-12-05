def compute(srcIp, L) : # Computing 13 different metrics per node
    print("compute method called for IP: " + srcIp)
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


    for iter in range(0, len(L), 1):
        print(L[iter][0])
	    # Data size metrics
        #print(str(L[iter][4]))
        if L[iter][5] == str(8): # tracking metrics for echo requests, index for ICMP type and comparison changed for the test packet
            if L[iter][2] == srcIp:
                reqSentNum += 1 # Number of echo requests sent
                reqSentByte = reqSentByte + (int(L[iter][4])) # echo request bytes sent- based on the total size of the frame
                reqSentData = reqSentData + (int(L[iter][4]) - 42) # echo request bytes sent sent - based on the payload size of the ICMP packet

            if L[iter][2] != srcIp:
                reqRecNum += 1 # Number of echo requests received
                reqRecByte = reqRecByte + (int(L[iter][4])) # echo request bytes received
                reqRecData = reqRecData + (int(L[iter][4]) - 42) # echo request data received


        if L[iter][5] == str(0): # tracking metrics for echo replies
            if L[iter][2] == srcIp:
                repSentNum += 1 # Number of echo replies sent
                repSentByte = repSentByte + (int(L[iter][4])) # echo reply bytes sent
                repSentData = repSentData + (int(L[iter][4]) - 42) # echo reply data

            if L[iter][2] != srcIp:
                repRecNum += 1 # Number of echo replies received
                repRecByte = repRecByte + (int(L[iter][4])) # echo reply bytes received
                repRecData = repRecData + (int(L[iter][4]) - 42) # echo reply data received

    print("ECHO REQ - Num Received: " + str(reqRecNum) + ", Num Sent: " + str(reqSentNum) + ", Bytes Received: " + str(reqRecByte) + ", Bytes Sent: " + str(reqSentByte) + ", Data Rec: " + str(reqRecData) + ", Data Sent: " + str(reqSentData))
    print("ECHO REP - Num Received: " + str(repRecNum) + ", Num Sent: " + str(repSentNum) + ", Bytes Received: " + str(repRecByte) + ", Bytes Sent: " + str(repSentByte) + ", Data Rec: " + str(repRecData) + ", Data Sent: " + str(repSentData))

    # Time based metrics
    req_sent = [] #requests sent
    req_rec = [] #requets received 
    rep_sent = [] #replyies sent
    rep_rec = [] # replies received
    totalRTT = 0 #initalize total RTT time 
    delayTotal = 0 # initialize delay total 
    totalHops = 0

    for iter in range(0, len(L), 1):
        if L[iter][5] == str(8): # if icmp type is 8 (echo request)
            if L[iter][2] == srcIp:#echo requests sent
                req_sent.append(L[iter]) #add the packet to requests sent list

            if L[iter][2] != srcIp: # echo requests received
                req_rec.append(L[iter]) #add packet to requests received list

        if L[iter][5] == str(0): # if icmp type is 0 (echo reply)
            if L[iter][2] == srcIp: #echo replies sent
                rep_sent.append(L[iter]) #add packet to replies sent list 

            if L[iter][2] != srcIp: # echo replies received
                rep_rec.append(L[iter])#add the packet to replies received list 

    #loop though each item in req_sent 
    for iter in req_sent:  
        #grab needed information
        reqTime = float(iter[1])
        reqSrc = iter[2]
        reqDest = iter[3]
        reqSeq = iter[6]
        # loop thought each item in rep_rec
        for iter in rep_rec:   
            #grab needed info
            repTime = float(iter[1])
            repDest = iter[3]
            repSeq = iter[6]
            # check if it is a reply for the current request that was sent 
            if (reqSrc == repDest) & (reqSeq == repSeq):
                rtt = repTime - reqTime # calculate Rtt by diference of Rep time and Req time 
                totalRTT = totalRTT + rtt # add to total rtt
                break
    # get Average RTT by dividing total rtt by the number of requests sent, multiply by 1000 to convert to Milliseconds  and round up to the 2nd decimal            
    avgRTT = round(((totalRTT/reqSentNum)*1000), 2) 

    # Echo Request Throughput (in kB/s), the sum of the frame sizes of all the Echo-Reqs sent divided by the sum of RTTs
    reqSentFramekB = (reqSentByte / 1000) #convert Total frame bytes of echo requests sent to kBs
    reqThroughput = (reqSentFramekB / totalRTT) #get throughput by dividing the total frame bytes by total round trip time
    reqThroughput = round(reqThroughput, 1) #round to the nearest decimal 
    
    # Echo Request Goodput (in kB/s) the sum of the ICMP payloads of all Echo-Reqs sent divided by the sum of the RTTs
    reqPayloadkB =  (reqSentData / 1000)
    reqGoodput = (reqPayloadkB / totalRTT)  #get goodput by dividing the total payload bytes by total round trip time
    reqGoodput = round(reqGoodput, 1) # round up to the nearest  first decimal
    
    # Avg. reply delay (in microseconds so *1000), the time between a node receiving an Echo-Req and sending an Echo-Rep
    for iter in req_rec: 
        #grab the needed info
        reqTime = float(iter[1]) 
        reqSrc = iter[2]
        reqDest = iter[3]
        reqSeq = iter[6]
        for iter in rep_sent:      
            #grab the needed info
            repTime = float(iter[1])
            repSrc = iter[2]
            repDest = iter[3]
            repSeq = iter[6]
            #check to see if the reply that we sent is for the current req that was received 
            if (reqDest == repSrc) & (reqSeq == repSeq):
                rtt = repTime - reqTime
                delayTotal = delayTotal + rtt
                break
    avgReplyDelay=round(((delayTotal/repSentNum)*1000000),2)

    print("Average RTT: " + str(avgRTT) + ", Echo Request Throughput(kB/sec):  " + str(reqThroughput) + ", Echo Request Goodput (kB/sec): " + str(reqGoodput) + ", Average Reply Delay (us): "+ str(avgReplyDelay))
	# Distance metrics
    # Avg. number of hops per Echo-Req (one hop per change of network, min. one hop)
    for iter in req_sent:
        reqSrc = iter[2]
        reqDest = iter[3]
        reqSeq = iter[6]
        reqSentTTL = int(iter[7])
        for iter in rep_rec:   
            #grab needed info
            repDest = iter[3]
            repSeq = iter[6]
            repRecTTL = int(iter[7])
            # check if it is a reply for the current request that was sent 
            if (reqSrc == repDest) & (reqSeq == repSeq):
                hops = abs((reqSentTTL- repRecTTL)) + 1
                totalHops = totalHops + hops 
                break
    avgHops = round((totalHops / reqSentNum), 2)
    print("Average Echo Request Hop Count: "+ str(avgHops))


