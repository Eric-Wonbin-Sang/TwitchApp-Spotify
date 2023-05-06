# TwitchApp-Spotify
This will showcase the songs you are playing on your Spotify account.

pip install pywin32 (not win32gui)
pip install spotipy
pip install pygame


## For Linux
might need to run sudo apt-get install python3-distutils

## Exceptions Found

```
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
```

