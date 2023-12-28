from datetime import date



from erori.repo_error import RepoError
from erori.validation_error import ValidError
filtru_text=""
filtru_pret=-1

class UI:
    def __init__(self,service):
        self.__service=service
        self.__comenzi={"adauga_tractor":self.adauga_tractor,
                        "sterge_tractoare":self.sterge_tractoare,
                        "filtreaza":self.filtreaza

        }
    def printeaza(self):
        lista=self.__service.get_all()
        for i in lista:
            print(i)
    def adauga_tractor(self):
        if len(self.__params)!=5:
            print("numar parametrii invalid")
            return
        id=int(self.__params[0])
        denumire=self.__params[1]
        pret=int(self.__params[2])
        model=self.__params[3]
        data=self.__params[4]
        self.__service.adauga_tractor(id,denumire,pret,model,data)
    def sterge_tractoare(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid")
            return
        cifra=int(self.__params[0])
        print(self.__service.sterge_tractor(cifra))
    def filtreaza(self):
        global filtru_text
        global filtru_pret
        if len(self.__params) != 2:
            print("numar parametrii invalid")
            return
        filtru_text=self.__params[0]
        filtru_pret=int(self.__params[1])
        lista=self.__service.filtrare_tractoare_text(filtru_text,filtru_pret)
        return lista
    def run(self):
        global filtru_text
        global filtru_pret
        while True:
            comanda=input(">>>")
            comanda=comanda.strip()
            if comanda==" ":
                continue
            if comanda=="exit":
                return
            parti=comanda.split(",")
            nume_comanda=parti[0]
            self.__params=parti[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                    if filtru_pret!=-1 or filtru_text!="":
                        lista=self.__service.filtrare_tractoare_text(filtru_text,filtru_pret)

                        for item in lista:
                            if self.__service.verofica_data(item)==1:
                                print(f"{item.get_id()}", f"{item.get_denumire()}",f"{item.get_pret()}",f"{item.get_model()}",
                                             f"*{item.get_data()}")
                            else:
                                print(item)

                except ValueError:
                    print("Eroare UI :tip numeric invalid!")
                except ValidError as ve:
                    print(f"ValidError{ve}")
                except RepoError as re:
                    print(f"RepoError:{re}")
            else:
                print ("comanda invalida!")
