class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.add_new_article(self)
        

    @classmethod
    def add_new_article(cls, new_instance):
        cls.all.append(new_instance)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
          if not hasattr(self, "_title"):
            if type(new_title) == str:
                if 5 <= len(new_title) <= 50:
                    self._title = new_title
                else:
                    raise ValueError("Title must be between 5 and 50 characters")
            else:
                raise TypeError("Name must be a string")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise TypeError("Author must be an instance of Author class")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise TypeError("Magazine must be of type Magazine")

    def __repr__(self):
        return f'<Article title="{self._title}", author="{self._author.name}", magazine="{self._magazine.name}">'     

class Author:
    def __init__(self, name):
        self._name = name
       

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not hasattr(self, "_name"):
            if isinstance(new_name, str) and len(new_name) > 0:
                self._name = new_name
            else:
                raise ValueError("Name must be longer than 0 characters")
        else:
            raise AttributeError("Name cannot be changed after the author is instantiated.")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine) and isinstance(title, str):
            new_article = Article(self, magazine, title)
            new_article.author = self
            return new_article
        else:
            raise ValueError("Invalid arguments for creating an article")


    def topic_areas(self):
       
        categories = {article.magazine.category for article in self.articles()}
        if categories:  
            return list(categories)
        else:
            return None
    
    def __repr__(self):
        return f'<Author name="{self.name}">'


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
            raise ValueError("Name must be between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            raise ValueError("Category must be longer than 0 characters")

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):

        titles = [article.title for article in self.articles()]
        
        if not titles:
            return None
        else:
            return titles

    def contributing_authors(self):
       
        author_counts = {}

        for article in self.articles():
    
            if article.author in author_counts:
                author_counts[article.author] += 1
            else:
                author_counts[article.author] = 1

       
        contributing_authors = [author for author, count in author_counts.items() if count > 2]

        return None if not contributing_authors else contributing_authors

    def __repr__(self):
        return f'<Article title="{self._title}", author="{self._author.name}", magazine="{self._magazine.name}">'