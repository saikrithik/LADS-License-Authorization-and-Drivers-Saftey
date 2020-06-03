import pandas as pd
import datetime
import io
from io import BytesIO
import base64
import numpy as np
now= datetime.datetime.now()
today=now.day
month=now.month
year=now.year
#car-no = 'TS09BX2356'

#d=[[now,'TS19BX2345','Sleepiness-Detected']]
#df = pd.DataFrame(d,columns=['Time','Car-No.','Status'])

text_file = open("Adminaccess.b64", "rb")
base64_encoded = text_file.read()
text_file.close()
decrypted=base64.b64decode(base64_encoded)
toread = io.BytesIO()
toread.write(decrypted)  # pass your `decrypted` string as the argument here
toread.seek(0)  # reset the pointer
df = pd.read_excel(toread ,usecols=['Time','Car-No.','Status'])
d2=[[now,'TS09BX2356','Sleepiness-Detected']]
df2 = pd.DataFrame(d2, columns=['Time','Car-No.','Status'])
df = pd.concat([df, df2],sort=True)
bio = BytesIO()
writer = pd.ExcelWriter(bio, engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
bio.seek(0)
workbook = bio.read()
base64_encoded = base64.b64encode(workbook).decode('UTF-8')
text_file = open("Adminaccess.b64", "w")
n = text_file.write(base64_encoded)
text_file.close()                       
