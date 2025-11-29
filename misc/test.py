import random
import time
import shutil

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

# JUST RUN THIS ONE LINE:
_hackerMode()