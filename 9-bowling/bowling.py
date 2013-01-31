def get_score(frames):
    frame_scores = [frame_score(frame) for frame in frames.split('|')]
    scores = [frame_score_to_scoring_tuple(score) for score in frame_scores]

    total_score = 0
    for f, score in enumerate(scores):
        if f < 10:
            total_score += score[0]
            if score[1] > 0:
                total_score += frame_scores[f + 1][0]
            if score[1] == 2:
                next = frame_scores[f + 1][1]
                if next:
                    total_score += next
                else:
                    total_score += frame_scores[f + 2][0]

    return total_score


def frame_score(frame):
    # Turns tuple of strings into tuple of integer scores
    score_1 = point_str_to_int(frame[0])

    if len(frame) == 1:
        score_2 = None
    else:
        if frame[1] == '/':
            score_2 = 10 - score_1
        else:
            score_2 = point_str_to_int(frame[1])

    return (score_1, score_2)


def point_str_to_int(point):
    scores = {
                'X': 10,
                '-': 0
             }

    return scores[point] if point in scores else int(point)


def frame_score_to_scoring_tuple(frame_score):
    if frame_score[1] is None:
        score = frame_score[0]
    else:
        score = sum(frame_score)

    if score == 10:
        bonus = 2 if frame_score[0] == 10 else 1
    else:
        bonus = 0

    return (score, bonus)