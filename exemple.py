###########################################
# TIPE : Truc Incroyable Provenant d'Erik #
###########################################
# Installation :
#   Dans cmd.exe ->
#      cd chemin/vers/python/Scripts/
#      pip3.6.exe install numpy matplotlib
#   Enjoy!
###########################################
# Usage :
# from TIPE import start
# class UnNomIci:
#
#       mon_coefficient = 5
#
#      def get(t):
#           """calculer ici les coordonnees du point, on peut utiliser
#            UnNomIci.mon_coefficient, il pourra etre modifié en temps réel"""
#           return x, y, z (ici les coordonnees du point)
# start(UnNomIci) # Demarre la visualisation

import math
from TIPE import start

class X:

    coef = 0.5
    autre_coef = 5
    def get(t):
        return (X.coef*math.cos(t)*t, X.coef*math.sin(t)*t, X.coef*((t-5)))


start(X)
