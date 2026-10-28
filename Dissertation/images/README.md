# Иллюстрации диссертации

Редактируемые схемы хранятся в `drawio/` и `svg/`, в диссертацию включаются
их векторные PDF. Правила оформления и перечень проверенных схем:
[DIAGRAMS.md](DIAGRAMS.md).

Для повторного экспорта всех используемых схем из корня проекта:

```sh
python3 Dissertation/images/export_diagrams.py
make dissertation
```

Для экспорта отдельных схем можно передать их имена без расширения:

```sh
python3 Dissertation/images/export_diagrams.py ch4_arch_qmix ch4_adaptive_control
```

Нужны draw.io Desktop и `rsvg-convert` из librsvg. На macOS скрипт находит
стандартную установку draw.io; другой путь можно задать переменной `DRAWIO`.
Скрипт экспорта использует только стандартную библиотеку Python.
