import numpy as np
import module as m
import matplotlib.pyplot as plt

comp = ["GAZP", "TATN", "SBER", "VTBR", "ALRS", "AFLT", "HYDR"]

def CopCount(date, prise):
    cop = {}
    for i in date:
        k = date[i][0][0] * prise[i][0][0]
        cop.update({i: k})
    prop = {}
    sum = 0
    for i in cop:
        sum += cop[i]
    for i in cop:
        prop.update({i: (cop[i]/sum)})
    return prop

def CorCoef(date):
    coef = {}
    prise = {}
    for i in date:
        comp_prise = []
        for j in range(len(date[i])):
            comp_prise.append(date[i][j][0])
        prise.update({i: comp_prise})
    for i in prise:
        cor = {}
        comp_1 = np.array(prise[i])
        for j in prise:
            if i != j:
                comp_2 = np.array(prise[j])
                k = np.corrcoef(comp_1, comp_2)
                cor.update({j: abs(k[0][1])})
        cor_sorted = sorted(cor.items(), key=lambda x: x[1])
        cor = dict(cor_sorted)
        coef.update({i: cor})
    #print(coef)
    return coef

def Buy(user, data, prise):
    money = user["cash"]
    person = user["name"]
    company = []
    profit = 0
    purch = {}
    #print(person)

    if person == 'anatoly':
        count = 0
        for i in data:
            count_2 = 0
            if count != 3:
                for j in data[i]:
                    if count_2 != 1:
                        company.append(i)
                        if prise[j][0][0] - prise[j][1][0] > 0:
                            #print(data[i][j], i, j, prise[j][0][0] - prise[j][1][0])
                            company.append(j)
                        count_2 += 1
                        #print(count_2)
                    else:
                        break
                count += 1
            else:
                break
        #print(company)
    if person == 'boris':
        count = 0
        #print(data)
        for i in data:
            count_2 = 0
            if count != 3:
                for j in data[i]:
                    if count_2 != 1:
                        company.append(i)
                        if prise[j][0][0] - prise[j][1][0] > 0:
                            company.append(j)
                        count_2 += 1
                    else:
                        break
                count += 1
            else:
                break
    if person == 'evgeny':
        n = CopCount(m.Kapit(comp), prise)

        for i in data:
            spend = money*n[i]
            count = 0
            while spend >= prise[i][0][0]:
                count += 1
                profit += prise[i][1][0]
                spend -= prise[i][0][0]
            purch.update({i: count})
        print(profit, purch)
        return profit, purch

    if person != "evgeny":
        for i in company:
            spend = money / len(company)
            count = 0
            #print(i, prise[i][1][0], prise[i][0][0])
            while spend >= prise[i][0][0]:
                count += 1
                profit += prise[i][1][0]
                spend -= prise[i][0][0]
            purch.update({i: count})
        print(profit, purch)
        return profit, purch


def Count():
    anatoly = {'name': 'anatoly', 'cash': 10000000, 'info': {}}
    boris = {'name': 'boris', 'cash': 10000000, 'info': {}}
    evgeny = {'name': 'evgeny', 'cash': 10000000, 'info': {}}
    anatoly_profit = []
    boris_profit = []
    evgeny_profit = []


    #Получение стартовой информации
    test_2 = m.newDate(comp, m.Data(2017, 2), m.Data(2017, 3))
    start = CorCoef(test_2[0])
    prise = test_2[1]

    answ1 = Buy(anatoly, start, prise)
    answ2 = Buy(boris, start, prise)
    answ3 = Buy(evgeny, start, prise)
    anatoly["cash"] = answ1[0]
    anatoly_profit.append(answ1[0])
    anatoly["info"].update(answ1[1])
    boris["cash"] = answ2[0]
    boris_profit.append(answ2[0])
    boris.update(answ2[1])
    evgeny["cash"] = answ3[0]
    evgeny_profit.append(answ3[0])
    evgeny.update(answ3[1])
    print(anatoly_profit)

    date = [1, 0]
    for i in range(8):
        info = m.newDate(comp, m.Data(2017 + date[0], date[1]), m.Data(2017 + date[0],  date[1] + 3))
        if date[1] >= 9:
            date[1] += -12
            date[0] += 1
        date[1] += 3
        info_coef = CorCoef(info[0])
        answ_1 = Buy(anatoly, info_coef, prise)
        answ_2 = Buy(boris, info_coef, prise)
        answ_3 = Buy(evgeny, info_coef, prise)
        anatoly["cash"] = answ_1[0]
        anatoly_profit.append(answ_1[0])
        anatoly["info"].update(answ_1[1])
        boris["cash"] = answ_2[0]
        boris_profit.append(answ_2[0])
        boris.update(answ_2[1])
        evgeny["cash"] = answ_3[0]
        evgeny_profit.append(answ_3[0])
        evgeny.update(answ_3[1])
        print(anatoly)
    return anatoly_profit, boris_profit, evgeny_profit
stat = Count()

graph1 = plt.plot(stat[0])
graph2 = plt.plot(stat[1])
graph3 = plt.plot(stat[2])
plt.show()
