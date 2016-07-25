import re

harmonica = [
    "+1 (C)",
    "-1' (C#)",
    "-1 (D)",
    None, # Eb
    "+2 (E)",
    "-2'' (F)",
    "-2' (F#)",
    "-2 (G)",
    "-3''' (Ab)",
    "-3'' (A)",
    "-3' (Bb)",
    "-3 (B)",
    "+4 (C)",
    "-4' (C#)",
    "-4 (D)",
    None, # Eb
    "+5 (E)",
    "-5 (F)",
    None, # F#
    "+6 (G)",
    "-6' (Ab)",
    "-6 (A)",
    None, # Bb
    "-7 (B)",
    "+7 (C)",
    None, # C#
    "-8 (D)",
    "+8' (Eb)",
    "+8 (E)",
    "-9 (F)",
    "+9' (F#)",
    "+9 (G)",
    None, # Ab
    "-10 (A)",
    "+10'' (Bb)",
    "+10' (B)",
    "+10 (C)",
]

harmonica_bitmap = 0
for index, note in enumerate(harmonica):
    if note != None:
        harmonica_bitmap += 1 << index

def get_notes(abc):
    return re.findall(r'[_^]?[a-gA-G]', abc)

def note_value(note):
    accidental = 0
    if note[0] == '_':
        accidental = -1
    elif note[0] == '^':
        accidental = 1
    letter = note[-1]
    value = accidental + simple_note_value(letter)
    return value

def simple_note_value(note):
    return 'C.D.EF.G.A.Bc.d.ef.g.a.b'.find(note)

def normalize_note_values(note_values):
    minimum = min(note_values)
    return [value - minimum for value in note_values]

def note_values_to_bitmap(normalized_note_values):
    unique_values = set(normalized_note_values)
    bitmap = 0
    for value in unique_values:
        bitmap += 1 << value
    return bitmap

def find_positions(bitmap):
    positions = []
    for position in range(0, len(harmonica)):
        if matches_position(bitmap, position):
           positions.append(position) 
    return positions

def matches_position(bitmap, position):
    shifted_bitmap = bitmap << position
    return shifted_bitmap & harmonica_bitmap == shifted_bitmap

def main():
    #abc_input = 'CDEFGABc'
    #abc_input = 'GFGF E2 C2 | EF GFGF | EFGA _BABA | G2 z2 z4'
    #abc_input = 'CDEGAc'
    abc_input = raw_input()

    notes = get_notes(abc_input)
    note_values = [note_value(note) for note in notes]
    normalized_note_values = normalize_note_values(note_values)
    print(set(normalized_note_values))
    first = normalized_note_values[0]
    bitmap = note_values_to_bitmap(normalized_note_values)
    positions = find_positions(bitmap)
    print("Start on:")
    for position in positions:
        print(harmonica[position + first])

if __name__ == '__main__':
    main()
