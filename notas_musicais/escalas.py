NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    r"""
    Gera uma escala a partir de uma tonica e uma tonalidade.
    Parameters:
        tonica: Nota que será a tônica da escala.
        tonalidade: Tonaliade da escala.
    Returns:
        Um dicionário com as notas e os graus da escala.
    Raises:
        ValueError: Caso a tônica não seja uma nota valida.
        KeyError: Caso a tonalidade não exista ou não tenha sido implementada.
    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
        >>> escala('a', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper()
    try:
        intervalos = ESCALAS[tonalidade]
        toinca_pos = NOTAS.index(tonica)
    except ValueError:
        raise ValueError(f'Essa nota não existe, tente uma dessas {NOTAS}')
    except KeyError:
        raise KeyError(
            'Essa escala não existe ou não foi implementada,'
            f' tente uma dessas {list(ESCALAS.keys())}'
        )
    temp = []
    for intervalo in intervalos:
        _nota = (toinca_pos + intervalo) % len(NOTAS)
        temp.append(NOTAS[_nota])
    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
