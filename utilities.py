import re
import streamlit as st

def multilingual_semi_syllable_break(user_input):
  # Multilingual Semi Syllabe Break (Malayalam, Khmer, Bengali, Sinhala, Tamil, Shan, Mon, Pali and Sanskrit, Sagaw Karen, Western Poh Karen, Eastern Poh Karen, Geba Karen, Kayah, Rumai Palaung, Khamathi Shan, Aiton and Phake, Burmese (Myanmar), Paoh, Rakhine Languages)
  result = re.sub(r"([a-zA-Z]+|[അ-ഺ൏-ൡ൰-ൿ][ഀ-ഄ഻-഼ാ-ൎൢ-൥]{0,}|[ក-ឳ។-៚ៜ][ា-៓៝]{0,}|[అ-ఽౘ-ౡ౷౸-౿][ఀ-ఄా-౗ౢ-౥]{0,}|[অ-঻ড়-ৡৰ-৽][ঁ-঄়-৛ৢ-৥৾-৿্]{0,}|[අ-෉][්-෥ෲ-ෳ඀-඄ි]{0,}|[அ-஽][஀-஄ா-௏ௗ]{0,}|[က-ဪဿ၌-၏ၐ-ၕၚ-ၝၡၥၦၮ-ၰၵ-ႁႎ႐-႙႟][ါ-ှၖ-ၙၞ-ၠၢ-ၤၧ-ၭၱ-ၴႂ-ႍႏႚ-႞]{0,}|.)",r"\1💗💗💗", user_input)
  result = re.sub(r" +", " ", result)
  return result

def valid_parantheses(user_input):
  open_brackets = {"{", "(", "["}
  dic = {"}":"{", ")":"(", "]":"["}
  stack = []
  
  for i in user_input:
    if (i not in dic and i in open_brackets):
      stack.append(i)
    elif(i in dic):
      if (stack):
        val = stack.pop()
        if (val != dic[i]):
          return False
      else:
        return False
      
  if (stack):
            return False
  else:
            return True
   
  
 # n-grams:#
"""i = syllable_break(i)
    print(i)
    i = i.strip().split()
    
    original = k
    if (k>len(i)):
      k = len(i)

    prev = i[0:k]
    #print(prev)

    result = ''.join([str(element) for element in prev])
    #print(result)

    for j in range(k, len(i)):
      prev = prev[1:]+ [i[j]]
      #print(prev)
      result += " "+''.join([str(element) for element in prev])
      #print(result)

    print(result)
    print()"""
     
            
      
   
        
  
  

  
