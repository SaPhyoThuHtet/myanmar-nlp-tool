import streamlit as st
import numpy as np
import pandas as pd
import re
import utilities

#import librosa
#from pydub import AudioSegment

st.sidebar.image(
    "images/peacock-3.png",
    width=200,
)
st.sidebar.markdown("<h3 style='text-align: center;'>NLP Tools</h3>", unsafe_allow_html=True)
select = pd.DataFrame()
select['topics'] = ['chracter-tokenization', 'syllable-tokenization', 'syllbreak-zawgyi', 'multilingual_semi_syllable_break', 'detect-email', 'burmese2braille(Muu Haung)', 'valid_parantheses']
option = st.sidebar.selectbox(
    '',select['topics'])


st.sidebar.write("Copyrights@SaPhyoThuHtet")

if (option == "valid_parantheses"):
    user_input = st.text_input("Input", "(aabb)]")
    result = utilities.valid_parantheses(user_input)
    st.write("Output:", result)
                               
if(option == "chracter-tokenization"):
    user_input = st.text_input("Input", "အမုန်းမပွားရဘူးနော်")
    result = re.sub(r"([^\s])",r"\1 ", user_input)   
    st.write("Output:",result)
    
if(option == "syllable-tokenization"):
    st.markdown("<h4 style='text-align: center;'>Syllable Tokenization</h4>", unsafe_allow_html=True)
    st.write("\n")
    st.write("Description: Syllable break for Burmese, Pali (Myanmar), Rakhine, Pa-Oh, Word break for English, Char break for other language")
    user_input = st.text_input("Input", "အမုန်းမပွားရဘူးနော်")
    result = re.sub(r"(([A-Za-z0-9]+)|[က-အ|ဥ|ဦ](င်္|[က-အ][့း]*[်]|္[က-အ]|[ါ-ှႏꩻ][ꩻ]*){0,}|.)",r"\1 ", user_input)    
    st.write("Output:",result)
    
if (option == 'syllbreak-zawgyi'):
    st.write("Description: Syllable break for Burmese in Zawgyi Encoding")
    user_input = st.text_input("Input", "သီဟိုဠ္မွ ဉာဏ္ႀကီးရွင္သည္ အာယုဝၯနေဆးၫႊန္းစာကို ဇလြန္ေဈးေဘး ဗာဒံပင္ထက္ အဓိ႒ာန္လ်က္ ဂဃနဏဖတ္ခဲ့သည္။ေဆာင္")
    result = re.sub(r'(ေ*ျ*ႀ*ၿ*ၾ*[က-အ|႐|ႏ|ဥ|ဦ|႒]([က-အ]့*္[့း]*|[ါ-ာ]|[ိ-ူ]|[ဲ-္]|်|[ြ-ှ]|[ၐ-ၽ]|[ႁ-ႎ]|[႑-႟]){0,}|.)',r'\1 ',user_input)
    st.write("Output:",result)
    
if (option == 'multilingual_semi_syllable_break'):
    
    st.markdown("<h4 style='text-align: center;'>Multilingual Semi_syllable Break</h4>", unsafe_allow_html=True)
    st.write("\n")
    st.write("Description: Semi-syllable-break for Tibetan, Telegu, Bengali, Sinhala, Tamil, Shan, Mon, Pali and Sanskrit, Sagaw Karen, Western Poh Karen, Eastern Poh Karen, Geba Karen, Kayah, Rumai Palaung, Khamathi Shan, Aiton and Phake, Burmese (Myanmar), Paoh, Rakhine Languages, Word break for English, Char break for other language")
    user_input = st.text_input("Input", "ཕྱི་ལོ་ ༢༠༡༦ ཟླ་ ༡༡ ཚེས་ ༩ ༸གོང་ས་༸སྐྱབས་མགོན་ཆེན་པོ་མཆོག་གིས་རིའི་སྲིད་འཛིན་གསར་པར་འཚམས་འདྲིའི་གསུང་འཕྲིན་སྩལ་བ། བོད་མིའི་བླ་ན་མེད་པའི་དབུ་ཁྲིད་སྤྱི་ནོར་༸གོང་ས་༸སྐྱབས་མགོན་ཆེན་པོ་མཆོག་གིས་ཨ་རིའི་སྲིད་འཛིན་གསར་པ་སྐུ་ཞབས་ཌོ་ནལ་ཊམ་མཆོག་ལ་འཚམས་འདྲི་གནང་འདུག དེ་ཡང་ཁ་ཉིན་ཨ་རིའི་སྤྱི་མཐུན་ཚོགས་པའི་སྲིད་འཛིན་འོས་མི་སྐུ་ཞབས་ Donald Trump མཆོག་ཨ་མི་རི་ཀའི་སྲིད་འཛིན་ ༤༥ པར་འདེམས་ཐོན་གྱིས་རྒྱལ་ཁ་ཐོབ་པ་དང་བསྟུན།  ཁ་སང་ཚེས་ ༩ ཉིན་༸གོང་ས་༸སྐྱབས་མགོན་ཆེན་པོ་མཆོག་གིས་སྲིད་འཛིན་མཆོག་ལ་འཚམས་འདྲི་བསྩལ་བའི་ནང་། వికీపీడియా ఎవరైనా రాయదగిన స్వేచ్ఛా విజ్ఞాన సర్వస్వము উত্তরবঙ্গ থেকে দক্ষিণবঙ্গ, সারা বাংলার প্রতিটি কোণের খবর জানতে চোখ রাখুন বাংলা NEWJ-এ।ඔබ සැමට නිදුක් නිරෝගී සුවය ලැබේවායි ප්‍රාර්ථනා කරමි. நீங்கள் அனைவரும் மகிழ்ச்சியாகவும் ஆரோக்கியமாகவும் இருக்க வாழ்த்துகிறேன். အားလုံးပဲ စိတ်ချမ်းသာ ကိုယ်ကျန်းမာကြပါစေ။ လိၵ်ႈတႆ, ပအိုဝ်")
    result = utilities.multilingual_semi_syllable_break(user_input)
    st.write("Output:", result)
    
if(option == "detect-email"):
     user_input = st.text_input("Input", "ဒီနေ့တော့ phyothuhtet39@gmail.com ဆီကို mail  ပို့ရမယ်။ နေဉီး သူက Microsoft Mail phyothuhtet@studentambassadors.com ကို သုံးတာလားမေးကြည့်ပါဦး။ ငါ ayethida89.young@utycc.edu.mm  ကနေ ပို့လိုက်မယ်။")
     emails = re.findall(r'[\w\.]+@[\w]+(?:\.[\w]+)+', user_input.strip())
     st.write("Emails:",";".join(sorted(emails)))
        
if (option == 'burmese2braille(Muu Haung)'):
     st.markdown("<h4 style='text-align: center;'>Burmese 2 Braille (Mu Haung)</h4>", unsafe_allow_html=True)
     st.write("\n")
     dictionary = {'က': '⡁', 'ခ': '⢈', 'ဂ': '⠛', 'ဃ': '⠟', 'င': '⡈', 'စ': '⡌', 'ဆ': '⡤', 'ဇ': '⠵', 'ဈ': '⣌', 'ည': '⠷', 'ဋ': '⠳', 'ဌ': '⠻', 'ဍ': '⠾', 'ဎ': '⠿', 'ဏ': '⡬', 'တ': '⠞', 'ထ': '⠚', 'ဒ': '⠙', 'ဓ': '⠋', 'န': '⠝', 'ပ': '⡖', 'ဖ': '⠰', 'ဗ': '⢉', 'ဘ': '⠃', 'မ': '⡉', 'ယ': '⠽', 'ရ': '⠗', 'လ': '⠇', 'ဝ': '⠺', 'သ': '⠹', 'ဟ': '⠓', 'ဠ': '⠸', 'အ': '⠣', 'ဉ': '⠧', 'ဤ': '⠰⠪', '၍': '⠯', '၏': '⠕', '၌': '⠦', '၎င်း': '⠬', '၊': '?', '။': '?', 'ာ': '⠁', 'ါ': '⠎', 'ိ': '⠊', 'ီ': '⠪', 'ု': '⠑', 'ူ': '⠥', 'ေ': '⠱', 'ဲ': '⠡', '?': '⠴', 'ံ': '⠉', 'င်္': '⡈⠄⠤', 'ျ': '⠔', 'ဥ': '⠰⠑', 'ဦး': '⠰⠑⠪⠆', 'ဧ': '⠰⠱', 'ဣ': '⠰⠊', 'ြ': '⠢', '်': '⠄', 'ွ': '⠜', 'ှ': '⠭', '့': '⠂', '္': '⠤', 'း': '⠆'}
     user_input = st.text_input("Input","မသန်ပေမယ့်စွမ်းသည်")
     user_input = re.sub(r'([က-အ])([ံ]|[ါ-ဲ]|[က-အ]်)',r'\1အ\2',user_input.strip())
     user_input = re.sub(r'([က-အ]([ျ-ှ]){1,})',r'\1အ',user_input);
     #user_input = re.sub(r'(([က-အ])([ွ])(ှ)အံ)',r'\1\3အံ\2',user_input);
     to_normal =  re.sub(r'([က-အ][ျ-ှ]{1,})အ',r'\1', user_input);
     to_normal =  re.sub(r'([က-အ])အ([ံ]|[ါ-ဲ]|[က-အ]်)',r'\1\2', to_normal)
    
     result = ""
     for i in user_input:
        if (i in dictionary.keys()):
            result += dictionary[i]
        else:
            result += i
            
     st.write("Muu Haung:", user_input)
     st.write("Back to Normal(Used RE):", to_normal)
     st.write("Output:", result)
    
    
