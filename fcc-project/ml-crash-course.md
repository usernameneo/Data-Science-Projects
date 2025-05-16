# ML Crash Course 

## What is Machine Learning?

Machine learning is a subdomain of computer sciences that focuse on algorithms which might help a computer learn from data without a programer telling the computer exactly what to do.

## AI vs ML vs DS

Artificial Intelligence is an area of compter science, where the goal is to enable computers and machines to perform human-like tasks and simulate himan behavior.

Machine Learning is a subset of AI that tries to solve a specific problem and make pedictions using data.

Data Science is a field that attemps to find patterns and draw insights from data.

All these fields might overlap and all of them might use Machine Learning.

## Types of Machine Learning

- **Supervised Learning** - uses labeled inputs (this means that every input we get has a correspinding output label) to train models and to learn outputs of different new inputs we might fed our model.

- **Unsupervides Learning** - used unlabeled data to learn about patterns in the data.

- **Reinforcement Learning** - usually there's some sort of agent that is learning in an interactive environment based on rewards and penalties.

A machine learning model will have a bunch of inputs, **features**, going into it and then the model will produce an output (our prediction). All the features used as inputs are what we call the **feature vectors**.

We will be focusing on supervised learning.

### Features

There are different kinds of features we can have including:

- **Qualitative** - Categorical data with a finite number of categories or groups.
- **Quantitative** - numerical valued data which could either be discrete, meaning integers, or continuos, meaning all real numbers

**Norminal data** refers to data that **has no inherent order**. One method used to feed norminal data into the computer is called **One-Hot Enocoding**. This is where a list is returned to indicate to which value a certain input belongs. E.g if we had 4 options for country for any record [USA, India, Canada, South Africa], One-Hot Encoding would return a 4 length list for each record where all values are set to 0 while the true value is set to 1 [0, 0, 0, 1]. This method returns a value of 1 for each category that the record belongs to.

**Ordinal data** refers to data that **has an inherent order**. These can be input as numbers on a scale.

Next we'll look at the types of predictions, outputs, that our models can have

### Supervised Learning Tasks

In supervised learning there are some different tasks, outputs:

1. **Clasiffication** - predict discrete classes. E.g If given 3 possible classes; a hotdog, a pizza and an ice cream; any instances of these classes can be placed under the corresponding label. This is known as **multiclass classification**. There is also **binary classification**; whether something is a hot-dog or not a hot-dog, regardless of what else it might be.

2. Regression - predict continuos values. E.g The price of a certain stock tomorrow, the temperature or the price of a house.

## Training a Model

How do we make the model learn? How can we tell whether or not it's learning?

To train a model a dataset is split into our feature vectors and our target. The feature vectors that will be used in the prediction are labeled X by convention and our target for that feature vector are labeled y. Each row of our X will be fed into our model and it will make some sort of prediction. What we then do is we compare that prediction to our y in our labeled dataset to validate the accuracy of our model. We'll continuousy adjust our model to increase its accuracy.

With our dataset, we do not want to use the entirety of the dataset to train our model. This is done in order to verify that our model can perform similarly on new, unseen data. Our dataset is thus divided into three: a training dataset, a validation dataset and a testing dataset. 

We first feed our model the training dataset and use the true values to measure our loss, in some numerical quantity, and then we make adjustments to our model. This is what we call training. The validation dataset is used a a reality check during or after training to ensure our model can handle unseen data. We can again measure our loss but this time, the loss is not feed back into training the model. Finally we use the test dataset to check how generalisable the final model is. The measured loss of the test dataset is our final reported performance for our model.

### Metrics of Performance

Loss formulae:

L1 loss = sum(|y<sub>real</sub> - y<sub>predicted</sub>|)
L1 loss is the sum of the absolute difference of the real y-value and the predicted y-value

L2 loss = sum((y<sup>real</sup> - y<sup>predicted</sup>)<sup>2</sup>)
L2 loss is the square of the difference of the real y-value and the predicted y-value

Binary Cross-Entropy Loss

loss = -1/N * sum(y<sub>real</sub> * log(y<sub>predicted>) + (1 - y<sub>real</sub>) * log((1 - y<sub>predicted</sub>)))

You just need to know that loss decreases as the performance gets better.