Все шаги для запуска указаны на примере командной строки Linux

### issue_01
Достаточно просто запустить программу:
<code>python issue_01.py</code>

### issue_02
Необходимо вызвать pytest:
<code>pytest issue_02.py</code>

### issue_03
Необходимо вызвать unittest, например, так:
<code>python -m unittest -v issue_03.py</code>

### issue_04
В этот раз я решил вызвать verbose режим
<code>pytest -v issue_04.py</code>

### issue_05
Пример запуска теста:
<code>python -m unittest -v issue_05.py</code>

Отчет о покрытии сгенерирован утилитой coverage:

<code>coverage run issue_05.py </code>

<code>coverage html issue_05.py</code>