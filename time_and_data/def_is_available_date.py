"""During the visit of the next guest, the hotel staff has to
check whether a particular date is available for booking a room.

booked_dates - a list of string dates or a period
(two dates separated by a hyphen)
that are not available for booking.

date_for_booking is a single string date or period
(two dates separated by a hyphen)
or which the guest wishes to book a room.

The is_available_date() function returns True if the date
or period date_for_booking is fully available for booking.
Otherwise, the function returns False."""

from datetime import datetime


def is_available_date(booked_dates: list, date_for_booking: str) -> bool:
    arr, arr2 = [], []
    for i in booked_dates:
        if len(i) == 10:
            arr.append(datetime.strptime(i, '%d.%m.%Y'))
        else:
            dt = i.split('-')
            dt[0] = datetime.strptime(dt[0], '%d.%m.%Y')
            dt[1] = datetime.strptime(dt[1], '%d.%m.%Y')
            while dt[0] <= dt[1]:
                arr.append(dt[0])
                dt[0] = dt[0].toordinal() + 1
                dt[0] = datetime.fromordinal(dt[0])

    if len(date_for_booking) == 10:
        arr2.append(datetime.strptime(date_for_booking, '%d.%m.%Y'))
    else:
        dt2 = date_for_booking.split('-')
        dt2[0] = datetime.strptime(dt2[0], '%d.%m.%Y')
        dt2[1] = datetime.strptime(dt2[1], '%d.%m.%Y')
        while dt2[0] <= dt2[1]:
            arr2.append(dt2[0])
            dt2[0] = dt2[0].toordinal() + 1
            dt2[0] = datetime.fromordinal(dt2[0])

    approved = 0
    for x in arr2:
        if x not in arr:
            approved += 1

    if approved == len(arr2):
        return True
    return False