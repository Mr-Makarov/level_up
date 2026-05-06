def play_list():
    play_list = ["trek1","trek2","trek3","trek4","trek5"]
    print(play_list)
    sound_one = play_list.index("trek1")
    sound_two = play_list.index("trek4")
    play_list[sound_one], play_list[sound_two] = play_list[sound_two], play_list[sound_one]
    print(play_list)

play_list()