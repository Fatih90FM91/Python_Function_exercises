# 3. Translating

# The code block below contains a very small dictionary that contains the translations of English words to Dutch.
#  Write a program that uses this dictionary to create a word-for-word translation of the given sentence.
#  A word for which you cannot find a translation, you can leave “as is.” The dictionary is supposed to be used case-insensitively,
#  but your translation may consist of all lower case words. It is nice if you leave punctuation in the translation, but if you take it out,
#  that is acceptable (as leaving punctuation in is quite a bit of work, and does not really have anything to do with dictionaries – besides,
#  leaving punctuation in is much easier to do once you have learned about regular expressions).



english_dutch = { "last":"laatst", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal", "saw":
"zaag", "first":"eerst", "performance":"optreden", "of":"van",
"a":"een", "new":"nieuw", "symphony":"symphonie", "by":"bij",
"one":"een", "world":"wereld", "leading":"leidend", "modern":
"modern", "composer":"componist", "composers":"componisten",
"two":"twee", "shed":"schuur", "sheds":"schuren" }

sentence = "Last week The Royal Festival Hall saw the first \
performance of a new symphony by one of the world's leading \
modern composers, Arthur \"Two-Sheds\" Jackson." 


result_sentence_english=""
for n in english_dutch.keys():
    if n == "composer":
        result_sentence_english=result_sentence_english 

    elif n =="composers":
        result_sentence_english=result_sentence_english +" " + n + " ,"
    elif n =="shed":
        result_sentence_english=result_sentence_english 
    else:

         result_sentence_english=result_sentence_english +" "+ n

print(result_sentence_english)


result_sentence_dutch=""
for n in english_dutch.values():
    if n == "componist":
        result_sentence_dutch=result_sentence_dutch 

    elif n =="componisten":
        result_sentence_dutch=result_sentence_dutch +" " + n + " ,"
    elif n =="schuur":
        result_sentence_dutch=result_sentence_dutch 
    else:

        result_sentence_dutch=result_sentence_dutch +" "+ n

print(result_sentence_dutch)


