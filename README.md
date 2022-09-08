# nlp-tools

 Name | Type | Time and Space Complexity| Usage|Note
| ------------- | ------------- |------------- |------------- |------------- |
Character Break| Regular Expression ||Can be used for any language.
Syllable Break (Unicode)| Regular Expression || Can be used for Unicode data of Myanmar (Burmese), Rakhine, Pali, and Paoh.
Syllable Break (Zawgyi)| Regular Expression || Can be used for Zawgyi Encoding Myanamr (Burmese) Language.
Multilingual Semi-syllable Break (Unicode)|Regular Expression||Can be used for Unicode Encoding Malayalam, Khmer, Bengali, Sinhala, Tamil, Shan, Mon, Pali and Sanskrit, Sagaw Karen, Western Poh Karen, Eastern Poh Karen, Geba Karen, Kayah, Rumai Palaung, Khamathi Shan, Aiton and Phake, Burmese (Myanmar), Paoh, Rakhine Languages)|I got this new idea while working in keywords detection in burmese, sinhala, and tamil. Regarding keywords detection, the word like "ဘောမ" can be found in the sentence like "သင်္ဘောမျိုး" and the scanerio is irrelevant. And luckily I found an alternative that would be helpful for three languages.<br>
Burmese to Braille (Muu Haung) Converter|Regular Expression||Can be used to change from burmese to burmese braille (Muu Haung)
Detect Email|Regular Expression||Can be used to detect emails in the text<br>
Valid Parantheses|Stack|Time Complexity O(n), Space Complexity O(n)|True if it is valid False if it is not<br>

## Streamlit

![ss](https://github.com/SaPhyoThuHtet/nlp-tools/blob/main/images/Screenshot%20from%202021-07-27%2016-52-42.png "Current Version")

## References
Y. K. Thu et al., "sylbreak4all: Regular Expressions for Syllable Breaking of Nine Major Ethnic Languages of Myanmar," 2021 16th International Joint Symposium on Artificial Intelligence and Natural Language Processing (iSAI-NLP), 2021, pp. 1-6, doi: 10.1109/iSAI-NLP54397.2021.9678188.

