from math import isinf

targetDict = {
    "AAPL": 30.09,
    "BAC": 14.67,
    "AXP": 12.54,
    "KO": 9.09,
    "CVX": 6.63,
    "OXY": 5.75,
    "KHC": 3.75,
    "MCO": 3.71,
    "CB": 2.46,
    "DVA": 1.79,
    "C": 1.25,
    "KR": 0.89,
    "VRSN": 0.81,
    "V": 0.78,
    "AMZN": 0.69,
    "MA": 0.63,
    "LSXMK": 0.55,
    "COF": 0.49,
    "NU": 0.49,
    "AON": 0.43,
    "ALLY": 0.41,
    "CHTR": 0.41,
    "TMUS": 0.29,
    "LSXMA": 0.28,
    "FWONK": 0.20,
    "LPX": 0.18,
    "LLYVK": 0.15,
    "FND": 0.14,
    "SIRI": 0.13,
    "ULTA": 0.10,
    # "HEI.A": 0.07,
    "LLYVA": 0.07,
    # "NVR": 0.03,
    "DEO": 0.01,
    "JEF": 0.01,
    # "LEN.B": 0.01,
    "LILA": 0.01,
    "SPY": 0.01,
    "VOO": 0.01,
    "BATRK": 0.01,
    "LILAK": 0.01,
}

pricesDict = {
    "AAPL": 225.89,
    "BAC": 39.67,
    "AXP": 254.05,
    "KO": 68.98,
    "CVX": 146.84,
    "OXY": 57.39,
    "KHC": 35.36,
    "MCO": 470.08,
    "CB": 274.03,
    "DVA": 152.17,
    "C": 62.03,
    "KR": 52.76,
    "VRSN": 182.81,
    "V": 266.47,
    "AMZN": 178.22,
    "MA": 466.98,
    "LSXMK": 22.67,
    "COF": 142.93,
    "NU": 14.45,
    "AON": 334.38,
    "ALLY": 42.77,
    "CHTR": 355.06,
    "TMUS": 197.58,
    "LSXMA": 22.68,
    "FWONK": 78.81,
    "LPX": 93.60,
    "LLYVK": 40.17,
    "FND": 107.25,
    "SIRI": 3.04,
    "ULTA": 377.06,
    # "HEI.A": 0.00,
    "LLYVA": 39.35,
    # "NVR": 0.00,      normaly 8854.82
    "DEO": 129.36,
    "JEF": 57.58,
    # "LEN.B": 0.00,
    "LILA": 9.73,
    "SPY": 559.61,
    "VOO": 514.35,
    "BATRK": 43.12,
    "LILAK": 9.78,
}

# dict to be written in
approxDict = {
    "AAPL": 1.00,
    "BAC": 1.00,
    "AXP": 1.00,
    "KO": 1.00,
    "CVX": 1.00,
    "OXY": 1.00,
    "KHC": 1.00,
    "MCO": 1.00,
    "CB": 1.00,
    "DVA": 1.00,
    "C": 1.00,
    "KR": 1.00,
    "VRSN": 1.00,
    "V": 1.00,
    "AMZN": 1.00,
    "MA": 1.00,
    "LSXMK": 1.00,
    "COF": 1.00,
    "NU": 1.00,
    "AON": 1.00,
    "ALLY": 1.00,
    "CHTR": 1.00,
    "TMUS": 1.00,
    "LSXMA": 1.00,
    "FWONK": 1.00,
    "LPX": 1.00,
    "LLYVK": 1.00,
    "FND": 1.00,
    "SIRI": 1.00,
    "ULTA": 1.00,
    # "HEI.A": 1.00,
    "LLYVA": 1.00,
    # "NVR": 1.00,
    "DEO": 1.00,
    "JEF": 1.00,
    # "LEN.B": 1.00,
    "LILA": 1.00,
    "SPY": 1.00,
    "VOO": 1.00,
    "BATRK": 1.00,
    "LILAK": 1.00,
}

qteDict = {
    "AAPL": 1,
    "BAC": 1,
    "AXP": 1,
    "KO": 1,
    "CVX": 1,
    "OXY": 1,
    "KHC": 1,
    "MCO": 1,
    "CB": 1,
    "DVA": 1,
    "C": 1,
    "KR": 1,
    "VRSN": 1,
    "V": 1,
    "AMZN": 1,
    "MA": 1,
    "LSXMK": 1,
    "COF": 1,
    "NU": 1,
    "AON": 1,
    "ALLY": 1,
    "CHTR": 1,
    "TMUS": 1,
    "LSXMA": 1,
    "FWONK": 1,
    "LPX": 1,
    "LLYVK": 1,
    "FND": 1,
    "SIRI": 1,
    "ULTA": 1,
    # "HEI.A": 1,
    "LLYVA": 1,
    # "NVR": 1,
    "DEO": 1,
    "JEF": 1,
    # "LEN.B": 1,
    "LILA": 1,
    "SPY": 1,
    "VOO": 1,
    "BATRK": 1,
    "LILAK": 1,
}

def verifyDictsCorrespondance():
    for key in targetDict.keys():
        if key not in pricesDict:
            print("Key " + key + " not found in pricesDict")
            return False
        if key not in approxDict:
            print("Key " + key + " not found in approxDict")
            return False
        if key not in qteDict:
            print("Key " + key + " not found in qteDict")
            return False
    return True

# calculate the repartition at each adjustment of all the quantities
def calculateRepartition():
    #calculate the total value
    totalValue = 0
    for key, value in pricesDict.items():
        totalValue += value * qteDict[key]

    #calculate the approx repartition
    for key in qteDict.keys():
        approxDict[key] = round((pricesDict[key] * qteDict[key]) / totalValue * 100, 2)

#  approx%  |  target%
#-----------|-----------
#   oldQte  | **betterTargetQte**
# returns the new quantity or -1 if no change
# the best quantity is temporary since the other will change the repartition each time a value in qteDict is updated,
# this is why we need to iterate until no change is made
def calculateQuantity(key):
    actualQte = qteDict[key]
    if (approxDict[key] == 0):
        approxDict[key] = 0.01
    newQte = qteDict[key] * targetDict[key] / approxDict[key]
    if isinf(newQte):
        newQte = actualQte + 1 if newQte > actualQte else actualQte - 1
    else:
        newQte = round(newQte)
    if newQte == 0:
        newQte = 1
    if newQte != actualQte:
        return newQte
    return -1


# fill the final dictionary with the best approximation of the target repartition with a least number of quantities
def fillLeastApprox():
    updateNumber = 1
    tolerance = 0.1
    maxIteration = 100
    iterations = 0
    calculateRepartition()
    while updateNumber != 0 and iterations < maxIteration:
        updateNumber = 0
        for key in list(approxDict.keys()):
            newQte = calculateQuantity(key)
            if newQte != -1:
                qteDict[key] = newQte
                updateNumber += 1
        calculateRepartition()
        iterations += 1

def main():
    if not verifyDictsCorrespondance():
        return
    fillLeastApprox()
    print(qteDict)

if __name__=="__main__":
    main()
