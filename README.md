# neural-experiment
A neural network from scratch in Python. Based off this guide: https://realpython.com/python-ai-neural-network/.

## Notes
These are notes on the reading itself, specially the section about AI.
In the broadest sense of the term, AI means any time a computer is used to solve a problem. For instance, a script that solves sudoku puzzles is an example of a hard-coded AI.
Machine learning and deep learning also use computers to solve problems. However, they are trained instead of hard coded.
### Machine Learning
Machine learning trains a system to solve problems. Specifically, data related to the problem is used to train a statistical model.
#### Supervised Learning
Supervised learning is a form of machine learning. A dataset of known inputs and outputs is used to train the model. The AI that results from this training is supposed to be able to predict outputs based on the inputs it receives.
Supervised learning assumes that new data it has to predict will be similar to the data it is trained on. It won't work if this isn't the case.
#### Feature Engineering
Feature is another word for input. Feature engineering means modifying a raw dataset to be more useful or easier to train on. The reading gives the example of removing inflection (tense, case, number, etc) from a dataset of words so that these extra "features" don't distract the model.
### Deep Learning
Deep learning is a subset of machine learning. What makes it different is that you don't perform feature engineering. Instead, the model is expected to learn which features do and don't matter on its own.
### Neural Networks
Neural networks do four main things.
1. Take input data
2. Make a prediction about that data
3. Compare the prediction to the desired output
4. Adjust its behavior to make better predictions
