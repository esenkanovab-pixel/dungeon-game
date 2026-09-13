import random

MAX_TURNS = 10


def check_number(value):
    if type(value) is not int:
        raise TypeError("Требуется целое число")
    if value < 0:
        raise ValueError("Число не может быть отрицательным")


def attack(hp, damage):
    check_number(hp)
    check_number(damage)
    return max(0, hp - damage)


def defend(damage):
    check_number(damage)
    return damage // 2



def heal(hp, potions, amount):
    for value in (hp, potions, amount):
        check_number(value)

    if hp > 100:
        raise ValueError("Здоровье не может превышать 100")

    if potions == 0:
        return hp, potions

    return min(100, hp + amount), potions - 1


def parse_action(value):
    if not isinstance(value, str):
        raise TypeError("Действие должно быть строкой")

    value = value.strip()
    if value not in ("1", "2", "3"):
        raise ValueError("Выбери 1, 2 или 3")

    return value


def get_result(player_hp, enemy_hp):
    check_number(player_hp)
    check_number(enemy_hp)

    if player_hp > enemy_hp:
        return "Победа"
    if player_hp < enemy_hp:
        return "Поражение"
    return "Ничья"


def main():
    player_hp = 100
    enemy_hp = 100
    potions = 3

    print("=== БИТВА В ПОДЗЕМЕЛЬЕ ===")
    print("У тебя 10 ходов, чтобы победить.")
    print("1 — атака, 2 — защита, 3 — аптечка")

    for turn in range(1, MAX_TURNS + 1):
        print(f"\nХод {turn}/{MAX_TURNS}")
        print(f"Твоё HP: {player_hp}")
        print(f"HP врага: {enemy_hp}")
        print(f"Аптечки: {potions}")

        try:
            action = parse_action(input("Действие: "))
        except ValueError:
            action = None
            print("Неверный выбор! Ход пропущен.")

        if action == "1":
            damage = random.randint(10, 25)
            enemy_hp = attack(enemy_hp, damage)
            print(f"Ты нанёс {damage} урона.")

        elif action == "2":
            print("Ты защищаешься.")

        elif action == "3":
            if potions > 0:
                old_hp = player_hp
                player_hp, potions = heal(
                    player_hp, potions, random.randint(15, 30)
                )
                print(f"Восстановлено {player_hp - old_hp} HP.")
            else:
                print("Аптечки закончились!")

        if enemy_hp == 0:
            print("Ты победил врага!")
            return

        damage = random.randint(8, 20)
        if action == "2":
            damage = defend(damage)

        player_hp = attack(player_hp, damage)
        print(f"Враг нанёс {damage} урона.")

        if player_hp == 0:
            print("Ты проиграл!")
            return

    print("\n10 ходов закончились.")
    print(get_result(player_hp, enemy_hp))


if __name__ == "__main__":
    main()