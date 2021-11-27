import numpy as np
import pandas as pd
import sys


def how_many_laps(question):
    valid = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
    prompt = "\n [1/2/3/4/5] "
    while True:
        sys.stdout.write(question + prompt)
        choice = input()
        if choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Invalid response: Please respond with a number between 1 and 5.\n")

def driver_select(question):
    valid = {"1": 1,
             "2": 2,
             "3": 3,
             "4": 4,
             "5": 5,
             "6": 6,
             "7": 7,
             "8": 8,
             "9": 9,
             "10": 10,
             "11": 11,
             "12": 12,
             "13": 13,
             "14": 14,
             "15": 15,
             "16": 16,
             "17": 17,
             "18": 18,
             "19": 19,
             "20": 20}

    prompt = ("""
              1: Lewis Hamilton
              2: Valtteri Bottas
              3: Max Verstappen
              4: Sergio Perez
              5: Lando Norris
              6: Daniel Ricciardo
              7: Charles Leclerc
              8: Carlos Sainz
              9: Pierre Gasly
              10: Yuki Tsunoda
              11: Sebastian Vettel
              12: Lance Stroll
              13: Esteban Ocon
              14: Fernando Alonso
              15: Kimi Raikkonen
              16: Antonio Giovinazzi
              17: George Russel
              18: Nicholas Latifi
              19: Mick Schumacher
              20: Nikita Mazepin

              Enter the corresponding number:
              """)
    while True:
        sys.stdout.write(question + prompt)
        choice = input()
        if choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Invalid response: Please a number from the list above!.\n")


def tyre_choice(question):
    valid = {"S": S, "s": s, "M": M, "m": m, "H": H, "h":h}
    prompt = " S - M - H "
    while True:
        sys.stdout.write(question + prompt)
        choice = input()
        if choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Invalid response: Please respond with S, M or H. \n")


def frame_rate_choice(question):
    valid = {"1": 1, "0.75": 0.75, "0.5": 0.5, "0.25": 0.25, "0.1": 0.1}
    prompt = """\n
    1: Collects data once every second
    0.75: Colelcts data every 0.75 seconds
    0.5: Collects data evert half second
    0.25: Collects data every quarter second
    0.1: collects data every tenth of a second
    """
    while True:
        sys.stdout.write(question + prompt)
        choice = input()
        if choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Invalid response! Please respond one of these options: 1,0.75,0.5,0.25,0.1 \n")

def track_select(question):
    valid = {"1": 1,
             "2": 2,
             "3": 3,
             "4": 4,
             "5": 5,
             "6": 6,
             "7": 7,
             "8": 8,
             "9": 9,
             "10": 10,
             "11": 11,
             "12": 12,
             "13": 13,
             "14": 14,
             "15": 15,
             "16": 16,
             "17": 17,
             "18": 18,
             "19": 19,
             "20": 20,
             "21": 21,
             "22": 22}

    prompt = ("""
           1: Albert Park - Australia
           2: Algarve International Circuit - Portugal
           3: Autódromo Hermanos Rodríguez - Mexico
           4: Autodromo Internazionale Enzo e Dino Ferrari - Italy
           5: Autodromo Josè Carlos Pace - Brasil
           6: Autodromo Nazionale di Monza - Italy
           7: Bahrain International Circuit - Bahrain
           8: Baku City Circuit - Azerbaijan
           9: Circuit de Barcelona Catalunya - Spain
           10: Circuit de Monaco - Monaco 
           11: Circuit de Spa-Francorchamps - Belgium
           12: Circuit of the Americas - United States
           13: Circuit Paul Ricard - France
           14: Circuit Zandvoort - Netherlands
           15: Hungaroring - Hungary         
           16: Jeddah Street Circuit - Saudi Arabia
           17: Red Bull Ring - Austria
           18: Silverstone Circuit - United Kingdom
           19: Sochi Autodrom - Russia
           20: Suzuka Circuit - Japan
           21: Yas Marina Circuit - United Arab Emirates
           22: Circuit Gilles Villeneuve - Canada

              Enter the corresponding number:
              """)
    while True:
        sys.stdout.write(question + prompt)
        choice = input()
        if choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Invalid response: Please a number from the list above!.\n")            
