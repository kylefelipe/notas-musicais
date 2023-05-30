![Logo do projeto](assets/logo_notas_musicais.png
){width='200' .center}

# Notas Musicais

Notas musicais é um CLI para ajudar na formação de escalas e acordes.

## Como usar?

### Escalas

Você pode usar as escalas via linha de comando. Por exemplo:

```bash
poetry run notas-musicais escala
```

Retornando os graus e as notas correspondentes a essa escala:

```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Alteração da tônica da escala

O primeiro parâmetro do CLI é a tônica da escala que deseja exibir. Desta forma, você pode alterar a escala a ser retornada. Por exemplo, a escala de `F#`:

```bash
poetry run notas-musicais escala F#
```

Resultando em:

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

#### Ateralção na tonalidade da escala

Você pode alterar a tonalidade da escala também! Esse é o segundo parametro da linha de comando. Por exemplo, a escala de `D#` maior

```bash
poetry run notas-musicais escala D# maior
```

Resultando em:

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ G   │ G# │ A# │ C  │ D   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

### Acordes

Uso básico:

```bash
poetry run notas-musicais acorde C
```

Irá retornar:

```bash
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

```bash
poetry run notas-musicais acorde C+
```

Irá retornar:

```bash
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```

```bash
poetry run notas-musicais acorde C°
```

Irá retornar:

```bash
┏━━━┳━━━━━━┳━━━━┓
┃ I ┃ III- ┃ V- ┃
┡━━━╇━━━━━━╇━━━━┩
│ C │ D#   │ F# │
└───┴──────┴────┘
```

Até o momento você pode usar acordes maiores, menores (`m`), aumentados (`+`) e diminutos (`°`)

## Mais informações sobre o CLI

Para descobir outras opções, você pode usar a flag `--help`:

```bash
poetry run notas-musicais --help
```

Que irá exibir:

```bash
 Usage: notas-musicais [OPTIONS] [TONICA] [TONALIDADE]                                                 
                                                                                                
╭─ Arguments ───────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tonica da escala [default: C]         │
│   tonalidade      [TONALIDADE]  Tonalidade da escala [default: maior] │
╰───────────────────────────────────────────────────────────────────────╯
```
