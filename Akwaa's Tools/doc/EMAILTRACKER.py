import subprocess

def check_email(email):
    result = subprocess.run(["holehe", email], capture_output=True, text=True)
    response = result.stdout
    response = response.replace("[+]", "Utilisé pour ")
    response = response.replace("[-]", "Libre pour ")
    response = response.replace("[x]", "NA pour ")
    return response

email = input("Entrez l'email : ")
response = check_email(email)
print(response)
