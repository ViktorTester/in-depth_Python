"""There is a list of blog_posts containing dictionaries.
The program counts the number of likes in all dictionaries.
If the dictionary does not contain the Likes key,
its value is considered equal to minus one."""

blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
              {'Likes': 13, 'Comments': 2, 'Shares': 1},
              {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
              {'Comments': 4, 'Shares': 2},
              {'Photos': 8, 'Comments': 1, 'Shares': 1},
              {'Photos': 3, 'Likes': 19, 'Comments': 3}]

total_likes = 0

for post in blog_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        total_likes -= 1

print(total_likes)
