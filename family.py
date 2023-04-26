class Family:
    def __init__(self, id):
        self.id = id
        self.members = {}
    
    def addmember(self, member):
        self.members[member.id] = member

class Person:
    def __init__(self, id, family_id, pco1, age, sex, married, numtrab, sector, wagehour, nlincome):
        self.id = id
        self.family_id = family_id
        self.pco1 = pco1
        self.age = age
        self.sex = sex
        self.married = married
        self.numtrab = numtrab
        self.sector = sector
        self.wagehour = wagehour
        self.nlincome = nlincome


