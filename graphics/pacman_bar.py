import sys


def pacman_bar(current_index, total_number):
    bar_length = 60
    fill_char = "="
    lead_char = ">"

    # How to give this bar a color

    progress = current_index / total_number
    block = int(round(bar_length * progress))

    if block == bar_length:
        bar = fill_char * block
    else:
        bar = fill_char * (block - 1) + lead_char + "-" * (bar_length - block)

    text = f"\rProgress:[{bar}] {progress * 100:.2f}%"
    sys.stdout.write(text)
    sys.stdout.flush()
