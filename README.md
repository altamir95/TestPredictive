# Пример работы скрипта Predictive
## Запуск на Pytho 2.7.12
Полседняя стабильная версия IronPython работает под python2.7.12 (номера версий совподают)

Поэтому для начало нужно подготовить окружние перед апуском:
- Установить [Python соответствующей версии](https://www.python.org/downloads/release/python-2712/)
- Под данным Python запустить команды:
  - python2 -m pip install numpy==1.16.6
  - python2 -m pip install pandas==0.23.4
- В классе [PredicriveController, в поле _searchPath](https://github.com/altamir95/TestPredictive/blob/main/TestPredictive/TestPredictive/Controllers/PredicriveController.cs) прописать путь до пакетов python2.7, до дерективы site-packages, напрмер в моем случае это "C:\Python27\Lib\site-packages"
- После вы можете запустить проект и наблюдать за ошибками которые сыпит IronPython

## Запуск на Pytho 3.4.0
Полседняя бета версия IronPython работает под python3.4.0 (номера версий совподают)

Поэтому для начало нужно подготовить окружние перед апуском:
- Установить [Python соответствующей версии](https://www.python.org/downloads/release/python-340/)
- Под данным Python запустить команды:
  - python2 -m pip install numpy==1.12.1
  - python2 -m pip install pandas==0.17.1
- В классе [PredicriveController, в поле _searchPath](https://github.com/altamir95/TestPredictive/blob/main/TestPredictive/TestPredictive/Controllers/PredicriveController.cs) прописать путь до пакетов python3.4, до дерективы site-packages, напрмер в моем случае это "C:\Python34\Lib\site-packages"
- После вы можете запустить проект и наблюдать за ошибками которые сыпит IronPython
