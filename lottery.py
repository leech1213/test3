# readline_all.py
#rf = open("kai_transfer_all.txt", 'r')
rf = open("trans.txt", 'r')
wf = open("ticket.txt", 'w')

i=0
while True:
    line = rf.readline()
    if not line: break
    line = line.strip()
    if (line != ""):
        NewLine = line.split(",")
        try:
            if (NewLine[6][2] == "0" and NewLine[6][3] == "5" and NewLine[6][4] == "5" and NewLine[6][5] == "a"):
             print("%d - 0x055a\n" % i)
             i=i+1
             wf.write("%s, %s, %s\n" % (NewLine[5],NewLine[6],NewLine[10]))
        except:
            print("except")
rf.close()
wf.close()
