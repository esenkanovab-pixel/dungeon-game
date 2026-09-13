
import random

MAX_TURNS = 10


def main():
    player_hp = 100
    enemy_hp = 100
    potions = 3

    print("=== БИТВА В ПОДЗЕМЕЛЬЕ ===")
    print("У тебя 10 ходов, чтобы победить врага.")
    print("1 - Атаковать")
    print("2 - Защищаться")
    print("3 - Использовать аптечку")

    for turn in range(1, MAX_TURNS + 1):
        print(f"\n--- Ход {turn}/{MAX_TURNS} ---")
        print(f"Твоё HP: {player_hp}")
        print(f"HP врага: {enemy_hp}")
        print(f"Аптечки: {potions}")

        choice = input("Выбери действие (1/2/3): ").strip()

        if choice == "1":
            damage = random.randint(10, 25)
            enemy_hp -= damage
            print(f"Ты атаковал врага и нанёс {damage} урона.")
        elif choice == "2":
            print("Ты приготовился защищаться.")
        elif choice == "3":
            if potions > 0:
                heal = min(random.randint(15, 30), 100 - player_hp)
                player_hp += heal
                potions -= 1
                print(f"Ты восстановил {heal} HP.")
            else:
                print("Аптечки закончились!")
        else:
            print("Неверный выбор! Ход пропущен.")

        if enemy_hp <= 0:
            print("\nТы победил врага!")
            break

        enemy_damage = random.randint(8, 20)
        if choice == "2":
            enemy_damage //= 2
        player_hp -= enemy_damage
        print(f"Враг атаковал тебя и нанёс {enemy_damage} урона.")

        if player_hp <= 0:
            print("\nТы проиграл!")
            break
    else:
        print("\n=== 10 ходов закончились ===")
        if player_hp > enemy_hp:
            print("Ты победил по оставшемуся здоровью!")
        elif player_hp < enemy_hp:
            print("Ты проиграл: у врага осталось больше здоровья.")
        else:
            print("Ничья!")


if __name__ == "__main__":
    main()
