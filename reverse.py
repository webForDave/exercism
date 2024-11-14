def reverse(text):
    new_text = ''
    for char in text:
        new_text = char + new_text
    return new_text


print(reverse("子猫"))
