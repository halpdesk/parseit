# Notes from programming sessions

Notes I've written down. I've had more sessions than this but not always documented my findings.

## 2020-11-22

```"The experiments on word senses show that there is not much difference between senses and words. The more plausible explanation is that the senses of a noun in documents of a category tend to be always the same. Moreover, different categories are characterized by different words rather than different senses."```

From https://www.researchgate.net/publication/221397355_Complex_Linguistic_Features_for_Text_Classification_A_Comprehensive_Study

https://scholar.google.se/scholar?q=linguistic+features+text+classification&hl=en&as_sdt=0&as_vis=1&oi=scholart

https://books.google.se/books?hl=en&lr=&id=iVuEBgAAQBAJ&oi=fnd&pg=PR8&dq=linguistic+features+text+classification&ots=RZztMnnCkn&sig=fCCEgvykI5SV-MhaTDva2KvnfFU&redir_esc=y#v=onepage&q=linguistic%20features%20text%20classification&f=false

LINGUISTIC FEATURE CLASSIFYING AND TRACING
Mohammadreza Moohebat 1 , Ram Gopal Raj 2 , Dirk Thorleuchter 3 and Sameem Binti Abdul Kareem 4
https://www.researchgate.net/publication/318600257_Linguistic_Feature_Classifying_and_Tracing

## 2020-10-26

- Skewed data - use StratifiedKFold
- Drop off skewd data so that we have similar sizes from all bins?
- Normalize bag of words features [0-1]

## 2020-10-17

- Always check user guide: https://scikit-learn.org/stable/user_guide.html
- Needs scaling?: https://stats.stackexchange.com/questions/244507/what-algorithms-need-feature-scaling-beside-from-svm
- Feature scaling: https://sebastianraschka.com/Articles/2014_about_feature_scaling.html
- Preprocessing and scaling: https://scikit-learn.org/stable/modules/preprocessing.html
- Preprocessing api list: https://scikit-learn.org/stable/modules/classes.html#module-sklearn.preprocessing

## 2020-10-08

- Try regression or otherwise bin/chunk labels
  - MSE on scoring (0 = good)
- Use transformers / scalers on labels (not Standard: because gaussian and labels are not normal distributed(?), maybe MinMax)

## 2020-09-29

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
