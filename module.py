import requests

#Стартовые данные
def Kapit(comp):
    comp_kap = {}
    for i in comp:
        kap = requests.get('https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/'+
                           i  + '.json?iss.meta=off&marketdata.columns=SECID,ISSUECAPITALIZATION&securities.columns=ISSUESIZE')
        comp_kap.update({i: kap.json()["securities"]["data"]})
    return comp_kap

def newDate(comp, date_s, date_f):
    comp_date = {}
    comp_info = {}
    for i in comp:
        kat = requests.get('https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/'+
                           i  + '.json?from='+ date_s +'-01&till='+ date_f +'-01&history.columns=CLOSE&iss.meta=off')
        comp_date.update({i: (kat.json()["history"]["data"])})
    for i in comp_date:
        comp_info.update({i: [comp_date[i][0], comp_date[i][-1]]})
    return comp_date, comp_info

#Доп функции
def Data(year=2016, month=1):
    data = str(year) + "-" + str(month)
    return data





