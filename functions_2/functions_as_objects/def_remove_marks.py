"""The remove_marks() function takes two arguments in the following order:

text - arbitrary string
marks - character set

The function also has a count attribute,
which represents the number of calls to this function."""


def remove_marks(text: str, marks: str) -> str:
    remove_marks.count += 1
    answer = ''
    for i in text:
        if i not in marks:
            answer += i
        else:
            continue
    return answer


remove_marks.count = 0
