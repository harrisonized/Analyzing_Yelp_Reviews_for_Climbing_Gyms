# Analyzing Yelp Reviews for Climbing Gyms

For this project, I analyzed [Yelp](https://www.yelp.com) customer reviews in order to gain high-level overviews or summaries about reviews on climbing gyms in California. First, given the text from a review, I wanted to be able to predict the number of stars given by the reviewer. Second, given a corpus of 1- or 5-star reviews, I wanted to be able to find the topics that best model the reviews. If I had more time, the next logical step would be to use these topics as features for my classification model to see if doing so improves my performance by reducing the modeling time without much loss of accuracy.

To obtain the data, I made an honest effort to learn how to use Yelp's [API](https://www.yelp.com/developers/graphql/guides/requests). After obtaining my API Key, I attempted to use their [online console](https://www.yelp.com/developers/graphiql) to grab the data, only to find that each query only returned 3 results and the review text is limited to the first 150 characters. I reasoned that this might be because Yelp does not want people to obtain large amounts of data through their online console, so I learned how to use [GraphQL](https://github.com/graphql-python/gql) for python, only to find the exact same result.

Hence, I had to resort to scraping Yelp, even though it is generally discouraged by the Yelp developers. In my scraping effort, I kept the data as close to the format found in the review.json and business.json files of the [Yelp Dataset](https://www.yelp.com/dataset/challenge) as possible.

After merging the review and business data, I used simple multi-class logistic regression with adjusted posterior biases in order to improve my model's performance on 2- and 3-star reviews.

Second, I used non-negative matrix factorization to obtain a list of words representing the most important topics. The topics returned provided reasonable confirmation that the topic model is performing as expected.

Lastly, I obtained some data on new gyms from the Climbing Business Journal [here](http://www.climbingbusinessjournal.com/gyms-and-trends-of-2016/), replotting it with Plotly to make it consistent with some of my other plots.

For more information, please read my blog post, which will be updated in a few days.