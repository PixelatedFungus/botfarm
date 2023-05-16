import pygame, os

class Util():
    def load_frames(file_folder, file_name, file_type, start, end):
        frames = []
        for frame_num in range(start, end + 1):
            file_path = os.path.join(file_folder, file_name + str(frame_num) + "." + file_type)
            frames.append(pygame.image.load(file_path))
        return frames