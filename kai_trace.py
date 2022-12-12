from web3 import Web3
rf = open("kai_transfer_recent.txt", 'r')
kaiwallet_frequency_from_file = open("Kai_Wallet_Frequency_from.txt", 'w')
kaiwallet_frequency_to_file = open("Kai_Wallet_Frequency_to.txt", 'w')
kaiwallet_balance_file = open("Kai_Wallet_Balance.txt", 'w')
kaiwallet_rank_file = open("sKai_Wallet_Rank.txt", 'w')
WalletFrequency_from={} #dic
WalletFrequency_to={} #dic
WalletBalance={}
WallAddress="" #string

#Special address
BBFund = ["0x931579fa23580cb2214fbe89ab487f6aede8a352"]
UserReservedSKAI = ["0xf81d1383e6d9877c9c0a768af7bb9d861c692899"]
#token_address,from_address,to_address,value,transaction_hash,log_index,block_number
def SortInDescendingOrder_Wallet(WalletDic): 
   sorted_walletDic = sorted(WalletDic.items(), key = lambda item: item[1], reverse = True)
   return sorted_walletDic

def SortInAscendingOrder_Wallet(WalletDic): 
   sorted_walletDic = sorted(WalletDic.items(), key = lambda item: item[1], reverse = False)
   return sorted_walletDic

def Count_Wallet_Frequency(FromWalletAddress, ToWalletAddress):
    try:
        WalletFrequency_from[FromWalletAddress]+=1
    except:
        WalletFrequency_from[FromWalletAddress]=1
    try:
        WalletFrequency_to[ToWalletAddress]+=1
    except:
        WalletFrequency_to[ToWalletAddress]=1

def Count_Wallet_Balance(FromWalletAddress, ToWalletAddress, Value):
    try:
        WalletBalance[FromWalletAddress] = WalletBalance[FromWalletAddress] - Value
    except:
        WalletBalance[FromWalletAddress] = -Value 

    try:
        WalletBalance[ToWalletAddress] = WalletBalance[ToWalletAddress] + Value
    except:
        WalletBalance[ToWalletAddress] = Value

while True:
    line = rf.readline()
    if not line: break
    line = line.strip()
    if (line != ""):
        NewLine = line.split(",")
        if ("0x" in NewLine[0]):
            Count_Wallet_Frequency(str(NewLine[1]),str(NewLine[2]))
            Value_wei = Web3.fromWei(int(NewLine[3]),"ether")
            Count_Wallet_Balance(str(NewLine[1]),str(NewLine[2]),Value_wei)

#print(WalletFrequency_from)
#print(WalletFrequency_to)
print(WalletBalance)

#sort
WalletFrequency_from = SortInDescendingOrder_Wallet(WalletFrequency_from)
WalletFrequency_to = SortInDescendingOrder_Wallet(WalletFrequency_to)
WalletBalance = SortInDescendingOrder_Wallet(WalletBalance)

#write to a file
kaiwallet_frequency_from_file.write(str(WalletFrequency_from))
kaiwallet_frequency_to_file.write(str(WalletFrequency_to))
kaiwallet_balance_file.write(str(WalletBalance))

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
kaiwallet_frequency_from_file.close()
kaiwallet_frequency_to_file.close()
kaiwallet_balance_file.close()
kaiwallet_rank_file.close()

