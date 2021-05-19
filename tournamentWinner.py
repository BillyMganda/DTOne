HOME_TEAM_WON = 1


def tournamentWinner(competitions, results):
    currentBest = ""
    scores = {currentBest: 0}

    for i, competition in enumerate(competitions):
        result = results[i]
        home, away = competition

        winningTeam = home if result == HOME_TEAM_WON else away

        updateHelper(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBest]:
            currentBest = winningTeam

    return currentBest


def updateHelper(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points

