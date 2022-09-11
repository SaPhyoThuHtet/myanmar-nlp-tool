# nlp-tools

 Name | Type | Time and Space Complexity| Usage|Note
| ------------- | ------------- |------------- |------------- |------------- |
Character Break| Regular Expression |O(n), O(1)|Can be used for any language.
Syllable Tokenization (Unicode)| Regular Expression |O(n), O(1)| Can be used for Unicode data of Myanmar (Burmese), Rakhine, Pali, and Paoh.
Syllable Tokenization (Zawgyi)| Regular Expression |O(n), O(1)| Can be used for Zawgyi Encoding Myanmar (Burmese) Language.
Multilingual Semi-syllable Tokenization (Unicode)|Regular Expression|O(n), O(1)|Can be used for Unicode Encoding Lao, Kannada, Oriya, Gujarati, Malayalam, Khmer, Bengali, Sinhala, Tamil, Mon, Pali and Sanskrit, Sagaw Karen, Western Poh Karen, Eastern Poh Karen, Geba Karen, Kayah, Rumai Palaung, Khamathi Shan, Aiton and Phake, Burmese (Myanmar), Paoh, Rakhine Languages). Can also be used as a word break for English and charcter break for any other languages.|I got this new idea while working in keywords detection in burmese and other two languages. Regarding keywords detection, the word like "ဘောမ" can be found in the sentence like "သင်္ဘောမျိုး" and the scanerio is irrelevant. And luckily I found an alternative that would be helpful for three languages.<br>
Burmese to Braille (Muu Haung) Converter|Regular Expression|O(n), O(1)|Can be used to change from burmese to burmese braille (Muu Haung)| The brialle to burmese dictonary may need to be updated. The data for the dicitonary is prepared by Phyo Thu Htet, Naing Linn Phyo and Thiha Nyein.
Detect Email|Regular Expression|O(n), O(1)|Can be used to detect emails in the text<br>|E.g. Input: ဒီနေ့တော့ phyothuhtet39@gmail.com ဆီကို mail  ပို့ရမယ်။ နေဉီး သူက Microsoft Mail phyothuhtet@studentambassadors.com ကို သုံးတာလားမေးကြည့်ပါဦး။ ငါ ayethida89.young@utycc.edu.mm  ကနေ ပို့လိုက်မယ်။, Output: ayethida89.young@utycc.edu.mm;phyothuhtet39@gmail.com;phyothuhtet@studentambassadors.com
Valid Parantheses|Stack|O(n), O(n)|Return True if the user input is valid False if it is not<br>
Remove these characters|Stack|O(n), O(n)|Remove the specified characters<br>

## Streamlit

![ss](https://github.com/SaPhyoThuHtet/nlp-tools/blob/main/images/Screenshot%20from%202021-07-27%2016-52-42.png "Current Version")

```
$ pip3 install requirements.txt
```

```
$ streamlit run nlptools.py
```

## References
1. Unicode Character Table, https://jrgraphix.net/r/Unicode/1000-109F
2. Y. K. Thu et al., "sylbreak4all: Regular Expressions for Syllable Breaking of Nine Major Ethnic Languages of Myanmar," 2021 16th International Joint Symposium on Artificial Intelligence and Natural Language Processing (iSAI-NLP), 2021, pp. 1-6, doi: 10.1109/iSAI-NLP54397.2021.9678188.
3. Rabbit Converter, http://www.rabbit-converter.org/
4. NLP Class UTYCC, https://github.com/ye-kyaw-thu/NLP-Class

## Acknowledgment
I would like to thank Dr. Ye Kyaw Thu, Dr. Hnin Aye Thant, Ma Aye Hninn Khine, ​and Ma Yi Yi Chan Myae Win Shein for their guidance, support, and suggestions. The skills acquired from Dr. Ye Kyaw Thu's NLP Class helped me a lot in order to develop new ideas in NLP Field and this repo.
