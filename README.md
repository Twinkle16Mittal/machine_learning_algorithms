# machine_learning_algorithms

Learn Basics of Machine learning topics like
1. how to use Tree Models like DecisionTreeRegressor
2. how to use ensemble model liks RandomForestRegressor 

code:
Basic_Ml_Models/ learn_ml.ipynb
Data: original_data/melb_data.csv

project:
Basic_Ml_Models/housing_price_prediction.ipynb
data: original_data/Housing_price_dataset/train.csv
      original_data/Housing_price_dataset/test.csv

output: original_data/Housing_price_dataset/home_result_prediction.csv

Some Terms should be know:

n_estimators: set the number of decision trees in the algorithm
ex:, 
n_estimators=10 means the random forest will be made up of 10 different decision trees, and their outputs will be averaged to make the final prediction.

random_state = 1/0
Sets the seed for random number generation, making results reproducible.
random_state=0 ensures that the same "random" trees are built every time you run the code, so you get the same results.
But random_state=1 will produce a different set of random numbers (and thus different trees) than random_state=0.

axis = 1/0
axis 1 -> drop columns
axis 0 -> drop rows

strides -> controls how far the convolution filter moves across the input each time it slides.

strides=(1,1) (default): The filter moves one pixel at a time horizontally and vertically.

strides=(2,2) or strides=2: The filter jumps two pixels at a time in both directions, effectively downsampling the feature map (reducing its spatial resolution by about half).
