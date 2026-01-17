

people = [('Joe',30),('Mike',28),
          ('Chris',38),('Kyle',29)]

sorted_p = sorted(people,
                  key=lambda x : x[1])

print(sorted_p)