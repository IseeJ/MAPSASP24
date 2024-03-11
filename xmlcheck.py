# $python3 xmlcheck.py QPT_35501_046R.xml

import Utils
import sys
import xml.etree.ElementTree as ET


def getID(sn):
    db_accessor = Utils.DBaccess()
    ID = db_accessor.component_id(sn,idt='serial_number')

    return ID

def checksn(allsn):
    wrongsn=[]
    for sn in allsn:
        ID = getID(sn)
        if ID is None:
            wrongsn.append(sn)

    return wrongsn

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

#print(get_serial(sys.argv[1]))                                                                                  
print(checksn(get_serial(sys.argv[1]))
