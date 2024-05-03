def check_tickets(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    wining_symbols = ["@", "#", "$", "^"]
    left_part = ticket[:10]
    right_part = ticket[10:]
    for match_symbol in wining_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            wining_symbols_repetitions = match_symbol * uninterrupted_match_length
            if wining_symbols_repetitions in left_part and wining_symbols_repetitions in right_part:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'



tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket in tickets:
    print(check_tickets(ticket))