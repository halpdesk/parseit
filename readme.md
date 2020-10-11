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

_Do we communicate in order to state truths or do we speak truths (occasionally) so we can communicate? (Cherpas)_

### Revision history

| Revision   | Comment                                    | Author          |
|------------|--------------------------------------------|-----------------|
| 2020-09-16 | First version - Introduction               | Daniel Leppänen |
| 2020-09-20 | Project, features list and links           | Daniel Leppänen |
| 2020-09-24 | Install and run                            | Daniel Leppänen |
| 2020-10-03 | More notes and links/meeting session notes | Daniel Leppänen |

## Project

This code project is set up as easily as possible; resembling of a simple script but with some concern for separation of code. The main packages used by this project are:

- nltk (natural language toolkit)
- seaborn (graphs)
- sklearn (ML)
- praw (python reddit api wrapper)

A pickle is used to store all reddit data after first run. SKLearn is used to classify and learn which comments score high depending on which combination of linguistic features gives high score.

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
- Muresan, S & Tzoukermann, E & Klavans, J L (), Combining Linguistic and Machine Learning Techniques for Email Summarization
- Cherpas, C (1992). Natural language processing, pragmatics, and verbal behavior. Analysis Verbal Behav 10, 135–147. https://doi.org/10.1007/BF03392880 (Fetched 2020-02-12)

#### Other links

- NLTK - Learning to classify text: https://www.nltk.org/book/ch06.html
- 10000 most common words in english (https://github.com/first20hours/google-10000-english or https://www.kaggle.com/rtatman/english-word-frequency)
- KNN example with sklearn: https://towardsdatascience.com/knn-using-scikit-learn-c6bed765be75#:~:text=KNN%20(K%2DNearest%20Neighbor),hence%20it%20is%20non%2Dparametric
- older KNN example: https://www.datacamp.com/community/tutorials/k-nearest-neighbor-classification-scikit-learn

Uncategorized:

- Also check https://catboost.ai/ (categories like for tempuses)
- https://www.kaggle.com/bittlingmayer/amazonreviews/notebooks
- https://www.kaggle.com/fabiendaniel/customer-segmentation

##### POS

Use POS to decide activum/passivum?

- https://wibbu.com/using-python-and-nltk-to-automate-language-analysis-of-our-scripts/ (replace this later, it's worhless)

##### TFIDF

- https://towardsdatascience.com/text-summarization-using-tf-idf-e64a0644ace3 - nltk
- https://towardsdatascience.com/natural-language-processing-feature-engineering-using-tf-idf-e8b9d00e7e76 - how to use sklearn in few rows
- https://gdcoder.com/nlp-transforming-tokens-into-features-tf-idf/ - sklearn with ngram

##### Other

- https://www.geeksforgeeks.org/removing-stop-words-nltk-python/ - how to remove stop-words

#### Concepts

- For each token/(here: comment), we will have a feature column and this is called text vectorization.
- Extracting n-grams to preserve some ordering (vs BOW - bag of words)
- Stop-words = words articles and prepositions

## Set up and run

### Requirements

1. python 3.8
2. NLTK data
3. lzma module

### Install NLTK

1. `python -m nltk.downloader all`
2. `sudo python -m nltk.downloader -d /usr/local/share/nltk_data all`

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

### Other / Old

- See how to scrape reddit here: [https://www.storybench.org/how-to-scrape-reddit-with-python/](https://www.storybench.org/how-to-scrape-reddit-with-python/)
- Use pandas, pendulum and praw
- Consider data store in binary files (with pickle), but look into HDF
- Use matplotlib, plotly or seaborn for graphs
- Use sklearn for ML
- What constitutes a "good" good and a "bad" content?
    Content might need to be classified and rate of new content might need to be learned

### Notes from meeting seesion 2020-09-29

- Check research and find text features
- Build text feature data from text, let the upvotes be the variable to predict (y)
- Split the data in training data and test
  Maybe use k-fold for training if not that much data https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html
- Use a regression, say random forest and train it on the data
  https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
- Select hyper paramaters with a baysain optimization algorithm or CVGrid
  https://scikit-optimize.github.io/stable/auto_examples/bayesian-optimization.html#sphx-glr-auto-examples-bayesian-optimization-py
- Score the test data and see if the regression learned anything
- Output the feature relevance for the score

  ```python
  # Let's have a look at the feature importance
  fi = pd.DataFrame(data={"Feature": X.columns, "Importance": clf.feature_importances_ * 100, "Std": 100 * np.std([tree.feature_importances_ for tree in clf.estimators_], axis=0)})
  sns.barplot(x='Importance', y='Feature', color='gray',
              data=fi.sort_values("Importance", ascending=False),
              **{'xerr':fi["Std"], 'ecolor': '#333333'})
  plt.title('Feature importance \n')
  plt.xlabel('Importance (%)')
  plt.ylabel('Feature')
  ```

### Notes from meeting seesion 2020-10-08

- Try regression or otherwise bin/chunk labels
  - MSE on scoring (0 = good)
- Use transformers / scalers on labels (not Standard: because gaussian and labels are not normal distributed(?), maybe MinMax)
