import base64
import pandas as pd
import io
from io import BytesIO


data = open("License.xlsx", 'rb').read()
base64_encoded = base64.b64encode(data).decode('UTF-8')

base64_encoded = base64.b64encode(data).decode('UTF-8')
text_file = open("Licensefinal.b64", "w")
n = text_file.write(base64_encoded)
text_file.close()
