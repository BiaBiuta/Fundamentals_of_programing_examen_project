class Validator:
    def __init__(self):
        pass
    def validari(self,tractor):
        erori=""
        if tractor.get_pret()<0:
            erori+="pret invalid"
        if tractor.get_model()=="":
            erori+="model invalid"
        if tractor.get_denumire()=="":
            erori+="denumire invalida"
        return erori