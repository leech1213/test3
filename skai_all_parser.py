from web3 import Web3
rf = open("skai_trans.txt", 'r')
kaiwallet_balance_file = open("skai_all_balance.txt", 'w')
WalletFrequency_from={} #dic
WalletFrequency_to={} #dic
WalletBalance={}
WallAddress="" #string

#Special address
BBFund = "0x931579fa23580cb2214fbe89ab487f6aede8a352"
#token_address,from_address,to_address,value,transaction_hash,log_index,block_number

while True:
    line = rf.readline()
    if not line: break
    line = line.strip()
    if (line != ""):
        NewLine = line.split(",")
        if ("0x" in NewLine[0]):
            Str = str(NewLine)
            Str = Str.replace("'", '')
            Str = Str.replace('[', '')
            Str = Str.replace(']', '')
            kaiwallet_balance_file.write(Str)
            kaiwallet_balance_file.write("\n")

#write to a file
#kaiwallet_balance_file.write(str(WalletBalance))

"""
WalletBalance = SortInDescendingOrder_Wallet(WalletBalance)
i=0
for key,value in WalletBalance.items():
    if (i>10): 
        break
    print("Key = %s value = %d" % (key,value))
    i=i+1
"""
#close file handles
rf.close()
kaiwallet_balance_file.close()

