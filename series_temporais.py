import pandas as pd
import matplotlib.pylab as plt
from datetime import datetime
from statsmodels.tsa.seasonal import seasonal_decompose
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# Carregando a base de dados
dataset = pd.read_csv('AirPassengers.csv')
print(dataset.head())

dateparse = lambda dates: pd.to_datetime(dates, format='%Y-%m')
dataset = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], index_col='Month', date_parser=dateparse)
print(dataset.head())

time_series = dataset['#Passengers']
print(time_series)

print(time_series[1])

print(time_series['1950-01-01':'1950-07-31'])

plt.plot(time_series)
plt.show()
#esta resampleando a serie temp-oral para a nivel anual('A'- indica resampling anual) e em seguida
#somando os valores dentro de cada ano
time_series_ano = time_series.resample('A').sum()
plt.plot(time_series_ano)
plt.show()
# esta agrupando os dados da série temporal pelo mês e em seguida somando os valores dentro de cada
#mes
time_series_mes = time_series.groupby([lambda x: x.month]).sum()
plt.plot(time_series_mes)
plt.show()

# selecionando um intervalo específico de datas na série temporal
time_series_datas= time_series['1960-01-01':'1960-12-01']
plt.plot(time_series_datas)
plt.show()

#Decomposição da série temporal

decomposicao = seasonal_decompose(time_series)
tendecia = decomposicao.trend
sazonal = decomposicao.seasonal
aleatorio = decomposicao.resid

plt.title("Tendencia")
plt.plot(tendecia)
plt.show()

plt.title("Sazonalidade")
plt.plot(sazonal)
plt.show()

plt.title("Aleatorio")
plt.plot(aleatorio)
plt.show()

# previsão com ARIMA
# parametros p,q e d
model = auto_arima(time_series)
# traz os melhores parametros para o ARIMA
print(model.order)

predictions = model.predict(n_periods=24)
print(predictions)

# Gráfico de previsões
print(len(time_series))

train = time_series[:130]
test = time_series[130:]

print(test.index)
model2 = auto_arima(train,suppress_warnings=True)
prediction= pd.DataFrame(model2.predict(n_periods=14), index=test.index)
prediction.columns = ['passengers_predictions']
print(prediction)

mse_arima = mean_squared_error(test, prediction)
print("Erro quadrático médio MSE ", mse_arima)

plt.figure(figsize=(8,5))
plt.plot(train, label='Training')
plt.plot(test, label='Test')
plt.plot(prediction, label='Prediction')
plt.legend()
plt.show()

