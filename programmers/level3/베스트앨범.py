"""
장르별, 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시
1. 속한 노래가 많이 재생된 장르를 먼저 수록
2. 장르 내에서 많이 재생된 노래를 먼저 수록
3. 장르 내에서 재생 횟수가 같다면 고유번호가 낮은 노래를 먼저수록
"""
from pprint import pprint

# genres = ["classic", "pop", "classic", "classic", "pop"]
genres = ["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"]

# plays = [500, 600, 150, 800, 2500]
plays = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
from collections import defaultdict


def solution(genres, plays):
    playlists = defaultdict(list)

    for i in range(len(genres)):
        playlists[genres[i]].append([plays[i], i])
    # pprint(playlists)

    idxs = []
    # 각각의 장르의 재생횟수를 통한 순서정립
    for key, values in playlists.items():
        playlists[key].sort(key=lambda x: [x[0], -x[1]])

        temp = 0
        for v in values:
            temp += v[0]

        idxs.append([temp, key])
    idxs.sort(key=lambda x:-x[0])

    # pprint(playlists)
    # print(idxs)

    cnt = len(genres)
    idx = 0

    answer = []
    while 1:

        for _ in range(2):
            answer.append(playlists[idxs[idx][1]].pop()[1])
            cnt -= 1

            if len(playlists[idxs[idx][1]]) == 0:
                idx += 1

        if cnt <= 1:
            break

    return answer


print(solution(genres, plays))
