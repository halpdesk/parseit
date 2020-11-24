# Parsit - A Reddit Parser

## Introduction

This project started for a university project (linguistics, statistical analysis and machine learning). It has a small wrapper written above PRAW to scrape a set of chosen subreddits and store submissions and comments, along witht their score (no other data).  
  
Why reddit?  

Reddit is the 17th most popular web site as of August 30, 2020 according to Alexa^[https://www.alexa.com/siteinfo/reddit.com], with above 430 million monthly active users according to Oberlog^[https://www.oberlo.com/blog/reddit-statistics]. As such, it should serve well as a corpus in various lunguistical fields (written down as keywords below).  
  
```json
Keywords:
language structure, mophology, synctactic structure,
semantics, pragmatics, secondary language usage,
grammatics, sociolinguistics, language technology.
```
  
_Do we communicate in order to state truths or do we speak truths (occasionally) so we can communicate? (Cherpas)_

### Revision history

| Revision   | Comment                                    | Author          |
|------------|--------------------------------------------|-----------------|
| 2020-09-16 | First version - Introduction               | Daniel Leppänen |
| 2020-09-20 | Project, features list and links           | Daniel Leppänen |
| 2020-09-24 | Install and run                            | Daniel Leppänen |
| 2020-10-03 | More notes and links/meeting session notes | Daniel Leppänen |
| Forward    | See [sessions.md](sessions.md) | All me ... |

## Scrape tool

### Requirements

1. python 3.8
2. lzma module

### Instlal lzma module for pandas

1. `sudo apt-get install liblzma-dev` (for ubuntu/debian)
2. Reinstall python from source: `configure && make && make install` (in pyton3.8 folder)

### Set up project

1. Create a reddit account and add an app: https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps
2. Create virtual env `python3.8 -m venv python_modules/`
3. Enable virtual env `source ./python_modules/bin/activate` (check with `which python`)
4. Install packages `pip install -r requirements.txt`
5. Add our python credentials and env settings in `.env`

### Run

**Run program:**
`python main.py`

> Note: It will return "No data loaded", because data must be loaded with --fetch-fresh or with --load-pickle [PICKLE FILE] command line arguments.

**To fetch reddit data again, run:**
`python main.py --fetch-fresh --save-pickle comments.p --subreddits science todayilearned dataisbeautiful --submissions 100`
> This command will create a new pickle file in the current directory called _comments.p_.

**To use earlierfetched reddit data:**
`python main.py --load-pickle comments.p `
> This command will load data from a pickle file called _comments.p_.

Here is a list of command line arguments.

```bash
optional arguments:
  -h, --help                                show this help message and exit
  --fetch-fresh                             Use to fetch new comments
  --save-pickle [SAVE_PICKLE]               Use to save comment data to a pickle
  --load-pickle [LOAD_PICKLE]               Use to load comment data to a pickle
  --subreddits SUBREDDITS [SUBREDDITS ...]  Which subreddits to parse for commments
  --submissions [SUBMISSIONS]               How many submissions to fetch for each subreddit
```

## Project

This project was initially set up with a simple architecture resembling that of a software; i.e. with some concern for separation of code, etc.
As I've progressed I learned to use a work flow with jupyter notebooks and recently set up them so they can be run as a pipeline:

1. First file loads pickle file and calculate all features for ML and saves to new pickle
2. Second file loads pickle and generate graphs
3. Third file loads pickle to train the ML

### Prerequisites

Install NLTK

1. `python -m nltk.downloader all`
2. `sudo python -m nltk.downloader -d /usr/local/share/nltk_data all`

### Features

#### Classical text features

- Bag of words
- Bag of bigrams
- TF-IDF (which is also a bag)

_Works with: **Naive Bayes** (MultinomialNB, both regression and classifier) and other models which can handle_ a lot _of features_

#### Other features implemented

- Number of significant words (might add a list for word ranking)
- Number of stop words
- Number of bad words (lemmatized words are matched against a common profanity filter list)
- Number of positive smilies
- Number of negative smilies
- Number of neutral smilies
- Similarity with topic
- Similarity with all other comments
- TF-IDF mean value

_Works with: **KNN**(?),  **SVM**(?)_ (currently trying)

> Note: Sentiment analysis has been made a couple of times for smilies. See http://kt.ijs.si/data/Emoji_sentiment_ranking/about.html

#### Other fields from where features might get extracted

- Lexical and morphological
- Otrhography - usage and quality of non-alphabetical characters (graphemes), capitalization, spelling (norms), emphasis
    (also consider rating emoticons / smilies usage)
- Syntax - phrase structure trees and dependency trees
  - activum / passivum might be derived from this
- Semantics
  - aspectual classes and reichenbach’s tenses
- Pragmatics
  - implicature / Grice maxims

### Problems

- Comment score depends on views - once a comment is "hot" it attracts more views and more votes: this leads to an unbalanced dataset
