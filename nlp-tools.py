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
select['topics'] = ['time-domain', 'frequency-domain']
option = st.sidebar.selectbox(
    '',select['topics'])

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(selected_filename)

if(option == "time-domain"):
    filename = file_selector()
    
    
if(option == "frequency-domain"):
    st.markdown("<h4 style='text-align: center;'>Syllable Tokenization</h4>", unsafe_allow_html=True)
    st.write("\n")
    st.write("Description: Syllable break for Burmese, Pali (Myanmar), Rakhine, Pa-Oh, Word break for English, Char break for other language")
    user_input = st.text_input("Input", "အမုန်းမပွားရဘူးနော်")
    result = re.sub(r"(([A-Za-z0-9]+)|[က-အ|ဥ|ဦ](င်္|[က-အ][့း]*[်]|္[က-အ]|[ါ-ှႏꩻ][ꩻ]*){0,}|.)",r"\1 ", user_input)    
    st.write("Output:",result)
    
           
