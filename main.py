
import fungsi

#github helmihy/so6

#INPUTKAN DATA DI ARRAY

#Array Data terdiri [Arrival/Waktu Kedatangan, Burst Time]
masukData = {'P1': [0,6], 'P2': [1,4], 'P3': [3,3], 'P4':[6,8]}
#Masukkan Nilai Quantum Time
masukQuant = 4
#Opsional (blm nemu)
masukContSwitch = 0.4

#Instansiasi 
fcfsScheduling,fcfsLine = fungsi.fcfs(masukData)
sjfScheduling,sjfLine = fungsi.sjf(masukData)
srtfScheduling,srtfLine = fungsi.srtf(masukData)
rrobinScheduling,rrLine = fungsi.rrobin(masukData,masukQuant)

#Memanggil & Print Data
print('PROGRAM KALKULASI CPU SCHEDULLING\n')
fungsi.printData(masukData,fcfsScheduling,fcfsLine, 'Hasil dari FCFS(First Come First Serve)')
fungsi.printData(masukData,sjfScheduling,sjfLine,'Hasil dari SJF(Shortest Job First)')
fungsi.printData(masukData,srtfScheduling,srtfLine,'Hasil dari SRTF(Shortest Remaning Time First)')
fungsi.printData(masukData,rrobinScheduling,rrLine,'Hasil dari Round Robin dengan QTime={}'.format(masukQuant))
#sum([len(x) for x in my_dict.values()]) - fungsi menjumlahkan untuk membuat jawaban rata-rata

#github helmihy/so5
