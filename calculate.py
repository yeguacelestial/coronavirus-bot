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

def covid19_today():
    parser = Coronavirus()
    
    cases_today = int(parser.getTotalCases())
    cases_yesterday = int(parser.getYesterdayTotalCases())

    factor = cases_today/cases_yesterday

    cases = cases_today
    for i in range(1, 8):
        cases = cases * factor
        print(cases)
        
    cases = int(cases)
    print(cases)

    return cases_today, cases_yesterday, factor
