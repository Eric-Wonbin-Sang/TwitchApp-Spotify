import queue
import pygame

from General import Constants
from classes.threads.SongInfoProducer import SongInfoProducer

from PygameClasses import SpotifyGUI
from exceptions.Exceptions import QuitException


def main():

    spotify_gui = SpotifyGUI.SpotifyGUI(Constants.system_type)

    song_info_queue = queue.Queue(1)

    song_info_producer = SongInfoProducer(1, "spotify", song_info_queue)
    song_info_producer.start()

    curr_song = None

    try:
        while True:
            try:
                curr_song = song_info_queue.get(block=False)
            except queue.Empty:
                pass

            spotify_gui.resizer.process_keys()

            if curr_song:
                spotify_gui.update_and_draw(curr_song)

            pygame.display.update()

    except QuitException:
        song_info_producer.kill_event.set()
        while song_info_producer.is_alive():
            pass
        pygame.quit()


if __name__ == "__main__":
    main()
