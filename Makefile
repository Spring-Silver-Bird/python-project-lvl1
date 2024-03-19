install: # Установление зависимостей.
		poetry install

brain-games: # Запуск приветствия Brain-games
		poetry run brain-games

brain-even: # Запуск игры на четность
		poetry run brain-even

brain-calc: # Запуск игры-калькулятора
		poetry run brain-calc

brain-gcd: # Запуск игры на поиск наименьшего общего делителя
		poetry run brain-gcd

brain-progression: # Запуск игры на поиск члена прогресии
		poetry run brain-progression

brain-prime: # Запуск игры простое число
		poetry run brain-prime

build: # Собирает и настраивает проект
		poetry build

publish: # Отладка публикаций (выполняем после сборки)
		poetry publish --dry-run

package-install: # Установка пакета из операционной системы.
		python3 -m pip install --force-reinstall dist/hexlet_code-0.1.0-py3-none-any.whl

lint: # Проверка стиля написания кода линтером
		poetry run flake8 brain_games
