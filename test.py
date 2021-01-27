import requests, sys, json, os, subprocess, pypandoc, pexpect

for arg in sys.argv: 
    1
    print(arg)

def read_json(file):
    with open(file) as f:
        data = json.load(f)
    return data

info = read_json(arg)
subprocess.run(["git", "clone",info['url']])

id = info['id']
file = info['file']
path  = os.getcwd()+"/"+id+"/"
list = os.listdir(path)

i = 0
while list[i] != file:
	i+=1

fichier = list[i]
path2 = path+fichier

split = file.split('.')

pypandoc.convert_file(path2, 'docx', outputfile=path + split[0] + ".docx")

#Ajout du résultat pour l'envoyer au dépot distant
subprocess.Popen(['git', 'add', '.'], cwd=path)

#Commit du résultat à envoyer
subprocess.Popen(['git', 'commit' ,'-m', 'Push du résultat après traitement'], cwd=path)

#Push du projet, rentrée auto du username et du password
child = pexpect.spawn('git push', cwd=path)
child.expect([pexpect.TIMEOUT, "Username for 'https://github.com':"])
child.sendline("Projet704\n".encode())
child.expect([pexpect.TIMEOUT, "Password for 'https://Projet704@github.com':"])
child.sendline("MaxenceThomas51\n".encode())
child.read()



