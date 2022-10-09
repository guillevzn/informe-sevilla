import os
os.chdir(r'C:\Users\guill\Documents\GitHub\informe-sevilla')
os.system('Jupyter nbconvert Informe_de_Coyuntura_del_Municipio_de_Sevilla.ipynb --to html --template classic --no-input --no-prompt')
os.system('Jupyter nbconvert Prolegomenos.ipynb --to html --template classic --no-input --no-prompt')

os.system('Jupyter nbconvert Informe_de_Coyuntura_del_Municipio_de_Sevilla.ipynb --to pdf --no-input')
os.system('Jupyter nbconvert Prolegomenos.ipynb --to pdf --no-input --no-prompt')