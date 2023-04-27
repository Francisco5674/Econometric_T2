import data_manager

def agemembers(minage, maxage, person, family):
    n = 0
    for key,member in family.members.items():
      if minage <= member.age <= maxage:
        n = n + 1
      else:
        pass

    return n 

