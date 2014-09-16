# -*- coding: utf-8 -*-

"""
An example of class inheritance.
"""


class Enemy(object):

    """A stupid enemy that doesn't know how to attack, but knows how to die.

    >>> stupid = Enemy(10)

    Let's hit him and see if he dies

    >>> stupid.take_damage(5)
    >>> stupid.alive
    True

    Nope, not dead yet ... let's try again!

    >>> stupid.take_damage(5)
    >>> stupid.alive
    False

    Woohoo, down you go stupid enemy!
    """

    def __init__(self, hp):
        self.hp = hp
        self.alive = True

    def take_damage(self, dmg):
        """Take some damage and check your HP for death."""

        self.hp -= dmg
        self.check_hp()

    def die(self):
        """Function called when the enemy dies."""

        self.alive = False

    def check_hp(self):
        """If HP is too low, die."""

        if self.hp <= 0:
            self.die()


class Shaman(Enemy):

    """A smarter enemy - can do everything Enemy can, but can also heal
    himself.

    >>> shaman = Shaman(12)

    Let's hit him and check if he was damaged

    >>> shaman.take_damage(5)
    >>> shaman.alive
    True
    >>> shaman.hp
    7

    Nope, not dead yet ... let's try again!

    >>> shaman.take_damage(5)
    >>> shaman.alive
    True
    >>> shaman.hp
    2

    Oops, better heal yourself fast shaman!

    >>> shaman.heal(20)
    >>> shaman.hp
    22

    Wow, that was a strong heal ... better bring out the big guns!

    >>> shaman.take_damage(100)
    >>> shaman.hp
    -78
    >>> shaman.alive
    False

    Wait ... what are you trying to do?

    >>> shaman.heal(100)
    >>> shaman.hp
    -78
    >>> shaman.alive
    False

    Silly shaman, you can't heal yourself if you're already dead ...
    """

    def __init__(self, hp):
        """Call the __init__ from our superclass."""

        super(Shaman, self).__init__(hp)

    def heal(self, hp):
        """Heal himself. Can only do that if he is alive."""

        if self.alive:
            self.hp += hp


if __name__ == "__main__":
    import doctest
    doctest.testmod()
