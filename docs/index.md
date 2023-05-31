![Logo do projeto](assets/logo_notas_musicais.png
){width='200' .center}

# Notas Musicais

Notas musicais é um CLI para ajudar na formação de escalas, acordes e campos hamônicos.

Toda a aplicação é baseada em um comando chamado `notas-musicais`. Esse comando tem um subcmando relacionando a cada ação que a aplicação pode realizar. Comando `escalas`, `acordes` e `campo-harmonico`.

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

## Campo hamônico

Você pode chamar os campos harmônicos via o subcomando `campo-harmonico`. Por exemplo:

```bash
poetry run notas-musicas campo-hamonico
```

Por padrão os parâmetros utilizado são a tônica de `C` e o campo hamrônico `maior`.

### Alterações nos campos harmõnicos

Você pode alterar os parâmetros da tônica e da tonalidade.

```bash
poetry run notas-musicais campo-hamonico [TONICA] [TONALIDADE]
```

### Alteração na tônica do campo

Um exemplo como campo harmônico de `E`:

```bash
poetry run notas-musicais E

┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ vii° ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#°  │
└───┴─────┴─────┴────┴───┴─────┴──────┘
```

### Alteração da tonalidade de campo

Um exemplo utilizando o campo harmonico de `E` na tonalidade `menor`:

```bash
poetry run notas-musicais campo-harmonico E menor

┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ ii° ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Em │ F#° │ G   │ Am │ Bm │ C  │ D   │
└────┴─────┴─────┴────┴────┴────┴─────┘
```

## Mais informações sobre o CLI

Para descobir outras opções, você pode usar a flag `--help`:

```bash
poetry run notas-musicais --help
```

Que irá exibir:

```bash
 Usage: notas-musicais [OPTIONS] [TONICA] [TONALIDADE]                                                 
                                                                                                
╭─ Commands ───────────────────────────────────────────────────╮
│ acorde                                                       │
│ campo-harmonico                                              │
│ escala                                                       │
╰──────────────────────────────────────────────────────────────╯
```

### Mais informações sobre os subcomandos

As informações sobre os subcomandos podem ser acessadas usando a flag `--help` após o nome do parâmentro. Um exemplo do uso do `help` nos campos hamrônicos:

```bash
 Usage: notas-musicais campo-harmonico [OPTIONS] [TONICA] [TONALIDADE]               
                                                                                     
╭─ Arguments ───────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tonica do campo harmonico [default: C]            │
│   tonalidade      [TONALIDADE]  Tonalidade do campo harmonico [default: maior]    │
╰───────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                       │
╰───────────────────────────────────────────────────────────────────────────────────╯
```
