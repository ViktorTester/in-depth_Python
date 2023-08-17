"""There is a name_log.csv file, which contains the username change
logs. The first column shows the username that was changed,
the second column shows the email address, and the third column
shows the date and time the change was made. At the same time,
the user cannot change the email, only the name.

The program selects only the most recent entries for each user from
the name_log.csv file and writes them to the new_name_log.csv file.
In the new_name_log.csv file, the first line is the column headings,
the same as in the name_log.csv file. The logs in the final file are
arranged in the lexicographic order of the names of the user's e-mail boxes."""
