from records import Coronavirus

def covid19_today():
    parser = Coronavirus()
    
    cases_today = parser.getTotalCases()
    cases_yesterday = parser.getYesterdayTotalCases()

    factor = cases_today/cases_yesterday

    cases = cases_today
    for i in range(1, 8):
        cases = cases * factor
        
    cases_week = round(cases)

    return cases_today, cases_yesterday, factor, cases_week
