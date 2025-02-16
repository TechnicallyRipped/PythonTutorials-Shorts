

import win32com.client as win32

outlook = win32.Dispatch('Outlook.Application')
email = outlook.CreateItem(0)
email.Subject = 'Test'
email.BodyFormat = 3
email.Body = "Wow, much text"
email.To = 'test@test.com'
# email.Send()
email.Display()
















































