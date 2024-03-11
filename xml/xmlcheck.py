# $python3 xmlcheck.py QPT_35501_046R.xml

import Utils
import sys
import xml.etree.ElementTree as ET


def getID(sn):
    db_accessor = Utils.DBaccess()
    ID = db_accessor.component_id(sn,idt='serial_number')

    return ID

def get_serial(filename):
    path = "/uscms/home/jennetd/nobackup/outer-tracker/preproduction/XML/"+filename
    tree = ET.parse(path)
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

parse_sn = get_serial(sys.argv[1])

print("correct serial numbers with IDs: ",checksn(parse_sn)[0])
print("wrong serial numbers: ", checksn(parse_sn)[1])
