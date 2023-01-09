import re
import streamlit as st
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

"""" Zawgyi Unicode Detection"""
@st.experimental_singleton
def load_zawgyi_unicode_detection_model():    
    model = tf.keras.models.load_model("model/zawgyi-unicode-detection/zawgyiunicodedetectionstreamlit.h5")
    return model

@st.experimental_singleton
def load_zawgyi_unicode_tokenizer():    
    with open('model/zawgyi-unicode-detection/tokenizer.pickle', 'rb') as file:
        tokenizer = pickle.load(file)
    return tokenizer

def zawgyi_unicode_detection(input:str)->str:
    st.write(input)
    st.write("Loading Tokenizer")
    zawgyi_unicode_tokenizer = load_zawgyi_unicode_tokenizer()
    model = load_zawgyi_unicode_detection_model()
    testing_sequences = zawgyi_unicode_tokenizer.texts_to_sequences([syllable_tokenization(input)])
    testing_padded = pad_sequences(testing_sequences,maxlen=150, truncating='post',padding='post')
    st.write("Unicode Encoding" if model.predict(testing_padded)[0][0]>=0.5 else "Zawgyi Encoding")



    
def syllable_tokenization(input:str)->str:
    return re.sub(r"(([A-Za-z0-9]+)|[က-အ|ဥ|ဦ](င်္|[က-အ][ှ]*[့း]*[်]|္[က-အ]|[ါ-ှႏꩻ][ꩻ]*){0,}|.)",r"\1 ", input.strip())

def character_tokenization(input:str)->str:
    return re.sub(r"([^\s])",r"\1 ", input)   

def n_grams(k, input, option):
    if (k <1):
      return ""
    
    if option == "Character":
        i = character_tokenization(input)
    else:
        i = syllable_tokenization(input)
        
    i = i.strip().split()
    
    if (k>len(i)):
      k = len(i)
    prev = i[0:k]
    
    result = ''.join([str(element) for element in prev])
    for j in range(k, len(i)):
      prev = prev[1:]+ [i[j]]
      result += " "+''.join([str(element) for element in prev])
    return result


@st.experimental_singleton
def loadModel(model_file):
    model = keras.models.load_model(model_file)
    return model
  
def zawgyiUnicodeDetection():
  model = loadModel()

def remove_chars(chars, text):
  # remove the user input characters
  text2 =""
  index = 0
  for i in range(len(text)):
    if (text[i] not in chars):
      text2 += text[i]
    
  return text2
      
      
def multilingual_semi_syllable_break(user_input):
  # Multilingual Semi Syllabe Break (Lao, Kannada, Oriya, Gujarati, Malayalam, Khmer, Bengali, Sinhala, Tamil, Shan, Mon, Pali and Sanskrit, Sagaw Karen, Western Poh Karen, Eastern Poh Karen, Geba Karen, Kayah, Rumai Palaung, Khamathi Shan, Aiton and Phake, Burmese (Myanmar), Paoh, Rakhine Languages)
  result = re.sub(r"([a-zA-Z]+|[຀-ຯຽ-໇ໜ-ໟ][ະ-ຼ່-໏]{0,}|[಄-಻ೞ-ೡ][಼ಀ-ಃಾ-ೝೢ-೥]{0,}|[ଅ-଻ଡ଼-ୡୱ][଼଀-଄ା-୛ୢ-୥]{0,}|[અ-઻ૐ-૟ૠ-ૡ૰ૹ][઀-઄઼ા-૏-ૣૺ-૿]{0,}|[അ-ഺ൏-ൡ൰-ൿ][ഀ-ഄ഻-഼ാ-ൎൢ-൥]{0,}|[ក-ឳ។-៚ៜ][ា-៓៝]{0,}|[అ-ఽౘ-ౡ౷౸-౿][ఀ-ఄా-౗ౢ-౥]{0,}|[অ-঻ড়-ৡৰ-৽][ঁ-঄়-৛ৢ-৥৾-৿্]{0,}|[අ-෉][්-෥ෲ-ෳ඀-඄ි]{0,}|[அ-஽][஀-஄ா-௏ௗ]{0,}|[က-ဪဿ၌-၏ၐ-ၕၚ-ၝၡၥၦၮ-ၰၵ-ႁႎ႐-႙႟][ါ-ှၖ-ၙၞ-ၠၢ-ၤၧ-ၭၱ-ၴႂ-ႍႏႚ-႞ꩻ]{0,}|.)",r"\1.....", user_input)
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
     
            
      
   
        
  
  

  
