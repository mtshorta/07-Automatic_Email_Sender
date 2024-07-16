import os

folder = ('/Users/mateushorta/Desktop/03-MAXbot/7 - Documentos Ther Sistemas Inovadores/Documentos legais comprobatorios')
patterns = ['1-THERIONTEC', '2-THERIONTEC', '3-THERIONTEC', '4-THERIONTEC', '5-THERIONTEC']

files = []
for file in os.listdir(folder):
    for pattern in patterns:
        if pattern in file:
            files.append(os.path.join(folder,file))


folder2 = ('/Users/mateushorta/Desktop')
patterns2 = ['SECULT', 'secult', 'Secult']

for file in os.listdir(folder2):
    for pattern in patterns2:
        if pattern in file:
            files.append(os.path.join(folder,file))


