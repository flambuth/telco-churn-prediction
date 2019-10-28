from sklearn.tree import DecisionTreeClassifier

def do_the_decisionTree(my_criterion, X_train, y_train):
    clf = DecisionTreeClassifier(criterion=my_criterion, max_depth=3, random_state=123)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_train)
    y_pred_proba = clf.predict_proba(X_train)
    score = clf.score(X_train, y_train)
    return score