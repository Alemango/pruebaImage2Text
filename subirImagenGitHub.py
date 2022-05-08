from git import Repo

repo = Repo(r"C:\Users\aleal\OneDrive\Documentos\Prog\pruebaImage2Text")
print(repo.git.status())
repo.git.add(r"C:\Users\aleal\OneDrive\Documentos\Prog\pruebaImage2Text\subirImagenGitHub.py")
print(repo.git.status())