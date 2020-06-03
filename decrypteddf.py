import base64
import pandas as pd
import io
from io import BytesIO




text_file = open("Licensefinal.b64", "rb")
base64_encoded = text_file.read()
text_file.close()

decrypted=base64.b64decode(base64_encoded)



toread = io.BytesIO()
toread.write(decrypted)  # pass your `decrypted` string as the argument here
toread.seek(0)  # reset the pointer
df = pd.read_excel(toread)
print(df)
