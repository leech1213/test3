# readline_all.py
rf = open("kai_transfer_1month.txt", 'r')
wf = open("kai_to_0000.txt", 'w')
i=0
while True:
    line = rf.readline()
    if not line: break
    line = line.strip()
    if (line != ""):
        NewLine = line.split(",")
        #print(NewLine)
        if (NewLine[2][2] == "0" and NewLine[2][3] == "0" and NewLine[2][4] == "0" and NewLine[2][5] == "0"):
            print("%d - 0x0000 Found\n" % i)
            wf.write("%s, %s, %s, %s, %s, %s, %s\n" % (NewLine[0],NewLine[1],NewLine[2],NewLine[3],NewLine[4],NewLine[5],NewLine[6]))
        i=i+1
    #wf.write("%s %s %s %s %s %s %s",NewLine[0],NewLine[1],NewLine[2],NewLine[3],NewLine[4],NewLine[5],NewLine[6])
    #wf.write(NewLine[1])
rf.close()
wf.close()
