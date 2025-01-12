# TFM data simulador

Simulador para generar datos para TFM.
TFM Proyecto de viabilidad de un modelo 
predictivo de la escala de depresión CES-D.

Generar datos aleatorios con sierta correlacion para evaluar 
modelos del TFM.

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