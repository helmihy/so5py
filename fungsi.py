
#Fungsi mencari FCFS/First Come First Serve
def fcfs(mhy):
    btHold,taHold = 0,0 
    pLine = []
    fcfsmhy = {}
    for key,value in mhy.items():
        at,bt = value[0],value[1]
        if (at == 0):
            taHold += bt
            fcfsmhy[key] = [btHold-at,bt-at]
            pLine.append([key,taHold])
            btHold = bt
        elif(btHold-at > 0):
            taHold += bt
            fcfsmhy[key] = [btHold-at,taHold-at]
            pLine.append([key,taHold])
            btHold += bt
        else:
            taHold += bt
            fcfsmhy[key] = [0,bt]
            pLine.append([key,taHold+1])
            btHold += bt
    return fcfsmhy,pLine
    
#Fungsi Mencari SJF/Shortest Job First
def sjf(mhy):
    begHold,endHold = 0,0
    sjfmhy,tempmhy,sortmhy,pLine ={},{},{},[]
    for key,value in mhy.items():
        at,bt = value[0],value[1]
        if (begHold == 0):
            endHold += bt
            sjfmhy[key] = [begHold-at,bt-at]
            pLine.append([key,endHold])
            begHold = bt
        else:
            tempmhy[key] = value[0],value[1]
    for key,value in sorted(tempmhy.items(), key = lambda x : x[1][1]):
        sortmhy[key] = value[0],value[1]
    for key,value in sortmhy.items():
        at,bt = value[0],value[1]
        if(begHold-at > 0):
            endHold += bt
            sjfmhy[key] = [begHold-at,endHold-at]
            pLine.append([key,endHold])
            begHold += bt
        else:
            endHold += bt
            sjfmhy[key] = [0,bt]
            pLine.append([key,endHold+1])
            begHold += bt            
    return sjfmhy,pLine
    
#Fungsi mencari SRTF/Shortest Remaining Time First
def srtf(mhy):
    begHold,endHold = 0,0
    srtfmhy,tempmhy,sortmhy,pLine = {},{},{},[]
    for key,value in mhy.items():
        at,bt = value[0],value[1]
        if (begHold == 0):
            second = list(mhy.values())[1]
            srtfmhy[key] = [begHold-at, bt-second[0]-at]
            endHold += bt-second[0]
            begHold = bt-second[0]
            tempmhy[key] = at, bt-begHold
            pLine.append([key,endHold])
        else:
            tempmhy[key] = at,bt
    for key,value in reversed(sorted(tempmhy.items(), key = lambda x : x[1][1],reverse=True)):
        sortmhy[key] = value[0],value[1]
    for key,value in sortmhy.items():
        at,bt = value[0], value[1]
        if key in srtfmhy.keys():
            hold = srtfmhy[key]
            endHold += bt
            srtfmhy[key] = [begHold-hold[1],endHold-at]
            pLine.append([key,endHold])
            begHold += bt
        elif(begHold-at > 0):
            endHold += bt
            srtfmhy[key] = [begHold-at,endHold-at]
            pLine.append([key,endHold])
            begHold += bt
        else:
            endHold += bt
            srtfmhy[key] = [0,bt]
            pLine.append([key,endHold+1])
            begHold += bt 
    return srtfmhy, pLine
    
#Fungsi Mencari Round Robins   
def rrobin(mhy,quantum):
    begHold = 0
    rrmhy,pLine = {},[]
    keyP = list(mhy.keys())
    at,bt = map(list, zip(*mhy.values()))
    atHold,btHold = at.copy(),bt.copy()
    while True:
        flag = True
        for i in range(len(keyP)):
            if (atHold[i] <= begHold):
                if (atHold[i] <= quantum):
                    if(btHold[i] > 0):
                        flag = False
                        if (btHold[i] > quantum):
                            begHold += quantum
                            btHold[i] -= quantum
                            atHold[i] += quantum
                            pLine.append([keyP[i],begHold])
                        else:
                            begHold += btHold[i]
                            rrmhy[keyP[i]] = [begHold-bt[i]-at[i],begHold-at[i]]
                            btHold[i] = 0
                            pLine.append([keyP[i],begHold])
                elif atHold[i] > quantum:
                    for j in range(len(keyP)):
                        if (atHold[j]<atHold[i]):
                            if(btHold[j] > 0):
                                flag = False
                                if(btHold[j] > quantum):
                                    begHold += quantum
                                    btHold[j] -= quantum
                                    atHold[j] += quantum
                                    pLine.append([keyP[j],begHold])
                                else:
                                    begHold += btHold[j]
                                    rrmhy[keyP[j]] = [begHold-bt[j]-at[j],begHold-at[j]]
                                    btHold[j] = 0
                                    pLine.append([keyP[j],begHold])
                    if(btHold[i]>0):
                        flag = False
                        if(btHold[i]>quantum):
                            begHold += quantum
                            btHold[i] -= quantum
                            atHold[i] += quantum
                            pLine.append([keyP[i],begHold])
                        else:
                            begHold += btHold[i]
                            rrmhy[keyP[i]] = [begHold-bt[i]-at[i],begHold-at[i]]
                            btHold[i] = 0
                            pLine.append([keyP[i],begHold])
            elif(atHold[i]>begHold):
                begHold += 1
                i -= 1
        if(flag):
            break
    return rrmhy,pLine
    
#Fungsi untuk Print Data + Kalkulasi
def printData(masukData, jenisData, pLine, Judul):
    avgWT,avgTT =0,0
    plinestr= "0 -> "
    print('---------------------------------------------')
    print(Judul.upper())
    print('---------------------------------------------')
    print('| KEY | ARRIVAL | BURST | WAIT | TURNAROUND |')
    for key,value in sorted(jenisData.items()):
        print('{:>4}{:>8}{:>9}{:>8}{:>10}'.format(key,masukData[key][0],masukData[key][1],value[0],value[1]))
        avgWT += value[0]
        avgTT += value[1]
    print('Rata-Rata Wait Time = {} \nRata-Rata Turnaround Time = {}\n'.format(avgWT/len(jenisData),avgTT/len(jenisData)))
    for x in pLine:
        plinestr += ('{} -> {} -> '.format(x[0],x[1]))
    print('{}\n'.format(plinestr[:-3]))