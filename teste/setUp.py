import unittest

from business.service import Service
from domain.domain import Tractor
from interfata.file_repo import FileRepo
from validare.valid import Validator


class Testerepo(unittest.TestCase):
    def setUp(self):
        self.__calea=r"C:\Users\bianc\PycharmProjects\Furtos\fisier_test.txt"
        self.__goleste()
        self.__validare=Validator()
        self.__file_repo=FileRepo(self.__calea)
        self.__tractor1=Tractor(1,"lala",15,"auriu","12:03:2023")
        self.__file_repo.adauga(self.__tractor1)
    def __goleste(self):
        with open(self.__calea,"w") as f:
            pass
    def tearDown(self) :
        pass
    def test_adauga(self):
        self.assertEqual(self.__file_repo.size(),1)
    def test_get_all(self):
        lista=self.__file_repo.get_all()
        self.assertEqual(self.__file_repo.size(),1)
    def test_sterge(self):
        self.__file_repo.sterge_tractor(self.__tractor1)
        self.assertEqual(self.__file_repo.size(),0)
class TesteService(unittest.TestCase):
    def setUp(self):
        self.__calea = r"C:\Users\bianc\PycharmProjects\Furtos\fisier_test.txt"
        self.__goleste()
        self.__validare = Validator()
        self.__file_repo = FileRepo(self.__calea)
        self.__service=Service(self.__validare,self.__file_repo)
        self.__tractor1 = Tractor(1, "lala", 15, "auriu", "12:03:2023")



    def __goleste(self):
        with open(self.__calea,"w") as f:
            pass
    def tearDown(self) :
        pass
    def test_adauga(self):
        self.__service.adauga_tractor(1, "lala", 15, "auriu", "12:03:2023")
        lista=self.__service.get_all()
        self.assertEqual(len(lista),1)
    def test_get_all(self):
        lista = self.__service.get_all()
        self.assertEqual(len(lista), 0)
        self.__service.adauga_tractor(1, "lala", 15, "auriu", "12:03:2023")
        lista2 = self.__service.get_all()
        self.assertEqual(len(lista2), 1)
    def test_sterge_tractor(self):
        self.__service.adauga_tractor(1, "lala", 15, "auriu", "12:03:2023")
        lista2 = self.__service.get_all()
        self.assertEqual(len(lista2), 1)
        self.__service.sterge_tractor(5)
        lista1 = self.__service.get_all()
        self.assertEqual(len(lista1), 0)
        self.__service.adauga_tractor(1, "lala", 15, "auriu", "12:03:2023")
        lista3 = self.__service.get_all()
        self.assertEqual(len(lista3), 1)
        self.__service.sterge_tractor(2)
        lista4 = self.__service.get_all()
        self.assertEqual(len(lista4), 1)
    def test_filtrare(self):
        self.__service.adauga_tractor(1,"bucsa",12,"metalic","12:02:23")
        self.__service.adauga_tractor(2,"hajdi",13,"auriu","13:03:23")
        self.__service.adauga_tractor(3,"haide",16,"albastru","13:03:23")
        lista=self.__service.filtrare_tractoare_text("ha",16)
        self.assertEqual(len(lista),1)
        lista_2=self.__service.filtrare_tractoare_text("ha",17)
        self.assertEqual(len(lista_2),2)


class Testdomain(unittest.TestCase):

    def setUp(self):
        self.__calea = r"C:\Users\bianc\PycharmProjects\Furtos\fisier_test.txt"
        self.__goleste()
        self.__validare = Validator()
        self.__file_repo = FileRepo(self.__calea)
        self.__service = Service(self.__validare, self.__file_repo)
        self.__tractor1 = Tractor(1, "lala", 15, "auriu", "12:03:2023")
    def __goleste(self):
        with open(self.__calea,"w") as f:
            pass
    def tearDown(self) :
        pass
    def test(self):
        self.assertEqual(self.__tractor1.get_id(),1)
        self.assertEqual(self.__tractor1.get_denumire(),"lala")
        self.assertEqual(self.__tractor1.get_pret(),15)
        self.assertEqual(self.__tractor1.get_model(),"auriu")
        self.assertEqual(self.__tractor1.get_data(),"12:03:2023")


