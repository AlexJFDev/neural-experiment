# neural-experiment
A neural network from scratch in Python. Based off this guide: https://realpython.com/python-ai-neural-network/.

## Notes
These are notes on the reading itself, specially the section about AI.\
In the broadest sense of the term, AI means any time a computer is used to solve a problem. For instance, a script that solves sudoku puzzles is an example of a hard-coded AI.\
Machine learning and deep learning also use computers to solve problems. However, they are trained instead of hard coded.
### Machine Learning
Machine learning trains a system to solve problems. Specifically, data related to the problem is used to train a statistical model.
#### Supervised Learning
Supervised learning is a form of machine learning. A dataset of known inputs and outputs is used to train the model. The AI that results from this training is supposed to be able to predict outputs based on the inputs it receives. An important note is that supervised learning assumes that new data it has to predict will be similar to the data it is trained on. It won't work if this isn't the case.
#### Feature Engineering
Feature is another word for input. Feature engineering means modifying a raw dataset to be more useful or easier to train on. The reading gives the example of removing inflection (tense, case, number, etc) from a dataset of words so that these extra "features" don't distract the model.
### Deep Learning
Deep learning is a subset of machine learning. What makes it different is that you don't perform feature engineering. Instead, the model is expected to learn which features do and don't matter on its own. Deep learning models use neural networks.
#### Neural Networks
Neural networks do four main things.
1. Take input data
2. Make a prediction about that data
3. Compare the prediction to the desired output
4. Adjust its behavior to make better predictions

Neural networks use vectors, layers, and linear regression.\
In this context, vectors mean tuples and they are used to store data.\
Layers transform the data (vector) that comes from the previous layer. 
#### Training
Training a neural network is a process of trial and error. In a neural network, it starts with random weights and biases, gets input, makes a prediction, and adjusts its weights and biases to predict more accurately next time around.

Basically all a neural network does is perform these operations using vectors. Vectors are used because the dot product allows for easy comparison. When a dot product is 0 that means the vectors are not similar when a dot product is something other than 0 that means the vectors are similar.
#### Linear Regression
Linear regression is used to estimate the relationship between a dependent variable and two or more independent variables. The approximation that is made is linear.\
Linear regression works by multiplying each input by its corresponding weight and then adding the bias. This is what each neuron in a neural network does.
#### Activation Functions
If only linear operations are used, then the model only needs to be one layer deep. This is because of the associative property. Consider if the first layer multiplied by 2 and then the second layer multiplied by 3. This is the same as multiplying by 6. So you could just have one layer that multiplies by 6 instead.

The tutorial uses the sigmoid activation function.
```
S(x) = 1 / (1 + e^-x)
```
#### Prediction Error
Once the network has made a prediction, you need to compute how wrong the model was. This is called the error. This tutorial uses mean squared error because it always results in a positive number.
```
mse = (prediction - target)^2
```
#### Error Reduction
The MSE can be plotted as a function. (prediction - target) is on the x axis and (prediction - target)^2 is on the y axis. A point on the left side of the graph (x < 0) has a prediction less than the target and a point on the right side of the graph (x > 0) has a prediction greater than the target. The goal of error reduction is to bring x, and therefore the error to 0.

Using a derivative of the MSE, you can determine how to update the weights. The derivative of the MSE is:
```
d_mse = 2 * (prediction - target)
```
If the derivative is positive, then the prediction was too large so the weights should be reduced. If the derivative is negative, then the prediction was too small so the weights should be increased. Once you have the derivative, it should be multiplied by the learning rate or alpha value. Typically this is 0.1, 0.01, or 0.001. Finally, subtract the derivative from the weights.
##### Chain Rule
