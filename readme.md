# Cat Dog Classifier

This is a image classifier project using Convolutional Neural Networks and Deep Learning. It classifies images of dogs and cats. The accuracy rate acchieved was 0.9045.
In addition, it was build an API that can receive a image transformed in array to be classified. 

## How to use it

* The image classifier model was build using tensorflow and keras;

* The data was preprocess in the Training Set and the Test Set, to prepare the images that would be used in the cnn model.

* The architecture of the CNN was build by adding the layers, pooling, adding the second cnn layer, flattening the results of all the cnn's and poolings into one dimensional vector, which will become the input of a fully conected neural network and finally conect all this to the final output layer.

* The cnn was trained then in the training set and evaluating on the test set;

* The model was saved to be used in the API;

* A single prediction was made to test if the model could classified an image as a cat or a dog.


### Requirements

The libraries used in the api can be seen in the requirements.txt.

### Using the API

* The program used to build the API was Visual Studio Code;

* Install the requirements;

* Execute api_prediction

* Make a [POST] request on /predict using:

{
	"user": " "

	"data": "imagebase64"
}


* Make a [POST] request on /predict64 with an base64 encoded image to get a prediction.

## References

Udemy course Deep Learning A-Z™: Hands-On Artificial Neural Networks by Kirill Eremenko, Hadelin de Ponteves, SuperDataScience Team

https://flask.palletsprojects.com/en/1.1.x/quickstart/

https://towardsdatascience.com/keras-save-model-and-keras-load-model-d516d6234776

https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask


## Author

Rodrigo Roth Vasconcellos
