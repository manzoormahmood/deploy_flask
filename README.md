# deploy_flask

The link for demo is (flask-deploy-github.herokuapp.com)

The dataset for house price prediction was obtained from kaggle (https://www.kaggle.com/harlfoxem/housesalesprediction/)
The house price dataset is for USA. 

Procedure for GitHub files
1. Develop the regression model(model.py) using a jupyuter notebook and create a house_model.pkl file using the model and pickle lib.
2.App.py is the python file for a flask. It is a web application framework.
3. Procfile is a mechanism for declaring what commands are run by your application's dynos on the Heroku platform.
4.The template folder contains index.html, which serves as webpage for taking input from the user along with a button to get the output.
5.Requirements.txt is a text file with all the necessary libraries. Created using command (pip freeze > requiremeents.txt).

Heroku is a cloud platform as a service supporting several programming languages.
Procedure for Heroku
Create a account on Heroku. As compared to aws and azure it is free.
Create new app.
Connect your GitHub account with Heroku.
Search for your repository in Heroku.
Then select deploy. For more detail visit this youtube link.(https://youtu.be/mrExsjcvF4o)

Here the focus was not on to increase the accuracy of the regression model, but to deploy the model on Heroku. 

