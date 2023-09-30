"""Books on mathematics for grades 1 - 11 are on sale. There is a list that
shows all the books available. 'n' buyers come, name the class number for which
they want to purchase the book, and the amount they are willing to pay,
and if the book is in stock, it is sold.

The program calculates the total amount of money earned from book sales."""

books = list(map(int, input().split()))
total = 0

for _ in range(int(input())):
    n = list(map(int, input().split()))
    if n[0] in books:
        total += n[1]
        books.remove(n[0])

print(total)
