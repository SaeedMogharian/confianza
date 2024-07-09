from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    user = models.OneToOneField(User, related_name='user_detail', on_delete=models.CASCADE, verbose_name='user')
    level = models.IntegerField(default=0, verbose_name='level')

    # preferred language
    # total score
    # get game count
    # avatar
    # most played as

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    class Meta:
        verbose_name = 'User Detail'
        verbose_name_plural = 'Users - Detail'


class Role(models.Model):
    ROLE_CHOICES = [
        ("Passenger", "Passenger"),
        ("Mentor", "Mentor"),
        ("Witch", "Witch"),
        ("Landlord", "Landlord"),
    ]
    name = models.CharField(max_length=255, choices=ROLE_CHOICES)
    image = models.FileField(upload_to='game/static/images/roles/', verbose_name='image')
    description = models.CharField(default='default', max_length=500, verbose_name='role_description')

    # def score calc for each role

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'


class Property(models.Model):
    PROP_CHOICE = [
        ("R1", "Thief"),
        ("R2", "Blackmailer"),
        ("R3", "Big Poison"),
        ("R4", "Small Poison"),
        ("A1", "Clue"),
        ("A2", "Horse"),
        ("A3", "Elephant"),
        ("A4", "Time Elixir"),
        ("A5", "Antidote"),
        ("A6", "Astrolabe"),
        ("S", "Supplies"),
    ]
    KIND = [
        ("R", "Risk"),
        ("A", "Ability"),
        ("S", "Supplies"),
    ]
    name = models.CharField(max_length=255, choices=PROP_CHOICE)
    kind = models.CharField(max_length=255, choices=PROP_CHOICE)
    probability = models.FloatField(default=0, verbose_name='score', max=100, min=1)
    image = models.FileField(upload_to='game/static/images/abilities/', verbose_name='image')
    description = models.CharField(default='default', max_length=500, verbose_name='ability_description')

    # def impact calc for each ability

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class GameRoom(models.Model):
    # owner

    # leaderboard

    # logs
    # date created
    # state

    def __str__(self):
        return f"GameRoom_{self.id}"

    class Meta:
        verbose_name = 'GameRoom'
        verbose_name_plural = 'GameRooms'


class Game(models.Model):
    # game room

    # number of bots
    # number of players
    # number of each role
    # difficulty level

    # logs

    # state

    # is won
    # is fin?
    # new move

    def __str__(self):
        return f"Game_{self.id}"

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Game'


class Map(models.Model):
    rows = models.IntegerField(default=0, verbose_name='row')
    cols = models.IntegerField(default=0, verbose_name='cols')
    # row = 4, col=4
    # data = [
    #  ["End"   , "R3"  , "S2"  , ""     ]
    #  ["R3"    , ""    , "A2"  , "R"    ]
    #  ["S1"    , "R"   , ""    , ""     ]
    #  [""      ,  "A3" , ""    , "Begin"]
    # ]
    data = models.JSONField()

    # map
    # revealed places
    # difficulty level

    def __str__(self):
        return f"G_Board"

    class Meta:
        verbose_name = 'Map'
        verbose_name_plural = 'Maps'


class GameBoard(models.Model):
    game = models.ForeignKey(Game, related_name='player', on_delete=models.CASCADE, verbose_name='game')

    # map
    # revealed places
    #

    def __str__(self):
        return f"G:{self.game.id}_Board"

    class Meta:
        verbose_name = 'Game board'
        verbose_name_plural = 'Games - boards'


class GameLog(models.Model):
    game = models.ForeignKey(Game, related_name='player', on_delete=models.CASCADE, verbose_name='game')
    text = models.CharField(default='default', max_length=1000, verbose_name='log text')

    def __str__(self):
        return f"G:{self.game.id}_L:{self.text}"

    class Meta:
        verbose_name = 'Game log'
        verbose_name_plural = 'Games - logs'


class Player(models.Model):
    user = models.ForeignKey(UserDetail, related_name='played_as', on_delete=models.CASCADE, verbose_name='user')
    game = models.ForeignKey(Game, related_name='players', on_delete=models.CASCADE, verbose_name='game')
    role = models.ForeignKey(Role, related_name='players', on_delete=models.CASCADE, verbose_name='role')
    score = models.FloatField(default=0, verbose_name='score')
    properties = users = models.ManyToManyField(Property, related_name='players', blank=True, verbose_name='properties')

    def __str__(self):
        return f"G{self.game.id}_U{self.user.id}"

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
