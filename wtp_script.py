"""
Mutes the volume of all processes, but unmutes chrome.exe process.
"""
from pycaw.pycaw import AudioUtilities
import time
from datetime import datetime
from playsound import playsound
from wtp_schedules import *
import os

project_root = os.path.dirname(os.path.dirname(__file__))+"/wtp_project"

def run_start_jingle():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == "Spotify.exe":
            volume.SetMute(1, None)
            playsound(project_root+"/wtp_jingles/start.mp3")
            volume.SetMute(0,None)
            return
    playsound(project_root+"/wtp_jingles/start.mp3")


def run_5min_jingle():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == "Spotify.exe":
            volume.SetMute(1, None)
            playsound(project_root+"/wtp_jingles/5min.mp3")
            volume.SetMute(0,None)
            return
    playsound(project_root+"/wtp_jingles/5min.mp3")


def run_end_jingle():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == "Spotify.exe":
            volume.SetMute(1, None)
            playsound(project_root+"/wtp_jingles/end.mp3")
            volume.SetMute(0,None)
            return
    playsound(project_root+"/wtp_jingles/end.mp3")


def main():
    game_started = False
    last_5_min = False
    game_ended = True
    printed = False
    while(True):
        if not printed:
            print("checking for next schedule ...")
            printed = True
        for game in TEST_SCHEDULE:
            for time in ["start", "5min", "end"]:
                now = datetime.now()
                current_time = datetime(now.year,now.month, now.day,now.hour, now.minute)

                if time == "start" \
                        and TEST_SCHEDULE[game][time] == current_time \
                        and game_ended \
                        and not game_started:
                    print("playing start jingle")
                    run_start_jingle()
                    game_started = True
                    game_ended = False
                    last_5_min = False
                    printed = False
                elif time == "5min" \
                        and TEST_SCHEDULE[game][time] == current_time \
                        and game_started \
                        and not last_5_min:
                    print("playing 5min jingle")
                    run_5min_jingle()
                    last_5_min = True
                    game_started = True
                    game_ended = False
                    printed = False
                elif time == "end" \
                        and TEST_SCHEDULE[game][time] == current_time \
                        and game_started and last_5_min \
                        and not game_ended:
                    print("playing end jingle")
                    run_end_jingle()
                    game_ended = True
                    game_started = False
                    last_5_min = False
                    printed = False


if __name__ == "__main__":
    main()

