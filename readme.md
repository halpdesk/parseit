# Parsit - A Reddit Parser

## Introduction

Reddit is the 17th most popular web site as of August 30, 2020 according to Alexa^[https://www.alexa.com/siteinfo/reddit.com], with above 430 million monthly active users according to Oberlog^[https://www.oberlo.com/blog/reddit-statistics]. As such, it should serve well as a corpus in various lunguistical fields (written down as keywords below).

```json
Keywords:
language structure, mophology, synctactic structure,
semantics, pragmatics, secondary language usage,
grammatics, sociolinguistics, language technology.
```

This project aims to scrape a set of chosen subreddits and parse the content (mainly comments) in a linguistic context for statistical analysis. It is specifically written for a university project, and might not be maintained when the first version of this program (considered an MVP, that is when it fully satisfies that project) is reached.

_Do we communicate in order to state truths or do we speak truths (occasionally) so we can communicate? (Cherpas, 139)_

### Revision history

| Revision   | Comment                       | Author          |
|------------|-------------------------------|-----------------|
| 2020-09-16 | First version - Introduction  | Daniel Leppänen |
| 2020-09-20 | Second version - Project      | Daniel Leppänen |

## Project

This code project is set up as easily as possible; resembling of a simple script but with some concern for separation of code.
The main

- nltk (natural language toolkit)
- seaborn (graphs)
- sklearn (ML)
- praw (python reddit api wrapper)

A pickle is used to store all reddit data after first run.
SKLearn is used to classify and learn which comments score high depending on which combination of linguistic features.

### Features

- Text length
- Lexical and morphological
  - TF*IDF
  - common words in english
  - profanity
- Otrhography - usage and quality of non-alphabetical characters (graphemes), capitalization, spelling (norms), emphasis
    (also consider rating emoticons / smilies usage)
- Syntax - phrase structure trees and dependency trees
- Semantics - aspectual classes and reichenbach’s tenses
- How well comment aligns with topic (similarity between topic and comment)

#### Uncertain

- Pragmatics - implicature / Grice maxims

### Problems

- Comment score depends on views - once a comment is "hot" it attracts more views and more votes
- n-level comments depend much on the first-level comment (POSSIBLE SOLUTION: consider only first-level comments)

### Interesting things

#### Papers

- Hatzivassiloglou, V & Klavans, J L & Eskin, E (1999), Detecting Text Similarity over Short Passages: Exploring Linguistic Feature Combinations via Machine Learning
- William Croft (1994) Semantic universals in classifier systems, Word, 45:2, 145-171, DOI: 10.1080/00437956.1994.11435922
- 10000 most common words in english (https://github.com/first20hours/google-10000-english or https://www.kaggle.com/rtatman/english-word-frequency)
- Muresan, S & Tzoukermann, E & Klavans, J L (), Combining Linguistic and Machine Learning Techniques for Email Summarization
- Cherpas, C (1992). Natural language processing, pragmatics, and verbal behavior. Analysis Verbal Behav 10, 135–147. https://doi.org/10.1007/BF03392880 (Hämtad 2020-02-12)

#### Links

##### TFIDF

- https://towardsdatascience.com/text-summarization-using-tf-idf-e64a0644ace3
- https://gdcoder.com/nlp-transforming-tokens-into-features-tf-idf/

#### Concepts

- For each token/(here: comment), we will have a feature column and this is called text vectorization.
- Extracting n-grams to preserve some ordering (vs BOW - bag of words)
- Stop-words = words articles and prepositions

## Set up and run

1. Create a reddit account and add an app: https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps
2. Enable virtual env `source ./python_modules/bin/activate` (check with `which python`)
3. Install packages `pip install -r requirements.txt`
4. Add our python credentials and env settings in `.env`
5. Run main file `python main.py`

To fetch reddit data again, run

```sh
python main.py --fetch-fresh --subreddits=science,todayilearned,dataisbeautiful --number-of-submissions=100
```

This command will create a new pickle file with the current timestamp in the filename. Each
time the program is run without the flag `--fetch-fresh` it will load the latest pickle-file
available in the _pickles_ subfolder.

### Install NLTK

1. `python -m nltk.downloader all`
2. `sudo python -m nltk.downloader -d /usr/local/share/nltk_data all`

### Other / Old

- See how to scrape reddit here: [https://www.storybench.org/how-to-scrape-reddit-with-python/](https://www.storybench.org/how-to-scrape-reddit-with-python/)
- Use pandas, pendulum and praw
- Consider data store in binary files (with pickle), but look into HDF
- Use matplotlib, plotly or seaborn for graphs
- Use sklearn for ML
- What constitutes a "good" good and a "bad" content?
    Content might need to be classified and rate of new content might need to be learned
