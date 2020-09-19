# Parsit - A Reddit Parser

## Introduction 

Reddit is the 17th most popular web site as of August 30, 2020 according to Alexa^[https://www.alexa.com/siteinfo/reddit.com], with above 430 million monthly active users according to Oberlog^[https://www.oberlo.com/blog/reddit-statistics]. As such, it should serve well as a corpus in various lunguistical fields (written down as keywords below).

```json
Keywords:
language structure, mophology, synctactic structure, 
semantics, pragmatics, secondary language usage, 
grammatics, sociolinguistics, language technology.
```

This project aims to scrape a set of chosen subreddits and parse the content in a linguistic context for statistical analysis. It is specifically written for a university project, and might not be maintained when the first version of this program (considered an MVP, that is when it fully satisfies that project) is reached.

## Revision history

| Revision   | Comment                      | Author          |
|------------|------------------------------|-----------------|
| 2020-09-16 | First version - Introduction | Daniel Leppänen |

## Ideas

### Code

- See how to scrape reddit here: [https://www.storybench.org/how-to-scrape-reddit-with-python/](https://www.storybench.org/how-to-scrape-reddit-with-python/)
- Use pandas, pendulum and praw
- Consider data store in binary files (with pickle), but look into HDF
- Use matplotlib, plotly or seaborn for graphs
- Use sklearn for ML

### Other

- What constitutes a "good" good and a "bad" content?
    Content might need to be classified and rate of new content might need to be learned
