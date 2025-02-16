

import re

s1 = 'This is  double  spaced.'
s2 = 'Double  then   triple   spaces.'
s3 = 'This      has          lots.'

clean_s1 = re.sub(r'\s+',' ',s1)
clean_s2 = re.sub(r'\s+',' ',s2)
clean_s3 = re.sub(r'\s+',' ',s3)

print(clean_s1)
print(clean_s2)
print(clean_s3)
