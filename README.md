# Пример работы скрипта Predictive
## Запуск на Python 2.7.12
Полседняя стабильная версия IronPython работает под python2.7.12 (номера версий совподают)

Поэтому для начало нужно подготовить окружние перед апуском:
- Установить [Python соответствующей версии](https://www.python.org/downloads/release/python-2712/)
- Под данным Python запустить команды:
  - python2 -m pip install numpy==1.16.6
  - python2 -m pip install pandas==0.23.4
- В классе [PredicriveController, в поле _searchPath](https://github.com/altamir95/TestPredictive/blob/main/TestPredictive/TestPredictive/Controllers/PredicriveController.cs) прописать путь до пакетов python2.7, до дерективы site-packages, напрмер в моем случае это "C:\Python27\Lib\site-packages"
- После вы можете запустить проект и наблюдать за ошибками которые сыпит IronPython

## Запуск на Python 3.4.0
Полседняя бета версия IronPython работает под python3.4.0 (номера версий совподают)

Поэтому для начало нужно подготовить окружние перед апуском:
- Установить [Python соответствующей версии](https://www.python.org/downloads/release/python-340/)
- Под данным Python запустить команды:
  - python2 -m pip install numpy==1.12.1
  - python2 -m pip install pandas==0.17.1
- В классе [PredicriveController, в поле _searchPath](https://github.com/altamir95/TestPredictive/blob/main/TestPredictive/TestPredictive/Controllers/PredicriveController.cs) прописать путь до пакетов python3.4, до дерективы site-packages, напрмер в моем случае это "C:\Python34\Lib\site-packages"
- После вы можете запустить проект и наблюдать за ошибками которые сыпит IronPython
## Инструмент IronPython для установки пакетов
Конечно же IronPython позабутились о свем инструмете для установки модулей python, но он не работает.
Вы можете испробовать его на своей машине.
Правила пользования слудующие ( (здесь официальная инструкция)[https://ironpython.net/blog/2014/12/07/pip-in-ironpython-275.html] )
- Если вы работаете под полседняя стабильная версия (IronPython2.7.12)[https://ironpython.net/]:
  - Устанавливаете IronPython с [его аккаунта GitHub](https://github.com/IronLanguages/ironpython2/releases/download/ipy-2.7.12/IronPython-2.7.12.msi)
  - Находясь в _ запускаете команды 
    - ipy -X:Frames -m ensurepip
    - ipy -X:Frames -m pip install html5lib
  - Эксперементально установлеемый пакет html5lib прервался с ошибками.
- Если вы работаете под beta стабильная версия (IronPython3.4.0)[https://ironpython.net/]:
  - Устанавливаете IronPython с [его аккаунта GitHub](https://github.com/IronLanguages/ironpython3/releases/download/v3.4.0-beta1/IronPython-3.4.0b1.msi)
  - Находясь в _ запускаете команды 
    - ipy -X:Frames -m ensurepip
    - ipy -X:Frames -m pip install html5lib
  - Эксперементально установлеемый пакет html5lib прервался с ошибками.
