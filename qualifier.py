"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        self.field_type = field_type
        self.name = ""
        self.values = {}

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, obj, value):
        if isinstance(value, self.field_type):
            self.values[obj] = value
        else:
            raise TypeError(
                f"expected an instance of type '{self.field_type.__name__}' for attribute '{self.name}', got '{type(value).__name__}' instead"
            )

    def __get__(self, obj, owner):
        return self.values[obj]


class Article:
    """The `Article` class you need to write for the qualifier."""

    counter = -1

    def __init__(
        self, title: str, author: str, publication_date: datetime.datetime, content: str
    ):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content
        self.last_edited = None
        Article.counter += 1
        self.id = Article.counter

    def __gt__(self, article):
        return self.publication_date > article.publication_date

    def __eq__(self, article):
        return self.publication_date == article.publication_date

    def __lt__(self, article):
        return self.publication_date < article.publication_date

    def __repr__(self):
        return f"<Article title=\"{self.title}\" author='{self.author}' publication_date='{self.publication_date.isoformat()}'>"

    def __len__(self):
        return len(self.content)

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
        self.last_edited = datetime.datetime.now()

    def short_introduction(self, n_characters: int):
        if self.content[n_characters] in " \n":
            return self.content[:n_characters]
        else:
            return self.short_introduction(n_characters - 1)

    def most_common_words(self, n_words: int):
        result = {}
        if n_words < 0:
            return result

        # Get rid of non-alphabet characters
        content_non_ascii = ""
        for char in self.content.lower():
            if char in "qwertyuiopasdfghjklzxcvbnm ":
                content_non_ascii += char
            else:
                content_non_ascii += " "

        words = content_non_ascii.split()
        max_value, current_value = 0, 0

        # Create list without word duplicates
        ordered_words = []
        for word in words:
            if not word in ordered_words:
                ordered_words.append(word)

        if n_words > len(ordered_words):
            n_words = len(ordered_words)

        for i in range(n_words):
            for word in ordered_words:
                count = words.count(word)
                if count > max_value:
                    current_value = word
                    max_value = count
            ordered_words.remove(current_value)
            result[current_value] = max_value
            max_value = 0

        return result
