"""
Court Calendar Extract Tool
Caleb Long, William Courcell, Trevor Crump
Coders United
4/17/24
"""
import csv
FIELDS = ['RunDate', 'Date', 'Time', 'Courtroom', 'No', 'File Number', 'Defendant', 
          'Complainant', 'Attorney', 'Cont', 'AKA', 'Needs Fingerprinting', 
          'Bond', 'Charge Type','Charge', 'Plea', 'Ver', 'CLS', 'P', 'L', 'Domestic Violence', 'Judgement', 'ADA']

HEADER_END = '*' * 30

def is_summary_header(line):
    return line[0] == '1' and 'RUN DATE:' in line

def is_report_header(line):
    return line[0] != '1' and 'RUN DATE:' in line

def process_report_header(line, infile):
    data = {}
    data['RunDate'] = line[12:20]

    while True:
        line = infile.readline()

        if line == '' or HEADER_END in line:
            break
        elif 'COURT DATE:' in line:
            data['Date'] = line[22:30]
            data['Time'] = line[44:52]
            data['Courtroom'] = line[78:].strip()

    return data

def is_page_header(line):
    return line[0] == '1' and 'RUN DATE:' not in line

def process_page_header(line, infile):
    data = {}
    while True:
        line = infile.readline()

        if line == '' or HEADER_END in line:
            break


def is_case(line):
    try:
        int(line[0:6])
        return True
    except ValueError:
        return False


def process_case(line, infile):
    data = {}
    data['No'] = line[0:6].strip()
    data['File Number'] = line[8:19].strip()
    data['Defendant'] = line[20:41].strip()
    data['Complainant'] = line[42:56].strip()
    data['Attorney'] = line[66:82].strip()
    data['Cont'] = line[83:].strip()


    data['AKA'] = 'N/A'
    data['Needs Fingerprinting'] = 'No'
    data['Bond'] = 'N/A'

    return data

def process_charge(line,infile):
    data = {}
    data['Charge Type'] = line[8:11].strip()
    data['Charge'] = line[11:41].strip()
    data['Plea'] = line[50:56].strip()
    data['Ver'] = line[77:84].strip()

    return data

def process_other(line,infile):
    data = {}
    data['CLS'] = line[12:14].strip()
    data['P'] = line[18:19].strip()
    data['L'] = line[23:24].strip()
# Isnt Working?
    data['Judgement'] = line[49:66].strip()
    
    data['Domestic Violence'] = 'N/A'
    data['ADA'] = 'N/A'
    
    return data

def write_rec(writer, rpt_data, defend_data, charge_data, other_data):
    all_data = dict(rpt_data)
    all_data.update(defend_data)
    all_data.update(charge_data)
    all_data.update(other_data)
    writer.writerow(all_data)



def main():
    rpt_data = {}
    defend_data = {}
    charge_data = {}
    other_data = {}

    filename = input("Enter filename: ")
    infile = open(filename, 'r')

    csvfile = open('records.csv', 'w', newline='')
    writer = csv.DictWriter(csvfile, fieldnames=FIELDS)

    writer.writeheader()

    while True:
        line = infile.readline()

        if line == '' or is_summary_header(line):
            break
        elif is_report_header(line):
            rpt_data = process_report_header(line, infile)
        elif is_page_header(line):
            process_page_header(line, infile)
        elif is_case(line):
            if len(defend_data) > 0:
                write_rec(writer, rpt_data, defend_data, charge_data, other_data)
                defend_data = {}
                charge_data = {}
                other_data = {}
            defend_data = process_case(line, infile)
    
        elif 'PLEA:' in line:
            if len(charge_data) > 0:
                write_rec(writer, rpt_data, defend_data, charge_data, other_data)
                charge_data = {}
                other_data = {}
            charge_data = process_charge(line, infile)
        elif 'AKA:' in line:
            defend_data['AKA'] = line[19:].strip()
        elif 'DEFENDANT NEEDS TO BE FINGERPRINTED' in line:
            defend_data['Needs Fingerprinting'] = 'Yes'
        elif 'BOND:' in line:
            defend_data['Bond'] = line[25:].strip()
        elif 'JUDGMENT:' in line:
            other_data = process_other(line, infile)
            if 'ADA' in line:
                other_data['ADA'] = line[82:85].strip()
            elif 'DOM VL' in line:
                other_data['Domestic Violence'] = line[35:40].strip()
        else:
            print(line, end='')

    #used to prevent last line skip
    write_rec(writer, rpt_data, defend_data, charge_data, other_data)
    infile.close()



if __name__ == '__main__':
    main()