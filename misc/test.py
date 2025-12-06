import random
import time
import shutil

intFloatTulp = (int, float)

def _hackerMode() -> None:
    """
    THE ONE. True Matrix rain with everything:
    - Full katakana + binary
    - Bright white heads
    - Block characters (█ ▓ ░ ▒)
    - Dense, no gaps
    - Works in any terminal
    """
    # All the characters from the actual Matrix
    chars = "01ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝ"
    blocks = "█▓▒░▉▊▋▌▍▎"

    try:
        w, h = shutil.get_terminal_size((80, 24))
        w = max(w, 50)
        h = max(h, 15)

        # One drop per column
        pos = [random.randint(-h*2, -1) for _ in range(w)]
        trail_len = [random.randint(12, 30) for _ in range(w)]

        while True:
            screen = [[" "] * w for _ in range(h)]

            for x in range(w):
                pos[x] += 1

                # Respawn when off-screen
                if pos[x] > h + 5:
                    pos[x] = random.randint(-20, -3)
                    trail_len[x] = random.randint(14, 32)

                y = pos[x]
                if 0 <= y < h:
                    # Bright white head (20% chance)
                    if random.random() < 0.2:
                        screen[y][x] = "█"
                    else:
                        screen[y][x] = random.choice(chars + blocks)

                    # Epic trail with blocks + katakana + fading
                    for i in range(1, trail_len[x]):
                        ty = y - i
                        if ty < 0 or ty >= h:
                            break

                        roll = random.random()
                        if i == 1:
                            screen[ty][x] = random.choice(chars + "▓▒")
                        elif i < 4:
                            screen[ty][x] = random.choice("░▒▊▋" + chars)
                        elif i < 8:
                            if roll < 0.6:
                                screen[ty][x] = random.choice("░▒·.")
                            else:
                                screen[ty][x] = random.choice(chars + blocks)
                        else:
                            if roll < 0.25:
                                screen[ty][x] = random.choice("·.")
                            elif roll < 0.4:
                                screen[ty][x] = random.choice("░▒")

            # Bright green + full redraw
            print("\033[92m\033[H" + "\n".join("".join(row) for row in screen), end="", flush=True)
            time.sleep(0.05)

    except KeyboardInterrupt:
        print("\033[0m\033[H\033[J", end="")
        _clearConsole()
        print("Wake up, Neo...")
        time.sleep(1)
        _clearConsole()


def _getNumberFromText(
    i: str,
    numberType: type = int,
    printExcept: bool = False,
) -> int | float | None:
    """
    Attempt to convert a string to int or float.
    Returns the number on success, None on failure.
    """
    if numberType in intFloatTulp:
        try:
            return numberType(i)
        except ValueError:
            if printExcept:
                print(f"Value is not {numberType.__name__}.")
            return None
    else:
        return None


def _confirm(prompt: str = "Confirm?", default: bool = True) -> bool:
    choices = " [Y/n]" if default else " [y/N]"
    response = input(prompt + choices + " ").strip()
    
    if not response:
        return default
    
    normalized = response.lower()
    if normalized in {'y', 'yes', 'yeah', 'yep', 'sure', 'ok', 'okay', '1'}:
        return True
    if normalized in {'n', 'no', 'nope', 'nah', '0'}:
        return False
    
    first = normalized[0]
    return first == 'y' if default else first == 'n'

# JUST RUN THIS ONE LINE:
while True:
    if not not _confirm("Test question"):
        break

    