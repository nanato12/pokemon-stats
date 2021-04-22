# pokemon-stats
スクレイピングでポケモンの種族値を取得する

## pipenv
```shell
$ pipenv shell
(pokemon-stats) $ pipenv install
```

## sample
```python
from pokemon import get_pokemon_stats

pokemons = get_pokemon_stats()

for pokemon in pokemons:
    print(pokemon)
```

```python
Pokemon(number=1, name='フシギダネ', H=45, A=49, B=49, C=65, D=65, S=45, total=318)
Pokemon(number=2, name='フシギソウ', H=60, A=62, B=63, C=80, D=80, S=60, total=405)
Pokemon(number=3, name='フシギバナ', H=80, A=82, B=83, C=100, D=100, S=80, total=525)
Pokemon(number=3, name='メガフシギバナ', H=80, A=100, B=123, C=122, D=120, S=80, total=625)
Pokemon(number=4, name='ヒトカゲ', H=39, A=52, B=43, C=60, D=50, S=65, total=309)
Pokemon(number=5, name='リザード', H=58, A=64, B=58, C=80, D=65, S=80, total=405)
Pokemon(number=6, name='リザードン', H=78, A=84, B=78, C=109, D=85, S=100, total=534)
Pokemon(number=6, name='メガリザードンX', H=78, A=130, B=111, C=130, D=85, S=100, total=634)
Pokemon(number=6, name='メガリザードンY', H=78, A=104, B=78, C=159, D=115, S=100, total=634)
Pokemon(number=7, name='ゼニガメ', H=44, A=48, B=65, C=50, D=64, S=43, total=314)
.....
```

## Pokemon object
```python
class Pokemon:
    number: int
    name: str
    H: int
    A: int
    B: int
    C: int
    D: int
    S: int
    total: int
```
