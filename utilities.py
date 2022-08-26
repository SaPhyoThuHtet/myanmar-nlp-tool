# Multilingual Semi Syllabe Break (Sinhala, Tamil, Myanmar (Burmese), Shan, Rakhine, Mon, Paoh)
import re

def multilingual_semi_syllable_break(user_input):
  result = re.sub(r"([a-zA-Z]+|[අ-෉][්-෥ෲ-ෳ඀-඄ි]{0,}|[அ-஽][஀-஄ா-௏ௗ]{0,}|[က-ဪဿ၌-၏ၐ-ၕၚ-ၝၡၥၦၮ-ၰၵ-ႁႎ႐-႙႟][ါ-ှၖ-ၙၞ-ၠၢ-ၤၧ-ၭၱ-ၴႂ-ႍႏႚ-႞]{0,}|[^ ])",r"\1--------------", user_input)
  result = re.sub(r" +", " ", result)
  return result
