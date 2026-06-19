import os

class FileParser:
    @staticmethod
    def parse(filename):

        if not os.path.exists(filename):
            raise FileNotFoundError(f"Файл '{filename}' не найден.")

        entries = []
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if not lines:
            raise ValueError("Файл пуст.")

        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if len(parts) != 2:
                raise ValueError(f"Строка {line_num}: ожидается формат 'Значение Код' (через пробел).")

            val_str, code_str = parts

            # Валидация значения
            try:
                value = int(val_str)
            except ValueError:
                raise ValueError(f"Строка {line_num}: значение '{val_str}' не является целым числом.")

            # Валидация кода
            if not code_str:
                raise ValueError(f"Строка {line_num}: код пути пуст.")

            if not all(c in '01' for c in code_str):
                raise ValueError(
                    f"Строка {line_num}: код '{code_str}' содержит недопустимые символы (разрешены только 0 и 1).")

            entries.append((value, code_str))

        return entries