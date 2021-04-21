# Text2Word-NLP-package
## Text pre-processing methods for NLP applications available on https://pypi.org/

**Main Class:** ```class performtext2word ```
**Class methods:** 
``` 
1. review_to_words(self, review): to clean a unit text using 'nltk'
2. preprocess_data(self, data_train, data_test): to convert individual training and test text data into a list of cleaned
        words using the 'review_to_words', collectively stored in a list
3. build_dict(self, data_train, vocab_size = 5000): to Construct and return a dictionary mapping each of the most frequently appearing words to a unique integer
4. extract_BoW_features(self, data_train, data_test, vocabulary_size=5000): to Extract Bag-of-Words for a given set of documents, already preprocessed into words
```

**To install**
```pip install Text2Word ```

**To test the code:**
```
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
```

