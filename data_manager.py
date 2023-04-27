from family import Family,Person
import csv

families = {}
persons = {}

with open("muestra06.csv", 'r', encoding="latin-1") as file:
  reader = csv.reader(file, delimiter="\t")
  person_id = 1
  for line in reader:
    # id de la familia
    family_id = int(line[25])

    # edad
    age = line[5]
    if age == "Menos de un año":
      age = 0
    else:
      age = int(age)

    # sexo
    sex = line[4]

    # participacion laboral
    part = line[22]

    # salario
    wage = line[22]

    # rol
    rol = line[3]

    # industria
    industry = line[16]

    #school
    school = line[15]

    # married
    married = line[6]

    # ingresos no laborales
    nlincome = int(line[26])

    # numero de trabajadores
    numtrab = line[8]

    person = Person(person_id,
                    family_id,
                    rol,
                    age,
                    sex,
                    married,
                    numtrab,
                    industry,
                    wage,
                    school,
                    nlincome)
    
    persons[person_id] = person
    person_id = person_id + 1

    if family_id in families.keys():
      pass
      family = families[family_id]
      family.addmember(person)
      families[family_id] = family
    else:
      family = Family(family_id)
      family.addmember(person)
      families[family_id] = family
  
    #print(f"ready family {family_id} with person {person_id - 1}")

    

  

    
          

        

