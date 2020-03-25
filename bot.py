import COVID19Py
import requests

def main():
    covid19 = COVID19Py.COVID19()
    latest = covid19.getLatest()
    locations = covid19.getLocations()
    location = covid19.getLocationByCountryCode("MX")
    changes = covid19.getLatestChanges()
    data = covid19.getAll()

    print(latest)
    print(location)
    print(changes)
    print(data)


if __name__ == '__main__':
    main()