# espn_soccer_results

scrape (with scrapy) all today's soccer results from ESPN (espnfc.com) including results and 
team stats like shots on goal, cards, ball possession, fouls and corner kicks.
The team stats are not available for all matches.

here is example JSON output of CL match between AS Roma and Bate Borisov on 09-Dec-2015:

{'attendance': u'29489',
 'away_corner_kicks': u'1',
 'away_fouls': u'14',
 'away_offsides': u'1',
 'away_possession': u'47%',
 'away_red_cards': u'0',
 'away_saves': u'9',
 'away_shots': u'8',
 'away_shots_on_goal': u'2',
 'away_team': u'bate borisov',
 'away_yellow_cards': u'0',
 'date': '2015-12-09 20:45:00.000000',
 'home_corner_kicks': u'7',
 'home_fouls': u'12',
 'home_offsides': u'1',
 'home_possession': u'53%',
 'home_red_cards': u'0',
 'home_saves': u'2',
 'home_shots': u'24',
 'home_shots_on_goal': u'9',
 'home_team': u'as roma',
 'home_yellow_cards': u'0',
 'league': u'uefa champions league',
 'match_id': u'434177',
 'match_url': 'http://www.espnfc.com/gamecast/statistics/id/434177/statistics.html',
 'ms': u'1449690300000',
 'result': u'0 - 0',
 'result_time': u'ft',
 'stadium': u'stadio olimpico, italy'}
