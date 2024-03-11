#$python3 xmlcheck_all.py /uscms/home/jennetd/nobackup/outer-tracker/preproduction/XML/QPT*


import Utils
import sys
import glob
import xml.etree.ElementTree as ET


def getID(sn):
    db_accessor = Utils.DBaccess()
    ID = db_accessor.component_id(sn,idt='serial_number')

    return ID                                                                                                                                                                                    

def get_serial(filepath):                                                                                                    
    tree = ET.parse(filepath)
    root = tree.getroot()
    serial_numbers = []
    for part in root.findall('.//PART'):
        serial = part.find('SERIAL_NUMBER')
        if serial is not None:
            serial_numbers.append(serial.text)
    return serial_numbers

def checksn(allsn):
    wrongsn = []
    sn_ID = {}
    for sn in allsn:
        ID = getID(sn)
        if ID is not None:
            sn_ID[sn] = ID
        else:
            wrongsn.append(sn)
    return sn_ID, wrongsn

xmlfiles = glob.glob(sys.argv[1])


for xmlfile in xmlfiles:
    print(xmlfile)
    parse_sn = get_serial(xmlfile)
    print("correct serial number with ID: ",checksn(parse_sn)[0])
    print("wrong serial number: ", checksn(parse_sn)[1])
