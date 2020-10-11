# Data Science Salary Estimator:
## Project Overview

Created a tool to help data scientists negotiate their income when they get a job by looking at the estimated data science salaries
Scraped over 1500 job descriptions from glassdoor using python and selenium 
Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
Built a client facing API using flask
Code and Resources Used

### Python Version: 3.7
### Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
### Scraper Github: https://github.com/arapfaik/scraping-glassdoor-selenium
### Scraper Article: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
### YouTube Project Walk-Through: https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t
### Flask Productionization: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2 Project Idea: https://www.youtube.com/channel/UCiT9RITQ9PW6BhXK0y2jaeg

#Web Scraping

Tweaked the web scraper github repo (above) to scrape 1500 job postings from glassdoor.com. With each job, we got the following:
*Job title *Salary Estimate *Job Description *Rating *Company *Company Size *Company Founded Date *Type of Ownership *Industry *Sector *Revenue
