import pandas as pd
import DateTime
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

text_file = open("Adminaccess.b64", "rb")
base64_encoded = text_file.read()
text_file.close()

decrypted=base64.b64decode(base64_encoded)
toread = io.BytesIO()
toread.write(decrypted)  # pass your `decrypted` string as the argument here
toread.seek(0)  # reset the pointer
df = pd.read_excel(toread,usecols=['Time','Car-No.','Status'])
print(df)
