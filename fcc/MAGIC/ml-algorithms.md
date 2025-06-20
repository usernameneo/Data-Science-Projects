# Machine Learning Algorithms

Machine learning algorithms are mathematical models that enable computers to learn from data and improve their performance on a specific task over time. For the purpose of this project we'll be looking into the implementation of the following models: 
- K-Nearest Neighbors
- Naive Bayes
- Logistic Regression
- Support Vector Machine
- Neural Networks
- Linear Regression
- K-Means Clustering
- Principal Component Analysis

## Classification Models

### K-Nearest Neighbors

KNN is a machine learning algorithm that classifies new data points based on their proximity to existing data points. This algorithm works by calculating the distance between a new data point and a given number, K, of existing data points nearest to the new data point in the training set. The new data point is then assigned the most common label among its K nearest neighbors.

The KNN algorithm relies on the idea that similar data points are likely to have similar labels. By finding the K nearest neighbors to a new data point, the algorithm can make an informed prediction about its label.

We will output a classification report on our predictions. An example of a report for our dataset will look as follows

||precision|recall|f1-score|support|
|-|-|-|-|-|
|0|0.76|0.74|0.75|1359|
|1|0.86|0.87|0.86|2445|
|accuracy|||0.82|3804|
|macro avg|0.81|0.80|0.81|3804|
|weighted avg|0.82|0.82|0.82|3804|

Looking at the output there are a few things we can gleem about the performance metrics of our model. The accuracy of the model is 0.82 or 82%, meaning that 82% of our predicted values are labeled correctly. Precision and recall are two key metrics used to evaluate the performance of our system. 

> *Precision* shows the ratio of **true positives** (relevant instances) to the total number of **positive predictions** (retrieved instances).

> *Recall* shows the ratio of **true positives** (relevant instances) to the total number of **actual positives** (all relevant instances).

Finally, the f1-score is a representative value of both the precision and recall ratios.

<img src="https://raw.githubusercontent.com/usernameneo/Data-Science-Projects/main/fcc-MAGIC/image.png" alt="Wikipedia Image illustrating Precision and Recall" style="display: block; margin: 0 auto;">

### Naive Bayes

The Naive Bayes algorithm uses a mathematical formula to classify data points into different categories. It makes a simplifying assumption that the features of the data points (like height, weight, etc.) are independent of each other, meaning that knowing one feature doesn't give you any information about another feature. This algorithm works by first assuming that eatures are independent of each other and then calculating the likelihood of each feature given the target variable. These likelihoods are multiplied together to get a final answer and from that, a category with the highest likelihood is chosen

Naive Bayes uses a simple formula to classify data points based on their features, assuming that each feature is independent of the others.

> P(C<sub>k</sub> | X) = P(X | C<sub>k</sub>) * P(C<sub>k</sub>) / P(X)

The formula tests the probability of a *feature vector*, X falling into a subset of categories, C<sub>k</sub>, and represented as P(C<sub>k</sub> | X),. 
The formula has four parts, the posterior, likelihood, prior and the evidence:
- **The posterior**, P(C<sub>k</sub> | X): *The probability of having of feature vector, X, falling into the specified number, k, of categories, C.*?

- **The likelihood**, P(X | C<sub>k</sub>): 

- **The prior**, P(C<sub>k</sub>):

- **The evidence**, P(X): 


### Logistic Regression

Logistic regression models the probability of a binary outcome based on one or more predictors. This algorithm uses one or more predictors (e.g., age, income) to make a prediction, and then maps these predictors to a probability between 0 and 1 using a logistic function. This probability is then used to predict the likelihood of a binary outcome.

Logistic regression uses a mathematical formula to predict the likelihood of a binary outcome based on one or more predictors.

*Sigmoid function?*

If we have a single X, then we'll have a **simple log reg.** If we have multiple, we'll have a **multiple log reg.**

### Support Vector Machine

The SVM algorithm finds a line or a plane that separates different groups of data in a way that maximizes the distance between them. Imagine you have a bunch of dots that represent different types of things (e.g., apples, bananas, oranges). SVM tries to draw a line or a plane that separates the apples from the bananas and the oranges in a way that makes it clear which group each dot belongs to.

The goal is to find the line or plane that is farthest away from all the dots, which means that it's the best possible separator between the groups.

### Neural Networks

Neural networks are more capable that simply classifying data however, we'll be focusing on the classification aspect. A neural network is a computer system that processes data by breaking it down into smaller parts, learning patterns from examples, and then making decisions based on those patterns. This is done through a network of interconnected nodes (neurons) that work together to mimic the way the human brain processes information.

The goal of a neural network is to learn and make decisions based on data, so it can do things like:

- Recognize pictures and objects
- Understand language and text
- Make predictions and forecasts

Neural networks use a network of interconnected nodes (neurons) to process data and make decisions, similar to how the human brain works

## Regression Models

### Linear Regression

Linear regression models the relationship between a continuous outcome variable and one or more predictor variables by making use of the linear equation to establish a **line of best fit**.

> y = b<sub>0</sub> + b<sub>1</sub>x

- b<sub>0</sub> : y-intercept
- b<sub>1</sub> : slope

In linear regression, **the residual/error** is the difference between the actual value of a dependent variable and its predicted value based on the regression model. It's a measure of how well the model fits the data.
> Residual = | y<sub>i</sub> - ŷ<sub>i</sub> |

Our intent with this model is to find a line of best fit that reduces, as much as possible, the sum of residuals or square residuals.
> Σ<sub>i</sub> | y<sub>i</sub> - ŷ<sub>i</sub> |

This is know as **simple linear regression**. **Multiple linear regression will have the following modified formula.
> y = b<sub>0</sub> + b<sub>1</sub>x<sub>1</sub> + b<sub>2</sub>x<sub>2</sub> + ... + + b<sub>n</sub>x<sub>n</sub>

#### Assumptions

- Linearity - does the data follow a linear pathing? Do the y-values increase as the x-values do, or vice-versa? If the two increase and decrease at a similar rate, then you're probably dealing with linear data
- Independence - all the data samples in the dataset should be independent.

Normality and homoscedasticity are concepts that make use of the residual and a plot drawn from the residuals. The plot shows how our data is distributed around the line of best fit

- Normality - the data should be normally distributed around the line of best fit
- Homoscedasticity - our variance for these points should remain constant throughout

If any of these assumptions are not fulfilled, then it might not be appropriate to use linear regression

#### Evaluation

1. Mean Absolute Error (MAE): This is the average of the sum of the residual/error to describe how far off our model is.
2. Mean Squared Error (MSE): Closely related to MAE. This is the average of the sum of the square of the residuals. This method is punitive of large errors in our model and allows for differentiability.
3. Root Mean Squared Error  (RMSE): Is the square root of the MSE
4. R<sup>2</sup>/Coeff. of Determination:  
> R<sup>2</sup> = 1 - (RSS/TSS)  

RSS - sum of squared residuals: Σ<sup>n</sup><sub>i=1</sub> | y<sub>i</sub> - ŷ<sub>i</sub> |<sup>2</sup>  
TSS - total sum of squares: Σ<sup>n</sup><sub>i=1</sub> | y<sub>i</sub> - ȳ<sub>i</sub> |<sup>2</sup> 


### K-Means Clustering

K-means clustering works by grouping similar data points into clusters based on their features.  It works by itereating through a series of steps until it gets the right groups. First, it picks some random starting points, called centroids, to group the data around. Then, it looks at each data point and says "this point is closest to this centroid, so I'll put it in that group". Next, it calculates the new center of each group by finding the average of all the points in that group. Finally, it keeps repeating these steps until the groups don't change anymore or it's done a certain number of times.

### Principal Component Analysis

Prinipal component analysis helps to simplify complex data by reducing the number of features it has, while keeping the most important information. It works by making the data consistent, finding the most important relationships, identifying the most important features, keeping the top features that matter most, and finally transforming the data into a simpler form.
