NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escalas(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tonica e uma tonalidade.
    
    Parameters:
        tonica: Nota que será a tônica da escala.
        tonalidade: Tonaliade da escala.
    Returns:
        Um dicionário com as notas e os graus da escala.
    Examples:
        >>> escalas('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
        >>> escalas('A', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    intervalos = ESCALAS[tonalidade]
    toinca_pos = NOTAS.index(tonica)
    temp = []
    for intervalo in intervalos:
        _nota = (toinca_pos + intervalo) % len(NOTAS)
        temp.append(NOTAS[_nota])
    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
