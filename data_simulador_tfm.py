import numpy as np
import pandas as pd
import argparse


def generar_dataframe(num_filas: int,
                      num_columnas: int,
                      num_col_relacionadas: int,
                      correlacion: float,
                      semilla: int = None) -> pd.DataFrame:
    """
    Genera un DataFrame de Pandas con valores aleatorios y una correlación positiva
    especificada entre las primeras columnas.

    Args:
    num_filas: Número de filas del DataFrame.
    num_columnas: Número de columnas del DataFrame.
    num_col_relacionadas: Número de columnas del DataFrame que estaran correlacionadas.
    correlacion: Coeficiente de correlación deseado entre las primeras columnas.
    semilla: Semilla para la generación de números aleatorios (opcional).

    Returns:
    Un DataFrame de Pandas con los datos generados.
    """

    # Fijamos la semilla si se proporciona
    if semilla is not None:
        np.random.seed(semilla)

    # Generamos una matriz de valores aleatorios estándar
    cov_matrix = np.eye(num_columnas)
    # La columnas correlacionadas no deben ser mayor al numero de columnas
    if num_col_relacionadas <= num_columnas:
        cov_matrix[:num_col_relacionadas, :num_col_relacionadas] = correlacion
        for i in range(len(cov_matrix)):
            cov_matrix[i][i] = 1  # correlacion por defecto de cada columna
    data = np.random.multivariate_normal(mean=np.zeros(num_columnas), cov=cov_matrix, size=num_filas)

    # Creamos el DataFrame
    df = pd.DataFrame(data, columns=[f'Columna_{i+1}' for i in range(num_columnas)])

    return df


def simular_data_tfm(num_filas: int,
                     num_columnas: int,
                     num_col_relacionadas: int,
                     correlacion: float,
                     semilla: int = 42,
                     nombre_csv: str = None) -> pd.DataFrame:
    df = generar_dataframe(num_filas, num_columnas, num_col_relacionadas, correlacion, semilla)
    # solo enteros no negativos
    for col in df.columns:
        df[col] = df[col].apply(lambda x: int(x*100)).abs()

    # exportar a csv
    if nombre_csv:
        df.to_csv(nombre_csv, index_label='index')

    print(df.corr())  # check correlation
    return df


if __name__ == '__main__':
    # uso para TFM
    # df = simular_data_tfm(50, 10, 5, 0.8, semilla=42, nombre_csv='BD_sintetica.csv')
    # print(df.head())
    # print(df.corr())
    parser = argparse.ArgumentParser(description='Generar datos aleatorios con sierta correlacion '
                                                 'para evaluar modelos del TFM.')
    parser.add_argument('-f', '--filas', type=int, help='numero de filas')
    parser.add_argument('-c', '--columnas', type=int, help='numero de columnas')
    parser.add_argument('-cr', '--columnas-relacionadas', type=int, help='numero de columnas relacionadas')
    parser.add_argument('-crr', '--correlacion', type=float, help='coeficiente de correlacion en tre las columnas relacionadas')
    parser.add_argument('-s', '--semilla', type=int, help='semilla', required=False)
    parser.add_argument('-n', '--nombre-csv', type=str, help='Path/nombre del fichero csv a generar')
    args = parser.parse_args()
    print(args)
    simular_data_tfm(args.filas,
                     args.columnas,
                     args.columnas_relacionadas,
                     args.correlacion,
                     semilla=args.semilla,
                     nombre_csv=args.nombre_csv)

    # ejemplo de ejecucion
    # data_simulador_tfm.py -f 100 -c 10 -cr 5 -crr 0.8 -s 42 -n BD_sintetica.csv
