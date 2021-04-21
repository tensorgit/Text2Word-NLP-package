# Text2Word-NLP-package
## Text pre-processing methods for NLP applications available on https://pypi.org/


**To install**
pip install Text2Word

**To test the code:**
from Text2Word import performtext2word

preproc = performtext2word()

test_review = 'This was an awesome movie man. I loved it!'

test_wordlist = preproc.review_to_words(test_review)
print(test_wordlist)


data_train = ['This is an awesome movie. superb.', 'Hated the climax, what a bore']
data_test = ['Not sure what I have watched really', 'Are you kidding me. I am in love with the actor']


words_train, words_test = preproc.preprocess_data(data_train, data_test)

print(words_train)
print(words_test)


