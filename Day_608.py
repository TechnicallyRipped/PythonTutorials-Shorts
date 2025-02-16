

from collections import UserList

class TR_list(UserList):
    def change_to_strings(self):
        self.data = [str(item) for item in self.data]

x = TR_list([1,2,3])

x.append(4)
x.change_to_strings()

print(x)







