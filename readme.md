<img width="388" alt="question2" src="https://user-images.githubusercontent.com/62911364/99906756-6d970200-2c9e-11eb-90c8-142bda403093.png">

# GitHub Repo Language Prediction Project

### Author: Ryvyn Young & George Arredondo

## Description: 
Can the primary programming language of the repository be determine through Natural Language Processing analysis of the readme text?
Scrape GitHub repos and collect a minimum 100 sample dataset to use for analysis.
Using NLP clean and prepare the data, then Explore and build a model using ML algorithms to predict the language of the repo.

## Instructions for Replication
Python scripts contain functions for Acquiring, Preparing, and Wrangling the data.
The Jupyter Notebook contains all Exploration and Modeling information.
Modeling functions are located in the model.py file

## Key Findings
Our top three models performed well on the train dataset, however, when used on unseen data the accuracy was significantly reduced. The reduction of our data set of the 4 most popular languages could of played a role in the reduction of our accuracy, as the validate and test distribution could of been unevenly distributed.


**Best Performing Model**
Our best performing model uses a Logistic Regression algorithm and TF-IDF to vectroize the text.
This model increased the prediction accuracy from a baseline of 35% to an average of 47% on unseen data.

**Possible Next Steps**
The current clean and prepare methods eliminate text symbols not in English as noise. Would recommend either obtaining new dataset of only English repos or otherwise adjusting for non-English text as our basic clean did remove a lot of non english words. We identified lists of specific words that were unique to each language, but were unable to incorporate those lists into features. Increasing the size of the dataset may help improve future models. Also, we may oversample the least occuring languages to have a more evenly distributed data set or reduce the most common language. 


## Project Organization
```
 Project [repo](https://github.com/Data-Investigators/nlp_environmental_project)
├── README.md     <- The top-level README for developers using this project.
│
├── acquire_ry.py    <- The script to generate data
├── ry-prepare.py    <- The script for preparing the raw data
├── ry_wrangle.py    <- The script for running the acquire and prepare functions, then splitting the data
├── explore.py    <- The script to produce visualizations for the notebook
├── model.py      <- The script to produce models and return results to the notebook
│
├── drafts folder     <- Contains all work done leading up to final.ipynb
│
├── final.ipynb   <- The finished notebook for presentation of the project
```

## Data Dictionary
| Field Name  | Data in field                       | Data Type |
|-------------|-------------------------------------|-----------|
| language    | text, programing language           | category  |
| content     | text, original scraped text         | object    |
| clean       | text, original text cleaned         | object    |
| stemmed     | cleaned and stemmed text            | object    |
| lemmatized  | cleaned and lemmatized text         | object    |
| words       | list of words in readme             | object    |
| doc_length  | count of words in readme            | int64     |


*****
## Project Description:
For this project, you will be scraping data from GitHub repository README files. The goal will be to build a model that can predict what programming language a repository is, given the text of the README file.

## GOALS:
Can we predict what language is being used based on the README.md documentation

## MVP Questions to answer:
- Where will the data come from?
    - GitHub repos with 'environmental' in search, sorted by Best Match
- What languages will we focus on?
    - Top 4 in dataset = Python, JavaScript, HTML, Java
- Are there words that need to be removed to reduce noise?
    - Yes, 'file', 'data', and 'environmental' occur in the top 5 words for all languages, these have been filtered out
    - Remaining duplicated word = 'sensor' in Top 5 of Python and JavaScript only
Is the dataset balanced?
    - Yes, the proportions represented range from 17%-35%
- Is there a significant difference in the mean length of the readme from the overall mean by language?
    - Only for HTML, there is not a significant difference for the other 3 languages
- Visualize the proportion of the Top 20 words in the dataset by language
- Build a predictive Model to determine the language of the repo from the readme text

## Delivery
- Jupyter notebook that contains your analysis
- One or two google slides suitable for a general audience that summarize your findings
- 5 min presentation


