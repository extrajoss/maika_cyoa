import paths

paths = {
  "wake_up": paths.wake_up,
  "wagon_hole": paths.wagon_hole,
  "wagon": paths.wagon,
  "hole": paths.hole,
  "help_the_man": paths.help_the_man,
  "the_tunnel": paths.the_tunnel,
  "torch": paths.torch,
  "alter": paths.alter,
  "voices": paths.voices,
  "magic_circle": paths.magic_circle,
  "cavern": paths.cavern,
  "river": paths.river,
  "beam_of_light": paths.beam_of_light,
  "stairs": paths.stairs,
  "door": paths.door,
  "trapped": paths.trapped,
  "despair": paths.despair,
  "goblin": paths.goblin,
  "riddle": paths.riddle,
  "sacrifice": paths.sacrifice,
}


def show_path(path_name):
  path = paths.get(path_name)
  if path is None:
    return
  print_text_array(path.get("text"))
  choices = path.get("choices")
  if choices:
    show_choices(choices)\


def path_divider():
  print("--~oo00oo~--\n")


def show_choices(path_choices):
  choices = path_choices.keys()
  choices_text = " or ".join(map(format_choice,choices))
  user_choice = input(f"\n>{choices_text}:").lower().strip()
  choice = path_choices.get(user_choice)
  if choice:
    path_divider()
    print_text_array(choice.get("text"))
    show_path(choice.get("path"))
  else:
    retry(path_choices)


def retry(path_choices):
  print("\n".join([
    "Choose an option carefully, and press Enter.",
    "Any sort of fumble in a situation like this could lead to an...unhappy ending.",
    "Make sure not to make a  mistake!"
  ]))
  show_choices(path_choices)


def format_choice(choice):
    return f"{choice!r}?"


def print_text_array(text_array):
  print("\n".join(text_array))


print("warning, this game contains some graphic imagery. players discretion is advised. Thank you!\n")
show_path("wake_up")
