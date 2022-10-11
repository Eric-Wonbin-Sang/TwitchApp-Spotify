from classes.keys.Key import Key


class ComboKey(Key):
    """
    A class for detecting if any specified target keys are pressed.

    Note:
        Keep in mind that the Key baseclass uses target to look up the
        pygame key code. Since update is overridden, this shouldn't matter,
        but beware of Key class changes.

    """

    def __init__(self, name, *targets):

        super().__init__(name)

        self.targets = targets
        self.key_list = [Key(target) for target in self.targets]
        self.is_pressed = False

    def update(self, event):
        if not self.can_update(event):
            return
        for key in self.key_list:
            key.update(event)
            if key.is_pressed:
                self.is_pressed = True
                return
        self.is_pressed = False

    def __str__(self):
        return f"ComboKey(target={self.target}, targets={self.targets}, is_pressed={self.is_pressed})"
