def minion_game(string):
    string = string.upper()
    winner = ""
    player_one_points = 0
    player_two_points = 0

    all_player_one_input = []
    all_player_two_input = []

    should_add_points_player_one = True
    should_add_points_player_two = True
    while winner == "":
        should_add_points_player_one = True
        print 'player 1'
        player_one_input = str(raw_input()).upper()
        for old_guess in all_player_one_input:
            if old_guess == player_one_input:
                print "already guessed"
                should_add_points_player_one = False

        if should_add_points_player_one == True:
            all_player_one_input.append(player_one_input)
            player_one_points += (string.count(player_one_input))
            print "Player 1 total points: ", player_one_points


        should_add_points_player_two = True
        print "player 2"
        player_two_input = str(raw_input()).upper()
        for old_guess in all_player_two_input:
            if old_guess == player_two_input:
                print "already guessed"
                should_add_points_player_two = False

        if should_add_points_player_two == True:
            all_player_two_input.append(player_two_input)
            player_two_points += (string.count(player_two_input))
            print "Player 2 total points: ", player_two_points




if __name__ == '__main__':
    s = str(raw_input())
    minion_game(s)
