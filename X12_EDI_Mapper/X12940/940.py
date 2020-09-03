#! python3
# 940 edi reader and print to xlsx
# http://www.jobisez.com/edi/documents/example-edi.aspx?set-id=940
# http://edi.aaltsys.info/11_940-guide.html

fileSet = []
file = '''ISA*00*          *00*          *ZZ*AMRETAIL       *ZZ*SHIPGLOBAL     *181008*1801*U*00401*000000172*1*P*>~GS*OW*AMRETAIL*SHIPGLOBAL*20181008*1801*172*T*004010~ST*940*0001~W05*N*48078328*0~N1*SF**92*782~N1*ST*WILSONS LEATHER 3211*92*3211~N3*FASHION OUTLETS OF CHICAGO*5220 FASHION OUTLETS WAY 1170~N4*ROSEMONT*IL*60018~W66*TP*U***FedEx*Ground****FDEG~LX*1~W01*1*EA**UP*400732310031**********VN*73231003~W76*1~SE*11*0001~GE*1*172~IEA*1*000000172~'''
for elem in file.split('~'):
    # uncomment to enable ISA header
    if 'ISA' in elem:
        print('I01,I02,I03,I04,I05,I06,I07,I08,I09,I10,I11,I12,I13,I14,I15,I16')
        print(elem[4:6] + ',' + elem[7:17] + ',' + elem[18:20] + ',' + elem[21:31] + ',' + elem[32:34] + ',' + elem[35:50] + ',' + elem[51:53] + ',' + elem[54:69] + ',' + elem[70:76] + ',' + elem[77:81] + ',' + elem[82:83] + ',' + elem[84:89] + ',' + elem[90:99] + ',' + elem[100:101] + ',' + elem[102:103] + ',' + elem[104:105] + '\n')
    #
    if 'GS' in elem:
        print(elem)
# Group 1.	0:2	`GS`
# Group 3.	3:5	`OW`
# Group 5.	6:14	`AMRETAIL`
# Group 7.	15:25	`SHIPGLOBAL`
# Group 9.	26:34	`20181008`
# Group 11.	35:39	`1801`
# Group 13.	40:43	`172`
# Group 15.	44:45	`T`
# Group 17.	46:52	`004010`
