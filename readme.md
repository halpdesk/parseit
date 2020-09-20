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

### Linguistic features

### Interesting papers and links

- Hatzivassiloglou, V & Klavans, J L & Eskin, E (1999), Detecting Text Similarity over Short Passages: Exploring Linguistic Feature Combinations via Machine Learning
- William Croft (1994) Semantic universals in classifier systems, Word, 45:2, 145-171, DOI: 10.1080/00437956.1994.11435922
- 10000 most common words in english (https://github.com/first20hours/google-10000-english or https://www.kaggle.com/rtatman/english-word-frequency)
- Muresan, S & Tzoukermann, E & Klavans, J L (), Combining Linguistic and Machine Learning Techniques for Email Summarization

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

### Other / Old

- See how to scrape reddit here: [https://www.storybench.org/how-to-scrape-reddit-with-python/](https://www.storybench.org/how-to-scrape-reddit-with-python/)
- Use pandas, pendulum and praw
- Consider data store in binary files (with pickle), but look into HDF
- Use matplotlib, plotly or seaborn for graphs
- Use sklearn for ML
- What constitutes a "good" good and a "bad" content?
    Content might need to be classified and rate of new content might need to be learned
