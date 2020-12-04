from src.astro_war.config import Config

import pyglet


class SoundPlayer:

    # ----- Attributes -----

    _music_player: pyglet.media.Player = None

    # ----- Sound methods -----

    @staticmethod
    def init():
        """
        Initialize the sound player
        """

        SoundPlayer._music_player = pyglet.media.Player()
        SoundPlayer._music_player.volume = Config.MUSIC_VOLUME
        SoundPlayer._music_player.loop = True

    @staticmethod
    def play_music(music: pyglet.media.Source):
        """
        Play a music by replacing the current
        """

        # Verify the sound is different than the current
        current_source = SoundPlayer._music_player.source
        if current_source != music:
            # Set the next music
            SoundPlayer._music_player.queue(music)

            # Start the music playing
            if current_source is None:
                SoundPlayer._music_player.play()
            else:
                SoundPlayer._music_player.next_source()
