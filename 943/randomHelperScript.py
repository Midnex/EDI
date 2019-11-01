# not really part of the EDI project, but used with 943 edi parser to catch items not imported from 832/888 files.
# Checks problem SKUs from 943 output, against internal database, export to file, for upload into 3PL WMS.

import pyperclip

lst = pyperclip.paste()

database = open('sortedDatabase.txt','r')
flatFileUpload = open('flatfile.txt','a')

# broke.... fix first!
def removeDuplicates():
    newFile = set()

    count = 0
    for line in database:
        newFile.add(line)
        count += 1
    print('Loaded',count,'records.')

    newFile = sorted(newFile)
    for line in newFile:
        databaseNew = open('sortedDatabase.txt','a')
        databaseNew.write(line)
    print(f'Wrote {len(newFile)} records.')
    print('Done...')
    menuSystem()

def exportSKU():
    newFile = set()

    count = 0
    for line in database:
        for sku in lst.split('\n'):
            if sku.strip() == line[0:8]:
                newFile.add(line)
                count += 1
    print(f'Loaded {count} records.')

    for line in sorted(newFile):
        flatFileUpload.write(line)
    print(f'Wrote {len(newFile)} records.')
    menuSystem()

def menuSystem():
        x = input('Select an item:\n1. Remove Duplicates\n2. Export Items from Clipboard List\n3. Quit\n')
        
        if x == '1':
            removeDuplicates()
        elif x == '2':
            exportSKU()
        elif x == '3':
            print('Quitting')
        else:
            menuSystem()

menuSystem()
