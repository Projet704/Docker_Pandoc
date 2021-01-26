import requests, sys, json, os, subprocess, pypandoc

for arg in sys.argv: 
    1
    print(arg)

def read_json(file):
    with open(file) as f:
        data = json.load(f)
    return data



test = read_json(arg)
print(test['url'])
subprocess.run(["git", "clone",test['url']])

id = test['id']
print(id)
print(os.getcwd())
path  = os.getcwd()+"/"+id+"/"
print(path)
list = os.listdir(path)
print(list)
i = 0
while list[i] != test['file']:
	i+=1
print(list)
fichier = list[i]
path2 = path+fichier

output = pypandoc.convert_file(path2, 'docx', outputfile="somefile.docx")
print(output)
test['etat'] = 'done'
print(test)

