# readline_all.py
#rf = open("kai_transfer_all.txt", 'r')
from web3 import Web3 
rf = open("kai_transfer_1month.txt", 'r')
wf = open("kai_from_0000_1month.txt", 'w')
i=0
while True:
    line = rf.readline()
    if not line: break
    line = line.strip()
    if (line != ""):
        NewLine = line.split(",")
        #print(NewLine)
        if (NewLine[1][2] == "0" and NewLine[1][3] == "0" and NewLine[1][4] == "0" and NewLine[1][5] == "0"):
            print("%d - 0x0000 Found\n" % i)
            value_wei=Web3.fromWei(int(NewLine[3]), "ether")
            print(value_wei)
            wf.write("%s, %s, %s, %s, %s, %s, %s\n" % (NewLine[0],NewLine[1],NewLine[2],str(value_wei),NewLine[4],NewLine[5],NewLine[6]))
        i=i+1
    #wf.write("%s %s %s %s %s %s %s",NewLine[0],NewLine[1],NewLine[2],NewLine[3],NewLine[4],NewLine[5],NewLine[6])
    #wf.write(NewLine[1])
rf.close()
wf.close()
