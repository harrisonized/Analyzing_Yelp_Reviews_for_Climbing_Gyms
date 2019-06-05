# Analyzing Yelp Reviews for Climbing Gyms

For this project, I analyzed [Yelp](https://www.yelp.com) customer reviews in order to gain high-level overviews or summaries about reviews on climbing gyms in California.

I had two goals:

1. Given the text from a review, predict the number of stars given by the reviewer. 
2. Given a corpus of 1- or 5-star reviews, I wanted to be able to find the topics that best model the reviews. 

If I had more time, the next logical step would be to use these topics as features for my classification model to see if doing so improves my performance by reducing the modeling time without much loss of accuracy.



To obtain the data, I had to scrape Yelp. In my scraping effort, I kept the data as close to the format found in the review.json and business.json files of the [Yelp Dataset](https://www.yelp.com/dataset/challenge) as possible. I did make an honest effort to use Yelp's [API](https://www.yelp.com/developers/graphql/guides/requests), even learning how to use [GraphQL](https://github.com/graphql-python/gql) for Python, only to find that the API can only return a max of 3 results and the review text is limited to the first 150 characters. 

Data on the number of new gyms in California was obtained from the Climbing Business Journal [here](http://www.climbingbusinessjournal.com/gyms-and-trends-of-2016/). I replotted the data using Plotly to make it consistent with the rest of my plots.

For more information, please read my [blog post]("https://harrisonized.github.io/2019/06/05/Project-4.html"), which will be updated in a few days.

