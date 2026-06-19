from file_parser import FileParser
from tree_builder import TreeBuilder


def print_menu():
    print("\n" + "=" * 40)
    print("   ПОСТРОЕНИЕ БИНАРНОГО ДЕРЕВА")
    print("   по двоичным кодам путей")
    print("=" * 40)
    print("1. Загрузить файл и построить дерево")
    print("2. Показать текущее дерево")
    print("3. Выход")
    print("=" * 40)


def main():
    builder = None

    while True:
        print_menu()
        choice = input("Выберите пункт (1-3): ").strip()

        if choice == '1':
            filename = input("Введите имя файла: ").strip()
            try:
                entries = FileParser.parse(filename)
                builder = TreeBuilder()

                success = True
                for value, code in entries:
                    if not builder.insert(value, code):
                        success = False
                        break

                if success:
                    print("\n Дерево успешно построено!")
                else:
                    print(f"\n Ошибка построения: {builder.error_message}")
                    builder = None  # Сброс при ошибке

            except (FileNotFoundError, ValueError) as e:
                print(f"\n Ошибка файла: {e}")
                builder = None

        elif choice == '2':
            if builder and builder.is_valid:
                print("\n--- Структура дерева ---")
                builder.print_tree()
            else:
                print("\n Дерево не построено или содержит ошибки. Загрузите файл (пункт 1).")

        elif choice == '3':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()