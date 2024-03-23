import streamlit as st
import numpy as np
import pandas as pd
import re
import utilities


# Streamlit User Interface

st.sidebar.image(
    "images/peacock-3.png",
    width=200,
)
st.sidebar.markdown("<h3 style='text-align: center;'>NLP Tool</h3>", unsafe_allow_html=True)

select = pd.DataFrame()
select['topics'] = ['chracter-tokenization', 'syllable-tokenization', 'syllable-tokenization-zawgyi', 'multilingual_semi_syllable_tokenization', 'syllable/character-n-grams', 'keywords-detection','detect-email', 'burmese2braille(Muu Haung)', 'zawgyi-unicode-detection','valid-parantheses', 'remove-characters']
option = st.sidebar.selectbox(
    '',select['topics'])
st.sidebar.markdown("Copyright (c) 2021 Sa Phyo Thu Htet")


# Tokenization
if(option == "chracter-tokenization"):
    st.markdown("<h4 style='text-align: center;'>Character Tokenization</h4>", unsafe_allow_html=True)
    st.write("\n")
    user_input = st.text_input("Input", "အမုန်းမပွားရဘူးနော်")
    result = re.sub(r"([^\s])",r"\1 ", user_input)   
    st.write("Output:",result)
    
if(option == "syllable-tokenization"):
    st.markdown("<h4 style='text-align: center;'>Syllable Tokenization</h4>", unsafe_allow_html=True)
    st.write("\n")
    st.write("Description: Syllable break for Burmese, Pali (Myanmar), Rakhine, Pa-Oh, Word break for English, Char break for other language")
    user_input = st.text_input("Input", "အမုန်းမပွားရဘူးနော်")
    #result = re.sub(r"(([A-Za-z0-9]+)|[က-အ|ဥ|ဦ](င်္|[က-အ][ှ]*[့း]*[်]|္[က-အ]|[ါ-ှႏꩻ][ꩻ]*){0,}|.)",r"\1 ", user_input)
    result = utilities.syllable_tokenization(user_input)
    st.write("Output:",result)
    
if (option == 'syllable-tokenization-zawgyi'):
    st.markdown("<h4 style='text-align: center;'>Burmese Syllable Tokenization (Zawgyi Encoding)</h4>", unsafe_allow_html=True)
    st.write("Description: Syllable tokenizer for Burmese in Zawgyi Encoding")
    user_input = st.text_input("Input", "ျမန္မာႏိုင္ငံ၊ (အဂၤလိပ္: Myanmar သို႔မဟုတ္ Burma (ဘားမား)) တရားဝင္အားျဖင့္ ျပည္ေထာင္စု သမၼတ ျမန္မာႏိုင္ငံေတာ္ (Republic of the Union of Myanmar) သည္ အေရွ႕ေတာင္အာရွရွိ ႏိုင္ငံတစ္ႏိုင္ငံျဖစ္သည္။ အေရွ႕ေတာင္အာရွ ကြၽန္းဆြယ္ေဒသတြင္ အႀကီးဆုံးႏိုင္ငံျဖစ္ၿပီး ၂၀၁၈ ခုႏွစ္အရ လူဦးေရ ၅၄ သန္းခန႔္ရွိသည္။[၅] ဘဂၤလားေဒ့ရွ္၊ အိႏၵိယ၊ တ႐ုတ္ျပည္သူ႔သမၼတႏိုင္ငံ၊ လာအို၊ ထိုင္းႏိုင္ငံ၊ ကပၸလီပင္လယ္ႏွင့္ ဘဂၤလားပင္လယ္ေအာ္တို႔ႏွင့္ ထိစပ္ေနသည္။ ျမန္မာႏိုင္ငံ၏ ၿမိဳ႕ေတာ္မွာ ေနျပည္ေတာ္ျဖစ္ၿပီး အႀကီးဆုံးၿမိဳ႕မွာ ရန္ကုန္ျဖစ္သည္။[၁]ျမန္မာႏိုင္ငံရွိ အေစာဆုံးအေျခခ်မႈမ်ားသည္ ပ်ဴၿမိဳ႕ျပႏိုင္ငံမ်ားႏွင့္ မြန္ဘုရင့္ႏိုင္ငံမ်ား၌ျဖစ္ၾကသည္။[၉] ေအဒီ ၉ရာစုခန႔္တြင္ ျမန္မာလူမ်ိဳးတို႔သည္ ဧရာဝတီျမစ္အနီး၌ ပုဂံျပည္ကိုတည္ေထာင္ခဲ့ၾကၿပီး ျမန္မာ့ယဥ္ေက်းမႈ၊ ျမန္မာဘာသာစကားစသည္တို႔ ေပၚေပါက္လာခဲ့သည္။ ပထမျမန္မာႏိုင္ငံေတာ္ ပုဂံျပည္သည္ မြန္ဂိုက်ဴးေက်ာ္စစ္ေၾကာင့္ က်ဆုံးခဲ့ရသည္။ ၁၆ ရာစု‌တြင္ ဒုတိယျမန္မာႏိုင္ငံေတာ္ ေတာင္ငူအင္ပါယာေပၚေပါက္လာခဲ့ၿပီး အေရွ႕ေတာင္အာရွသမိုင္း၏ အႀကီးဆုံးအင္ပါယာအျဖစ္ ေခတၱရပ္တည္ႏိုင္ခဲ့သည္။[၁၀] ၁၉ ရာစုတြင္ တတိယျမန္မာႏိုင္ငံေတာ္ ကုန္းေဘာင္အင္ပါယာသည္ မ်က္ေမွာက္ေခတ္ ျမန္မာႏိုင္ငံ၏ေဒသမ်ားကိုပါမက အာသံႏွင့္ မဏိပူရေဒသမ်ားကိုပါ အုပ္ခ်ဳပ္ႏိုင္ခဲ့သည္။ ၿဗိတိသွ်အင္ပါယာသည္ ျမန္မာႏိုင္ငံကို က်ဴးေက်ာ္စစ္မ်ားဆင္ႏႊဲၿပီး သိမ္းပိုက္ခဲ့သည္။ ဒုတိယကမာၻစစ္အတြင္း၌ ျမန္မာႏိုင္ငံကို ဂ်ပန္တို႔ကေခတၱသိမ္းပိုက္ထားခဲ့ၿပီး မဟာမိတ္ႏိုင္ငံတို႔က ျပန္လည္သိမ္းယူခဲ့သည္။ ၁၉၄၈ ခုႏွစ္တြင္ ျမန္မာႏိုင္ငံသည္ ၿဗိတိသွ်တို႔ထံမွ လြတ္လပ္ေရးကိုရရွိခဲ့သည္။ျမန္မာႏိုင္ငံသည္ အေရွ႕အာရွ ထိပ္သီးအစည္းအေဝး၊ ဘက္မလိုက္လႈပ္ရွားမႈ၊ အာဆီယံ၊ ဘင္းမ္စတက္စသည္တို႔၏ အဖြဲ႕ဝင္ႏိုင္ငံျဖစ္သည္။ ၿဗိတိသွ်အင္ပါယာလက္ေအာက္သို႔ က်ေရာက္ခဲ့ဖူးေသာ္လည္း ဓနသဟာယႏိုင္ငံမ်ား၏ အဖြဲ႕ဝင္ႏိုင္ငံမဟုတ္ေပ။ သဘာဝသံယံဇာတႂကြယ္ဝေသာ ႏိုင္ငံျဖစ္သည္သာမက ေနေရာင္ျခည္စြမ္းအင္အသုံးခ်ရန္အတြက္ အလားအလာေကာင္းမြန္သည္။[၁၁] ႏိုင္ငံ၏စီးပြားေရးအမ်ားစုကို ျမန္မာစစ္တပ္ႏွင့္ ၎၏ခ႐ိုနီမ်ားကခ်ဳပ္ကိုင္ထားသျဖင့္ စီးပြားေရးမညီမမွ်မႈမ်ားျပားသည္။[၁၂]")
    result = re.sub(r'(ေ*ျ*ႀ*ၿ*ၾ*ႂ*[က-အၫ|႐|ႏ|ဥ|ဦ|႒]([က-အ]ွ*့*္[့း]*|[ါ-ာ]|[ိ-ူ]|[ဲ-္]|်|[ြ-ှ]|[ၐ-ၪ]|်|[ၬ-ၽ]|[ႁ]|[ႃ-ႎ]|[႑]|[႓-႟]){0,}|.)',r'\1  ',user_input)
    st.write("Output:",result)
   
if (option == 'multilingual_semi_syllable_tokenization'):
    
    st.markdown("<h4 style='text-align: center;'>Multilingual Semi_syllable Tokenizer</h4>", unsafe_allow_html=True)
    st.write("\n")
    st.write("Description: Semi-syllable-break for Lao, Kannada, Oriya, Gujarati, Malayalam, Khmer, Telegu, Bengali, Sinhala, Tamil, Shan, Mon, Pali and Sanskrit, Sagaw Karen, Western Poh Karen, Eastern Poh Karen, Geba Karen, Kayah, Rumai Palaung, Khamathi Shan, Aiton and Phake, Burmese (Myanmar), Paoh, Rakhine Languages, Word break for English, Char break for other language")
    st.write("Here, semi-syllable does not refer to the minor syllable in phonology. Instead, it is new tokenization that does not break into a full syllable mode. Now I found that it is useful in keyword detection to reduce False Positive errors. (I may explain why keywords detection later)")
    st.write("The beauty of this tokenization would be you don't need to know much about the nature of the specific language.")
    user_input = st.text_input("Input", "ພາສາລາວ ແມ່ນພາສາລັດຖະການຂອງ ສາທາລະນະລັດ ປະຊາທິປະໄຕ ປະຊາຊົນລາວ. ແລະເປັນພາສາແມ່ຂອງຄົນເຊື້ອຊາດລາວ ທັງຢູ່ພາຍໃນແລະຕ່າງປະເທດ. ພາສາລາວມີວັນນະຍຸດ ມີການປາກເວົ້າໃນພາກຕາເວັນອອກສຽງເໜືອຂອງປະເທດໄທແລະພາກຕາເວັນອອກສຽງເໜືອຂອງປະເທດກຳປູເຈຍ. ທາງລັດຖະບານປະເທດໄທມີການສະໜັບສະໜຸນໃຫ້ເອີ້ນພາສາລາວຖິ່ນໄທວ່າ ພາສາລາວຖິ່ນອີສານ(Lao), ವರೆಗೆ ಟಿಬಿಎಂ ಯಂತ್ರ ಈ ಸುರಂಗ ಕೊರೆಯುವುದನ್ನು ಯಶಸ್ವಿಗೊಳಿಸಿದೆ(Kannada), ଭୁବନେଶ୍ୱରର ମାଷ୍ଟର କ୍ୟାଣ୍ଟିନ ଛକରେ ଥିବା କୋଣାର୍କର ଘୋଡ଼ା ગુજરાતી શબ્દ ઘણાં સંદર્ભોમા વપરાય છે, જે નીચેનામાંનો એક અર્થ ધરાવી શકે છે വിക്കിപീഡിയ, ഒരു സ്വതന്ത്ര വിജ്ഞാനകോശംខ្មែរអ្នកបកប្រែអង់គ្លេសవికీపీడియాఎవరైనా రాయదగిన స్వేచ్ఛా విజ్ఞాన సర్వస్వము উত্তরবঙ্গ থেকে দক্ষিণবঙ্গ, সারা বাংলার প্রতিটি কোণের খবর জানতে চোখ রাখুন বাংলা NEWJ-এ।ඔබ සැමට නිදුක් නිරෝගී සුවය ලැබේවායි ප්‍රාර්ථනා කරමි. நீங்கள் அனைவரும் மகிழ்ச்சியாகவும் ஆரோக்கியமாகவும் இருக்க வாழ்த்துகிறேன். အားလုံးပဲ စိတ်ချမ်းသာ ကိုယ်ကျန်းမာကြပါစေ။ မႂ်ႇသုင်ၶႃႈ,နာꩻ အုံ‌‌ဟောဝ်နေဟောဝ်း။")
    result = utilities.multilingual_semi_syllable_break(user_input)
    st.write("Output:", result)

if (option == "keywords-detection"):
     st.markdown("<h4 style='text-align: center;'>Keywords Detection</h4>", unsafe_allow_html=True)
     st.write("Please use ||| to delimt between different keywords")
     lexicon = st.text_input("Text Input:", "တောင်းစုတ်|||ပလုံးစုတ်|||punnets|||discard")
     text = st.text_input("Text Input:", "တောင်းစုတ် ပလုံးစုတ်သာ ပစ်ရိုးထုံးစံ ရှိသည်။ သားဆိုးသမီးဆိုးကို ပစ်ရိုးထုံးစံမရှိ။ Discard only bad baskets and punnets, not bad sons and daughters.")
     st.write("Detected Keywords:", utilities.keywords_detection(lexicon, text))
    
if (option == "zawgyi-unicode-detection"):
    
    st.markdown("<h4 style='text-align: center;'>Burmese Sentence Level Zawgyi Unicode Detection</h4>", unsafe_allow_html=True)
    st.write("Please Enter a sentence to determine it is written in Zawgyi or Unicode Encoding")
    text  = st.text_input("Text Input:", "အခြေအနေ နဲ့ အချိန်အခါ ကို အကျိုုးရှိစွာ အသုံးချ ခြင်း။")
    result = utilities.zawgyi_unicode_detection(text)
    st.write("Output:", result)
    
    
if (option == "syllable/character-n-grams"):
    st.markdown("<h4 style='text-align: center;'>Syllable/ Character n-grams with sliding windows approach</h4>", unsafe_allow_html=True)
    
    n      = st.number_input("How many grams do you want to apply:", 1)
    option = st.radio('Which type of Tokenization would you like to perform?', ('Syllable', 'Character'))

    text  = st.text_input("Text Input:", "ဝါဆိုဝါခေါင် ရေတွေကြီးလို့ သပြေသီးမှည့် ကောက်စို့ကွယ်")
    result = utilities.n_grams(n, text, option)
    st.write("Output:", result)
    
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
                               

    
if(option == "detect-email"):
     st.markdown("<h4 style='text-align: center;'>Email Detection</h4>", unsafe_allow_html=True)
     st.write("\n")
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

if (option == 'crawl'):
    utilities.crawl()
    
    
