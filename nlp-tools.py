import streamlit as st
import numpy as np
import pandas as pd
import re

select = pd.DataFrame()
select['topics'] = ['chracter-tokenization', 'syllable-tokenization', 'detect-email']
option = st.sidebar.selectbox(
    'Select one to explore',select['topics'])


user_input = st.text_input("Input", "ရွှံ့ပေါ်ရှဉ့်ပြေး ရှည့်မွှေး ရွှံ့မလူး")
if(option == "chracter-tokenization"):
    result = re.sub(r"([^\s])",r"\1 ", user_input)    
    st.write("Output:",result)
    
if(option == "syllable-tokenization"):
    result = re.sub(r"(([A-Za-z0-9]+)|[က-အ|ဥ|ဦ](င်္|[က-အ][့း]*[်]|္[က-အ]|[ါ-ှႏꩻ][ꩻ]*){0,}|.)",r"\1 ", user_input)    
    st.write("Output:",result)
    
if(option == "detect-email"):
     emails = re.findall(r'[\w\.]+@[\w]+(?:\.[\w]+)+', user_input.strip())
     st.write("Emails:", emails)
