# -*- coding: utf-8 -*-
"""FinalAccuracy_Code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qSzvyuypHtIP1HbQ2li1D6bWs4vwjCCd
"""

import ast
import json

with open('/content/output.json') as f:
    data = f.read()
res = ast.literal_eval(data)
print(res)

with open('/content/train_closed.json') as f:
  data = f.read()
original_question = ast.literal_eval(data)
print(original_question)

accuaracy = 0
for i in range(len(res)):
  if 'response' in res[i]:
    if res[i]['response'] == 'NoResponse':  
      for j in range(len(original_question)):
        if original_question[j]['id'] == res[i]['id']:
          try:
            if len(original_question[j]['choices']!=0):
              res[i]['response'] = 'D'
              if original_question[j]['answer'] =='D':
                accuaracy = accuaracy +1
            else:
              res[i]['response'] = 0
              if original_question[j]['answer'] ==0:
                accuaracy = accuaracy +1
          except:
            continue
    else:
      for j in range(len(original_question)):
        if original_question[j]['id'] == res[i]['id']:
          if res[i]['response'][0] == 'C':
            if 'ChoiceResponse('+original_question[j]['answer']+')' ==res[i]['response']:
              accuaracy = accuaracy +1
          else:
            if 'NumericResponse('+str(original_question[j]['answer'])+')' ==res[i]['response']:
              accuaracy = accuaracy +1

accuaracy = accuaracy/len(res)

print('Accuarcy',accuaracy)

with open('/content/Final_Output.json', 'w') as outfile:
    json.dump(res, outfile,indent=2)



