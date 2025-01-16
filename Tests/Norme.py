from CheckerLib import *
import os

@AddTest("Norme")
class TestNorme(BaseTest):
    def __init__(self, id, *args, **kargs):
        super().__init__(id, *args, **kargs)

    def Init(self):
        return
    
    def Run(self):
        normeflag = ["-R","CheckForbiddenSourceHeader"]
        norme = True
        norme = CheckNorme(".",normeflag) and norme
        #Exemple de si vous voulez checker uniquement la libft et src :
        #norme = CheckNorme("libft",normeflag) and norme
        #norme = CheckNorme("src",normeflag) and norme
        return norme
    
    def PrintResult(self):
        return
    
    def Close(self):
        return True