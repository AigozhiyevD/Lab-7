import pygame
import os

pygame.init()
pygame.mixer.init()

if not pygame.mixer.get_init():
    print("Ошибка: pygame.mixer не инициализировался.")
    exit()

music_files = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_song = 0
volume = 0.5  # Начальная громкость (от 0.0 до 1.0)
pygame.mixer.music.set_volume(volume)

screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Music Player")

# Загрузка изображений
play_img = pygame.image.load("back1.png")
stop_img = pygame.image.load("play.png")
next_img = pygame.image.load("stop.png")
prev_img = pygame.image.load("next.png")

# Координаты кнопок
play_rect = play_img.get_rect(topleft=(200, 300))
stop_rect = stop_img.get_rect(topleft=(400, 300))
next_rect = next_img.get_rect(topleft=(600, 300))
prev_rect = prev_img.get_rect(topleft=(800, 300))

def play_music():
    if os.path.exists(music_files[current_song]):
        try:
            pygame.mixer.music.load(music_files[current_song])
            pygame.mixer.music.play()
            print(f"Playing: {music_files[current_song]}")
        except pygame.error as e:
            print(f"Ошибка воспроизведения: {e}")
    else:
        print(f"File not found: {music_files[current_song]}")

def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped")

def next_music():
    global current_song
    current_song = (current_song + 1) % len(music_files)
    play_music()

def prev_music():
    global current_song
    current_song = (current_song - 1) % len(music_files)
    play_music()

def increase_volume():
    global volume
    volume = min(1.0, volume + 0.1)
    pygame.mixer.music.set_volume(volume)
    print(f"Volume increased: {volume:.1f}")

def decrease_volume():
    global volume
    volume = max(0.0, volume - 0.1)
    pygame.mixer.music.set_volume(volume)
    print(f"Volume decreased: {volume:.1f}")

running = True
while running:
    screen.fill((200, 200, 200))
    screen.blit(play_img, play_rect.topleft)
    screen.blit(stop_img, stop_rect.topleft)
    screen.blit(next_img, next_rect.topleft)
    screen.blit(prev_img, prev_rect.topleft)
    
    for event in pygame.event.get():
        print(f"Event: {event}")
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print(f"Key pressed: {pygame.key.name(event.key)}")
            if event.key == pygame.K_p:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_music()
            elif event.key == pygame.K_b:
                prev_music()
            elif event.key == pygame.K_UP:
                increase_volume()
            elif event.key == pygame.K_DOWN:
                decrease_volume()
    
    pygame.display.update()
pygame.quit()
