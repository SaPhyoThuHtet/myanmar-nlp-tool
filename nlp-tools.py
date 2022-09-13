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
select['topics'] = ['chracter-tokenization', 'syllable-tokenization', 'syllable-tokenization-zawgyi', 'multilingual_semi_syllable_tokenization', 'detect-email', 'burmese2braille(Muu Haung)', 'valid-parantheses', 'remove-characters']
option = st.sidebar.selectbox(
    '',select['topics'])

if (option == "remove-characters"):
    st.write("Please types characters to remove, please use ||| signs to denote as a different char. E.g.မ|||ဝ")
    chars = st.text_input("Char Input:", "ည|||လ")
    text  = st.text_input("Text Input:", "ညအခါ လသာသာ ကစားမလား နားမလား")
    result = utilities.remove_chars(chars, text)
    st.write("Output:", result)

if (option == "valid-parantheses"):
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
    
if (option == 'syllable-tokenization-zawgyi'):
    st.write("Description: Syllable tokenizer for Burmese in Zawgyi Encoding")
    user_input = st.text_input("Input", "သီဟိုဠ္မွ ဉာဏ္ႀကီးရွင္သည္ အာယုဝၯနေဆးၫႊန္းစာကို ဇလြန္ေဈးေဘး ဗာဒံပင္ထက္ အဓိ႒ာန္လ်က္ ဂဃနဏဖတ္ခဲ့သည္။ေဆာင္")
    result = re.sub(r'(ေ*ျ*ႀ*ၿ*ၾ*[က-အၫ|႐|ႏ|ဥ|ဦ|႒]([က-အ]့*္[့း]*|[ါ-ာ]|[ိ-ူ]|[ဲ-္]|်|[ြ-ှ]|[ၐ-ၽ]|[ႁ-ႎ]|[႑-႟]){0,}|.)',r'\1 ',user_input)
    #new_rule = re.sub(r'([ေျႀၿၾ]*[က-ဪႏဿႎၐ-ၕၛ-ၝၡၦၮ-ၰၵ-ၽႁ႞-႟][]*[]*{0,}|.)', r'\1 ', user_input)
    st.write("Output:",result)
    #st.write("Output:",new_rule)
    
if (option == 'multilingual_semi_syllable_tokenization'):
    
    st.markdown("<h4 style='text-align: center;'>Multilingual Semi_syllable Tokenizer</h4>", unsafe_allow_html=True)
    st.write("\n")
    st.write("Description: Semi-syllable-break for Lao, Kannada, Oriya, Gujarati, Malayalam, Khmer, Telegu, Bengali, Sinhala, Tamil, Shan, Mon, Pali and Sanskrit, Sagaw Karen, Western Poh Karen, Eastern Poh Karen, Geba Karen, Kayah, Rumai Palaung, Khamathi Shan, Aiton and Phake, Burmese (Myanmar), Paoh, Rakhine Languages, Word break for English, Char break for other language")
    user_input = st.text_input("Input", "ພາສາລາວ ແມ່ນພາສາລັດຖະການຂອງ ສາທາລະນະລັດ ປະຊາທິປະໄຕ ປະຊາຊົນລາວ. ແລະເປັນພາສາແມ່ຂອງຄົນເຊື້ອຊາດລາວ ທັງຢູ່ພາຍໃນແລະຕ່າງປະເທດ. ພາສາລາວມີວັນນະຍຸດ ມີການປາກເວົ້າໃນພາກຕາເວັນອອກສຽງເໜືອຂອງປະເທດໄທແລະພາກຕາເວັນອອກສຽງເໜືອຂອງປະເທດກຳປູເຈຍ. ທາງລັດຖະບານປະເທດໄທມີການສະໜັບສະໜຸນໃຫ້ເອີ້ນພາສາລາວຖິ່ນໄທວ່າ ພາສາລາວຖິ່ນອີສານ(Lao), ವರೆಗೆ ಟಿಬಿಎಂ ಯಂತ್ರ ಈ ಸುರಂಗ ಕೊರೆಯುವುದನ್ನು ಯಶಸ್ವಿಗೊಳಿಸಿದೆ(Kannada), ଭୁବନେଶ୍ୱରର ମାଷ୍ଟର କ୍ୟାଣ୍ଟିନ ଛକରେ ଥିବା କୋଣାର୍କର ଘୋଡ଼ା ગુજરાતી શબ્દ ઘણાં સંદર્ભોમા વપરાય છે, જે નીચેનામાંનો એક અર્થ ધરાવી શકે છે വിക്കിപീഡിയ, ഒരു സ്വതന്ത്ര വിജ്ഞാനകോശംខ្មែរអ្នកបកប្រែអង់គ្លេសవికీపీడియాఎవరైనా రాయదగిన స్వేచ్ఛా విజ్ఞాన సర్వస్వము উত্তরবঙ্গ থেকে দক্ষিণবঙ্গ, সারা বাংলার প্রতিটি কোণের খবর জানতে চোখ রাখুন বাংলা NEWJ-এ।ඔබ සැමට නිදුක් නිරෝගී සුවය ලැබේවායි ප්‍රාර්ථනා කරමි. நீங்கள் அனைவரும் மகிழ்ச்சியாகவும் ஆரோக்கியமாகவும் இருக்க வாழ்த்துகிறேன். အားလုံးပဲ စိတ်ချမ်းသာ ကိုယ်ကျန်းမာကြပါစေ။ မႂ်ႇသုင်ၶႃႈ,နာꩻ အုံ‌‌ဟောဝ်နေဟောဝ်း။")
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
    
    
