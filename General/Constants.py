
system_type = "windows"
# system_type = "linux"

if system_type == "windows":
    spotify_credentials_file_path = "C:\\LocalCodingProjects\\0 - Secrets\\spotify_credentials.json"
else:
    spotify_credentials_file_path = "/stash/CodingProjects/0 - Secrets/TwitchHelper/spotify_credentials.json"


song_update_time = 0.2 * 1000000
window_adjust_multiplier = 1
window_adjust_x_delta = 7
window_adjust_y_delta = 3

rolling_average_number_x_average_count = 30
rolling_average_number_y_average_count = 30

regular_font = "resources/fonts/Product Sans Regular.ttf"
bold_font = "resources/fonts/Product Sans Bold.ttf"
itallic_font = "resources/fonts/Product Sans Italic.ttf"
bold_itallic_font = "resources/fonts/Product Sans Bold Italic.ttf"

app_name = "Twitchy - Spotify"

display_width = 700
display_height = 120
