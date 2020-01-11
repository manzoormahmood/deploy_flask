# deploy_flask

The dataset for house price prediction was obtained from kaggle (https://www.kaggle.com/harlfoxem/housesalesprediction/)
The house price dataset is for USA. 

Procedure for github files
1.Develop the regression model(model.py) using using jyputer notebook and created houde_model.pkl file using the model and pickle lib.
2.App is the python file for flask. It is web application framework.
3.Procfile is a mechanism for declaring what commands are run by your application's dynos on the Heroku platform.
4.Template folder contains index.html, which serves as webpage for taking input from user along with a button to get the output.
5.Requirements.txt is a text file with all the necessary libraries. Created using command (pip freeze > requiremeents.txt).

Heroku is a cloud platform as a service supporting several programming languages.
Procedure for Heroku
Create a account on Heroku. As comapred to aws and azure it is free.
Create new app.
Connect your github account with Heroku.
Search for your repository in Heroku.
Then select deploy. For more detail visit this youtube link.(https://youtu.be/mrExsjcvF4o)
