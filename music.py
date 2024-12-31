from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional
import random
from midiutil import MIDIFile
from midi2audio import FluidSynth
from pydub import AudioSegment
import os
class MusicTheory:
    """Constants and music theory data structures."""
    NOTES: List[int] = (60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71)
    # Mood-based tempo ranges (BPM)
    MOOD_TEMPOS: Dict[str, Tuple[int, int]] = {
        'happy': (120, 140),       # Upbeat tempos
        'sad': (65, 80),          # Slow, melancholic tempos
        'energetic': (140, 160),   # Fast tempos
        'suspense': (90, 110),     # Moderate, tense tempos
        'competition': (130, 150),  # Driving tempos
        'gloomy': (60, 75)         # Very slow tempos
    }
    
    # General MIDI program numbers for instruments
    INSTRUMENTS: Dict[str, int] = {
        'piano': 0,      # Track 0: Melody (Piano)
        'strings': 48,   # Track 1: Chords (Strings)
        'bass': 32,      # Track 2: Bass
        'pad': 88,      # Track 3: Strings pad
        'drums': 0       # Track 4: Drums (Uses channel 9)
    }
    
    # Drum note numbers (General MIDI)
    DRUM_NOTES: Dict[str, int] = {
        'kick': 36,
        'snare': 38,
        'closed_hat': 42,
        'open_hat': 46,
        'crash': 49,
        'ride': 51,
    }
    
    SCALES: Dict[str, List[int]] = {
        'major': [0, 2, 4, 5, 7, 9, 11, 12],
        'minor': [0, 2, 3, 5, 7, 8, 10, 12],
        'pentatonic': [0, 2, 4, 7, 9],
        'dorian': [0, 2, 3, 5, 7, 9, 10, 12],
        'phrygian': [0, 1, 3, 5, 7, 8, 10, 12],
        'lydian': [0, 2, 4, 6, 7, 9, 11, 12],
        'mixolydian': [0, 2, 4, 5, 7, 9, 10, 12],
        'locrian': [0, 1, 3, 5, 6, 8, 10, 12],
        'blues': [0, 3, 5, 6, 7, 10],
        'chromatic': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'whole_tone': [0, 2, 4, 6, 8, 10, 12],
        'harmonic_minor': [0, 2, 3, 5, 7, 8, 11, 12],
        'melodic_minor': [0, 2, 3, 5, 7, 9, 11, 12]
    }
    

    
    SCALE_CHORDS: Dict[str, List[List[int]]] = {
 'major': [[0, 4, 7], [0, 5, 9], [2, 5, 9], [0, 4, 7]],  # I-IV-V-I progression
    'lydian': [[0, 4, 7], [2, 5, 9], [4, 8, 11], [0, 5, 9]],  # I-IV-V-I progression in lydian mode
    'mixolydian': [[0, 4, 7], [5, 9, 12], [4, 7, 11], [0, 4, 7]],  # I-IV-V-I progression in mixolydian mode
    'pentatonic': [[0, 4, 7], [7, 10, 14], [0, 5, 9], [7, 12, 16]],  # Simple pentatonic chords
    'minor': [[0, 3, 7], [2, 5, 9], [5, 8, 12], [0, 3, 7]],  # i-iv-v-i progression
    'phrygian': [[0, 3, 7], [2, 5, 9], [5, 8, 12], [0, 3, 7]],  # i-iv-v-i progression in phrygian mode
    'blues': [[0, 3, 7], [3, 6, 9], [7, 10, 14]],  # Blues chords
    'locrian': [[0, 3, 6], [2, 5, 8], [5, 8, 11], [0, 3, 6]],  # i-bIII-bVII-i progression in locrian mode
    'dorian': [[0, 3, 7], [2, 5, 9], [4, 7, 11], [0, 3, 7]],  # i-IV-V-i progression in dorian mode
    'harmonic_minor': [[0, 3, 7], [2, 5, 9], [5, 8, 12], [0, 3, 7]],  # i-iv-V-i progression in harmonic minor
    'melodic_minor': [[0, 3, 7], [2, 5, 9], [5, 8, 12], [0, 3, 7]],  # i-ii-V-i progression in melodic minor
    'chromatic': [[0, 3, 6], [1, 4, 7], [2, 5, 8], [3, 6, 9]],  # Chromatic chord progression
    'whole_tone': [[0, 4, 8], [2, 6, 10], [4, 8, 0], [6, 10, 2]],  # Whole tone chord progression
    }
    
    MOOD_SCALES: Dict[str, List[str]] = {
        'happy': ['major', 'lydian', 'mixolydian', 'pentatonic'],
        'sad': ['minor', 'phrygian', 'blues', 'locrian'],
        'energetic': ['dorian', 'harmonic_minor'],
        'suspense': ['chromatic', 'whole_tone'],
        'competition': ['melodic_minor', 'harmonic_minor']
    }
    MOOD_WITH_STRINGS: List[str] = ['sad', 'gloomy']
class ScaleGenerator:
    """Handles scale and chord generation based on mood."""
    
    def __init__(self, theory: MusicTheory):
        self.theory = theory
    
    def get_scale_for_mood(self, mood: str) -> Tuple[List[int], List[List[int]]]:
        """Generate scale and chord progression based on mood."""
        scale_types = self.theory.MOOD_SCALES.get(mood.lower())
        if not scale_types:
            print(f"Mood '{mood}' not recognized. Defaulting to 'major'.")
            scale_type = 'major'
        else:
            scale_type = random.choice(scale_types)
        
        root_note = random.choice(self.theory.NOTES)
        chord_progression = self._generate_chord_progression(root_note, scale_type)
        scale = self._generate_scale(root_note, scale_type)
        
        return scale, chord_progression
    
    def _generate_chord_progression(self, root_note: int, scale_type: str) -> List[List[int]]:
        """Generate chord progression with optional seventh notes."""
        base_progression = self.theory.SCALE_CHORDS[scale_type]
        enhanced_progression = []
        
        for chord in base_progression:
            if random.random() > 0.7:  # 30% chance for seventh
                chord = chord + [chord[0] + 10]
            enhanced_progression.append([root_note + note for note in chord])
        
        return enhanced_progression
    
    def _generate_scale(self, root_note: int, scale_type: str) -> List[int]:
        """Generate scale notes based on root note and scale type."""
        return [root_note + interval for interval in self.theory.SCALES[scale_type]]
class MelodyGenerator:
    """Generates melodic phrases and rhythms."""
    
    @staticmethod
    def generate_rhythm_pattern(length: int) -> List[float]:
        """Generate dynamic rhythm patterns."""
        base_patterns = [
            [1, 0.5, 0.5, 0.5, 0.5],
            [0.5, 0.5, 1, 0.5, 0.5],
            [0.25, 0.25, 0.5, 0.5, 0.5]
        ]
        
        pattern = []
        while len(pattern) < length:
            pattern.extend(random.choice(base_patterns))
        
        return pattern[:length]
    
    @staticmethod
    def generate_melodic_phrase(
        scale: List[int],
        length: int,
        previous_phrase: Optional[List[int]] = None
    ) -> List[int]:
        """Generate an engaging melodic phrase."""
        phrase = [previous_phrase[-1] if previous_phrase else scale[0]]
        patterns = [[0, 2, 4, 3], [0, 1, 2, 1], [0, 4, 2, 3]]
        current_pattern = random.choice(patterns)
        
        for i in range(1, length):
            last_note = phrase[-1]
            last_index = scale.index(last_note) if last_note in scale else 0
            
            if i % 4 == 0:
                pattern_index = (i // 4) % len(current_pattern)
                next_index = (last_index + current_pattern[pattern_index]) % len(scale)
            else:
                moves = [-2, -1, 1, 2] if i % 2 == 0 else [-1, 0, 1]
                next_index = (last_index + random.choice(moves)) % len(scale)
            
            phrase.append(scale[next_index])
        
        return phrase
class DrumGenerator:
    """Generates drum patterns."""
    
    def __init__(self, theory: MusicTheory):
        self.theory = theory
    
    def generate_pattern(self, bars: int) -> List[Tuple[int, float, float]]:
        """Generate a drum pattern for specified number of bars."""
        pattern = []
        for bar in range(bars):
            # Basic drum pattern: kick on 1 and 3, snare on 2 and 4
            pattern.extend([
                (self.theory.DRUM_NOTES['kick'], bar + 0.0, 0.25),
                (self.theory.DRUM_NOTES['closed_hat'], bar + 0.0, 0.25),
                (self.theory.DRUM_NOTES['snare'], bar + 0.5, 0.25),
                (self.theory.DRUM_NOTES['closed_hat'], bar + 0.5, 0.25),
                (self.theory.DRUM_NOTES['kick'], bar + 1.0, 0.25),
                (self.theory.DRUM_NOTES['closed_hat'], bar + 1.0, 0.25),
                (self.theory.DRUM_NOTES['snare'], bar + 1.5, 0.25),
                (self.theory.DRUM_NOTES['closed_hat'], bar + 1.5, 0.25),
            ])
            
            # Occasionally add fills
            if random.random() > 0.8:
                pattern.extend([
                    (self.theory.DRUM_NOTES['snare'], bar + 1.75, 0.125),
                    (self.theory.DRUM_NOTES['snare'], bar + 1.875, 0.125),
                ])
        
        return pattern

class BassGenerator:
    """Generates bass lines based on chord progressions."""
    
    def generate_bass_line(self, chord_progression: List[List[int]], bars_per_chord: int) -> List[Tuple[int, float, float]]:
        """Generate a bass line that follows the chord progression."""
        bass_line = []
        current_time = 0.0
        
        for chord in chord_progression:
            root_note = chord[0] - 12  # Move root note down one octave
            
            for _ in range(bars_per_chord):
                # Basic walking bass pattern
                bass_line.extend([
                    (root_note, current_time, 0.5),
                    (root_note + 7, current_time + 0.5, 0.5),
                    (root_note + 12, current_time + 1.0, 0.5),
                    (root_note + 7, current_time + 1.5, 0.5)
                ])
                current_time += 2.0
        
        return bass_line

class StringsGenerator:
    """Generates sustained string accompaniment."""
    
    def generate_pad(self, chord_progression: List[List[int]], bars_per_chord: int) -> List[Tuple[List[int], float, float]]:
        """Generate sustained string pads following the chord progression."""
        pad_notes = []
        current_time = 0.0
        
        for chord in chord_progression:
            # Add sustaining strings for each chord
            duration = bars_per_chord * 2.0  # 2 beats per bar
            pad_notes.append((chord, current_time, duration))
            current_time += duration
        
        return pad_notes

class MIDIComposer:
    """Handles multi-track MIDI file creation and audio conversion."""
    
    def __init__(self, tempo: int = 120):
        self.midi = MIDIFile(5)  # 5 tracks
        for track in range(5):
            self.midi.addTempo(track, 0, tempo)
    
    def add_melody(self, melody: List[int], rhythm_pattern: List[float], track: int = 0):
        """Add melody with dynamics to specified track."""
        self.midi.addProgramChange(track, 0, 0, 0)  # Piano
        melody_time = 0
        for i, (note, duration) in enumerate(zip(melody, rhythm_pattern)):
            velocity = random.randint(100, 127) if i % 4 == 0 else random.randint(85, 110)
            self.midi.addNote(track, 0, note, melody_time, duration, velocity)
            melody_time += duration
    
    def add_chords(self, progression: List[List[int]], track: int = 1):
        """Add chords to specified track."""
        self.midi.addProgramChange(track, 0, 0, 48)  # Strings
        current_time = 0
        for chord in progression:
            for note in chord:
                self.midi.addNote(track, 0, note, current_time, 2.0, 80)
            current_time += 2.0
    
    def add_bass(self, bass_notes: List[Tuple[int, float, float]], track: int = 2):
        """Add bass line to specified track."""
        self.midi.addProgramChange(track, 0, 0, 32)  # Acoustic Bass
        for note, time, duration in bass_notes:
            self.midi.addNote(track, 0, note, time, duration, 90)
    
    def add_strings(self, string_notes: List[Tuple[List[int], float, float]], track: int = 3):
        """Add string pads to specified track."""
        self.midi.addProgramChange(track, 0, 0, 88)  # String Pad
        for chord, time, duration in string_notes:
            for note in chord:
                self.midi.addNote(track, 0, note, time, duration, 70)
    
    def add_drums(self, drum_pattern: List[Tuple[int, float, float]], track: int = 4):
        """Add drums to specified track (channel 9)."""
        for note, time, duration in drum_pattern:
            self.midi.addNote(track, 9, note, time, duration, 100)
    
    def save_and_convert(self, filename: str, soundfont_path: str, duration_ms: int = 10000):
        """Save MIDI file and convert to audio formats."""
        with open(filename+'.mid', 'wb') as file:
            self.midi.writeFile(file)
        
        fs = FluidSynth(soundfont_path)
        fs.midi_to_audio(filename+'.mid', filename+'.wav')
        
        audio = AudioSegment.from_wav(filename+'.wav')
        audio.export(filename+'.mp3', format="mp3")
        os.remove(filename+'.mid')
        os.remove(filename+'.wav')
        audio = AudioSegment.from_mp3(filename+'.mp3')
        
        # Cut the audio to specified duration
        cut_audio = audio[:duration_ms]
        
        # Export the cut audio
        cut_audio.export(filename+'.mp3', format="mp3")
        print(f"Generated: {filename}'.mp3")

def get_tempo_for_mood(theory: MusicTheory, mood: str) -> int:
    """Get an appropriate tempo based on the mood."""
    if mood.lower() in theory.MOOD_TEMPOS:
        min_tempo, max_tempo = theory.MOOD_TEMPOS[mood.lower()]
        return random.randint(min_tempo, max_tempo)
    return 120  # Default tempo if mood not found

def create_multi_track_song(mood: str = 'happy', soundfont_path: str = "FluidR3_GM.sf2"):
    """Create a complete song with multiple instrument tracks."""
    # Initialize components
    theory = MusicTheory()
    scale_gen = ScaleGenerator(theory)
    scale, chord_progression = scale_gen.get_scale_for_mood(mood)
    
    # Double the chord progression for longer song
    chord_progression = chord_progression + chord_progression
    
    # Get mood-appropriate tempo
    tempo = get_tempo_for_mood(theory, mood)
    print(f"Selected tempo for {mood} mood: {tempo} BPM")
    
    # Generate all parts
    melody_gen = MelodyGenerator()
    melody = melody_gen.generate_melodic_phrase(scale, length=64)
    rhythm = melody_gen.generate_rhythm_pattern(len(melody))
    
    bass_gen = BassGenerator()
    bass_line = bass_gen.generate_bass_line(chord_progression, bars_per_chord=2)
    
    # Generate strings only for sad/gloomy moods
    strings_gen = StringsGenerator()
    string_pads = strings_gen.generate_pad(chord_progression, bars_per_chord=2)
    
    drum_gen = DrumGenerator(theory)
    drum_pattern = drum_gen.generate_pattern(bars=len(chord_progression) * 3)
    
    # Create MIDI file with all tracks
    composer = MIDIComposer(tempo=tempo)
    composer.add_melody(melody, rhythm, track=0)
    
    # Add strings only for specific moods
    if mood.lower() in theory.MOOD_WITH_STRINGS:
        composer.add_chords(chord_progression, track=1)
        composer.add_strings(string_pads, track=3)
        print(f"Added string sections for {mood} mood")
    
    composer.add_bass(bass_line, track=2)
    composer.add_drums(drum_pattern, track=4)
    
    composer.save_and_convert('output', soundfont_path)

if __name__ == "__main__":
    create_multi_track_song(mood="energetic")