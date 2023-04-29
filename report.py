import data_manager

agents = data_manager.persons
households = data_manager.families

def agemembers(minage, maxage, person, family):
    n = 0
    for key,member in family.members.items():
      if minage <= member.age <= maxage:
        n = n + 1
      else:
        pass
    return n 

with open("data_p1.csv", mode= "w", encoding= "latin-1") as file:
  file.write("""parcial,parti,edad,edad2,escolaridad,casada,N(0_5),N(6_17),D[2_5],D[6_9],D[10_49],D[50_199],D[200+],D[minas],D[manu],D[EGA],D[constru],D[comercio],D[transporte],D[serv fin],D[servicios],Log_salario,nlingreso,N(18+),mujer""" + "\n")
  for key,person in agents.items():
    record = []
    # dependent variable
    record.append(person.parcial())
    # parti
    record.append(person.part)
    # age
    record.append(person.age)
    # age^2
    record.append(person.age*person.age)
    # school
    record.append(person.school)
    # ismarried
    record.append(person.ismarried())
    # children 0-5
    record.append(agemembers(0, 5, person, households[person.family_id]))
    # children 6-17
    record.append(agemembers(6, 17, person, households[person.family_id]))
    # trabajadores
    record = record + person.dummy_nworkers()
    # industry
    record = record + person.which_industry()
    # salary ln
    record.append(person.lnwage())
    # nlincome
    record.append(person.nlincome)
    # adults
    record.append(agemembers(18, 200, person, households[person.family_id]))
    # sex
    record.append(person.isfemale())
    
    record = [str(j) for j in record]
    file.write((",").join(record) + "\n")

with open("selected.csv", mode= "w", encoding= "latin-1") as file:
  file.write("""parcial,parti,edad,edad2,escolaridad,casada,N(0_5),N(6_17),D[2_5],D[6_9],D[10_49],D[50_199],D[200+],D[minas],D[manu],D[EGA],D[constru],D[comercio],D[transporte],D[serv fin],D[servicios],Log_salario,nlingreso,N(18+),mujer""" + "\n")
  for key,person in agents.items():
    if person.part == "1" and person.isfemale() == 1 and person.parcial() != "." and person.lnwage() != "." and person.school != '' and not("." in person.dummy_nworkers()) and not("." in person.which_industry()):
      record = []
      # dependent variable
      record.append(person.parcial())
      # parti
      record.append(person.part)
      # age
      record.append(person.age)
      # age^2
      record.append(person.age*person.age)
      # school
      record.append(person.school)
      # ismarried
      record.append(person.ismarried())
      # children 0-5
      record.append(agemembers(0, 5, person, households[person.family_id]))
      # children 6-17
      record.append(agemembers(6, 17, person, households[person.family_id]))
      # trabajadores
      record = record + person.dummy_nworkers()
      # industry
      record = record + person.which_industry()
      # salary ln
      record.append(person.lnwage())
      # nlincome
      record.append(person.nlincome)
      # adults
      record.append(agemembers(18, 200, person, households[person.family_id]))
      # sex
      record.append(person.isfemale())
      
      record = [str(j) for j in record]
      file.write((",").join(record) + "\n")



