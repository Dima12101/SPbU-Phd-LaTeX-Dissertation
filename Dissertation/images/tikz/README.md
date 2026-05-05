# Editable dissertation figures

Формат исходников: TikZ/PGF (`tikz/*.tikz`) + единый стиль `tikz/figures_style.tex`.
Векторные результаты: PDF (`pdf/*.pdf`) и SVG (`svg/*.svg`).

## Подключение в диссертацию

1. Скопировать каталог `tikz` в `Dissertation/images/tikz`.
2. В преамбулу диссертации перенести содержимое `figures_style.tex` или подключить его через `\input{Dissertation/images/tikz/figures_style.tex}`.
3. Вставлять рисунки так:

```tex
\begin{figure}[h]
  \centering
  \resizebox{0.95\textwidth}{!}{\input{Dissertation/images/tikz/fig03_ample_amr_pipeline.tikz}}
  \caption{Общий контур метода AMPLE-AMR}
  \label{fig:ample_amr_pipeline}
\end{figure}
```

Если нужно избежать TikZ-компиляции внутри основного файла, используйте готовые PDF из каталога `pdf` через `\includegraphics`.

## Состав

- `fig01_system_levels` — уровни облако/MEC/сеть/AMR.
- `fig02_amr_task_taxonomy` — типы задач AMR и их требования.
- `fig03_ample_amr_pipeline` — один управляющий раунд AMPLE-AMR.
- `fig04_auction_round_sequence` — последовательность VCG-подобного раунда.
- `fig05_qmix_ctde_architecture` — архитектура QMIX в CTDE.
- `fig06_decpomdp_mapping` — связь модели Dec-POMDP с системой.
- `fig07_clustered_c_ample` — кластеризация C-AMPLE-AMR.
- `fig08_simulation_warehouse` — схема имитационной складской среды.
- `fig09_validation_map` — связь гипотез, сценариев и метрик валидации.
