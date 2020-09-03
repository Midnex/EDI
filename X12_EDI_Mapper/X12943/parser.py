print('943 Loaded')

def translate(file, segd="~", eled="*", seled=":"):
    fileData = []
    with open(file, 'r') as f:
        for data in f:
            for line in data.split('~'):
                fileData.append(line)
                segment = line.split(eled)[0]
                if segment == 'ISA':
                    print(segment, len(line.split('*')))
                    print([i.strip() for i in line.split(eled)])
                if segment == 'GS':
                    print(segment, len(line.split('*')))
                    print([i.strip() for i in line.split(eled)])
                if segment == 'ST':
                    print(segment, len(line.split('*')))
                    print([i.strip() for i in line.split(eled)])
                if segment == 'W06':
                    print(segment, len(line.split('*')))
                    print([i.strip() for i in line.split(eled)])
                if segment == 'N1':
                    print(segment, len(line.split('*')))
                    print([i.strip() for i in line.split(eled)])
                if segment == 'G62':
                    print(segment, len(line.split('*')))
                    print([i.strip() for i in line.split(eled)])
                if segment == 'W04':
                    print(segment, len(line.split('*')))
                    print([i.strip() for i in line.split(eled)])
                if segment == 'W03':
                    print(segment, len(line.split('*')))
                    print([i.strip() for i in line.split(eled)])
                if segment == 'SE':
                    print(segment, len(line.split('*')))
                    print([i.strip() for i in line.split(eled)])
                if segment == 'GE':
                    print(segment, len(line.split('*')))
                    print([i.strip() for i in line.split(eled)])
                if segment == 'IEA':
                    print(segment, len(line.split('*')))
                    print([i.strip() for i in line.split(eled)])

                


    # return fileData


if __name__ == "__main__":
    print('Must be run from X12EDIMapper.py')
else:
    file = 'D:\\Programming\\Github\\home\\python\\EDI\\X12_EDI_Mapper\\examples\\710_AMRETAIL_7553788_0_0.943'
    print(translate(file))
