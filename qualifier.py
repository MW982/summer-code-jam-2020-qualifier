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
        pass


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

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
        self.last_edited = datetime.datetime.now()

    def __lt__(self, article):
        return self.publication_date < article.publication_date

    def __repr__(self):
        return f"<Article title=\"{self.title}\" author='{self.author}' publication_date='{self.publication_date.isoformat()}'>"

    def __len__(self):
        return len(self.content)

    def short_introduction(self, n_characters: int):
        if self.content[n_characters] in " \n":
            return self.content[:n_characters]
        else:
            return self.short_introduction(n_characters - 1)

    def most_common_words(self, n_words: int):
        words = {}
        content_non_ascii = ""
        for char in self.content.lower():
            if char in "qwertyuiopasdfghjklzxcvbnm ":
                content_non_ascii += char
            else:
                content_non_ascii += " "

        spl = content_non_ascii.split()
        maxw = 0
        curr = 0
        set_spl = []
        for word in spl:
            if not word in set_spl:
                set_spl.append(word)

        if n_words > len(set_spl):
            n_words = len(set_spl)

        for i in range(n_words):
            for word in set_spl:
                c = spl.count(word)
                if c > maxw:
                    curr = word
                    maxw = c
            set_spl.remove(curr)
            words[curr] = maxw
            maxw = 0

        return words


# fairytale1 = Article(
#     title="The emperor's new clothes",
#     author="Hans Christian Andersen",
#     content="'But he has nothing at all on!' at last cried out all the people. The Emperor was vexed, for he knew that the people were right.",
#     publication_date=datetime.datetime(1837, 4, 7, 12, 15, 0),
# )
# fairytale1.attribute = "lmao"
# print(fairytale1.id)

# fairytale2 = Article(
#     title="The emperor's new clothes",
#     author="Hans Christian Andersen",
#     content="'But he has nothing at all on!' at last cried out all the people. The Emperor was vexed, for he knew that the people were right.",
#     publication_date=datetime.datetime(1837, 4, 7, 12, 15, 0),
# )
# print(fairytale2.id)


# fairytale3 = Article(
#     title="The emperor's new clothes",
#     author="Hans Christian Andersen",
#     content="'But he has nothing at all on!' at last cried out all the people. The Emperor was vexed, for he knew that the people were right.",
#     publication_date=datetime.datetime(1837, 4, 7, 12, 15, 0),
# )
# fairytale3.attribute = "lmao"
# print(fairytale3.id)

# fairytale4 = Article(
#     title="The emperor's new clothes",
#     author="Hans Christian Andersen",
#     content="'But he has nothing at all on!' at last cried out all the people. The Emperor was vexed, for he knew that the people were right.",
#     publication_date=datetime.datetime(1837, 4, 7, 12, 15, 0),
# )
# print(fairytale4.id)
# print(fairytale4.most_common_words(5111))
