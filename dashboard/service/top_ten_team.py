import operator
from dashboard.models import TopTenTeam, Team
from dashboard.service.predict_team_outcome import PredictTeamWin

class TopTenTeamService:

    def __init__(self, engine):
        self.engine = engine

    def top_ten_teams(self):
        all_teams_dict = Team.objects.all().values('name')
        all_teams = [x['name'] for x in all_teams_dict]
        #all_teams = Team.objects.all().values_list('name', flat = True)
        print('this is the team name {}'.format(all_teams))

        top_ten = {}
        for team in all_teams:
            top_ten[team] = 0;

        engine = self.engine
        predict = PredictTeamWin(engine)

        k=0
        for blue_team in all_teams[: -1]:
            print('{}. team : {}'.format(k, blue_team))
            k += 1
            for red_team in all_teams[all_teams.index(blue_team) + 1 :]:
                predict_single_game = predict.predict_on_single_game(blue_team, red_team)
                blue_prob = predict_single_game.get(blue_team)
                red_prob = predict_single_game.get(red_team)
                if blue_prob > red_prob:
                    top_ten[blue_team] += 1
                else:
                    if red_prob > blue_prob:
                        top_ten[red_team] += 1
                    else:
                        top_ten[red_team] += + 0.5
                        top_ten[blue_team] += 0.5
                # 2nd round: change the sides
                #
                predict_single_game = predict.predict_on_single_game(red_team, blue_team)
                blue_prob = predict_single_game.get(blue_team)
                red_prob = predict_single_game.get(red_team)
                if blue_prob > red_prob:
                    top_ten[blue_team] += 1
                else:
                    if red_prob > blue_prob:
                        top_ten[red_team] += 1
                    else:
                        top_ten[red_team] += 0.5
                        top_ten[blue_team] += 0.5

        sorted_teams_and_wins = sorted(top_ten.items(),  key=operator.itemgetter(1), reverse=True) #tuples
        #print("top ten sorted : --- {}".format(sorted_teams_and_wins))
        a = range(1, len(sorted_teams_and_wins) + 1)
        tt = zip(sorted_teams_and_wins, a)

        #delete all records 1st:
        TopTenTeam.objects.all().delete()

        for item, r in tt:
            t10 = TopTenTeam.objects.create(name = item[0], score = item[1], rank = r)

        #well, not returning anything
        #sorted_teams = [ x[0] for x in sorted_teams_and_wins ]
        #print("sorted list : --- {}".format(sorted_teams))
        #return sorted_teams

