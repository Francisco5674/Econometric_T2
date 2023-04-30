from math import log

class Family:
    def __init__(self, id):
        self.id = id
        self.members = {}
    
    def addmember(self, member):
        self.members[member.id] = member

class Person:
  def __init__(self, 
              id, 
              family_id, 
              pco1, 
              age, 
              sex, 
              married, 
              numtrab, 
              sector, 
              wagehour, 
              school, 
              nlincome,
              hours,
              part):
    self.id = id
    self.family_id = family_id
    self.pco1 = pco1
    self.age = age
    self.sex = sex
    self.married = married
    self.numtrab = numtrab
    self.sector = sector
    self.wagehour = wagehour
    self.school = school
    self.nlincome = nlincome
    self.hours = hours
    self.part = part
     
  def dummy_nworkers(self):
    result = [0,0,0,0,0]
    if self.numtrab == "B":
      result[0] = 1
    elif self.numtrab == "C":
      result[1] = 1
    elif self.numtrab == "D":
      result[2] = 1
    elif self.numtrab == "E":
      result[3] = 1
    elif self.numtrab == "F":
      result[4] = 1
    elif self.numtrab == "X":
      result[4] = "."
    return result
  
  def ismarried(self):
    if self.married == "Casado(a)" or self.married == "Conviviente o pareja":
      return 1
    else:
      return 0
  
  def which_industry(self):
    result = [0,0,0,0,0,0,0,0]
    if self.sector == "EXPLOTACION MINAS Y CANTERAS":
      result[0] = 1
    elif self.sector == "IND.MANUFACTURERAS":
      result[1] = 1
    elif self.sector == "ELECTRICIDAD GAS Y AGUA":
      result[2] = 1
    elif self.sector == "CONSTRUCCION":
      result[3] = 1
    elif self.sector == "COMERCIO MAYOR/MENOR REST.HOTELES":
      result[4] = 1
    elif self.sector == "TRANSPORTE Y COMUNICACIONES":
      result[5] = 1
    elif self.sector == "ESTAB.FINANCIEROS SEGUROS":
      result[6] = 1
    elif self.sector == "SERVICIOS COMUNALES SOCIALES":
      result[7] = 1
    elif self.sector == "ACT. NO BIEN ESPECIFICADAS":
      result[7] = "."
    
    return result

  def lnwage(self):
    try:
      return log(float(self.wagehour))
    except:
      pass
    return "."
  
  def parcial(self):
    if self.hours.isnumeric():
      if int(self.hours) <= 30:
        return 1
      else:
        return 0
    return "."
  
  def work_hours(self):
    if self.hours.isnumeric():
      return int(self.hours)
    return "."
   
  def isfemale(self):
    if self.sex == "Mujer":
      return 1
    else:
      return 0
    
  




