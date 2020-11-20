from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

######################## Logistic Regression ##########################

def logistic_regression(X_train, y_train, X_bow, X_tfidf):
    '''
    This function takes in X_train (features using for model) and y_train (target) and performs logistic
    regression giving us accuracy of the model and the classification report
    '''
    # Calling out funtion
    lm = LogisticRegression().fit(X_bow, y_train)

    # Array of the predicitons
    X_train['predicted'] = lm.predict(X_bow)

    # X_bow
    print('X_bow Accuracy: {:.0%}\n'.format(accuracy_score(y_train, X_train.predicted)))
    print('-----------------------')
    print(f'X_bow Confusion Matrix: \n\n {pd.crosstab(y_train.language, X_train.predicted)}\n' )
    print('-----------------------')
    print("X_bow Random Forest Classification Report:\n", classification_report(y_train, X_train.predicted))
    
    lm_tfidf = lm.fit(X_tfidf, y_train)
    X_train['pred_tfidf'] = lm_tfidf.predict(X_tfidf)

    # TF-IDF
    print('-----------------------')
    print('TF-IDF Accuracy: {:.0%}\n'.format(accuracy_score(y_train, X_train.pred_tfidf)))
    print('-----------------------')
    print(f'TF-IDF Confusion Matrix: \n\n {pd.crosstab(y_train.language, X_train.pred_tfidf)}\n' )
    print('-----------------------')
    print("TF-IDF KNN Classification Report:\n", classification_report(y_train, X_train.pred_tfidf))

    ######################## Decesion Tree ##########################

def decesion_tree(X_train, y_train, X_bow, X_tfidf, k):
    '''
    This function requires X_train, y_train and k (max_depth). A confusion matrix, models accuracy and 
    classification report are outputed
    '''
    # Creating the decision tree object
    clf = DecisionTreeClassifier(max_depth=k, random_state=123)

    # Fitting the data to the trained data using xbow
    clf.fit(X_bow, y_train)

    # Array of the predicitons
    X_train['predicted'] = clf.predict(X_bow)

    # Confusion matrix
    print('X_bow Accuracy: {:.0%}\n'.format(accuracy_score(y_train, X_train.predicted)))
    print('-----------------------')
    print(f'X_bow Confusion Matrix: \n\n {pd.crosstab(y_train.language, X_train.predicted)}\n' )
    print('-----------------------')
    print("X_bow Decesion Tree Classification Report:\n", classification_report(y_train, X_train.predicted))
                                        
    # tfidf
    clf_tfidf = clf.fit(X_tfidf, y_train)
    X_train['pred_tfidf'] = clf_tfidf.predict(X_tfidf)
                                    
    # Confusion matrix
    print('-----------------------')
    print('TF-IDF Accuracy: {:.0%}\n'.format(accuracy_score(y_train, X_train.pred_tfidf)))
    print('-----------------------')
    print(f'TF-IDF Confusion Matrix: \n\n {pd.crosstab(y_train.language, X_train.pred_tfidf)}\n' )
    print('-----------------------')
    print("TF-IDF Decesion Tree Classification Report:\n", classification_report(y_train, X_train.pred_tfidf))

    ######################## Random Forest ##########################

def random_forest(X_train, y_train, X_bow, X_tfidf, k):
    # Random forest object
    rf = RandomForestClassifier(n_estimators=100, max_depth=k, random_state=123)

    # Fitting the data to the trained data
    rf.fit(X_bow, y_train)

    # Array of the predicitons
    X_train['predicted'] = rf.predict(X_bow)

    # Confusion matrix
    print('X_bow Accuracy: {:.0%}\n'.format(accuracy_score(y_train.language, X_train.predicted)))
    print('-----------------------')
    print(f'X_bow Confusion Matrix: \n\n {pd.crosstab(y_train.language, X_train.predicted)}\n' )
    print('-----------------------')
    print("X_bow Random Forest Classification Report:\n", classification_report(y_train.language, X_train.predicted))

    rf_tfidf = rf.fit(X_tfidf, y_train)
    X_train['pred_tfidf'] = rf_tfidf.predict(X_tfidf)

   # Confusion matrix
    print('-----------------------')
    print('TF-IDF Accuracy: {:.0%}\n'.format(accuracy_score(y_train.language, X_train.pred_tfidf)))
    print('-----------------------')
    print(f'TF-IDF Confusion Matrix: \n\n {pd.crosstab(y_train.language, X_train.pred_tfidf)}\n' )
    print('-----------------------')
    print("TF-IDF Random Forest Classification Report:\n", classification_report(y_train.language, X_train.pred_tfidf))

    ######################## KNN ##########################

def knn(X_train, y_train, X_bow, X_tfidf, k):
    # KNN object
    knn = KNeighborsClassifier(n_neighbors=k, weights='uniform')

    # Fit the model
    knn.fit(X_bow, y_train)

    # Make predictions
    X_train['predicted'] = knn.predict(X_bow)
    
    # X_bow
    print('X_bow Accuracy: {:.0%}\n'.format(accuracy_score(y_train.language, X_train.predicted)))
    print('-----------------------')
    print(f'X_bow Confusion Matrix: \n\n {pd.crosstab(y_train.language, X_train.predicted)}\n' )
    print('-----------------------')
    print("X_bow Random Forest Classification Report:\n", classification_report(y_train.language, X_train.predicted))
    
    knn_tfidf = knn.fit(X_tfidf, y_train)
    X_train['pred_tfidf'] = knn_tfidf.predict(X_tfidf)

    # TF-IDF
    print('-----------------------')
    print('TF-IDF Accuracy: {:.0%}\n'.format(accuracy_score(y_train.language, X_train.pred_tfidf)))
    print('-----------------------')
    print(f'TF-IDF Confusion Matrix: \n\n {pd.crosstab(y_train.language, X_train.pred_tfidf)}\n' )
    print('-----------------------')
    print("TF-IDF KNN Classification Report:\n", classification_report(y_train.language, X_train.pred_tfidf))