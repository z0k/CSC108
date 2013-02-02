REGULAR_TICKET_PRICE = 3.99
STUDENT_TICKET_PRICE = 2.99

def total_ticket_price(regular_tickets, student_tickets, holiday):
    ''' (int, int, bool) -> float

    >>> total_ticket_price(1, 2, True)
    9.4715
    >>> total_ticket_price(5, 10, False)
    44.86500000000001

    Return the total ticket price after applying discounts (holiday or
    no holiday) given the number of regular tickets and student tickets.
    '''

    if holiday:
        return (REGULAR_TICKET_PRICE * regular_tickets + STUDENT_TICKET_PRICE * student_tickets) * 0.95
    else:
        return (REGULAR_TICKET_PRICE * regular_tickets + STUDENT_TICKET_PRICE * student_tickets) * 0.90
