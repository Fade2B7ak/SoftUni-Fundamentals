import re

tickets = [ticket.strip() for ticket in input().split(",")]
symbols = r"(\@{6,10}|\#{6,10}|\${6,10}|\^{6,10})"

for ticket in tickets:
    match = 0
    if len(ticket) != 20:
        print("invalid ticket")
    else:
        left_ticket_half = ticket[:10]
        right_ticket_half = ticket[10:]
        left_ticket_half = ''.join(re.findall(symbols, left_ticket_half))
        right_ticket_half = ''.join(re.findall(symbols, right_ticket_half))

        if (left_ticket_half and right_ticket_half) and (left_ticket_half[0] and right_ticket_half[0]):
            wining_symbol = left_ticket_half[0]
            match = min(len(left_ticket_half), len(right_ticket_half))
            if match < 10:
                print(f'ticket "{ticket}" - {match}{wining_symbol}')
            else:
                print(f'ticket "{ticket}" - {match}{wining_symbol} Jackpot!')
        else:
            print(f'ticket "{ticket}" - no match')
