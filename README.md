# Similarity between Genres using Natural Language Processing

## Key Terms:
**Blurb:** A blurb is a short description of a book, film, or other product written for promotional purposes.

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

### Are Blurbs accurate representation of books?
  Yes, to an extent. The most common words in the choosen categories gave an insight into this question. 
  
 ![most common words](https://github.com/EdidiongEsu/genre_NLP/blob/master/img/most_common_words.PNG)
  
  When a person looks for a romantic novel, he/she is looking for some kind of **LOVE** story. For religious books, it is inevitabe that words like God, 
