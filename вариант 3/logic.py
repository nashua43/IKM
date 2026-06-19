from queue import Queue
def get_hamming_numbers(n):
    if n <= 0:
        return []

    # Инициализация очередей
    q2 = Queue()
    q3 = Queue()
    q5 = Queue()

    result = [1]  # Первое число всегда 1

    # Заполняем очереди начальными значениями (1 * 2, 1 * 3, 1 * 5)
    q2.enqueue(2)
    q3.enqueue(3)
    q5.enqueue(5)

    # Генерируем оставшиеся n-1 чисел
    for _ in range(n - 1):
        # Находим минимальное значение среди голов очередей
        min_val = min(q2.peek(), q3.peek(), q5.peek())

        result.append(min_val)

        # Удаляем минимальное значение из всех очередей, где оно есть.
        if q2.peek() == min_val:
            q2.dequeue()
        if q3.peek() == min_val:
            q3.dequeue()
        if q5.peek() == min_val:
            q5.dequeue()

        # Добавляем новые кандидаты в очереди
        q2.enqueue(min_val * 2)
        q3.enqueue(min_val * 3)
        q5.enqueue(min_val * 5)

    return result