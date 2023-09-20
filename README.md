# delstat scraper - a webscraper for the penny-del statistic pages

## Goaliestats - usage and methods

```python
from delstats import DelStats

with DelStats(debug=DEBUG) as delstats:

    goaliestats = delstats.goaliestats()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/goaliestats/basis
    goaliestats.basis()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/goaliestats/schuesse
    goaliestats.schuesse()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/goaliestats/xg
    goaliestats.xg()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/goaliestats/gegentore
    goaliestats.gegentore()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/goaliestats/paesse
    goaliestats.paesse()

```

## Playerstats - usage and methods

```python
with DelStats(debug=DEBUG) as delstats:

    playerstats = delstats.playerstats()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/playerstats/basis
    playerstats.basis()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/playerstats/team-play
    playerstats.teamplay()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/playerstats/paesse
    playerstats.paesse()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/playerstats/schuesse
    playerstats.schuesse()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/playerstats/xg
    playerstats.xg()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/playerstats/skating
    playerstats.skating()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/playerstats/puckbesitz
    playerstats.puckbesitz()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/playerstats/toi
    playerstats.toi()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/playerstats/verteidigung
    playerstats.verteidigung()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/playerstats/strafen
    playerstats.strafen()

    # all the above
    playerstats.all()
```

## Tabelle - usage and methods

```python
with DelStats(debug=DEBUG) as delstats:

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/playerstats/basis
    delstats.tabelle()
```

## Teamstats - usage and methods

```python
with DelStats(debug=DEBUG) as delstats:

    teamstats = delstats.teamstats()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/teamstats/schuesse
    teamstats.schuesse()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/teamstats/team-play
    teamstats.teamplay()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/teamstats/paesse
    teamstats.paesse()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/teamstats/defensive
    teamstats.defensive()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/teamstats/puckbesitz
    teamstats.puckbesitz()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/teamstats/strafen
    teamstats.strafen()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/teamstats/special-teams
    teamstats.specialteams()

    # https://www.penny-del.org/statistik/saison-2023-24/hauptrunde/teamstats/zuschauer
    teamstats.zuschauer()

    # a single report containing all the above
    teamstats.all()
```

## Contributing

Please read [CONTRIBUTING.md](https://github.com/grindsa/delstat_scraper/blob/main/CONTRIBUTING.md) for details on my code of conduct, and the process for submitting pull requests.
Please note that I have a life besides programming. Thus, expect a delay in answering.

## License

This project is licensed under the GPLv3 - see the [LICENSE.md](https://github.com/grindsa/dkb-robo/blob/master/LICENSE) file for details
