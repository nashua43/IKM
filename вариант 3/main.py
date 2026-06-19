import sys
from logic import get_hamming_numbers


def print_menu():
    """Вывод главного меню программы."""
    print("\n" + "=" * 40)
    print("   ГЕНЕРАТОР ЧИСЕЛ ХЭММИНГА")
    print("   (Простые множители: 2, 3, 5)")
    print("=" * 40)
    print("1. Получить последовательность")
    print("2. Справка об алгоритме")
    print("3. Выход")
    print("=" * 40)


def handle_sequence_generation():
    """Обработка пункта меню: генерация чисел."""
    try:
        user_input = input("\nВведите количество чисел (n > 0): ")
        n = int(user_input)

        if n <= 0:
            print("Ошибка: Количество чисел должно быть положительным.")
            return

        # Ограничение для безопасности консоли
        if n > 10000:
            confirm = input("Запрошено очень большое количество (>10000). Продолжить? (y/n): ")
            if confirm.lower() != 'y':
                print("Операция отменена.")
                return

        numbers = get_hamming_numbers(n)

        print(f"\nПервые {n} чисел:")
        # Вывод по 10 чисел в строке для удобства чтения
        for i, num in enumerate(numbers):
            print(f"{num:<12}", end="")
            if (i + 1) % 10 == 0:
                print()
        print()  # Перенос строки в конце

    except ValueError:
        print("Ошибка: Введено некорректное значение. Пожалуйста, введите целое число.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def show_help():
    """Вывод справки по алгоритму."""
    print("\n--- Справка ---")
    print("Числа Хэмминга — это натуральные числа,")
    print("разложение которых на простые множители содержит только 2, 3 и 5.")
    print("Пример: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...")
    print("\nАлгоритм использует 3 очереди для хранения кандидатов,")
    print("что позволяет получать числа строго в порядке возрастания")
    print("без необходимости сортировки всего массива.")


def main():
    """Основной цикл программы."""
    while True:
        print_menu()
        choice = input("Выберите пункт (1-3): ").strip()

        if choice == '1':
            handle_sequence_generation()
        elif choice == '2':
            show_help()
        elif choice == '3':
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()