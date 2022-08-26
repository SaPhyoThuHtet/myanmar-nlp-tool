import re
import streamlit as st

def multilingual_semi_syllable_break(user_input):
  # Multilingual Semi Syllabe Break (Sinhala, Tamil, Myanmar (Burmese), Shan, Rakhine, Mon, Paoh)
  result = re.sub(r"([a-zA-Z]+|[අ-෉][්-෥ෲ-ෳ඀-඄ි]{0,}|[அ-஽][஀-஄ா-௏ௗ]{0,}|[က-ဪဿ၌-၏ၐ-ၕၚ-ၝၡၥၦၮ-ၰၵ-ႁႎ႐-႙႟][ါ-ှၖ-ၙၞ-ၠၢ-ၤၧ-ၭၱ-ၴႂ-ႍႏႚ-႞]{0,}|[^ ])",r"\1--------------", user_input)
  result = re.sub(r" +", " ", result)
  return result

def valid_parantheses(user_input):
  open_brackets = {"{", "(", "["}
  dic = {"}":"{", ")":"(", "]":"["}
  stack = []
  
  for i in user_input:
    if (i not in dic and i in open_brackets):
      stack.append(i)
    else:
      if (stack):
        val = stack.pop()
        st.write("Val", val)
        st.write(dic[i])
        if (val != dic[i]):
          return False
      else:
        return False
      
  if (stack):
            return False
  else:
            return True
   
    
     
            
      
   
        
  
  

  
