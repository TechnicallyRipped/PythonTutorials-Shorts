


import win32com.client as win32

outlook = win32.Dispatch("Outlook.Application")

contacts_folder = outlook.GetNamespace('MAPI').GetDefaultFolder(10)

contact = contacts_folder.Items.Add()

contact.FirstName = "John"
contact.LastName = "Johnson"
contact.Email1Address = "johnjohnson@example.com"
contact.MobileTelephoneNumber = '8675309'

contact.Save()






































