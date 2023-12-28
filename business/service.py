from datetime import date, datetime

from domain.domain import Tractor


class Service:
    def __init__(self,validator,file_repo):
        self.__validator=validator
        self.__file_repo=file_repo
    def get_all(self):
        return self.__file_repo.get_all()
    def adauga_tractor(self,id,denumire,pret,model,data):
        tractor=Tractor(id,denumire,pret,model,data)
        erori=self.__validator.validari(tractor)
        if erori=="":
            self.__file_repo.adauga(tractor)
        else:
            return erori
    def sterge_tractor(self,n):
        nr=0
        tractoare=self.__file_repo.get_all()
        for tractor in tractoare:
            pret=tractor.get_pret()
            aux=pret
            while aux>0:
                c=aux%10
                aux=aux/10
                if c==n:
                    self.__file_repo.sterge_tractor(tractor)
                    nr+=1
        return nr
    def filtrare_tractoare_text(self,text,pret):
        tractoare=self.__file_repo.get_all()

        lista_filtrata=[]
        if text!="":
            for tractor in tractoare:
                if tractor.get_denumire().rfind(text)!=-1:

                    if pret!=-1:
                        if tractor.get_pret()<pret:
                            lista_filtrata.append(tractor)

                    else:
                        lista_filtrata.append(tractor)

        else:
            for tractor in tractoare:
                    if tractor.get_pret() < pret:
                        if text != "":
                            if tractor.get_denumire().rfind(text)!=-1:
                                lista_filtrata.append(tractor)

                        else:
                            lista_filtrata.append(tractor)

        return lista_filtrata
    def verofica_data(self,tractor):

        data=date.today().strftime("%d:%m:%y")

        parti=data.split(":")
        zi= int(parti[0])
        luna=int(parti[1])

        an=int(parti[2])
        data_tractor=tractor.get_data()

        part1=data_tractor.split(":")
        zi1=int(part1[0])
        luna1=int(part1[1])
        an1=int(part1[2])

        if an>an1 :
            return 1
        elif an<an1:
            if luna>luna1:

                return 1
            elif luna<luna1:
                if zi1<zi:
                    return 1
                else: return 0

            elif luna1==luna:
                if zi1<zi:
                    return 1
                else: return 0

        elif an1==an:
            if luna>luna1:

                return 1
            elif luna<luna1:
                return 0
            elif luna1==luna:
                if zi1<zi:
                    return 1
                else: return 0




