array = ["A","B", "A","A","C","B"]

counter = {}
for value in array:
    try: counter[value]+=1
    except: counter[value]=1
            
print(array)
print(counter)
