import pygame
import os
from pygame import mixer

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.init()
        mixer.init()
        self.music_folder = music_folder
        self.music_files = [file for file in os.listdir(music_folder) if file.endswith(('.mp3', '.wav'))]
        self.current_track = 0
        self.playing = False

    def load_music(self):
        pygame.mixer.music.load(os.path.join(self.music_folder, self.music_files[self.current_track]))

    def play_music(self):
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_track(self):
        self.current_track = (self.current_track + 1) % len(self.music_files)
        self.load_music()
        if self.playing:
            self.play_music()

    def prev_track(self):
        self.current_track = (self.current_track - 1) % len(self.music_files)
        self.load_music()
        if self.playing:
            self.play_music()

    def run(self):
        self.load_music()

        while True:
            query = input('  ')
                
            if query == 's':
                self.stop_music()
            elif query == ' ':
                self.play_music()
                self.playing = True
            elif query == 'n':
                self.next_track()
            elif query == 'p':
                self.prev_track()
            elif query == 'q':
                pygame.quit()
                exit()

if __name__ == "__main__":
    player = MusicPlayer("C:\\Users\\Daniyar\\Desktop\\pp2\\music")
    player.run()
    
    pygame.quit()
    exit()
    

