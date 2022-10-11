import pygame

from lib import SpotifyLib
from PygameClasses import SpotifyGUI
from classes import WindowsMouse

from General import Functions, Constants


def get_spotipy_client():
    spotify_credentials_dict = Functions.parse_json(Constants.spotify_credentials_file_path)
    scope = "user-read-currently-playing"
    redirect_uri = "http://localhost:44444/callback"
    return SpotifyLib.get_spotipy_client(
        client_id=spotify_credentials_dict["client_id"],
        client_secret=spotify_credentials_dict["secret"],
        scope=scope,
        redirect_uri=redirect_uri
    )


def main():

    pygame.init()
    display_width, display_height = 700, 120
    clock = pygame.time.Clock()
    pygame.display.set_caption("Twitchy")
    pygame.display.set_icon(pygame.image.load("Twitchy Logo.png"))
    screen = pygame.display.set_mode([display_width, display_height], pygame.NOFRAME)
    mouse = WindowsMouse.WindowsMouse()
    hwnd = pygame.display.get_wm_info()["window"]

    spotipy_client = get_spotipy_client()
    song = SpotifyLib.get_currently_playing_song(spotipy_client)
    spotify_gui = SpotifyGUI.SpotifyGUI(song=song, screen=screen)

    window_adjust = Constants.window_adjust
    drag = False
    expand_right = False
    expand_down = False
    shrink_left = False
    shrink_up = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.NOFRAME)
            if event.type == pygame.MOUSEBUTTONDOWN:
                drag = True
            if event.type == pygame.MOUSEBUTTONUP:
                drag = False

            mods = pygame.key.get_mods()
            if event.type == pygame.KEYDOWN and mods and pygame.KMOD_CTRL:
                shrink_up = event.key == pygame.K_w
                shrink_left = event.key == pygame.K_a
                expand_down = event.key == pygame.K_s
                expand_right = event.key == pygame.K_d
            if event.type == pygame.KEYUP and mods and pygame.KMOD_CTRL:
                if event.key == pygame.K_w:
                    shrink_up = False
                if event.key == pygame.K_a:
                    shrink_left = False
                if event.key == pygame.K_s:
                    expand_down = False
                if event.key == pygame.K_d:
                    expand_right = False

        w, h = pygame.display.get_surface().get_size()
        if shrink_up:
            screen = pygame.display.set_mode((w, h - window_adjust), pygame.NOFRAME)
        if shrink_left:
            screen = pygame.display.set_mode((w - window_adjust, h), pygame.NOFRAME)
        if expand_down:
            screen = pygame.display.set_mode((w, h + window_adjust), pygame.NOFRAME)
        if expand_right:
            screen = pygame.display.set_mode((w + window_adjust, h), pygame.NOFRAME)

        try:
            mouse.update()
        except:
            pass

        if drag:
            x_delta, y_delta = mouse.x - mouse.prev_x, mouse.y - mouse.prev_y
            w, h = pygame.display.get_surface().get_size()
            Functions.alter_window(hwnd, x_delta=x_delta, y_delta=y_delta, width=w, height=h)

        spotify_gui.update(update_song=not drag)
        screen.fill((23, 23, 23))
        spotify_gui.draw()

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
