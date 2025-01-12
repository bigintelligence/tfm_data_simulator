# TFM data simulador

Simulador para generar datos para TFM.
TFM Proyecto de viabilidad de un modelo 
predictivo de la escala de depresión CES-D.

Generar datos aleatorios con cierta correlacion para evaluar 
modelos del TFM. 

La ultima columna será siempre la variable dependiente (CES-D).

# Requerimientos

- Python 3.10
- pip 23.2.1

# Instalacion y ejecucion
- crear un entorno virtual
```
python3 -m venv myenv
```
- instalar *requirements.txt*
```
pip install -r requirements.txt
```
- ejecutar el script
```
data_simulador_tfm.py -f 100 -c 10 -cr 5 -crr 0.8 -s 42 -n test2.csv

```
### Argumentos del script
- f --filas, type=int, numero de filas
- c --columnas, type=int, numero de columnas
- cr --columnas-relacionadas, type=int, numero de columnas relacionadas
- crr --correlacion, type=float, coeficiente de correlacion en tre las columnas relacionadas
- s --semilla, type=int, semilla'
- n --nombre-csv, type=str, Path/nombre del fichero csv a generar


### Ejemplo se salida

|index|Columna_1|Columna_2|Columna_3|Columna_4|Columna_5|Columna_6|Columna_7|Columna_8|Columna_9|Columna_10|CES-D|
|-----|---------|---------|---------|---------|---------|---------|---------|---------|---------|----------|-----|
|0    |51       |59       |47       |47       |57       |48       |65       |75       |43       |44        |34   |
|1    |68       |78       |78       |58       |62       |58       |3        |9        |35       |30        |40   |
|2    |61       |71       |68       |55       |57       |15       |36       |47       |21       |54        |29   |
|3    |77       |76       |79       |78       |81       |73       |20       |49       |2        |25        |46   |
|4    |94       |86       |90       |77       |78       |33       |38       |66       |56       |18        |50   |
|5    |57       |50       |55       |37       |39       |30       |42       |51       |71       |39        |24   |
|6    |64       |67       |69       |42       |73       |78       |58       |31       |57       |74        |35   |