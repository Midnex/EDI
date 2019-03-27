# seriously nothing to see here yet. Just opens a file and does nothing.

import csv, tkinter as tk, os
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
path = os.path.dirname(os.path.abspath(__file__))

x12_940_file = filedialog.askopenfilename(initialdir = path, title = "Select 943 File", filetypes = (("943 X12 EDI File","*.943"),("all files","*.*")))

out_file = x12_940_file.split('/')[-1].split('.')[0] + '.csv'

output_file = open(out_file,'w')

stCount = 0
gsCount = 0
w04Count = 0
w04CountTotal = 0

stLoop = []
gsLoop = []


with open(x12_940_file,'r') as csv_in_file:
    csv_reader = csv.reader(csv_in_file, delimiter='~')
    for line in csv_reader:
        for row in line:
            splitRow = row.split('*')
            if 'ISA' in splitRow[0]:
                print(splitRow[0], splitRow[1], splitRow[3], splitRow[5], splitRow[6],splitRow[7], splitRow[8], splitRow[9], splitRow[10], splitRow[12],splitRow[13], splitRow[14])
                output_file.write(splitRow[0])
                output_file.write(',')
                output_file.write(splitRow[1])
                output_file.write(',')
                output_file.write(splitRow[3])
                output_file.write(',')
                output_file.write(splitRow[5])
                output_file.write(',')
                output_file.write(splitRow[6])
                output_file.write(',')
                output_file.write(splitRow[7])
                output_file.write(',')
                output_file.write(splitRow[8])
                output_file.write(',')
                output_file.write(splitRow[9])
                output_file.write(',')
                output_file.write(splitRow[10])
                output_file.write(',')
                output_file.write(splitRow[12])
                output_file.write(',')
                output_file.write(splitRow[13])
                output_file.write(',')
                output_file.write(splitRow[14])
                output_file.write('\n')

            if 'GS' in splitRow[0]:
                gsCount += 1
                output_file.write(splitRow[0].strip())
                output_file.write(',')
                output_file.write(splitRow[2])
                output_file.write(',')
                output_file.write(splitRow[3])
                output_file.write(',')
                output_file.write(str(splitRow[4][4:6] + '/' + splitRow[4][-2:] + '/' + splitRow[4][0:4]))
                output_file.write('\n')

            if 'ST' in splitRow[0]:
                stCount += 1
                print(splitRow[0], splitRow[1], splitRow[2])
            if 'W06' in splitRow[0]:
                print(splitRow[0], splitRow[2], splitRow[3])
            if 'N1' in splitRow[0]:
                if 'ST' in splitRow[1]:
                    print(splitRow[0], splitRow[1], splitRow[2])
                if 'SF' in splitRow[1]:
                    print(splitRow[0], splitRow[1], splitRow[2].replace('~',''))
            if 'W04' in splitRow[0]:
                w04CountTotal += int(splitRow[1])
                print(splitRow[0], splitRow[1], splitRow[2], splitRow[-1].replace('~',''))
            if 'SE' in splitRow[0]:
                print(splitRow[0], splitRow[1], splitRow[2])
            if 'GE' in splitRow[0]:
                print(splitRow[0], splitRow[1], splitRow[2])
            if 'IEA' in splitRow[0]:
                print(splitRow[0], splitRow[1], splitRow[2])


    print('Closing:', x12_940_file.split('/')[-1])
    print('\tTotal Files:', gsCount)
    print('\tTotal Receipts:', stCount)
    print('\tTotal Units:', w04CountTotal)
    print('Writing:', out_file)



            # if 'W06*J*' in row:
            #     # po_num =
            #     print(row.split('*')[2])
            #
            #     if 'W04' in row:
            #         sku = row.split('*')[-1]
            #         cartons = row.split('*')[1]
            # linePrint = po_num,sku,cartons
            # print(linePrint)



#ISALoop = ISA - IEA
    #GSLoop  = GS - GE
    # st_Loop_count = 0
    #STLoop = ST - SE
    # w3_count = sum of W04[1]
