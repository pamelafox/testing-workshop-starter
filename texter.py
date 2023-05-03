import random
import re


def leet(message):
    return message.replace("e", "3")


def clapify(message):
    return "👏".join(list(message))


def emojify(s):
    mappings = {
        "kiss": "😘",
        "airplane": "✈️",
        "pizza": "🍕",
        "happy": "😊",
        "sad": "😭",
        "star": "⭐️",
        "sleep": "😴",
        "sun": "☀️",
        "moon": "🌙",
        "christmas": "🎄",
        "birthday": "🎉",
        "ball": "🏀",
        "balloon": "🎈",
        "cake": "🎂",
        "laugh": "😂",
        "sick": "😷",
        "cheese": "🧀",
        "cow": "🐮",
        "horse": "🐴",
        "bear": "🐻",
        "monkey": "🐒",
        "surprised": "😳",
        "clap": "👏",
        "prayer": "🙏🏽",
        "run": "🏃🏻",
        "pencil": "✏️",
        "fire": "🔥",
        "rocket": "🚀",
        "car": "🚗",
        "movie": "🎥",
        "lips": "👄",
        "eyes": "👀",
        "tv": "📺",
        "soccer": "⚽️",
        "football": "🏈",
        "hat": "🎩",
        "dog": "🐶",
        "cat": "🐱",
        "elephant": "🐘",
        "lol": "😂",
        "dancer": "💃🏿",
        "world": "🌏",
    }
    return " ".join([mappings.get(word, word) for word in re.findall(r"[\w']+|[.,!?;]", s)])


def shortener(message):
    vowels = ["A", "E", "I", "O", "U"]
    return "".join([letter for letter in message if letter.upper() not in vowels])


def exclamify(message):
    end_marks = ["❣️", "‼️", "❗️", "!", "᥄", "❣", "‼︎"]
    start = random.choice(["¡", "¡¡"] + end_marks)
    end = random.choice(end_marks)
    return f"{start} {message} {end}"
