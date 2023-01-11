
def get_name_list():
    with open("Input\\Names\\invited_names.txt") as names:
        content = names.readlines()
        name_list = [i.strip("\n") for i in content]
        return name_list


def swap_names():
    with open("Input\\Letters\\starting_letter.txt", mode="r") as letter:
        text = letter.read()
        for name in get_name_list():
            named_letter = text.replace("[name]", f"{name}")
            with open(f".\\Output\\ReadyToSend\\{name}_letter.txt", mode="w") as completed_letter:
                completed_letter.write(named_letter)

