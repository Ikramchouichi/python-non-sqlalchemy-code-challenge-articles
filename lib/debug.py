#!/usr/bin/env python3
import ipdb;


from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    magazine = Magazine("Vogue", "Fashion")
    author1 = Author("agatha crusty")
    author2 = Author("Fyodor Dostoevsky")
    article1 = Article(magazine, author1, "How to wear a tutu with style")
    article1 = Article(magazine, author2 , "How to wear a tutu with style")
    
ipdb.set_trace()
