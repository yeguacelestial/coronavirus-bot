# Graph
# x -> TIME
# y -> Personas infectadas
# Nuevos infectados en un dia (DELTA_I)

# D_I7 = I8 - I7
# D_I6 = I7 - I6

# In+1 = In(EP+1)
# F = EP + 1
# Las medidas son para intentar minimizar EP
# F = In+1 / In
# In+1 = In(EP+1)
# In+1 = In*F

# In+1 = 367 -> Infectados martes
# In = 317 -> Infectados lunes
# F-actual = 367 / 317
# F-actual =  1.1613

#I(miercoles) = I(martes) * F-actual
#I(miercoles) = 367 * 1.1613
#I(miercoles) = 426

from records import Coronavirus

def operations():
    parser = Coronavirus()
    I_np1 = int(parser.getTotalCases())
    I_n = int(parser.getYesterdayTotalCases())

    factor = I_np1/I_n

    return I_np1, I_n, factor
