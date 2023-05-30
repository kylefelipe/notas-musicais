from notas_musicais.escalas import NOTAS, escala


def _menor(cifra):
    nota, _ = cifra.split('m')
    if '+' in cifra:
        tonica, terca, quinta = triade(nota, 'menor')
        notas = [tonica, terca, semiton(quinta, intervalo=+1)]
        graus = ['I', 'III-', 'V+']
    else:
        notas = triade(nota, 'menor')
        graus = ['I', 'III-', 'V']
    return notas, graus


def semiton(nota, intervalo):
    pos = NOTAS.index(nota)
    return NOTAS[(pos + intervalo) % len(NOTAS)]


def triade(nota, tonalidade):
    graus = (0, 2, 4)
    notas_da_escala, _ = escala(nota, tonalidade).values()

    return [notas_da_escala[grau] for grau in graus]


def acorde(cifra: str) -> dict[str, list[str]]:
    """
    Gera as notas de um acorde a partir de uma cifra
    Parameters:
        cifra: Cifra de um acorde
    Returns:
        Um dicionário com as notas e graus do acorde
    Examples:
        >>> acorde('C')
        {'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}
        >>> acorde('Cm')
        {'notas': ['C', 'D#', 'G'], 'graus': ['I', 'III-', 'V']}
        >>> acorde('C°')
        {'notas': ['C', 'D#', 'F#'], 'graus': ['I', 'III-', 'V-']}
        >>> acorde('C+')
        {'notas': ['C', 'E', 'G#'], 'graus': ['I', 'III', 'V+']}
    """
    graus = (0, 2, 4)
    if 'm' in cifra:
        notas, graus = _menor(cifra)
    elif '°' in cifra:
        nota, _ = cifra.split('°')
        tonica, terca, quinta = triade(nota, 'menor')
        notas = [tonica, terca, semiton(quinta, intervalo=-1)]
        graus = ['I', 'III-', 'V-']
    elif '+' in cifra:
        nota, _ = cifra.split('+')
        tonica, terca, quinta = triade(nota, 'maior')
        notas = [tonica, terca, semiton(quinta, intervalo=+1)]
        graus = ['I', 'III', 'V+']
    else:
        notas = triade(cifra, 'maior')
        graus = ['I', 'III', 'V']

    return {'notas': notas, 'graus': graus}
