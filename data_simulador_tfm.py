import numpy as np
import pandas as pd
import argparse
from sklearn.preprocessing import MinMaxScaler


def generar_dataframe(num_filas: int,
                      num_columnas: int,
                      num_col_relacionadas: int,
                      correlacion: float,
                      semilla: int = None) -> pd.DataFrame:
    """
    Genera un DataFrame de Pandas con valores aleatorios y una correlación positiva
    especificada entre las primeras columnas.La ultima columna será siempre la dependiente CES-D.

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
    cov_matrix = np.eye(num_columnas+1)
    # La columnas correlacionadas no deben ser mayor al numero de columnas
    if num_col_relacionadas <= num_columnas:
        cov_matrix[:num_col_relacionadas, :num_col_relacionadas] = correlacion
        for i in range(len(cov_matrix)):
            cov_matrix[i][i] = 1  # correlacion por defecto de cada columna

    # agregar la variable dependiente
    cov_matrix[:num_col_relacionadas, num_columnas] = correlacion
    cov_matrix[num_columnas, :num_col_relacionadas] = correlacion
    # print(cov_matrix)
    # print(cov_matrix.shape)
    data = np.random.multivariate_normal(mean=np.zeros(num_columnas+1), cov=cov_matrix, size=num_filas)

    # Creamos el DataFrame
    col_names = [f'Columna_{i+1}' for i in range(num_columnas)]
    col_names.append("CES-D")
    df = pd.DataFrame(data, columns=col_names)
    return df


def simular_data_tfm(num_filas: int,
                     num_columnas: int,
                     num_col_relacionadas: int,
                     correlacion: float,
                     semilla: int = 42,
                     nombre_csv: str = None) -> pd.DataFrame:
    df = generar_dataframe(num_filas, num_columnas, num_col_relacionadas, correlacion, semilla)
    # escalar las columnas
    scaler_x = MinMaxScaler(feature_range=(0, 100))
    x_scaled = scaler_x.fit_transform(df.drop(columns=['CES-D']))
    df_scaled = pd.DataFrame(x_scaled, columns=df.columns[:-1])

    # escalar la variable dependiente de 0 a 60
    scaler_y = MinMaxScaler(feature_range=(0, 60))
    df_scaled['CES-D'] = scaler_y.fit_transform(df[['CES-D']]).flatten()
    # solo enteros no negativos
    for col in df_scaled.columns:
        df_scaled[col] = df_scaled[col].apply(lambda x: int(x)).abs()

    # exportar a csv
    if nombre_csv:
        df_scaled.to_csv(nombre_csv, index_label='index')

    print(df_scaled.corr())  # check correlation
    return df_scaled


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
