import unittest                                  # Импортируем библиотеку unittest
from runner import Runner                        # Импортируем из модуля runner класс Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):                         # Создаем метод test_walk
        run1 = Runner("Test_1")                  # Создаем объект run1 класса Runner (из модуля runner)
        i = 1                                    # Объявляем переменную для цикла while
        while i <= 10:                           # Цикл вызывает функцию walk из класса Runner (из модуля runner) 10 раз
            run1.walk()
            i += 1                               # С каждым проходом увеличиваем переменную i на единицу
        self.assertEqual(run1.distance, 50)  # Методом assertEqual сравниваем distance объекта run1
                                                     # со значением 50


    def test_run(self):                          # Создаем метод test_run
        run2 = Runner("Test_2")                  # Создаем объект run2 класса Runner (из модуля runner)
        j = 1                                    # Объявляем переменную j для цикла while
        while j <= 10:                           # Цикл вызывает функцию run из класса Runner (из модуля runner) 10 раз
            run2.run()
            j += 1                               # С каждым проходом увеличиваем переменную j на единицу
        self.assertEqual(run2.distance, 100)   # Методом assertEqual сравниваем distance объекта run2
                                                       # со значением 100

    def test_challenge(self):                    # Создаем метод test_challenge
        run3 = Runner("Test_3")                  # Создаем объектs run3 класса Runner (из модуля runner)
        run4 = Runner("Test_3")                  # Создаем объектs run4 класса Runner (из модуля runner)
        l = 1                                    # Объявляем переменную l для цикла while
        while l <= 10:                           # Цикл вызывает функцию run из класса Runner (из модуля runner) 10 раз
            run3.run()
            run4.walk()
            l += 1                               # С каждым проходом увеличиваем переменную l на единицу
        self.assertNotEqual(run3.distance, run4.distance)  # Методом assertNotEqual сравниваем distance объектов run3 и
                                                           # run4, и убеждаемся в их неравенстве

if __name__ == "__main__":                       # Для запуска используем юнит-тест "main"
    unittest.main()
