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
                # print(curr_song)
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

'''
Exceptions found:

Z:\TwitchApp-Spotify>python_3.9 main.py
pygame 2.1.2 (SDL 2.0.18, Python 3.9.0)
Hello from the pygame community. https://www.pygame.org/contribute.html
Traceback (most recent call last):
  File "Z:\TwitchApp-Spotify\main.py", line 45, in <module>
    main()
  File "Z:\TwitchApp-Spotify\main.py", line 30, in main
    spotify_gui.resizer.process_keys()
  File "Z:\TwitchApp-Spotify\classes\gui_helpers\Resizer.py", line 64, in process_keys
    self.key_dict["mouse"].update_position()
  File "Z:\TwitchApp-Spotify\classes\keys\MouseKey.py", line 33, in update_position
    x, y = self.get_cursor_position()
  File "Z:\TwitchApp-Spotify\classes\keys\MouseKey.py", line 27, in get_cursor_position
    _, _, (x, y) = win32gui.GetCursorInfo()
pywintypes.error: (5, 'GetCursorInfo', 'Access is denied.')

pygame 2.1.2 (SDL 2.0.18, Python 3.9.0)
Hello from the pygame community. https://www.pygame.org/contribute.html
HTTP Error for GET to https://api.spotify.com/v1/me/player/currently-playing with Params: {'market': None, 'additional_types': None} returned 401 due to The access token expired

Z:\TwitchApp-Spotify>pause


'''