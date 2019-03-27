import xlsxwriter, transaction
from pprint import pprint

def main():
    parse(getData('data/709_AMRETAIL_3059585_0_0.940'), 'data/Test.xlsx')

def getData(pFile):
    return open(pFile, 'r').read()

def parse(pInput, pOutput):
    data = pInput.split('~')
    sortedData = []

    # Loop Variables
    set = 0
    index = 0
    tempData = []
    for i in xrange(3, len(data) - 1):
        if set == 11:
            set = 0
            sortedData.append(tempData)
            tempData = []
            index += 1

        tempData.append(data[i])
        set += 1

    # Transaction Variables
    transactions = []
    for transData in sortedData:
        newTransaction = transaction.Transaction(
            transData[0].split('*')[2],  # Transaction Number

            transData[1].split('*')[4],  # DC Number

            transData[2].split('*')[2],  # Store Number

            transData[3].split('*')[1],  # Address 1
            transData[3].split('*')[2],  # Address 2

            transData[4].split('*')[1],  # City
            transData[4].split('*')[2],  # State
            transData[4].split('*')[3],  # Zip

            transData[5].split('*')[5],  # Carrier X
            transData[5].split('*')[6],  # Service X
            transData[5].split('*')[10],  # SCAC

            transData[7].split('*')[1],  # Units
            transData[7].split('*')[5],  # UPC X
            transData[7].split('*')[16],  # SKU X
        )

        transactions.append(newTransaction)

    workbook = xlsxwriter.Workbook(pOutput)
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'FILE_NAME')

    worksheet.write('A2', 'TRANSACTION NUM')
    worksheet.write('B2', 'DC#')
    worksheet.write('C2', 'STORE NUM')
    worksheet.write('D2', 'ADDRESS 1')
    worksheet.write('E2', 'ADDRESS 2')
    worksheet.write('F2', 'CITY')
    worksheet.write('G2', 'STATE')
    worksheet.write('H2', 'ZIP')
    worksheet.write('I2', 'CARRIER')
    worksheet.write('J2', 'SERVICE')
    worksheet.write('K2', 'SCAC')
    worksheet.write('L2', 'UNITS')
    worksheet.write('M2', 'UPC')
    worksheet.write('N2', 'SKU')

    #worksheet.write('A3', transData.dcNum + '_' + data[1].split('*')[2] + '_' + 'RANDOMNUMBER' + '_' + 'RANDOMNUMBER' + '_' + 'RANDOMNUMBER' + '.CSV')

    transRow = 5
    for transData in transactions:
        worksheet.write('A' + str(transRow), transData.id)
        worksheet.write('B' + str(transRow), transData.dcNum)
        worksheet.write('C' + str(transRow), transData.storeNum)
        worksheet.write('D' + str(transRow), transData.addressPrimary)
        worksheet.write('E' + str(transRow), transData.addressSecondary)
        worksheet.write('F' + str(transRow), transData.city)
        worksheet.write('G' + str(transRow), transData.state)
        worksheet.write('H' + str(transRow), transData.zip)
        worksheet.write('I' + str(transRow), transData.carrier)
        worksheet.write('J' + str(transRow), transData.service)
        worksheet.write('K' + str(transRow), transData.scac)
        worksheet.write('L' + str(transRow), transData.units)
        worksheet.write('M' + str(transRow), transData.upc)
        worksheet.write('N' + str(transRow), transData.sku)
        transRow += 1

    workbook.close()

main()
