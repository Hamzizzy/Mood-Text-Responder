import random
import time
import textwrap

SPLASH = r"""
   __  ___               __          __        __        __        
  /  |/  /___  ____ _   / /   ____ _/ /_____  / /_____ _/ /___ ___ 
 / /|_/ / __ \/ __ `/  / /   / __ `/ __/ __ \/ __/ __ `/ / __ `__ \
/ /  / / /_/ / /_/ /  / /___/ /_/ / /_/ /_/ / /_/ /_/ / / / / / / /
/_/  /_/\____/\__, /  /_____/\__,_/\__/\____/\__/\__,_/_/_/ /_/ /_/ 
             /____/         🌟 Mood-to-Quote 🌟
"""

BANNER = """
╔═════════════════════════════════════════════════════╗
║             Pick a mood — get a tiny boost!         ║
╚═════════════════════════════════════════════════════╝
"""

MOODS = {
    "happy": [
        "😊 Keep smiling—happiness looks good on you!",
        "🌞 Happiness is contagious—spread it today!"
    ],
    "stressed": [
        "🧘 Breathe. You’ve handled tough days before—you will again.",
        "☕ Tiny steps count. One thing at a time."
    ],
    "tired": [
        "😴 Rest now, conquer later.",
        "🛌 Sleep is a superpower—recharge!"
    ],
    "sad": [
        "🌦 Every storm runs out of rain.",
        "💪 You’ve made it through 100% of your hard days."
    ]
}

TIPS = {
    "happy": [
        "Text someone a compliment — double your joy.",
        "Take a 60-second dance break."
    ],
    "stressed": [
        "Box breathing: In 4s, hold 4s, out 4s, hold 4s (×4).",
        "Write the next *one* tiny action and do only that."
    ],
    "tired": [
        "Close your eyes for 90 seconds. Just breathe.",
        "Drink water, stretch your neck/shoulders."
    ],
    "sad": [
        "Name 3 things you can see, 2 you can hear, 1 you can feel.",
        "Message a friend one honest sentence."
    ]
}

MENU = """
Choose an option:
  1) 😊 Happy
  2) 🧘 Stressed
  3) 😴 Tired
  4) 🌦 Sad
  5) 🎲 Surprise me
  6) ➕ Add my own quote
  h) ❓ Help / About
  0) 🚪 Exit
"""

HELP = """
This tiny terminal app gives you a quote + a quick tip based on your mood.

How to use:
- Pick a number (or 'h' for help).
- Try '🎲 Surprise me' to randomize the mood.
- Use '➕ Add my own quote' to insert your own line into a mood category
  for this session.

Tech notes:
- Pure Python 3, no external packages.
- Demonstrates functions, dictionaries, loops, input validation, and simple UI.
"""

def wrap(text, width=70):
    return "\n".join(textwrap.wrap(text, width=width))

def loader(msg="Finding your quote"):
    print("\n" + msg, end="", flush=True)
    for _ in range(3):
        time.sleep(0.35)
        print(".", end="", flush=True)
    print()

def confetti():
    # quick celebratory sprinkle
    frames = ["✨", "🎉", "✨🎉", "🎉✨", "✨🎉✨"]
    for f in frames:
        print(f, end="\r", flush=True)
        time.sleep(0.12)
    print("✨🎉✨")

def pretty_box(text):
    lines = []
    for line in text.split("\n"):
        lines.extend(wrap(line, width=66).split("\n"))
    width = max(len(line) for line in lines) + 2
    top = "╔" + "═" * width + "╗"
    bottom = "╚" + "═" * width + "╝"
    body = "\n".join("║ " + line.ljust(width - 2) + " ║" for line in lines)
    return f"{top}\n{body}\n{bottom}"

def pick_mood(choice):
    mapping = {"1": "happy", "2": "stressed", "3": "tired", "4": "sad"}
    if choice == "5":
        return random.choice(list(MOODS.keys()))
    return mapping.get(choice)

def add_custom_quote():
    print("\nAdd a custom quote to a mood!")
    mood = input("Mood (happy/stressed/tired/sad): ").strip().lower()
    if mood not in MOODS:
        print("Unknown mood. Try one of: happy, stressed, tired, sad.")
        return
    quote = input("Type your quote: ").strip()
    if not quote:
        print("Empty quote not added.")
        return
    if quote not in MOODS[mood]:
        MOODS[mood].append(quote)
        print("✅ Added to this session!")
    else:
        print("That quote already exists for this mood.")

def show_help():
    print(pretty_box(HELP))

def main():
    print(SPLASH)
    print(BANNER)
    while True:
        print(MENU)
        choice = input("Enter choice: ").strip().lower()

        if choice == "0":
            print("\nThanks for visiting. Take care! ✨")
            break
        if choice == "h":
            show_help()
            continue
        if choice == "6":
            add_custom_quote()
            continue

        mood = pick_mood(choice)
        if not mood:
            print("Invalid choice. Please try again.\n")
            continue

        loader()
        quote = random.choice(MOODS[mood])
        tip = random.choice(TIPS[mood])

        output = f"{quote}\n\n💡 Quick tip: {tip}"
        print(pretty_box(output))
        confetti()

        again = input("\nAnother one? (y/n): ").strip().lower()
        if again != "y":
            print("\nSee you next time! 🌟")
            break

if __name__ == "__main__":
    main()