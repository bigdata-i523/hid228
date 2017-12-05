import csv
import matplotlib.pylab as plt
import numpy as np
import csv
so_data = []
with open('impacts.csv', 'r') as csvfile:
    so = csv.reader(csvfile, delimiter=',')

    for row in so:
        so_data.append(row)

len=len(so_data)
teamstats=so_data[0][1:]
for i in range(1,len):
    print(so_data[i][1:])
    nparray=np.array(list(map(float,so_data[i][1:])))
   # plt.yticks(np.arange(nparray.min(), nparray.max()))
    plt.xticks(rotation='vertical')
    plt.subplots_adjust(bottom=0.50)
    plt.bar(teamstats,nparray)
    plt.xlabel('Team Name')
    plt.ylabel('Contribution of the factor')

    plt.title(so_data[i][0])
    plt.savefig(so_data[i][0]+'.png')
    plt.show()

