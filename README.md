# Similarity between genres by analyzing blurbs using Natural Language Processing

## Key Terms:
**Blurb:** A blurb is a short description of a book, film, or other product written for promotional purposes. Book blurbs are usually around 200 words.

**Genre:** A style or category of literature. In this repository genre is used interchangeably with category of books(including non-fiction). This is an EDA done on the data gotten from scraping okadabooks, an e-book store. More details on the webcrawler [here](https://github.com/EdidiongEsu/okadabooks_scraper). 

Okadabooks is a popular online store for african literature, based in Nigeria. Since the company was founded in 2013, it has helped increase the reading culture in the country and pioneered a lot of writing initiatives. For more info, check the [website](https://okadabooks.com.).

## Aim:
In this repository I tried to answer some questions:
- Are blurbs accurate representation of books?
- Can blurbs be used to differentiate categories of books?
- Similarities between different genres of books/novels using Natural Language Processing.

## Choosing the genres to be used for analysis
In okadabooks.com, there are 22 categories/genres of books. To increase my chances of having an accurate result, I choose genres with at least a total number of 100,000  words. In total there are about 1.12 Million blurb words used in all categories.


![](https://github.com/EdidiongEsu/genre_NLP/blob/master/img/books_total.PNG)

From my results, I went with romance, religious, self_help (also called Motivational) and fiction categories. I also created a datframe of 2000 rows from random books from all the choosen(4) categories.

### Are Blurbs accurate representation of books? / Can blurbs be used to differentiate categories of books?
  The first question helps answer the second.
  Yes, to an extent. The most common words in the choosen categories gave insights into these questions. 
  
 ![most common words](https://github.com/EdidiongEsu/genre_NLP/blob/master/img/most_common_words.PNG)
  
  When a person looks for a romantic novel, he/she is looking for some kind of **LOVE** story. For religious books, it is inevitabe not to see words like **GOD**, **CHURCH**. Most motivational books(self help) usually talk about tips on how to be **SUCCESSFUL** within a span of **TIME**. Fiction in the easiest terms is some kind of **STORY**.

#### Quick deductions
A lot more deductions were made (more details in code sheet) from the  most common words in the genres:
* There are a lot of repeated words throughout the genres. The drastic difference between the total length of words in the norm_blurb and the Number of unique words explains this.
* God, christ,Jesus are the most common 10 words in the religious category. This was somewhat expected. It might also suggest that a lot of religious books are of christian religion.
* Success is mentioned a lot in self help books (also known as motivational books) which tend to preach motivate/ give tips for prosperity.
* God is the 10th most common word in **SELF HELP(MOTIVATIONAL) BOOKS**. This suggest that success is sometimes linked with spiritual aspects of life.
* Love is the most common word in the romance genre. This concludes that blurbs are indeed an avid representation of the romance genre.
* Some of the words suggest there are many words with grammatical contractions, example dont's that are used in the blurb content.
* There are more lexical terms in the religious books blurb/description which suggests that the average length of the number of words per book might be longer than the others. To look further into this, A function was created to calculate the average length of words per blurb.


## Similarities between different genres of books/novels using Natural Language Processing.
How similar are these genres? Which is most similar? Which is least similar? Since blurbs are avid representation of whole books, they can be used to calculate similarities betweeen these categories. In this readme, I will focus only on the similarities between religion and the remaining categories of books.

After [stopwords](https://en.wikipedia.org/wiki/Stop_words) were removed from all choosen blurbs, [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) was used in calculating similarities between each category. To visualize this similarity, a donut plot was used.

![](https://github.com/EdidiongEsu/genre_NLP/blob/master/img/jaccardPlot.jpg)

Excluding self similarity of religion to religion, religion is most similar to self help(motivational books) by approximately 34%. This strengthens a deduction that was made above that motivation/success/prosperity is usually linked with the religious/spiritual aspects of life. If you have read both self_help books and religious books, do you agree with this statement? To further expantiate on this, I checked for the 10 most common words that were used in both religious and selfhelp category.

![](https://github.com/EdidiongEsu/genre_NLP/blob/master/img/religion_to_selfhelp.PNG)

For more details, look at my jupyter notebook file in this repository. To get data used, check my [repository](https://github.com/EdidiongEsu/okadabooks_scraper).

**Happy Coding**


