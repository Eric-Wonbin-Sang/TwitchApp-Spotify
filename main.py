import queue
import pygame

from classes.threads.SongInfoProducer import SongInfoProducer

from PygameClasses import SpotifyGUI


def main():

    spotify_gui = SpotifyGUI.SpotifyGUI()

    song_info_queue = queue.Queue(1)
    song_info_producer = SongInfoProducer(1, "spotify", song_info_queue)
    song_info_producer.start()

    curr_song = None

    while True:
        try:
            curr_song = song_info_queue.get(block=False)
        except queue.Empty:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                pygame.display.set_mode((event.w, event.h), pygame.NOFRAME)
            for key in spotify_gui.key_dict.values():
                key.update(event)
        spotify_gui.process_keys()

        if curr_song:
            spotify_gui.update_and_draw(curr_song)

        pygame.display.update()


if __name__ == "__main__":
    main()
