import random
import pygame
import pygame.midi

pygame.init()
pygame.midi.init()

player = pygame.midi.Output(0)

# Note string to int map
note_map = {'C0': 0, 'D0': 2, 'E0': 4, 'F0': 5, 'G0': 7, 'A0': 9, 'B0': 11,
            'C1': 12, 'D1': 14, 'E1': 16, 'F1': 17, 'G1': 19, 'A1': 21, 'B1': 23,
            'C2': 24, 'D2': 26, 'E2': 28, 'F2': 29, 'G2': 31, 'A2': 33, 'B2': 35, 
            'C3': 36, 'D3': 38, 'E3': 40, 'F3': 41, 'G3': 43, 'A3': 45, 'B3': 47,
            'C4': 48, 'D4': 50, 'E4': 52, 'F4': 53, 'G4': 55, 'A4': 57, 'B4': 59,
            'C5': 60, 'D5': 62, 'E5': 64, 'F5': 65, 'G5': 67, 'A5': 69, 'B5': 71,
            'C6': 72, 'D6': 74, 'E6': 76, 'F6': 77, 'G6': 79, 'A6': 81, 'B6': 83,
            'C7': 84, 'D7': 86, 'E7': 88, 'F7': 89, 'G7': 91, 'A7': 93, 'B7': 95,
            'C8': 96, 'D8': 98, 'E8': 100, 'F8': 101, 'G8': 103, 'A8': 105, 'B8': 107}
# Piano note arrays
piano_notes = {
  "octave_1": ["C1", "D1", "E1", "F1", "G1", "A1", "B1"],
  "octave_2": ["C2", "D2", "E2", "F2", "G2", "A2", "B2"], 
  "octave_3": ["C3", "D3", "E3", "F3", "G3", "A3", "B3"],
  "octave_4": ["C4", "D4", "E4", "F4", "G4", "A4", "B4"],
  "octave_5": ["C5", "D5", "E5", "F5", "G5", "A5", "B5"],
  "octave_6": ["C6", "D6", "E6", "F6", "G6", "A6", "B6"],
  "octave_7": ["C7", "D7", "E7", "F7", "G7", "A7", "B7"],
  "octave_8": ["C8", "D8", "E8", "F8", "G8", "A8", "B8"]  
}

# Rest of code to generate and play melody...
# Generate random melody 
melody = []
for i in range(100):
  random_octave = random.choice(list(piano_notes.keys()))
  melody.append(random.choice(piano_notes[random_octave]))

# Convert note strings to ints
int_melody = []
for note in melody:
  int_note = note_map[note]
  int_melody.append(int_note)

# Play melody  
for note in int_melody:
  player.note_on(note, 100)
  pygame.time.delay(500)
  player.note_off(note, 100)