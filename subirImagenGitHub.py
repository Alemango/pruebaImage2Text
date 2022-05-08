from git import Repo

repo = Repo(r"C:\Users\aleal\OneDrive\Documentos\Prog\pruebaImage2Text")
print(repo.git.status())
repo.git.add(r"C:\Users\aleal\OneDrive\Documentos\Prog\pruebaImage2Text\test2.png")
repo.git.commit(message="test with image")
repo.git.push()