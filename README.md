# Grailed Clothing Price Prediction
---
## Albert Frantz
---
### *Please Note That All Data Files Were Zipped To Allow For Upload To Github*
--- 
## Purpose:
Predict the price that a piece of clothing will sell at on Grailed.com.

---
## Impact:
Increase the profit of sellers on Grailed.com by providing them with an accurate listing price for their items.

---
## Problem Statement:
Platforms like Grailed provide an easy platform for users to sell used clothing. That being said many users do not know the value of the clothing they have. Grailed does not proived price prediction services that can help users have a general idea about what the value of their items may be worth. For many that means that selling on Grailed is a guessing game when it comes to price. I am attempting to make an application that will help Grailed users have a better idea of what price they should list their item at. 

I attempt to web scrape data from Grailed.com using selenium. Ultimately, my dataset will have 100,000 postings. Using this data I will train various regression models to try and accurately model used clothing price. I will then use this model when creating a Flask application so that users can more easily get price predictions for their used clothing. 

---

## The Data
Data collection took up the bulk of work time on this project. I collected data from Grailed.com using python and selenium. My code allows for all of the sold postings to be collected, but for time constraint reasons I collected only 100,000 sold postings. I decided to collect sold postings rather than unsold postings to make a better prediction model. I collect 10 other variables excluding sale price, including things such as Designer, Color and Size. The data is labeled. 
 
---
## Cleaning the Job postings datasets

1. feedback_count column - changed NANs to 0
2. dropped remaining NANs
3. sold_price - changed to a flaot
4. category - removed the designer from the category then stripped spaces
5. category - removed all observations if category was less than 10
6. size_color_condition - Created a column for size, color, condition seperately
7. size_color_condition - dropped all rows that all 3 columns could not be created
8. condition - removed all rows of condition count less than 100
9. color - removed all rows of color count less than 100
10. size - removed all rows of size count less than 20
11. description - removed all '\n'
12. designer - change coloborations of designers into a single designer
13. designer - dropped all rows of designer count less than 25
14. dropped remaining duplicate postings

---

## Modeling
I attempted to use 5 different models to best predict clothing value:
1. Decision tree Regressor
    1. cross val mse = -14727
    2. r2 training = .996
    3. r2 testing = .078
2. Random Forest Regressor
    1. cross val mse = -10825
    2. r2 training = .889
    3. r2 testing = .420
3. Adaboost Regressor
    1. cross val mse = -21679
    2. r2 training = -.676
    3. r2 testing = -.731
4. Gradient Boost Regressor
    1. cross val mse = -27879
    2. r2 training = .853
    3. r2 testing = .323
    
Although the model was still highly overfit I decided that the random froest regressor was the best model. I determined this as it had the lowest MSE and the highest r2 testing score. The model still needs further refinement and overfitting needs to be addressed. 

---
## Flask App
Using Flask and a pickled version of the random forest model I created an easy to use form for sellers to input relevant item information to quickly recieve an estimated price value for their item. The app has yet to be deployed to Heroku.

---
 
## Going Forward
Going forward there are a few things I would like to achieve. First I would like to collect more data. Second I would like to continue to refine my model to make better predictions. Third I would like to deploy the Flask app to Heroku. Fourth I would like to add the functionality of this app directly with Grailed. 
