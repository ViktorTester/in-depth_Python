"""There are two lists. The first list represents a set of sent messages in
some messenger, the second list represents a set of senders of these messages.
Moreover, the message messages[i] was sent by the user senders[i].
Each message is a sequence of words separated by a space
(punctuation marks are considered parts of words).
The word count is the total number of words submitted by the user.
Each user can send more than one message.

The function determines the sender with the most words and returns his name.
If there are several such senders, the name of the one whose name is larger
in the lexicographic comparison is returned."""

from collections import defaultdict


def best_sender(messages: list, senders: list) -> str:
    ddict = defaultdict(int)

    for i in range(len(senders)):
        ddict[senders[i]] += len(messages[i].split())

    max_value = max(ddict.values())

    arr = [key for key, value in ddict.items() if value == max_value]

    return max(arr)
