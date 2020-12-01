# Affinity-Analysis 
Simple Market Basket Analysis for product recommendations task

Affinity analysis is the study of when things exist togheter. Affinity Analysis can take place in the contex of market basket analysis where the goal is to improve sales of certain products.
Affinity analysis is a data mining tecnique that gives similarity between samples.

For this exercise is provided a .txt format dataset which is a numpy 2-d array, the rows represent different samples and the columns represents different features, in particular each rows of the dataset is of the form (0,1,1,0,1) [this is an example row]. This represent a single transaction where we identify with 0 the product that has not been taken and 1 otherwise. The products in this example are:

- bread, milk, cheese, apples, banananas.

In this exercise I will focus on thi point:when two items are historically purchased together, they are more likely to be purchased together in the future. So the objective is to find simle rules of the form: "If a person buys product X, then they are likely to purchase product Y".

The rule is extracted and measured by two variable that takes place in this type of analysis: "Support" and "Confidence". 

> Support: the number of times that a rule occurs into dataset, which is computed by counting the number of samples that the rule is valid for. The support is normalized by the division with the total number of times that the rule is valid

> Confidence: measure how accurate rules are when they are used. It is computed by determining the percentage of times the rule applies when the premise applies. So first count how many times the rule applies in the dataset and the divide it by the number of samples where the premise occurs.

For better understanding premise: let's consider how many rows contains 1 for an apple so it means that a person buy apples, this is the premise.

So we can figure out it by saying that premise is: "if a persone buys apples" then "he/she will buy banans" conclusion. If both are given the rule is considere valid and so we proceed is this way for the entire dataset.It is clear that the premise is represented by all the purchased items, i.e. the 1ones in the dataset.

So, after valid rules  has been stored the confidence and support can be calculated. 

After all, I compute a sorting on support and confidence for obtain a ranking with the top rules.
