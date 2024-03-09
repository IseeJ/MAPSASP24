import Utils

def getID(sn):
    db_accessor = Utils.DBaccess()
    ID = db_accessor.component_id(sn,idt='serial_number')

    return ID

def checksn(allsn):
    wrongsn=[]
    for sn in allsn:
        ID = getID(sn)
        if str(ID) == "None":
            wrongsn.append(sn)

    return wrongsn
  
serial_numbers = [
    "939534613",
    "1342187798",
    "1342187808",
    "10530",
    "805316902",
    "939534629",
    "1342187811",
    "1207970084",
    "939534599",
    "1073752321",
    "2684365060",
    "272649",
    "1207970050",
    "1073752321",
    "805316872",
    "272649"
]

print(checksn(serial_numbers))
#badsn = 10530, 2684365060, 272649, 272649
#this returns ['2684365060', '272649', '272649']

print(getID("10530")) 
#this one should also be invalid but turns out it found some matching sn from the database (the ID is 7169)!
