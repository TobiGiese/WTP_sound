from datetime import datetime

now = datetime.now()

WTP_GAMES_SATURDAY = {
    "game1": {
        "start":    datetime(year=2019,month=6,day=15,hour=10,minute=0),
        "5min":     datetime(year=2019,month=6,day=15,hour=10,minute=40),
        "end":      datetime(year=2019,month=6,day=15,hour=10,minute=45)
    },
    "game2": {
        "start":    datetime(year=2019, month=6, day=15, hour=11, minute=0),
        "5min":     datetime(year=2019, month=6, day=15, hour=11, minute=40),
        "end":      datetime(year=2019,month=6,day=15,hour=11,minute=45)
    },
    # ...
}

WTP_GAMES_SUNDAY = {
    "game1": {
        "start":    datetime(year=2019,month=6,day=16,hour=10,minute=0),
        "5min":     datetime(year=2019,month=6,day=16,hour=10,minute=40),
        "end":      datetime(year=2019,month=6,day=16,hour=10,minute=45)
    },
    "game2": {
        "start":    datetime(year=2019, month=6, day=16, hour=11, minute=0),
        "5min":     datetime(year=2019, month=6, day=16, hour=11, minute=40),
        "end":      datetime(year=2019,month=6,day=16,hour=11,minute=45)
    },
    # ...
}

TEST_SCHEDULE = {
    "game1": {
        "start":    datetime(now.year,now.month, now.day,now.hour, now.minute),
        "5min":    datetime(now.year,now.month, now.day,now.hour, now.minute+1),
        "end":    datetime(now.year,now.month, now.day,now.hour, now.minute+2),

    },
    "game2": {
        "start":    datetime(year=2019,month=6,day=13,hour=17,minute=30),
        "5min":     datetime(year=2019,month=6,day=13,hour=17,minute=31),
        "end":      datetime(year=2019,month=6,day=13,hour=17,minute=32)
    },
    # ...
}