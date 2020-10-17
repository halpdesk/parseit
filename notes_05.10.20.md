# Meeting: Monday 5th Oct 2020, 14:00 - 14:50

> Notes from supervisor

Thesis:

- think about concrete research question
- the idea is to classify comments from Reddit into two categories: popular and unpopular
- the main idea (thesis contribution) is to use various linguistic features as input to the classifier
- expected: different features would produce different results for the classification task
- based on the evaluation results, draw conclusions about which features perform better / worse, general differences
- thesis scope: more linguistic analysis rather than machine learning

Data:

- Reddit forum
- each post has a popularity rating assigned to it
- the classification method would use representation of the text as its input and try to match it with the expected label (0/1)
- Resources:
  - GitHub repository, which implements various realisations of data representation for the model
  - kaggle.com and its datasets, for example, https://www.kaggle.com/reddit/reddit-comments-may-2015
  - think about size of the data (for this, need to learn about train/val/test sets in basics of ML, nice resource of more information:
    https://machinelearningmastery.com/difference-test-validation-datasets/)

Features:

- https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
- https://scikit-learn.org/stable/modules/feature_extraction.html
- look at the two types of features (at the moment): bag of words and tf-idf
- Algorithms: start with Naive Bayes (useful: https://www.youtube.com/watch?v=gQZPxuw6cEs)
- good resource: https://pparacch.github.io/2016/12/22/naive_bayes_in_r.html (more technical though)

Evaluation:

- accuracy of the classification model
- confusion matrix (some good information: https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62)

Reading:

- best resource: https://web.stanford.edu/~jurafsky/slp3/ (chapters 3, 4, 5 in particular)
- classification basics: https://www.youtube.com/watch?v=-la3q9d7AKQ
- otherwise, look for materials on 'binary classification'

Notes:

- all implementations for features/algorithms/etc. exist in scikit-learn documentation
- this would be useful to have some kind of a general idea about classification in NLP,
  for example, https://towardsdatascience.com/a-complete-nlp-classification-pipeline-in-scikit-learn-bf1f2d5cdc0d
- do not forget the the focus is on *linguistic* features, so a substantial part of the thesis should be devoted to
  the analysis of using different types of features (their advantages and drawbacks, books like the one from Jurafsky can be helpful in it)
- the framework in GitHub repo will be used to prepare linguistic features from the Reddit comments

Next week:

- Nikolai: prepare code for some toy examples on classification, be ready to walk through the code and motivation behind it
- Hannah: think about more concrete research question, draft re-writing, start reading the materials
