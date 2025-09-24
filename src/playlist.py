# src/playlist.py

class Playlist:
    def __init__(self):
        self._songs = []
        self._current_index = None  # No song playing initially

    def add_song(self, title: str):
        """Add a song to the playlist."""
        self._songs.append(title)

    def to_list(self):
        """Return the playlist as a list."""
        return list(self._songs)

    def play_first(self):
        """Start playing the first song and return it."""
        if not self._songs:
            return None
        self._current_index = 0
        return self._songs[self._current_index]

    def next(self):
        """Move to the next song. If already at the end, stay there."""
        if self._current_index is None:
            return None
        if self._current_index < len(self._songs) - 1:
            self._current_index += 1
        return self._songs[self._current_index]

    def prev(self):
        """Move to the previous song. If already at the start, stay there."""
        if self._current_index is None:
            return None
        if self._current_index > 0:
            self._current_index -= 1
        return self._songs[self._current_index]

    def insert_after_current(self, title: str):
        """Insert a song after the current song."""
        if self._current_index is None:
            # If nothing is playing, just append
            self._songs.append(title)
        else:
            self._songs.insert(self._current_index + 1, title)

    def remove_current(self) -> bool:
        """Remove the current song from the playlist.
        Returns True if removed, False if no song playing.
        """
        if self._current_index is None or not self._songs:
            return False
        self._songs.pop(self._current_index)
        # Adjust index if needed
        if self._current_index >= len(self._songs):
            self._current_index = len(self._songs) - 1 if self._songs else None
        return True
