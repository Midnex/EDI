# Goal Parse EDI File to Excel, can be called from other programs such as ABI, and AMR_Util backup features.
# Error detection will be added but less of a concern for now.
# Customer uses non standard EDI files for some elements.

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

            # ISA - Interchange Control Header
            if 'ISA' in splitRow[0]:
                print('Processing ISA loop')

                ISA00 = splitRow[0]             # Interchange Control Header
                ISA01 = splitRow[1]             # Authorization Information Qualifier
                ISA02 = splitRow[2].strip()     # Authorization Information
                ISA03 = splitRow[3]             # Security Information Qualifier
                ISA04 = splitRow[4].strip()     # Security Information
                ISA05 = splitRow[5]             # Interchange ID Qualifier
                ISA06 = splitRow[6].strip()     # Interchange Sender ID
                ISA07 = splitRow[7]             # Interchange ID Qualifier
                ISA08 = splitRow[8].strip()     # Interchange Receiver ID
                ISA09 = splitRow[9]             # Interchange Date
                ISA10 = splitRow[10]            # Interchange Time
                ISA11 = splitRow[11]            # Interchange Control Standards Identifier
                ISA12 = splitRow[12]            # Interchange Control Version Number
                ISA13 = splitRow[13]            # Interchange Control Number
                ISA14 = splitRow[14]            # Acknowledgment Requested
                ISA15 = splitRow[15]            # Usage Indicator
                ISA16 = splitRow[16]            # Component Element Separator

                output_file.write('ISA for ' + x12_940_file.split('/')[-1] + '\n')
                output_file.write('ID,Sender,ID,Receiver,Date,Time\n')
                line_to_write = ISA05 + ',' + ISA06 + ',' + ISA07 + ',' + ISA08 + ',' + ISA09 + ',' + ISA10 + '\n\n'
                output_file.write(line_to_write)

            # GS - Functional Group Header
            if 'GS' in splitRow[0]:
                print('Processing GSLoop', gsCount)
                gsCount += 1

                GS00 = splitRow[0].strip()      # Functional Group Header
                GS01 = splitRow[1]              # Functional Identifier Code
                GS02 = splitRow[2]              # Application Sender's Code
                GS03 = splitRow[3]              # Application Receiver's Code
                GS04 = splitRow[4][4:6] + '/' + splitRow[4][-2:] + '/' + splitRow[4][0:4] # Date
                GS05 = splitRow[5]              # Time
                GS06 = splitRow[6]              # Group Control Number
                GS07 = splitRow[7]              # Responsible Agency Code
                GS08 = splitRow[8]              # Version / Release / Industry Identifier Code

                output_file.write('Header,SenderCode,ReceiverCode,Date\n')
                line_to_write =  'GS,' + GS02 + ',' + GS03 + ',' + GS04 + '\n\n'
                output_file.write(line_to_write)

            # ST - Transaction Set Header
            if 'ST' in splitRow[0]:
                print('Processing STLoop',stCount)
                stCount += 1

                ST00 = splitRow[0]              # Transaction Set Header
                ST01 = splitRow[1]              # Transaction Set Identifier Code
                ST02 = splitRow[2]              # Transaction Set Control Number
            
            # W06 - Warehouse Shipment Identification
            if 'W06' in splitRow[0]:
                print('Processing W06')

                W0600 = splitRow[0]             # Warehouse Shipment Identification
                W0601 = splitRow[1]             # Reporting Code
                W0602 = splitRow[2]             # Depositor Order Number
                W0603 = splitRow[3][4:6] + '/' + splitRow[3][-2:] + '/' + splitRow[3][0:4] # Date
                W0604 = splitRow[4]             # Shipment Identification Number
                W0612 = splitRow[5]             # Action Code

            # N1 - Name
            if 'N1' in splitRow[0]:
                N100 = splitRow[0]              # N1 Loop
                if 'ST' in splitRow[1]:
                    print('Processing N1*ST')
                    N1ST01 = splitRow[1]        # Entity identifer Code
                    N1ST02 = splitRow[2]        # Name
                    N1ST03 = splitRow[3]        # Identification Code Qualifier
                    N1ST04 = splitRow[4]        # Identification Code

                if 'SF' in splitRow[1]:
                    print('Processing N1*SF')

                    N1SF01 = splitRow[1]        # Entity identifer Code
                    N1SF02 = splitRow[2]        # Name
                    # N1SF03 = splitRow[3]        # Identification Code Qualifier
                    # N1SF04 = splitRow[4]        # Identification Code

            # G62 Not used for this, need example to implement better.
            # W27 Not used for this, hard coded, need example to implement better.

            # Item Detail
            if 'W04' in splitRow[0]:
                if w04CountTotal == 0:
                    output_file.write('EDI,Line,PO#,Customer,PO Date,UPC,Units,UoM\n')
                w04CountTotal += int(splitRow[1])
                print('Processing W04Loop')

                W0400 = splitRow[0]             # Item Detail Loop
                W0401 = splitRow[1]             # Number of Units Shipped
                W0402 = splitRow[2]             # Unit or Basis for Measurement Code
                W0403 = splitRow[3]             # Not used, Not sure what it is
                W0404 = splitRow[4]             # Product/Service ID Qualifier
                W0405 = splitRow[5]             # Product/Service ID
                W0408 = splitRow[8]             # Customer defined
                W0409 = splitRow[9].replace('~', '') # Customer defined

                line_to_write = ST01 + ',' + ST02 + ',' + W0602 + ',' + GS02 + ',' + W0603 + ',' + W0409 + ',' + W0401 + ',' + W0402 + '\n'
                output_file.write(line_to_write)

            # W03 to be implemented, not needed right now though present.
            # Total Shipment Information

            # Not needed for this
            # Transaction Set Trailer
            # if 'SE' in splitRow[0]:
            #     print('Processing closing SE')

            #     line_to_write = splitRow[0] + ',' + splitRow[1] + ',' + splitRow[2] + '\n'
            #     output_file.write(line_to_write)

            # # Not needed for this
            # # Functional Group Trailer
            # if 'GE' in splitRow[0]:
            #     print('Processing closing GE')

            #     line_to_write = splitRow[0] + ',' + splitRow[1] + ',' + splitRow[2] + '\n'
            #     output_file.write(line_to_write)

            # # Not needed for this
            # # Interchange Control Trailer
            # if 'IEA' in splitRow[0]:
            #     print('Processing closing IEA')

            #     line_to_write = splitRow[0] + ',' + splitRow[1] + ',' + splitRow[2] + '\n'
            #     output_file.write(line_to_write)


    print('\nClosing:', x12_940_file.split('/')[-1])
    print('\tTotal Files:', gsCount)
    print('\tTotal PO#s:', stCount)
    print('\tTotal Units:', w04CountTotal)
    print('Writing:', out_file)





#ISALoop = ISA - IEA
    #GSLoop  = GS - GE
    # st_Loop_count = 0
    #STLoop = ST - SE
    # w3_count = sum of W04[1]
