<p align="center"><img src="https://github.com/SaPhyoThuHtet/nlp-tool/blob/main/images/peacock-3.png" width="150" height="100"></p># nlp-tool

 No|Name | Type | Time and Space Complexity| Usage|Note
| -------------| ------------- | ------------- |------------- |------------- |------------- |
1|Character Break| Used Regular Expression |O(n), O(1)|Can be used for any language.
2|Syllable Tokenization (Unicode)| Regular Expression |O(n), O(1)| Can be used for Unicode data of Myanmar (Burmese), Rakhine, Pali, and Paoh Languages.
3|Syllable Tokenization (Zawgyi)| Regular Expression |O(n), O(1)| Can be used for Zawgyi Encoding Myanmar (Burmese) Language.
4|Multilingual Semi-syllable Tokenization (Unicode)|Regular Expression|O(n), O(1)|Can be used for Unicode Encoding Lao, Kannada, Oriya, Gujarati, Malayalam, Khmer, Bengali, Sinhala, Tamil, Mon, Pali and Sanskrit, Sagaw Karen, Western Poh Karen, Eastern Poh Karen, Geba Karen, Kayah, Rumai Palaung, Khamathi Shan, Aiton and Phake, Burmese (Myanmar), Paoh, Rakhine Languages). Can also be used as a word break for English and charcter break for any other languages.|I got this new idea while working in keywords detection in burmese and other two languages. Regarding keywords detection, the word like "ဘောမ" can be found in the sentence like "သင်္ဘောမျိုး" and the scanerio is irrelevant. And luckily I found an alternative that would be helpful for three languages. Here, semi-syllable does not refer to the minor syllable in phonology. Instead, it is new tokenization that does not break into a full syllable mode. Now I found that it is useful in keyword detection to reduce False Positive errors. (I may explain why keywords detection later)The beauty of this tokenization would be you don't need to know much about the nature of the specific language. It will especially work for a similar script like Brahmic Script. Since it is in the initial state, it may have some errors.
5|Burmese to Braille (Muu Haung) Converter|Regular Expression|O(n), O(1)|Can be used to change from burmese to burmese braille (Muu Haung)| The brialle to burmese dictonary may need to be updated. The data for the dicitonary is prepared by Phyo Thu Htet, Naing Linn Phyo and Thiha Nyein.
6|Detect Email|Regular Expression|O(n), O(1)|Can be used to detect emails in the text<br>|E.g. Input: ဒီနေ့တော့ phyothuhtet39@gmail.com ဆီကို mail  ပို့ရမယ်။ နေဉီး သူက Microsoft Mail phyothuhtet@studentambassadors.com ကို သုံးတာလားမေးကြည့်ပါဦး။ ငါ ayethida89.young@utycc.edu.mm  ကနေ ပို့လိုက်မယ်။, Output: ayethida89.young@utycc.edu.mm;phyothuhtet39@gmail.com;phyothuhtet@studentambassadors.com
7|Burmese Sentence Level Zawgyi Unicode Detection|Machine Learning||
8|Valid Parantheses|Stack|O(n), O(n)|Return True if the user input is valid False if it is not<br>
9|Remove these characters|Stack|O(n), O(n)|Remove the specified characters<br>



### Streamlit

![ss](https://github.com/SaPhyoThuHtet/nlp-tools/blob/main/images/Screenshot%20from%202021-07-27%2016-52-42.png "Current Version")

```
$ pip3 install requirements.txt
```

```
$ streamlit run nlptools.py
```
## gdg 2022
Text Classification with Zero Shot and Few Shot Learning pdf: https://github.com/SaPhyoThuHtet/nlp-tool/tree/main/gdg-2022

Zero Shot Example Notebook: https://colab.research.google.com/drive/1jocViLorbwWIkTXKwxCOV9HLTaDDgCaw?usp=sharing (This is the original notebook provided by hugging face)

## References
1. Unicode Character Table, https://jrgraphix.net/r/Unicode/1000-109F
2. Rabbit Converter, http://www.rabbit-converter.org/
3. NLP Class UTYCC, https://github.com/ye-kyaw-thu/NLP-Class
4. Y. K. Thu et al., "sylbreak4all: Regular Expressions for Syllable Breaking of Nine Major Ethnic Languages of Myanmar," 2021 16th International Joint Symposium on Artificial Intelligence and Natural Language Processing (iSAI-NLP), 2021, pp. 1-6, doi: 10.1109/iSAI-NLP54397.2021.9678188.


## Acknowledgment
I would like to thank Dr. Ye Kyaw Thu, Dr. Hnin Aye Thant, Ma Aye Hninn Khine, ​and Ma Yi Yi Chan Myae Win Shein for their guidance, support, and suggestions. The skills acquired from Dr. Ye Kyaw Thu's NLP Class helped me a lot in order to develop new ideas in NLP Field and this repo. And a shoutout to the creators of Rabbit Converter and jrgraphix.net's Unicode Character Table. These tools were super helpful to develop nlp-concepts especially for Burmese Language. Thanks.

### License
MIT License

Copyright (c) 2021 Sa Phyo Thu Htet

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
