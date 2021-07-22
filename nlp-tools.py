import streamlit as st
import numpy as np
import pandas as pd
import re

st.sidebar.image(
    "images/peacock-3.png",
    width=200,
)
st.sidebar.markdown("<h3 style='text-align: center;'>NLP Tools</h3>", unsafe_allow_html=True)

select = pd.DataFrame()
select['topics'] = ['chracter-tokenization', 'syllable-tokenization', 'detect-email']
option = st.sidebar.selectbox(
    '',select['topics'])

st.sidebar.write("Copyrights@SaPhyoThuHtet")

if(option == "chracter-tokenization"):
    user_input = st.text_input("Input", "ရွှံ့ပေါ်ရှဉ့်ပြေး ရှည့်မွှေး ရွှံ့မလူး")
    result = re.sub(r"([^\s])",r"\1 ", user_input)   
    st.write("Output:",result)
    
if(option == "syllable-tokenization"):
    st.markdown("<h4 style='text-align: center;'>Syllable Tokenization</h4>", unsafe_allow_html=True)
    st.write("\n")
    st.write("Description: Syllable break for Burmese, Pali (Myanmar), Rakhine, Pa-Oh), Word break for English, Char break for other language")
    user_input = st.text_input("Input", "ရွှံ့ပေါ်ရှဉ့်ပြေး ရှည့်မွှေး ရွှံ့မလူး")
    result = re.sub(r"(([A-Za-z0-9]+)|[က-အ|ဥ|ဦ](င်္|[က-အ][့း]*[်]|္[က-အ]|[ါ-ှႏꩻ][ꩻ]*){0,}|.)",r"\1 ", user_input)    
    st.write("Output:",result)
    
if(option == "detect-email"):
     user_input = st.text_input("Input", "ဒီနေ့တော့ phyothuhtet39@gmail.com ဆီကို mail  ပို့ရမယ်။ နေဉီး သူက Microsoft Mail phyothuhtet@studentambassadors.com ကို သုံးတာလားမေးကြည့်ပါဦး။ ငါ ayethida89.young@utycc.edu.mm  ကနေ ပို့လိုက်မယ်။")
     emails = re.findall(r'[\w\.]+@[\w]+(?:\.[\w]+)+', user_input.strip())
     st.write("Emails:",";".join(sorted(emails)))
