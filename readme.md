# Cat Dog Classifier

This is a image classifier project using Convolutional Neural Networks and Deep Learning. It classifies images of dogs and cats. The accuracy rate acchieved was 0.8597.
In addition, it was built an API that can receive an encoded image in base64 to be classified. 
A database was created to store the user, prediction and timestamp getted from the API.

## How to use it

* The image classifier model was built using tensorflow and keras;

* The data was preprocessed in the Training Set and the Test Set, to prepare the images that would be used in the cnn model.

* The architecture of the CNN was built by adding the first convolutional layer, than pooling, adding the second cnn layer, than flattening the results of all the cnn's and poolings into one dimensional vector, which will become the input of a fully conected neural network and finally conect all this to the final output layer.

* The cnn was trained then in the training set and evaluating on the test set;

* The model was saved to be used in the API;

* A single prediction was made to test if the model could classified an image as a cat or a dog.


### Requirements

The libraries used in the api can be seen in the requirements.txt.

### Using the API

* The program used to build the API was Visual Studio Code;

* Install the requirements;

* Execute api_prediction

* Make a [POST] request on /predict64 using:

{

	"user": " ",

	"image": "imagebase64"
}


* Make a [POST] request on /predict64 with an base64 encoded image to get a prediction.

* The user, prediction and timestamp will be added in the database created.

## References

Udemy course Deep Learning A-Z™: Hands-On Artificial Neural Networks by Kirill Eremenko, Hadelin de Ponteves, SuperDataScience Team

https://flask.palletsprojects.com/en/1.1.x/quickstart/

https://towardsdatascience.com/keras-save-model-and-keras-load-model-d516d6234776

https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask


## Author

Rodrigo Roth Vasconcellos
