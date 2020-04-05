from records import Coronavirus

def covid19_today():
    parser = Coronavirus()
    
    total_cases = parser.getTotalCases()
    new_cases = parser.getNewCases()
    total_death_cases = parser.getTotalDeaths()

    cases_yesterday = parser.getYesterdayTotalCases()
    
    parser.quit()

    factor = total_cases/cases_yesterday

    cases = total_cases
    for i in range(1, 8):
        cases = cases * factor
        
    cases_week = round(cases)

    return total_cases, cases_yesterday, factor, cases_week, new_cases, total_death_cases
