import pandas as pd
import json

read_file = pd.read_csv(r'C:\Users\Admin\Downloads\Chandigarh Tourist Places\Tourist Place List.csv')


dictionary = read_file.to_json(r'C:\Users\Admin\Downloads\Chandigarh Tourist Places\Tourist Place List.json')



j = json.dumps(dictionary)

with open ('Tourist Places.json' , 'w') as f:
    f.write(j)
    f.close()



