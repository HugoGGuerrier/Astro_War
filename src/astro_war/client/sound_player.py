from src.astro_war.config import Config

import pygame


class SoundPlayer:

    # ----- Attributes -----

    _music_channel: pygame.mixer.Channel = None

    # ----- Sound methods -----

    @staticmethod
    def init():
        """
        Initialize the sound player
        """

        SoundPlayer._music_channel = pygame.mixer.Channel(0)
        SoundPlayer._music_channel.set_volume(Config.MUSIC_VOLUME)

    @staticmethod
    def play_music(sound: pygame.mixer.Sound, loops: int = -1):
        """
        Play a music by replacing the current
        """

        # Stop the current music
        if SoundPlayer._music_channel.get_busy():
            SoundPlayer._music_channel.stop()

        SoundPlayer._music_channel.play(sound, loops=loops)
