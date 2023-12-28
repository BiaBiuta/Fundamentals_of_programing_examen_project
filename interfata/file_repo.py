from domain.domain import Tractor
from interfata.repo import Repo

class FileRepo(Repo):
    def __init__(self,calea):
        self.__calea=calea
        Repo.__init__(self)
    def __read_all_from_file(self):
        with open(self.__calea,"rt") as f:
            lines=f.readlines()
            self._tractoare.clear()
            for line in lines:
                line=line.strip()
                if line!="":
                    parti=line.split(",")
                    id=int(parti[0])
                    denumire=parti[1]
                    pret=int(parti[2])
                    model=parti[3]
                    data=parti[4]
                    tractor=Tractor(id,denumire,pret,model,data)
                    self._tractoare[id]=tractor
    def __write_all_from_file(self):
        with open(self.__calea,"w") as f:
            for tractor in self._tractoare.values():
                f.write(str(tractor)+"\n")
    def get_all(self):
        self.__read_all_from_file()
        return Repo.get_all(self)
    def adauga(self,tractor):
        self.__read_all_from_file()
        Repo.adauga(self,tractor)
        self.__write_all_from_file()
    def sterge_tractor(self,tractor):
        self.__read_all_from_file()
        Repo.sterge_tractor(self,tractor)
        self.__write_all_from_file()
    def size(self):
        self.__read_all_from_file()
        return Repo.size(self)
