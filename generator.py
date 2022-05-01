import MyQR
from MyQR import myqr
import os
import base64

f = open('1.csv', 'r')
lines = f.read().split('\n')
print(lines)

for i in range(0, len(lines)):
    data = lines[i].encode()
    name = base64.b64encode(data)
    version, level, qr_name = MyQR.myqr.run(
        str(name),
        level='H',
        colorized=True,
        version=1,
        contrast=1.0,
        brightness=1.0,
        save_name=str(lines[i] + '.jpg'),
        save_dir=os.getcwd()
    )
