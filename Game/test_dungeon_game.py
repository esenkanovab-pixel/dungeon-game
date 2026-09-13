import pytest
import dungeon_game as game


# Позитивные и граничные тесты

@pytest.mark.parametrize("hp,damage,expected", [
    (100, 20, 80),
    (10, 25, 0),
    (20, 20, 0),
    (100, 0, 100),
])
def test_attack(hp, damage, expected):
    assert game.attack(hp, damage) == expected


def test_defend():
    assert game.defend(20) == 10


@pytest.mark.parametrize("damage,expected", [
    (9, 4),
    (0, 0),
    (1, 0),
])
def test_defend_boundaries(damage, expected):
    assert game.defend(damage) == expected


@pytest.mark.parametrize("hp,potions,amount,expected", [
    (50, 3, 20, (70, 2)),
    (95, 2, 30, (100, 1)),
    (100, 1, 20, (100, 0)),
    (50, 0, 20, (50, 0)),
])
def test_heal(hp, potions, amount, expected):
    assert game.heal(hp, potions, amount) == expected


@pytest.mark.parametrize("value,expected", [
    ("1", "1"),
    (" 2 ", "2"),
    ("3", "3"),
])
def test_valid_action(value, expected):
    assert game.parse_action(value) == expected


@pytest.mark.parametrize("player,enemy,expected", [
    (80, 50, "Победа"),
    (20, 50, "Поражение"),
    (50, 50, "Ничья"),
])
def test_result(player, enemy, expected):
    assert game.get_result(player, enemy) == expected


# Негативные тесты

@pytest.mark.parametrize("value", ["", "0", "4", "abc", "1.5"])
def test_invalid_action(value):
    with pytest.raises(ValueError):
        game.parse_action(value)


@pytest.mark.parametrize("value", [None, 1, True])
def test_invalid_action_type(value):
    with pytest.raises(TypeError):
        game.parse_action(value)


@pytest.mark.parametrize("function,args,error", [
    (game.attack, (-1, 10), ValueError),
    (game.attack, (100, -5), ValueError),
    (game.attack, (100, "20"), TypeError),
    (game.defend, (-10,), ValueError),
    (game.defend, (2.5,), TypeError),
    (game.defend, (True,), TypeError),
    (game.heal, (101, 1, 20), ValueError),
    (game.heal, (50, -1, 20), ValueError),
    (game.heal, (50, 1, -20), ValueError),
    (game.get_result, (100, -1), ValueError),
])
def test_invalid_numbers(function, args, error):
    with pytest.raises(error):
        function(*args)


# Интеграционные тесты: проверяем игру целиком.
# Заменяем пользовательский ввод и случайные числа.

def test_ten_turns(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "2")
    monkeypatch.setattr(game.random, "randint", lambda a, b: 8)

    game.main()

    output = capsys.readouterr().out
    assert output.count("Ход ") == 10
    assert "10 ходов закончились." in output


def test_early_victory(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    monkeypatch.setattr(game.random, "randint", lambda a, b: b)

    game.main()

    output = capsys.readouterr().out
    assert output.count("Ход ") == 4
    assert output.count("Враг нанёс") == 3
    assert "Ты победил врага!" in output


def test_invalid_input_in_game(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "wrong")
    monkeypatch.setattr(game.random, "randint", lambda a, b: 20)

    game.main()

    output = capsys.readouterr().out
    assert output.count("Неверный выбор! Ход пропущен.") == 5
    assert "Ты проиграл!" in output