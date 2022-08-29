import re
import streamlit as st

def multilingual_semi_syllable_break(user_input):
  # Multilingual Semi Syllabe Break (Sinhala, Tamil, Shan, Mon, Pali and Sanskrit, Sagaw Karen, Western Poh Karen, Eastern Poh Karen, Geba Karen, Kayah, Rumai Palaung, Khamathi Shan, Aiton and Phake, Burmese (Myanmar), Paoh, Rakhine Languages)
  result = re.sub(r"([a-zA-Z]+|[අ-෉][්-෥ෲ-ෳ඀-඄ි]{0,}|[அ-஽][஀-஄ா-௏ௗ]{0,}|[က-ဪဿ၌-၏ၐ-ၕၚ-ၝၡၥၦၮ-ၰၵ-ႁႎ႐-႙႟][ါ-ှၖ-ၙၞ-ၠၢ-ၤၧ-ၭၱ-ၴႂ-ႍႏႚ-႞]{0,}|.)",r"\1--------------", user_input)
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
   
    
     
            
      
   
        
  
  

  
