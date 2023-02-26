# TMMSM_Project
Final project for Text Mining and Social Media Mining (2022 Winter) course - Analyzing men and women comments on Reddit using NLP methods                          

Project:

The purpose of this project is to analyze differences in comments between sexes and on posts titles made on /r/AskMen and /r/AskWomen subreddits on Reddit.

It is hypothesized that women tend to use milder language with positive sentiment while men tend to use rougher language with mostly negative sentiment. To analyze the sentiment the Valence Aware Dictionary and Sentiment Reasoner (VADER) was used. Additionally predictions of comments and posts origin were made according to the subreddits in order to check whether based user submissions characteristic were distinct enough for model to predict the differences.

The data was scraped using Reddit API and PRAW python library.

The results regarding sentiment analysis showed that both men and women comments and posts were classified as relatively more negative than positive. Women were slightly less relatively negative than men, which could suggest that they do in fact use milder and more positive language than men. Predictions results for categorization of comments and posts were very high, with origin of posts predictions close to 99% for both training and test dataset splits. Prediction results really underline differences between /r/AskMen and /r/AskWomen subreddits user submissions - both comments and posts. 