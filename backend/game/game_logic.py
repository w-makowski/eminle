import re

    
def get_total_seconds_from_track_length(track_length):
    """
    Converts given track length string in format mm:ss to total seconds.
    :param track_length: str, track length in the format minute:seconds
    :return: int, total seconds
    """
    minutes, seconds = map(int, track_length.split(":"))
    return minutes * 60 + seconds
    

def get_hints_and_colours(guessed_value, correct_value, is_numeric=False, diff=3):
    """Returns hint (lower: '-', equal: '=' , higher: '+') and color (green - equal, yellow - close, grey - incorrect)"""
    if guessed_value == correct_value:
        return '=', 'green'
    if is_numeric:
        values_diff = correct_value - guessed_value
        return ('+' if values_diff > 0 else '-'), ('yellow' if abs(values_diff) < diff else 'grey')
    return 'incorrect', 'grey'


def process_guess(correct_song, user_gues):
    """Processes the user's guess and returns hints for each attribute."""
    album_hint, album_color = get_hints_and_colours(user_gues.album.album_number, correct_song.album.album_number, is_numeric=True)
    track_hint, track_color = get_hints_and_colours(user_gues.track_number, correct_song.track_number, is_numeric=True)
    track_length_hint, track_length_color = get_hints_and_colours(
        get_total_seconds_from_track_length(user_gues.track_length),
        get_total_seconds_from_track_length(correct_song.track_length),
        is_numeric=True,
        diff=31
    )

    correct_features = set(re.split(r"[,|and|&]", correct_song.features or ''))
    guessed_features = set(re.split(r"[,|and|&]", user_gues.features or ''))
    feature_color = 'green' if correct_features == guessed_features else ('yellow' if correct_features & guessed_features else "grey")

    return {
        'song_name': user_gues.song_name,
        'album': {'value': user_gues.album.name, 'hint': album_hint, 'color': album_color},
        'track_number': {'value': user_gues.track_number, 'hint': track_hint, 'color': track_color},
        'track_length': {'value': user_gues.track_length, 'hint': track_length_hint, 'color': track_length_color},
        'features': {'value': user_gues.features or 'None', 'color': feature_color}
    }
