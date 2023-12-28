from erori.repo_error import RepoError


class Repo:
    def __init__(self):
        self._tractoare={}
    def get_all(self):
        return [x for x in self._tractoare.values()]
    def adauga(self,tractor):
        if tractor.get_id() in self._tractoare:
            raise RepoError("tractor existent!")
        self._tractoare[tractor.get_id()]=tractor
    def sterge_tractor(self,tractor):
        if tractor.get_id() not in self._tractoare:
            raise RepoError("tractor inexistent!")
        del self._tractoare[tractor.get_id()]

    def size(self):
        return len(self._tractoare)