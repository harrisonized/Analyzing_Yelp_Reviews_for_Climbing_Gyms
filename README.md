# Analyzing Yelp Reviews for Climbing Gyms

For this project, I analyzed [Yelp](https://www.yelp.com) customer reviews in order to gain high-level overviews or summaries about reviews on climbing gyms in California.

I had two separate, but related goals. First, given the text from a review, I wanted to classify the review as being a 1, 2, 3, 4, or 5 star review. Second, given a corpus of 1- or 5-star reviews, I wanted to be able to find the topics that best model the reviews. If I had more time, the next logical step would be to use these topics as features for my classification model to see if doing so improves my performance by reducing the modeling time without much loss of accuracy.

To obtain the data, I made an honest effort to learn how to use Yelp's [API](https://www.yelp.com/developers/graphql/guides/requests). After obtaining my API Key, I attempted to use their [online console](https://www.yelp.com/developers/graphiql) to grab the data, only to find that each query only returned 3 results and the review text is limited to the first 150 characters. I reasoned that this might be because Yelp does not want people to obtain large amounts of data through their online console, so I learned how to use [GraphQL](https://github.com/graphql-python/gql) for python, only to find the exact same result.

Hence, I reluctantly had to resort to scraping Yelp, even though it is generally discouraged. My scraping notebooks represent my best effort to return data in the same format as found in the review.json and business.json files of the [Yelp Dataset](https://www.yelp.com/dataset/challenge).

After merging the review and business data, I obtained a preliminary model using simple multi-class logistic regression and was able to adjust the weights of the multi-class logistic regression to balance the class predictions, thus improving my model's performance on 2- and 3-star reviews.

Finally, I used non-negative matrix factorization in order to obtain a list of words representing the most important topics. This is a quick and qualitative sanity check, because the topics are reasonable within the class they represent (for example, 5-star reviews contained reviews about "day passes" or "membership").

For more information, please read my blog post, which will be up in a few days.