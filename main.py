from business.service import Service
from interfata.file_repo import FileRepo
from prezentare.consola import UI
from validare.valid import Validator

if __name__ == '__main__':
    calea="fisier_text.txt"
    repo=FileRepo(calea)
    validare=Validator()
    service=Service(validare,repo)
    ui=UI(service)
    ui.printeaza()
    ui.run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
