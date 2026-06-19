from node import TreeNode
class TreeBuilder:

    def __init__(self):
        self.root = TreeNode(value=0)
        self.is_valid = True
        self.error_message = ""

    def insert(self, value, path_code):

        if not self.is_valid:
            return False

        current = self.root

        # Проходим по всем битам, кроме последнего
        for bit in path_code[:-1]:
            if bit == '0':
                if current.left is None:
                    current.left = TreeNode()
                current = current.left
            elif bit == '1':
                if current.right is None:
                    current.right = TreeNode()
                current = current.right
            else:
                self._set_error(f"Недопустимый символ в пути: '{bit}'")
                return False

        # Обработка последнего бита (целевая ячейка)
        last_bit = path_code[-1]
        if last_bit == '0':
            if current.left is None:
                current.left = TreeNode()
            target = current.left
        elif last_bit == '1':
            if current.right is None:
                current.right = TreeNode()
            target = current.right
        else:
            self._set_error(f"Недопустимый символ в пути: '{last_bit}'")
            return False

        # Проверка конфликта: ячейка уже занята ДРУГИМ значением
        if target.value is not None and target.value != value:
            self._set_error(f"Конфликт: позиция '{path_code}' уже занята значением {target.value}")
            return False

        # Записываем значение (перезапись того же значения допустима)
        target.value = value
        return True

    def _set_error(self, msg):
        self.is_valid = False
        self.error_message = msg

    def print_tree(self, node=None, prefix="", is_left=True):
        """
        Рекурсивный вывод дерева в консоль (повёрнутое на 90°).
        """
        if node is None:
            node = self.root

        if node.right:
            new_prefix = prefix + ("│   " if is_left else "    ")
            self.print_tree(node.right, new_prefix, False)

        connector = "└── " if is_left else "── "
        val_str = str(node.value) if node.value is not None else "·"
        print(prefix + connector + val_str)

        if node.left:
            new_prefix = prefix + ("    " if is_left else "│   ")
            self.print_tree(node.left, new_prefix, True)