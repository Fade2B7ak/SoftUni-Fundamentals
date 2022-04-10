def pianist():
    number_of_pieces = int(input())
    pieces = {}
    while True:
        command = input().split("|")
        if command == 'Stop':
            break
        elif command == 'Add':
            command_prob = command[0]
            piece = command_prob[1]
            composer = command_prob[2]
            key = command_prob[3]
            if piece


        elif command == 'Remove':
            pass
        elif command == 'ChangeKey':
            pass


pianist()