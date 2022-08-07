# -*- coding: utf-8 -*-
"""
Created on Sat May  5 18:25:53 2018

@author: Richie
"""

import pandas as pd
from difflib import SequenceMatcher

#find the best matching string name in a list of known strings
def bestFitName(nameList, inputName, threshold):
    bestMatchName = ''
    maxScore = 0
    for knownName in nameList:
        score = SequenceMatcher(None, knownName.lower(), inputName.lower()).ratio()
        if score > maxScore:
            maxScore = score
            bestMatchName = knownName

    return bestMatchName if maxScore > threshold else 'NOMATCH ' + inputName





if __name__ == '__main__':
    data = pd.read_csv("C:/Users/Richie/Downloads/tastePredictionProject/Batch_4391393_batch_results.csv")
    data = data.iloc[:, 27:-2]
    nameList = ['mcdonalds', 'chick-fil-a', 'taco bell', 'kfc', 
                'olive garden', 'dominos', 'popeyes', 'wendys', 
                'outback', 'burger king', 'chipotle', 'five guys',
                'arbys', 'subway', 'cheesecake factory', 'pizza hut',
                'texas roadhouse', 'panera bread', 'starbucks', 'culvers',
                'red lobster', 'red robin', 'jack in the box', 'carls jr',
                'pf changs', 'zaxbys', 'in and out', 'sonic', 'dairy queen',
                'chilis', 'applebees', 'panda express', 'raising canes', 
                'bonefish grill']
    
    threshold = 0.75
    for col in range(4):
        for i,name in enumerate(data.iloc[:,col]):
            data.iloc[i,col] = bestFitName(nameList, name, threshold)
    
    print(data.iloc[:,1])
    
    data.to_csv('C:/Users/Richie/Downloads/tastePredictionProject/output.csv')

