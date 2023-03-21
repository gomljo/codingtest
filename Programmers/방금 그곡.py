def get_score_length(score):
    new_score = score.replace('#', '')

    return len(new_score)


def change_score_sharp(score):
    changed_score = ''
    splited_score = score.split('#')

    if len(splited_score) > 1:

        for i in range(len(splited_score)):
            new_score = list(splited_score[i])
            if i < len(splited_score) - 1:
                new_score[-1] = new_score[-1].lower()
            changed_score += ''.join(new_score)
    else:
        changed_score += ''.join(splited_score)
    return changed_score


def get_time_token(time):
    token = time.split(':')
    hour, minute = int(token[0]), int(token[1])

    return [hour, minute]


def time_processing(start, end):
    play_minute = 0
    hour = 60

    end_hour = end[0]
    end_minute = end[1]

    start_hour = start[0]
    start_minute = start[1]

    if end_hour == start_hour:
        play_minute = end_minute - start_minute
    else:
        elapsed_hour = end_hour - start_hour

        end_minute = hour * elapsed_hour
        play_minute = end_minute - start_minute

    return play_minute


def solution(m, musicinfos):
    answer = ''

    changed_melody = change_score_sharp(m)

    song_dict = dict()

    for order, info in enumerate(musicinfos):
        items = info.split(',')
        start, end, name, score = items[0], items[1], items[2], items[3]

        score_length = get_score_length(score)
        changed_score = change_score_sharp(score)

        start_time = get_time_token(start)
        end_time = get_time_token(end)

        played_minutes = time_processing(start_time, end_time)

        iteration = played_minutes // score_length
        reminder = played_minutes % score_length

        played_song = changed_score * iteration + changed_score[:reminder]
        song_dict[name] = [order, played_minutes, played_song]

    possible_answers = list()
    for name in song_dict.keys():

        enter_order = song_dict[name][0]
        played_time = song_dict[name][1]
        played_song = song_dict[name][2]
        if changed_melody in played_song:
            possible_answers.append([enter_order, played_time, name])

    sorted_possible_answers = sorted(possible_answers, key=lambda x: (-x[1], x[0]))

    answer = sorted_possible_answers[0][2]
    return answer


song = 'BB#A#'

print(change_score_sharp(song))