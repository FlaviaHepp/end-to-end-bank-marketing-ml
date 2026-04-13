"""Marketing bancario
Resumen:
Los datos están relacionados con campañas de marketing directo (llamadas telefónicas) de una institución bancaria portuguesa. El objetivo 
de la clasificación es predecir si el cliente suscribirá un depósito a plazo (variable y).

Información del conjunto de datos:
Los datos están relacionados con campañas de marketing directo de una institución bancaria portuguesa. Las campañas de marketing se basaban 
en llamadas telefónicas. A menudo, era necesario más de un contacto con el mismo cliente para saber si el producto (depósito a plazo bancario)
estaría suscrito ('sí') o no ('no').

Información del atributo:
Datos del cliente bancario:
Edad (numérica)
Trabajo: tipo de trabajo (categórico: 'administrador', 'obrero', 'empresario', 'empleado doméstico', 'gerente', 'jubilado', 'autónomo', 
'servicios', 'estudiante', 'técnico', 'desempleado', 'desconocido')
Marital: estado civil (categórico: 'divorciado', 'casado', 'soltero', 'desconocido'; nota: 'divorciado' significa divorciado o viudo)
Educación (categórica: 'básica.4a', 'básica.6a', 'básica.9a', 'secundaria', 'analfabeto', 'curso profesional', 'título universitario', 
'desconocido')
Predeterminado: ¿tiene crédito en mora? (categórico: 'no', 'sí', 'desconocido')
Vivienda: ¿tiene crédito para vivienda? (categórico: 'no', 'sí', 'desconocido')
Préstamo: ¿tiene préstamo personal? (categórico: 'no', 'sí', 'desconocido')
Relacionado con el último contacto de la campaña actual:
Contacto: tipo de comunicación de contacto (categórica:
'celular', 'teléfono')
Mes: último mes de contacto del año (categórico: 'jan', 'feb', 'mar',
…, 'nov', 'dic')
Day_of_week: último día de contacto de la semana (categórico:
'mon', 'tue', 'wed', 'thu', 'fri')
Duración: duración del último contacto, en segundos (numérico).
Nota importante: este atributo afecta en gran medida el resultado final (por ejemplo, si
duración=0 entonces y='no'). Sin embargo, la duración no se conoce antes de que
se realice una llamada. Además, después del final de la llamada, obviamente se conoce y.
Por lo tanto, esta entrada solo se debe incluir con fines de referencia y
se debe descartar si la intención es tener un
modelo predictivo realista.
Otros atributos:
Campaña: número de contactos realizados durante esta campaña y para
este cliente (numérico, incluye el último contacto)
Pdays: número de días transcurridos desde que se
contactó por última vez al cliente de una campaña anterior (numérico; 999 significa que el cliente no fue
contactado previamente)
Anterior: número de contactos realizados antes de esta campaña y para
este cliente (numérico)
Poutcome: resultado de la campaña de marketing anterior (categórico:
'fracaso', 'inexistente', 'éxito')
Atributos del contexto social y económico
Tasa de variación del empleo: indicador trimestral
(numérico)
Cons.price.idx: índice de precios al consumidor - indicador mensual (numérico)
Cons.conf.idx: índice de confianza del consumidor - indicador mensual
(numérico)
Euribor3m: tipo de interés del euríbor a 3 meses - indicador diario (numérico)
Nr.employed: número de empleados - indicador trimestral (numérico)
Variable de salida (objetivo deseado):
y - ¿el cliente ha suscrito un depósito a plazo? (binario: 'sí', 'no')
Pasos del análisis:
Análisis de información de atributos.
Aprendizaje automático (Regresión logística, KNN, SVM, árbol de decisiones,
bosque aleatorio, Naive Bayes)
Aprendizaje profundo (ANN)"""
"""
Marketing Bancario
Resumen: Los datos corresponden a campañas de marketing directo (llamadas telefónicas) de una entidad bancaria portuguesa. El objetivo de la clasificación es predecir si el cliente contratará un depósito a plazo fijo (variable y).

Información del conjunto de datos: Los datos corresponden a campañas de marketing directo de una entidad bancaria portuguesa. Las campañas de marketing se basaron en llamadas telefónicas. A menudo, se requería más de un contacto con el mismo cliente para determinar si contrataría («sí») o no («no») el producto (depósito a plazo fijo).

Información de atributos:
Datos del cliente bancario:
Edad (numérica)
Empleo: tipo de empleo (categórico: 'administrativo', 'obrero', 'emprendedor', 'empleada doméstica', 'gerencia', 'jubilado', 'autónomo', 'servicios', 'estudiante', 'técnico', 'desempleado', 'desconocido')
Estado civil: estado civil (categórico: 'divorciado', 'casado', 'soltero', 'desconocido'; nota: 'divorciado' significa divorciado o viudo)
Educación (categórico: 'básico 4 años', 'básico 6 años', 'básico 9 años', 'secundaria', 'analfabeto', 'curso profesional', 'título universitario', 'desconocido')
Impago: ¿tiene crédito en mora? (categórico: 'no', 'sí', 'desconocido')
Vivienda: ¿Tiene préstamo hipotecario? (categórico: 'no', 'sí', 'desconocido')
Préstamo: ¿Tiene préstamo personal? (categórico: 'no', 'sí', 'desconocido')
Relacionado con el último contacto de la campaña actual:
Contacto: Tipo de comunicación del contacto (categórico: 'celular', 'teléfono')
Mes: Mes del año del último contacto (categórico: 'ene', 'feb', 'mar', ..., 'nov', 'dic')
Día de la semana: Día de la semana del último contacto (categórico: 'lun', 'mar', 'mié', 'jue', 'vie')
Duración: Duración del último contacto, en segundos (numérico). Nota importante: este atributo afecta significativamente al resultado final (por ejemplo, si duración = 0, entonces y = 'no'). Sin embargo, la duración no se conoce antes de realizar la llamada. Además, una vez finalizada la llamada, el valor de y es obviamente conocido. Por lo tanto, este dato solo debe incluirse con fines comparativos y debe descartarse si se pretende obtener un modelo predictivo realista. Otros atributos:
Campaña: número de contactos realizados durante esta campaña y para este cliente (numérico, incluye el último contacto)
Días transcurridos: número de días desde el último contacto con el cliente en una campaña anterior (numérico; 999 significa que no se contactó previamente con el cliente)
Anterior: número de contactos realizados antes de esta campaña y para este cliente (numérico)
Resultado: resultado de la campaña de marketing anterior (categórico: 'fracaso', 'inexistente', 'éxito')
Atributos del contexto socioeconómico
Tasa de variación del empleo: indicador trimestral (numérico)
Índice de precios al consumidor: indicador mensual (numérico)
Índice de confianza del consumidor: indicador mensual (numérico)
Euribor a 3 meses: indicador diario (numérico)
Número de empleados: indicador trimestral (numérico)
Variable de salida (objetivo deseado):
¿El cliente ha contratado un depósito a plazo fijo? (binario: 'sí', 'no')
Fuente: """
#Conjunto de datos de: http://archive.ics.uci.edu/ml/datasets/Bank+Marketing#
# Importación de bibliotecas de análisis de datos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
bank = pd.read_csv('bank-additional-full.csv', sep = ';')

#Conversión de variable dependiente categórica a variable ficticia
y = pd.get_dummies(bank['y'], columns = ['y'], prefix = ['y'], drop_first = True)
bank.head()

# Eche un vistazo al tipo, número de columnas, entradas, valores nulos, etc.
bank.info()
# bank.isnull().any() # Una forma de buscar valores nulos

#bank.columns1. Análisis y tratamiento categórico de datos de clientes bancarios
#Trabajar con los atributos relacionados con los clientes bancarios
#Para mayor claridad, voy a crear un nuevo conjunto de datos que contenga solo esta parte de los datos.
bank_client = bank.iloc[: , 0:7]
bank_client.head()

#1.1. Conocer las variables categóricas
# conocer las variables categóricas, para saber que tipo de variables tenemos y como tratarlas
print('Jobs:\n', bank_client['job'].unique())

print('Marital:\n', bank_client['marital'].unique())

print('Education:\n', bank_client['education'].unique())

print('Default:\n', bank_client['default'].unique())
print('Housing:\n', bank_client['housing'].unique())
print('Loan:\n', bank_client['loan'].unique())

#1.2. Edad
#Intentando obtener información al cruzar esas variables
#Intentando encontrar valores extraños o nulos
print('Min age: ', bank_client['age'].max())
print('Max age: ', bank_client['age'].min())
print('Null Values: ', bank_client['age'].isnull().any())

fig, ax = plt.subplots()
fig.set_size_inches(20, 8)
sns.countplot(x = 'age', data = bank_client)
ax.set_xlabel('Age', fontsize=15)
ax.set_ylabel('Count', fontsize=15)
ax.set_title('Age Count Distribution', fontsize=15)
sns.despine()

fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize = (13, 5))
sns.boxplot(x = 'age', data = bank_client, orient = 'v', ax = ax1)
ax1.set_xlabel('People Age', fontsize=15)
ax1.set_ylabel('Age', fontsize=15)
ax1.set_title('Age Distribution', fontsize=15)
ax1.tick_params(labelsize=15)

sns.distplot(bank_client['age'], ax = ax2)
sns.despine(ax = ax2)
ax2.set_xlabel('Age', fontsize=15)
ax2.set_ylabel('Occurence', fontsize=15)
ax2.set_title('Age x Ocucurence', fontsize=15)
ax2.tick_params(labelsize=15)

plt.subplots_adjust(wspace=0.5)
plt.tight_layout() 

# Cuartiles
print('1º Quartile: ', bank_client['age'].quantile(q = 0.25))
print('2º Quartile: ', bank_client['age'].quantile(q = 0.50))
print('3º Quartile: ', bank_client['age'].quantile(q = 0.75))
print('4º Quartile: ', bank_client['age'].quantile(q = 1.00))
#Calcular los valores atípicos:
   # Rango intercuartil (RIC) = Q3 - Q1
   # Bigote inferior (1,5 * RIC) = Q1 - 1,5 * RIC
   # Bigote superior (1,5 * RIC) = Q3 + 1,5 * RIC
    
print('Ages above: ', bank_client['age'].quantile(q = 0.75) + 
                      1.5*(bank_client['age'].quantile(q = 0.75) - bank_client['age'].quantile(q = 0.25)), 'are outliers')
                      
print('Numerber of outliers: ', bank_client[bank_client['age'] > 69.6]['age'].count())
print('Number of clients: ', len(bank_client))
#Valores atípicos en %
print('Outliers are:', round(bank_client[bank_client['age'] > 69.6]['age'].count()*100/len(bank_client),2), '%')

# Calcular algunos valores para evaluar esta variable independiente
print('MEAN:', round(bank_client['age'].mean(), 1))
# Una desviación estándar baja indica que los puntos de datos tienden a estar cerca de la media o del valor esperado.
# Una desviación estándar alta indica que los puntos de datos están dispersos.
print('STD :', round(bank_client['age'].std(), 1))
#Creo que la mejor manera de obtener una idea precisa de la dispersión es utilizando el coeficiente de variación (CV) (desviación estándar/media)*100.
#CV < 15%: baja dispersión.
#V > 30%: alta dispersión.
print('CV  :',round(bank_client['age'].std()*100/bank_client['age'].mean(), 1), ', High middle dispersion')

#Conclusión sobre la EDAD: en mi opinión, debido a la alta dispersión y a que solo observamos este gráfico, no podemos concluir si la edad tiene un gran efecto sobre nuestra variable y. Necesitamos seguir buscando algún patrón. Una dispersión media-alta significa que tenemos personas de todas las edades y que tal vez todas puedan contratar un depósito a plazo fijo, o no. Se calcularon los valores atípicos, así que mi idea es ajustar el modelo con y sin ellos.

#1.3. EMPLEOS
# ¿Qué tipo de empleos tienen los clientes de este banco? Si cruzamos empleos con impago, préstamos o vivienda, no hay relación.
fig, ax = plt.subplots()
fig.set_size_inches(20, 8)
sns.countplot(x = 'job', data = bank_client)
ax.set_xlabel('Job', fontsize=15)
ax.set_ylabel('Count', fontsize=15)
ax.set_title('Age Count Distribution', fontsize=15)
ax.tick_params(labelsize=15)
sns.despine()

#1.4. MATRIMONIAL
# ¿Qué tipo de "clientes matrimoniales" tiene este banco? Si se combina "matrimonial" con "impago", "préstamo" o "vivienda", no hay relación.
fig, ax = plt.subplots()
fig.set_size_inches(10, 5)
sns.countplot(x = 'marital', data = bank_client)
ax.set_xlabel('Marital', fontsize=15)
ax.set_ylabel('Count', fontsize=15)
ax.set_title('Age Count Distribution', fontsize=15)
ax.tick_params(labelsize=15)
sns.despine()

#1.5. EDUCACIÓN
# ¿Qué tipo de clientes con formación académica tiene este banco? Si se relaciona educación con impago, préstamo o vivienda, no hay ninguna relación.
fig, ax = plt.subplots()
fig.set_size_inches(20, 5)
sns.countplot(x = 'education', data = bank_client)
ax.set_xlabel('Education', fontsize=15)
ax.set_ylabel('Count', fontsize=15)
ax.set_title('Education Count Distribution', fontsize=15)
ax.tick_params(labelsize=15)
sns.despine()

#1.6. INCUMPLIMIENTO DE PRÉSTAMO DE VIVIENDA
# ¿Tiene crédito en mora?
fig, (ax1, ax2, ax3) = plt.subplots(nrows = 1, ncols = 3, figsize = (20,8))
sns.countplot(x = 'default', data = bank_client, ax = ax1, order = ['no', 'unknown', 'yes'])
ax1.set_title('Default', fontsize=15)
ax1.set_xlabel('')
ax1.set_ylabel('Count', fontsize=15)
ax1.tick_params(labelsize=15)

# Vivienda, ¿tiene préstamo hipotecario?
sns.countplot(x = 'housing', data = bank_client, ax = ax2, order = ['no', 'unknown', 'yes'])
ax2.set_title('Housing', fontsize=15)
ax2.set_xlabel('')
ax2.set_ylabel('Count', fontsize=15)
ax2.tick_params(labelsize=15)

# Préstamo, ¿tiene préstamo personal?
sns.countplot(x = 'loan', data = bank_client, ax = ax3, order = ['no', 'unknown', 'yes'])
ax3.set_title('Loan', fontsize=15)
ax3.set_xlabel('')
ax3.set_ylabel('Count', fontsize=15)
ax3.tick_params(labelsize=15)

plt.subplots_adjust(wspace=0.25)

print('Default:\n No credit in default:'     , bank_client[bank_client['default'] == 'no']     ['age'].count(),
              '\n Unknown credit in default:', bank_client[bank_client['default'] == 'unknown']['age'].count(),
              '\n Yes to credit in default:' , bank_client[bank_client['default'] == 'yes']    ['age'].count())

print('Housing:\n No housing in loan:'     , bank_client[bank_client['housing'] == 'no']     ['age'].count(),
              '\n Unknown housing in loan:', bank_client[bank_client['housing'] == 'unknown']['age'].count(),
              '\n Yes to housing in loan:' , bank_client[bank_client['housing'] == 'yes']    ['age'].count())

print('Housing:\n No to personal loan:'     , bank_client[bank_client['loan'] == 'no']     ['age'].count(),
              '\n Unknown to personal loan:', bank_client[bank_client['loan'] == 'unknown']['age'].count(),
              '\n Yes to personal loan:'    , bank_client[bank_client['loan'] == 'yes']    ['age'].count())

#CONCLUSIÓN SOBRE CLIENTES BANCARIOS
#Las edades no son muy relevantes, presentan una dispersión media y su relación con otras variables no aporta información útil.

#Empleo, Estado Civil y Educación: creo que el mejor análisis consiste simplemente en el recuento de cada variable. Si se relacionan con las demás, no se llega a una conclusión definitiva. Todas estas variables tienen valores "sí", "desconocido" y "no" para préstamos, impagos y vivienda.

#Impago, préstamos y vivienda: solo sirven para observar la distribución de la población.

#1.7. Tratamiento Categórico de Clientes Bancarios
#Empleo, Estado Civil, Educación, Impago, Vivienda, Préstamo. Se convertirá a variables continuas debido a que posteriormente se aplicará el escalado de características.
#El orden del codificador de etiquetas es alfabético.

from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
bank_client['job']      = labelencoder_X.fit_transform(bank_client['job']) 
bank_client['marital']  = labelencoder_X.fit_transform(bank_client['marital']) 
bank_client['education']= labelencoder_X.fit_transform(bank_client['education']) 
bank_client['default']  = labelencoder_X.fit_transform(bank_client['default']) 
bank_client['housing']  = labelencoder_X.fit_transform(bank_client['housing']) 
bank_client['loan']     = labelencoder_X.fit_transform(bank_client['loan']) 
#función para crear un grupo de edades, esto ayuda porque aquí tenemos 78 valores diferentes.
def age(dataframe):
    dataframe.loc[dataframe['age'] <= 32, 'age'] = 1
    dataframe.loc[(dataframe['age'] > 32) & (dataframe['age'] <= 47), 'age'] = 2
    dataframe.loc[(dataframe['age'] > 47) & (dataframe['age'] <= 70), 'age'] = 3
    dataframe.loc[(dataframe['age'] > 70) & (dataframe['age'] <= 98), 'age'] = 4
           
    return dataframe

age(bank_client);
bank_client.head()

# Manera manual de convertir categórica en continua

bank_client['job'].replace(['housemaid' , 'services' , 'admin.' , 'blue-collar' , 'technician', 'retired' , 'management', 'unemployed', 'self-employed', 'unknown' , 'entrepreneur', 'student'] , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], inplace=True)

bank_client['education'].replace(['basic.4y' , 'high.school', 'basic.6y', 'basic.9y', 'professional.course', 'unknown' , 'university.degree' , 'illiterate'], [1, 2, 3, 4, 5, 6, 7, 8], inplace=True)

bank_client['marital'].replace(['married', 'single', 'divorced', 'unknown'], [1, 2, 3, 4], inplace=True)

bank_client['default'].replace(['yes', 'no', 'unknown'],[1, 2, 3], inplace=True)

bank_client['housing'].replace(['yes', 'no', 'unknown'],[1, 2, 3], inplace=True)

bank_client['loan'].replace(['yes', 'no', 'unknown'],[1, 2, 3], inplace=True)

#Una forma de convertir variables categóricas usando variables ficticias si lo considera necesario, aunque en este caso no lo es porque ya se han convertido a continuas.

bank_client = pd.get_dummies(data = bank_client, columns = ['job'] , prefix = ['job'] , drop_first = True)

bank_client = pd.get_dummies(data = bank_client, columns = ['marital'] , prefix = ['marital'] , drop_first = True)

bank_client = pd.get_dummies(data = bank_client, columns = ['education'], prefix = ['education'], drop_first = True)

bank_client = pd.get_dummies(data = bank_client, columns = ['default'] , prefix = ['default'] , drop_first = True)

bank_client = pd.get_dummies(data = bank_client, columns = ['housing'] , prefix = ['housing'] , drop_first = True)

bank_client = pd.get_dummies(data = bank_client, columns = ['loan'] , prefix = ['loan'] , drop_first = True)

print(bank_client.shape)
bank_client.head()

#2. Relacionado con el último contacto de la campaña actual
# Tratar variables categóricas, ver esos valores
# Agrupar variables continuas si es necesario
# Segmentar el DataFrame para tratarlo por separado, simplificar el proceso
bank_related = bank.iloc[: , 7:11]
bank_related.head()

bank_related.isnull().any()

print("Kind of Contact: \n", bank_related['contact'].unique())
print("\nWhich monthis this campaing work: \n", bank_related['month'].unique())
print("\nWhich days of week this campaing work: \n", bank_related['day_of_week'].unique())

#2.1 Duración
fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize = (13, 5))
sns.boxplot(x = 'duration', data = bank_related, orient = 'v', ax = ax1)
ax1.set_xlabel('Calls', fontsize=10)
ax1.set_ylabel('Duration', fontsize=10)
ax1.set_title('Calls Distribution', fontsize=10)
ax1.tick_params(labelsize=10)

sns.distplot(bank_related['duration'], ax = ax2)
sns.despine(ax = ax2)
ax2.set_xlabel('Duration Calls', fontsize=10)
ax2.set_ylabel('Occurence', fontsize=10)
ax2.set_title('Duration x Ocucurence', fontsize=10)
ax2.tick_params(labelsize=10)

plt.subplots_adjust(wspace=0.5)
plt.tight_layout() 

#Nota: la duración es diferente de la edad. La edad tiene 78 valores y la duración tiene 1544 valores diferentes.
print("Max duration  call in minutes:  ", round((bank_related['duration'].max()/60),1))
print("Min duration  call in minutes:   ", round((bank_related['duration'].min()/60),1))
print("Mean duration call in minutes:   ", round((bank_related['duration'].mean()/60),1))
print("STD duration  call in minutes:   ", round((bank_related['duration'].std()/60),1))
# Desviación estándar cercana a la media significa que los valores de los datos están cerca de la media.

# Cuartiles
print('1º Quartile: ', bank_related['duration'].quantile(q = 0.25))
print('2º Quartile: ', bank_related['duration'].quantile(q = 0.50))
print('3º Quartile: ', bank_related['duration'].quantile(q = 0.75))
print('4º Quartile: ', bank_related['duration'].quantile(q = 1.00))
#Calcular los valores atípicos:
   # Rango intercuartil (RIC) = Q3 - Q1
   # Bigote inferior (1,5 * RIC) = Q1 - 1,5 * RIC
   # Bigote superior (1,5 * RIC) = Q3 + 1,5 * RIC
    
print('Duration calls above: ', bank_related['duration'].quantile(q = 0.75) + 
                      1.5*(bank_related['duration'].quantile(q = 0.75) - bank_related['duration'].quantile(q = 0.25)), 'are outliers')

print('Numerber of outliers: ', bank_related[bank_related['duration'] > 644.5]['duration'].count())
print('Number of clients: ', len(bank_related))
#Valores atípicos en %
print('Outliers are:', round(bank_related[bank_related['duration'] > 644.5]['duration'].count()*100/len(bank_related),2), '%')

# Mira, si la duración de la llamada es igual a 0, entonces es obvio que esta persona no se suscribió.
# ESTAS LÍNEAS DEBEN ELIMINARSE DESPUÉS
bank[(bank['duration'] == 0)]

#2.2 Contacto, Mes, Día de la semana
fig, (ax1, ax2, ax3) = plt.subplots(nrows = 1, ncols = 3, figsize = (15,6))
sns.countplot(bank_related['contact'], ax = ax1)
ax1.set_xlabel('Contact', fontsize = 10)
ax1.set_ylabel('Count', fontsize = 10)
ax1.set_title('Contact Counts')
ax1.tick_params(labelsize=10)

sns.countplot(bank_related['month'], ax = ax2, order = ['mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
ax2.set_xlabel('Months', fontsize = 10)
ax2.set_ylabel('')
ax2.set_title('Months Counts')
ax2.tick_params(labelsize=10)

sns.countplot(bank_related['day_of_week'], ax = ax3)
ax3.set_xlabel('Day of Week', fontsize = 10)
ax3.set_ylabel('')
ax3.set_title('Day of Week Counts')
ax3.tick_params(labelsize=10)

plt.subplots_adjust(wspace=0.25)

print('Ages above: ', bank_related['duration'].quantile(q = 0.75) + 
                      1.5*(bank_related['duration'].quantile(q = 0.75) - bank_related['duration'].quantile(q = 0.25)), 'are outliers')

bank_related[bank_related['duration'] > 640].count()

#2.1 Contacto, Mes, Día de la Semana del tratamiento
# El orden del codificador de etiquetas es alfabético
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
bank_related['contact']     = labelencoder_X.fit_transform(bank_related['contact']) 
bank_related['month']       = labelencoder_X.fit_transform(bank_related['month']) 
bank_related['day_of_week'] = labelencoder_X.fit_transform(bank_related['day_of_week']) 

#Una forma de convertir variables categóricas usando variables ficticias si lo considera necesario

bank_related = pd.get_dummies(data = bank_related, prefix = ['contact'] , columns = ['contact'] , drop_first = True)

bank_related = pd.get_dummies(data = bank_related, prefix = ['month'] , columns = ['month'] , drop_first = True)

bank_related = pd.get_dummies(data = bank_related, prefix = ['day_of_week'], columns = ['day_of_week'], drop_first = True)

bank_related.head()

def duration(data):

    data.loc[data['duration'] <= 102, 'duration'] = 1
    data.loc[(data['duration'] > 102) & (data['duration'] <= 180)  , 'duration']    = 2
    data.loc[(data['duration'] > 180) & (data['duration'] <= 319)  , 'duration']   = 3
    data.loc[(data['duration'] > 319) & (data['duration'] <= 644.5), 'duration'] = 4
    data.loc[data['duration']  > 644.5, 'duration'] = 5

    return data
duration(bank_related);
bank_related.head()

#Atributos del contexto social y económico
bank_se = bank.loc[: , ['emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']]
bank_se.head()

#Otros atributos                                        
bank_o = bank.loc[: , ['campaign', 'pdays','previous', 'poutcome']]
bank_o.head()

bank_o['poutcome'].unique()

bank_o['poutcome'].replace(['nonexistent', 'failure', 'success'], [1,2,3], inplace  = True)

#Modelo
bank_final= pd.concat([bank_client, bank_related, bank_se, bank_o], axis = 1)
bank_final= pd.concat([bank_client, bank_related, bank_se, bank_o], axis = 1)
bank_final.shape
print("checkpoint")
print(bank_final.columns)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(bank_final, y, test_size = 0.1942313295, random_state = 101)

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix, accuracy_score
k_fold = KFold(n_splits=10, shuffle=True, random_state=0)
X_train.head()

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression() 
logmodel.fit(X_train,y_train)
logpred = logmodel.predict(X_test)


print(confusion_matrix(y_test, logpred))
print(round(accuracy_score(y_test, logpred),2)*100)
LOGCV = (cross_val_score(logmodel, X_train, y_train, cv=k_fold, n_jobs=1, scoring = 'accuracy').mean())

from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier

X_trainK, X_testK, y_trainK, y_testK = train_test_split(bank_final, y, test_size = 0.2, random_state = 101)

#Neighbors
neighbors = np.arange(0,25)

#Crea una lista vacía que contendrá las puntuaciones de los currículos
cv_scores = []

#Realizar validación cruzada de 10 pliegues en el conjunto de entrenamiento para valores impares de k:
for k in neighbors:
    k_value = k+1
    knn = KNeighborsClassifier(n_neighbors = k_value, weights='uniform', p=2, metric='euclidean')
    kfold = model_selection.KFold(n_splits=10, shuffle=True, random_state=123)
    scores = model_selection.cross_val_score(knn, X_trainK, y_trainK, cv=kfold, scoring='accuracy')
    cv_scores.append(scores.mean()*100)
    print("k=%d %0.2f (+/- %0.2f)" % (k_value, scores.mean()*100, scores.std()*100))

optimal_k = neighbors[cv_scores.index(max(cv_scores))]
print ("The optimal number of neighbors is %d with %0.1f%%" % (optimal_k, cv_scores[optimal_k]))

plt.plot(neighbors, cv_scores)
plt.xlabel('Number of Neighbors K')
plt.ylabel('Train Accuracy')
plt.show()

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=22)
knn.fit(X_train, y_train)
knnpred = knn.predict(X_test)

print(confusion_matrix(y_test, knnpred))
print(round(accuracy_score(y_test, knnpred),2)*100)
KNNCV = (cross_val_score(knn, X_train, y_train, cv=k_fold, n_jobs=1, scoring = 'accuracy').mean())

from sklearn.svm import SVC
svc= SVC(kernel = 'sigmoid')
svc.fit(X_train, y_train)
svcpred = svc.predict(X_test)
print(confusion_matrix(y_test, svcpred))
print(round(accuracy_score(y_test, svcpred),2)*100)
SVCCV = (cross_val_score(svc, X_train, y_train, cv=k_fold, n_jobs=1, scoring = 'accuracy').mean())

from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier(criterion='gini') #criterion = entopy, gini
dtree.fit(X_train, y_train)
dtreepred = dtree.predict(X_test)

print(confusion_matrix(y_test, dtreepred))
print(round(accuracy_score(y_test, dtreepred),2)*100)
DTREECV = (cross_val_score(dtree, X_train, y_train, cv=k_fold, n_jobs=1, scoring = 'accuracy').mean())

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators = 200)#criterion = entopy,gini
rfc.fit(X_train, y_train)
rfcpred = rfc.predict(X_test)

print(confusion_matrix(y_test, rfcpred ))
print(round(accuracy_score(y_test, rfcpred),2)*100)
RFCCV = (cross_val_score(rfc, X_train, y_train, cv=k_fold, n_jobs=1, scoring = 'accuracy').mean())

from sklearn.naive_bayes import GaussianNB
gaussiannb= GaussianNB()
gaussiannb.fit(X_train, y_train)
gaussiannbpred = gaussiannb.predict(X_test)
probs = gaussiannb.predict(X_test)

print(confusion_matrix(y_test, gaussiannbpred ))
print(round(accuracy_score(y_test, gaussiannbpred),2)*100)
GAUSIAN = (cross_val_score(gaussiannb, X_train, y_train, cv=k_fold, n_jobs=1, scoring = 'accuracy').mean())

from xgboost import XGBClassifier
xgb = XGBClassifier()
xgb.fit(X_train, y_train)
xgbprd = xgb.predict(X_test)

print(confusion_matrix(y_test, xgbprd ))
print(round(accuracy_score(y_test, xgbprd),2)*100)
XGB = (cross_val_score(estimator = xgb, X = X_train, y = y_train, cv = 10).mean())

from sklearn.ensemble import GradientBoostingClassifier
gbk = GradientBoostingClassifier()
gbk.fit(X_train, y_train)
gbkpred = gbk.predict(X_test)
print(confusion_matrix(y_test, gbkpred ))
print(round(accuracy_score(y_test, gbkpred),2)*100)
GBKCV = (cross_val_score(gbk, X_train, y_train, cv=k_fold, n_jobs=1, scoring = 'accuracy').mean())

models = pd.DataFrame({
                'Models': ['Random Forest Classifier', 'Decision Tree Classifier', 'Support Vector Machine',
                           'K-Near Neighbors', 'Logistic Model', 'Gausian NB', 'XGBoost', 'Gradient Boosting'],
                'Score':  [RFCCV, DTREECV, SVCCV, KNNCV, LOGCV, GAUSIAN, XGB, GBKCV]})

models.sort_values(by='Score', ascending=False)

#La precisión se mide mediante el área bajo la curva ROC. Un área de 1 representa una prueba perfecta; un área de 0,5 representa una prueba inútil.

#Una guía aproximada para clasificar la precisión de una prueba diagnóstica es el sistema de puntuación académico tradicional:

#0,90-1 = excelente (A)

#0,80-0,90 = buena (B)

#0,70-0,80 = regular (C)

#0,60-0,70 = deficiente (D)

#0,50-0,60 = suspenso (F)

#XGBOOST ROC/AUC, MEJOR MODELO
from sklearn import metrics
fig, (ax, ax1) = plt.subplots(nrows = 1, ncols = 2, figsize = (15,5))
probs = xgb.predict_proba(X_test)
preds = probs[:,1]
fprxgb, tprxgb, thresholdxgb = metrics.roc_curve(y_test, preds)
roc_aucxgb = metrics.auc(fprxgb, tprxgb)

ax.plot(fprxgb, tprxgb, 'b', label = 'AUC = %0.2f' % roc_aucxgb)
ax.plot([0, 1], [0, 1],'r--')
ax.set_title('Receiver Operating Characteristic XGBOOST ',fontsize=10)
ax.set_ylabel('True Positive Rate',fontsize=20)
ax.set_xlabel('False Positive Rate',fontsize=15)
ax.legend(loc = 'lower right', prop={'size': 16})

#Gradiente Boosting ROC/AUC, SEGUNDO MEJOR MODELO
probs = gbk.predict_proba(X_test)
preds = probs[:,1]
fprgbk, tprgbk, thresholdgbk = metrics.roc_curve(y_test, preds)
roc_aucgbk = metrics.auc(fprgbk, tprgbk)

ax1.plot(fprgbk, tprgbk, 'b', label = 'AUC = %0.2f' % roc_aucgbk)
ax1.plot([0, 1], [0, 1],'r--')
ax1.set_title('Receiver Operating Characteristic GRADIENT BOOST ',fontsize=10)
ax1.set_ylabel('True Positive Rate',fontsize=20)
ax1.set_xlabel('False Positive Rate',fontsize=15)
ax1.legend(loc = 'lower right', prop={'size': 16})

plt.subplots_adjust(wspace=1)

#fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows = 2, ncols = 3, figsize = (15, 4))
fig, ax_arr = plt.subplots(nrows = 2, ncols = 3, figsize = (20,15))

#LOGMODEL#MODELO DE REGISTRO
probs = logmodel.predict_proba(X_test)
preds = probs[:,1]
fprlog, tprlog, thresholdlog = metrics.roc_curve(y_test, preds)
roc_auclog = metrics.auc(fprlog, tprlog)

ax_arr[0,0].plot(fprlog, tprlog, 'b', label = 'AUC = %0.2f' % roc_auclog)
ax_arr[0,0].plot([0, 1], [0, 1],'r--')
ax_arr[0,0].set_title('Receiver Operating Characteristic Logistic ',fontsize=20)
ax_arr[0,0].set_ylabel('True Positive Rate',fontsize=20)
ax_arr[0,0].set_xlabel('False Positive Rate',fontsize=15)
ax_arr[0,0].legend(loc = 'lower right', prop={'size': 16})

#RANDOM FOREST --------------------
probs = rfc.predict_proba(X_test)
preds = probs[:,1]
fprrfc, tprrfc, thresholdrfc = metrics.roc_curve(y_test, preds)
roc_aucrfc = metrics.auc(fprrfc, tprrfc)

ax_arr[0,1].plot(fprrfc, tprrfc, 'b', label = 'AUC = %0.2f' % roc_aucrfc)
ax_arr[0,1].plot([0, 1], [0, 1],'r--')
ax_arr[0,1].set_title('Receiver Operating Characteristic Random Forest ',fontsize=20)
ax_arr[0,1].set_ylabel('True Positive Rate',fontsize=20)
ax_arr[0,1].set_xlabel('False Positive Rate',fontsize=15)
ax_arr[0,1].legend(loc = 'lower right', prop={'size': 16})

#KNN----------------------
probs = knn.predict_proba(X_test)
preds = probs[:,1]
fprknn, tprknn, thresholdknn = metrics.roc_curve(y_test, preds)
roc_aucknn = metrics.auc(fprknn, tprknn)

ax_arr[0,2].plot(fprknn, tprknn, 'b', label = 'AUC = %0.2f' % roc_aucknn)
ax_arr[0,2].plot([0, 1], [0, 1],'r--')
ax_arr[0,2].set_title('Receiver Operating Characteristic KNN ',fontsize=20)
ax_arr[0,2].set_ylabel('True Positive Rate',fontsize=20)
ax_arr[0,2].set_xlabel('False Positive Rate',fontsize=15)
ax_arr[0,2].legend(loc = 'lower right', prop={'size': 16})

#DECISION TREE ---------------------
probs = dtree.predict_proba(X_test)
preds = probs[:,1]
fprdtree, tprdtree, thresholddtree = metrics.roc_curve(y_test, preds)
roc_aucdtree = metrics.auc(fprdtree, tprdtree)

ax_arr[1,0].plot(fprdtree, tprdtree, 'b', label = 'AUC = %0.2f' % roc_aucdtree)
ax_arr[1,0].plot([0, 1], [0, 1],'r--')
ax_arr[1,0].set_title('Receiver Operating Characteristic Decision Tree ',fontsize=20)
ax_arr[1,0].set_ylabel('True Positive Rate',fontsize=20)
ax_arr[1,0].set_xlabel('False Positive Rate',fontsize=15)
ax_arr[1,0].legend(loc = 'lower right', prop={'size': 16})

#GAUSSIANO ---------------------
probs = gaussiannb.predict_proba(X_test)
preds = probs[:,1]
fprgau, tprgau, thresholdgau = metrics.roc_curve(y_test, preds)
roc_aucgau = metrics.auc(fprgau, tprgau)

ax_arr[1,1].plot(fprgau, tprgau, 'b', label = 'AUC = %0.2f' % roc_aucgau)
ax_arr[1,1].plot([0, 1], [0, 1],'r--')
ax_arr[1,1].set_title('Receiver Operating Characteristic Gaussian ',fontsize=20)
ax_arr[1,1].set_ylabel('True Positive Rate',fontsize=20)
ax_arr[1,1].set_xlabel('False Positive Rate',fontsize=15)
ax_arr[1,1].legend(loc = 'lower right', prop={'size': 16})

#TODAS LAS GRÁFICAS ----------------------------------
ax_arr[1,2].plot(fprgau, tprgau, 'b', label = 'Gaussian', color='black')
ax_arr[1,2].plot(fprdtree, tprdtree, 'b', label = 'Decision Tree', color='blue')
ax_arr[1,2].plot(fprknn, tprknn, 'b', label = 'Knn', color='brown')
ax_arr[1,2].plot(fprrfc, tprrfc, 'b', label = 'Random Forest', color='green')
ax_arr[1,2].plot(fprlog, tprlog, 'b', label = 'Logistic', color='grey')
ax_arr[1,2].set_title('Receiver Operating Comparison ',fontsize=20)
ax_arr[1,2].set_ylabel('True Positive Rate',fontsize=20)
ax_arr[1,2].set_xlabel('False Positive Rate',fontsize=15)
ax_arr[1,2].legend(loc = 'lower right', prop={'size': 16})

plt.subplots_adjust(wspace=0.2)
plt.tight_layout() 
"""
ANALIZANDO LOS RESULTADOS
Ahora debemos decidir cuál es el mejor modelo, y tenemos dos tipos de valores erróneos:

Falso positivo: significa que el cliente NO se suscribió al depósito a plazo fijo, pero el modelo cree que sí.

Falso negativo: significa que el cliente se suscribió al depósito a plazo fijo, pero el modelo indica que no.

En mi opinión:

El primer caso es el más perjudicial, porque creemos que ya tenemos a ese cliente, pero no es así, y podríamos perderlo en futuras campañas.
El segundo caso no es ideal, pero es aceptable; tenemos a ese cliente y en el futuro descubriremos que, en realidad, ya es nuestro cliente.
Nuestro objetivo es encontrar el mejor modelo mediante la matriz de confusión con el menor número posible de falsos positivos.

Objetivo 1: revisemos la mejor matriz de confusión que cumpla con este criterio. Objetivo 2: realizaré los cálculos manualmente para que sean más visibles y comprensibles.
"""
from sklearn.metrics import classification_report
print('KNN Confusion Matrix\n', confusion_matrix(y_test, knnpred))

print('KNN Reports\n',classification_report(y_test, knnpred))

#Bien, ahora profundicemos en estos valores
#ANÁLISIS DEL MODELO SELECCIONADO
#RECALL
#Recall - Especificidad
#TN / (TN + FP) [ LÍNEA 1 DE LA MATRIZ ]

#¿Para todos los VALORES REALES NEGATIVOS (0), cuántas predicciones correctas tenemos?

#Otra forma de entenderlo: nuestro conjunto de prueba real tiene 7163 + 116 = 7279 clientes que no se suscribieron (0), y nuestro modelo predice un 98 % de aciertos, es decir, 7163 aciertos y 116 errores.

print(round(7163 /(7163 + 116),2))

#Recall - Sensibilidad
#TP / (TP + FN) [ LÍNEA DE MATRIZ 2 ]

#¿Para todos los VALORES REALES POSITIVOS (1), cuántas predicciones correctas tenemos?

#Otra forma de entenderlo: nuestro conjunto de prueba real tiene 706 + 253 = 959 clientes suscritos (1), y nuestro modelo predice un 26 % de aciertos, es decir, 253 aciertos y 706 errores. PERO RECUERDA: es mejor tener un falso negativo que un falso positivo.

print(round(253 / (253 + 706  ),2))
print(round(metrics.recall_score(y_test, knnpred),2))

#PRECISIÓN
#Precisión
#TN / (TN + FN) [ COLUMNA 1 DE LA MATRIZ ]

#Para todas las predicciones NEGATIVAS (0) de nuestro modelo, ¿cuántas predicciones correctas tenemos?

#Otra forma de entenderlo: nuestro modelo identificó 7163 + 706 = 7869 clientes que no se suscribieron (0), y predijo un 91 % de aciertos, es decir, 7163 aciertos y 706 errores.

print(round(7163 / (7163 + 706),2))

#Precisión
#TN / (TN + FN) [ COLUMNA 1 DE LA MATRIZ ]

#Para todas las predicciones POSITIVAS (1) de nuestro modelo, ¿cuántas predicciones correctas tenemos?

#Otra forma de entenderlo: nuestro modelo identificó 116 + 253 = 369 clientes suscritos (1), y predijo un 69 % de aciertos, es decir, 253 aciertos y 116 errores.

print(round(253 / (253 + 116),2))
print(round(metrics.precision_score(y_test, knnpred),2))

#Puntuación F1
#La puntuación F1 es la "mediana" de la precisión y la exhaustividad. Considérela cuando busque un equilibrio entre estas métricas.
#F1 = 2(Precisión(0) - Exhaustividad(0)) / (Precisión(0) + Exhaustividad(0))

F1_0 = 2*0.91*0.98/(0.91+0.98)
round(F1_0,2)

F1_1 = 2*0.69*0.26/(0.69+0.26)
round(F1_1,2)

#PROMEDIO/TOTAL
#Esto considera los pesos de la suma de VALORES REALES [línea 1] [línea 2]
AVG_precision =  (0.91*(7279/8238))+ (0.69*(959/8238))
round(AVG_precision,2)

AVG_Recall =  (0.98*(7279/8238))+ (0.26*(959/8238))
round(AVG_Recall,2)

AVG_f1 =  (0.95*(7279/8238))+ (0.38*(959/8238))
round(AVG_f1,2)

#Importando las bibliotecas
import pandas as pd
# Algunas herramientas de scikit-learn para el preprocesamiento y la creación de un pipeline.
# ColumnTransformer se introdujo en la versión 0.20, así que asegúrate de tener esta versión.
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report

# Nuestros algoritmos, ordenados del más fácil al más difícil de interpretar.
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost.sklearn import XGBClassifier

#El conjunto de datos
#El conjunto de datos se puede descargar aquí. Contiene información de campañas de marketing de un banco portugués. Intentaremos crear clasificadores que puedan predecir si el cliente objetivo de la campaña contrató o no un depósito a plazo fijo (columna y).

df = pd.read_csv('bank-additional-full.csv', sep = ';')

df.y.value_counts()

# El conjunto de datos está desequilibrado; ¡debemos tenerlo en cuenta al construir nuestros modelos!

# Obtener X, y
y = df["y"].map({"no":0, "yes":1})
X = df.drop("y", axis=1)
#Veamos las características de la matriz X:

#Diccionario de datos
#Edad (numérica)
#Trabajo: tipo de trabajo (categórico: 'administrativo', 'obrero', 'emprendedor', 'empleada doméstica', 'gerencia', 'jubilado', 'autónomo', 'servicios', 'estudiante', 'técnico', 'desempleado', 'desconocido')
#Estado civil: estado civil (categórico: 'divorciado', 'casado', 'soltero', 'desconocido'; nota: 'divorciado' significa divorciado o viudo)
#Educación (categórico: 'básico 4 años', 'básico 6 años', 'básico 9 años', 'secundaria', 'analfabeto', 'curso profesional', 'título universitario', 'desconocido')
#Incumplimiento: ¿tiene crédito en mora? (categórico: 'no', 'sí', 'desconocido')
#vivienda: ¿tiene préstamo hipotecario? (categórico: 'no', 'sí', 'desconocido')
#préstamo: ¿tiene préstamo personal? (categórico: 'no', 'sí', 'desconocido')
#contacto: tipo de comunicación del contacto (categórico: 'celular', 'teléfono')
#mes: mes del año del último contacto (categórico: 'ene', 'feb', 'mar', ..., 'nov', 'dic')
#día_de_la_semana: día de la semana del último contacto (categórico: 'lun', 'mar', 'mié', 'jue', 'vie')
#duración: duración del último contacto, en segundos (numérico). Nota importante: este atributo afecta significativamente al resultado (por ejemplo, si duración = 0, entonces y = 'no'). Sin embargo, la duración no se conoce antes de realizar una llamada. Además, después de finalizar la llamada, y se conoce. Por lo tanto, este dato solo debe incluirse con fines comparativos y debe descartarse si se pretende obtener un modelo predictivo realista. #campaña: número de contactos realizados durante esta campaña y para este cliente (numérico, incluye el último contacto)
#días: número de días transcurridos desde el último contacto con el cliente en una campaña anterior (numérico; 999 significa que no se contactó previamente con el cliente)
#anterior: número de contactos realizados antes de esta campaña y para este cliente (numérico)
#resultado: resultado de la campaña de marketing anterior (categórico: 'fracaso', 'inexistente', 'éxito')
#tasa de variación del empleo: tasa de variación del empleo - indicador trimestral (numérico)
#índice de precios al consumidor: índice de precios al consumidor - indicador mensual (numérico)
#índice de confianza del consumidor: índice de confianza del consumidor - indicador mensual (numérico)
#euribor3m: tasa euribor a 3 meses - indicador diario (numérico)
#n.empleados: número de empleados - indicador trimestral (numérico)
#Nota: la función de duración se excluirá de nuestro análisis.

X.drop("duration", inplace=True, axis=1)
X.dtypes

# Algunas de estas características predeterminadas serían binarias, pero como # tienen una tercera clase "desconocido", las procesaremos como categóricas no binarias.
num_features = ["age", "campaign", "pdays", "previous", "emp.var.rate", 
                "cons.price.idx", "cons.conf.idx","euribor3m", "nr.employed"]

cat_features = ["job", "marital", "education","default", "housing", "loan",
                "contact", "month", "day_of_week", "poutcome"]

#Definiremos un nuevo objeto ColumnTransformer (novedad en sklearn 0.20) que conservará nuestras características numéricas y aplicará codificación one-hot a nuestras características categóricas. Esto nos permitirá crear un flujo de trabajo limpio que incluya tanto la ingeniería de características (codificación one-hot en este caso) como el entrenamiento del modelo (una buena manera de evitar la fuga de datos).
preprocessor = ColumnTransformer([("numerical", "passthrough", num_features), 
                                  ("categorical", OneHotEncoder(sparse_output=False, handle_unknown="ignore"),
                                   cat_features)])
#Ahora podemos definir nuestros cuatro modelos como objetos Pipeline de scikit-learn, que contienen el paso de preprocesamiento y el entrenamiento de un algoritmo específico.

#Creación de pipelines de entrenamiento de modelos
#Regresión logística
lr_model = Pipeline([("preprocessor", preprocessor), 
                     ("model", LogisticRegression(class_weight="balanced", solver="liblinear", random_state=42))])

# Decision Tree
dt_model = Pipeline([("preprocessor", preprocessor), 
                     ("model", DecisionTreeClassifier(class_weight="balanced"))])

# Random Forest
rf_model = Pipeline([("preprocessor", preprocessor), 
                     ("model", RandomForestClassifier(class_weight="balanced", n_estimators=100, n_jobs=-1))])

# XGBoost
xgb_model = Pipeline([("preprocessor", preprocessor), 
                      # Add a scale_pos_weight to make it balanced
                      ("model", XGBClassifier(scale_pos_weight=(1 - y.mean()), n_jobs=-1))])
#Dividamos los datos en conjuntos de entrenamiento y prueba.

#División de datos
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=.3, random_state=42)

#Bibliotecas para IA explicable
#La biblioteca Eli5: Interpretación de modelos de "caja blanca"
#Con regresión logística
#Primero, ajustemos nuestra regresión logística y evaluemos su rendimiento.

gs = GridSearchCV(lr_model, {"model__C": [1, 1.3, 1.5]}, n_jobs=-1, cv=5, scoring="accuracy")
gs.fit(X_train, y_train)

#Veamos nuestros mejores parámetros y puntuación

print(gs.best_params_)
print(gs.best_score_)

lr_model.set_params(**gs.best_params_)

lr_model.get_params("model")

#Ahora podemos ajustar el modelo a todo el conjunto de entrenamiento y calcular la precisión en el conjunto de prueba.

lr_model.fit(X_train, y_train)

#Generar predicciones

y_pred = lr_model.predict(X_test)
accuracy_score(y_test, y_pred)

print(classification_report(y_test, y_pred))

#Usemos eli5 para visualizar los pesos asociados a cada característica:

import eli5
eli5.show_weights(lr_model.named_steps["model"])

#Esto nos da los pesos asociados a cada característica, que pueden interpretarse como la contribución de cada una a la predicción de que la clase será y=1 (el cliente se suscribirá después de la campaña).

#Los nombres de las características no son de mucha ayuda; podemos pasar una lista de nombres de columnas a eli5, pero primero tendremos que hacer algunos ajustes para extraer los nombres de nuestro preprocesador en el pipeline (ya que hemos generado nuevas características sobre la marcha con el codificador one-hot).
preprocessor = lr_model.named_steps["preprocessor"]
ohe_categories = preprocessor.named_transformers_["categorical"].categories_
new_ohe_features = [f"{col}__{val}" for col, vals in zip(cat_features, ohe_categories) for val in vals]
all_features = num_features + new_ohe_features
#Genial, ahora tenemos una buena lista de columnas después del procesamiento. Visualicemos los datos en un dataframe solo para comprobar que todo esté correcto:

pd.DataFrame(lr_model.named_steps["preprocessor"].transform(X_train), columns=all_features).head()

#¡Se ve bien! Ahora podemos pasar esta lista de características a eli5 para obtener una visualización más legible de los pesos asociados a cada característica:

eli5.show_weights(lr_model.named_steps["model"], feature_names=all_features)

#Parece que depende principalmente de si es marzo o no. ¿La campaña de marketing fue más eficiente en marzo?

#También podemos usar eli5 para explicar una predicción específica. Seleccionemos una fila de los datos de prueba:

i = 4
X_test.iloc[[i]]

y_test.iloc[i]

#Nuestro cliente se suscribió al plan de depósito a plazo fijo después de la campaña. Veamos qué habría predicho nuestro modelo y cómo lo explicaría.

#Primero, tendremos que transformar nuestra fila al formato que espera nuestro modelo, ya que eli5 no puede trabajar directamente con nuestra canalización.

#Nota: eli5 sí admite canalizaciones, pero solo con un número limitado de transformaciones. En nuestra canalización, no admite la transformación de paso directo (que, curiosamente, no hace nada...).

eli5.show_prediction(lr_model.named_steps["model"], 
                     lr_model.named_steps["preprocessor"].transform(X_test)[i],
                     feature_names=all_features, show_feature_values=True)

#Con un árbol de decisión
#eli5 también se puede usar para interpretar árboles de decisión:

gs = GridSearchCV(dt_model, {"model__max_depth": [3, 5, 7], 
                             "model__min_samples_split": [2, 5]}, 
                  n_jobs=-1, cv=5, scoring="accuracy")

gs.fit(X_train, y_train)

#Veamos nuestros mejores parámetros y puntuación

print(gs.best_params_)
print(gs.best_score_)

dt_model.set_params(**gs.best_params_)


dt_model.fit(X_train, y_train)
y_pred = dt_model.predict(X_test)
accuracy_score(y_test, y_pred)

print(classification_report(y_test, y_pred))


#Para los árboles de decisión, eli5 solo da la importancia de las características, lo que no dice en qué dirección una característica impacta el resultado previsto.
eli5.show_weights(dt_model.named_steps["model"], feature_names=all_features)

#Aquí la característica más importante parece ser nr.employed. También podemos obtener una explicación para una predicción dada, esto calculará la contribución de cada característica en la predicción:
eli5.show_prediction(dt_model.named_steps["model"], 
                     dt_model.named_steps["preprocessor"].transform(X_test)[i],
                     feature_names=all_features, show_feature_values=True)
                     
#Aquí, la explicación de una predicción individual se calcula siguiendo la ruta de decisión en el árbol y sumando la contribución de cada característica de cada nodo cruzado a la probabilidad total predicha.

#Eli5 también se puede usar para explicar modelos de caja negra, pero en su lugar usaremos Lime y SHAP para nuestros dos últimos modelos.

#LIME (Explicación Local Interpretable Independiente del Modelo) para generar interpretaciones locales de modelos de caja negra.
#LIME significa Explicaciones Locales Interpretables Independientes del Modelo. Podemos usarlo con cualquier modelo que hayamos construido para explicar por qué tomó una decisión específica para una observación dada. Para ello, LIME crea un conjunto de datos en la localidad de nuestra observación perturbando las diferentes características. Luego ajusta un modelo lineal local a estos datos y usa los pesos de cada característica para proporcionar una explicación.

#Con un Bosque Aleatorio
gs = GridSearchCV(rf_model, {"model__max_depth": [10, 15], 
                             "model__min_samples_split": [5, 10]}, 
                  n_jobs=-1, cv=5, scoring="accuracy")

gs.fit(X_train, y_train)

#Veamos nuestros mejores parámetros y puntuación

print(gs.best_params_)
print(gs.best_score_)

rf_model.set_params(**gs.best_params_)

rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)
accuracy_score(y_test, y_pred)

print(classification_report(y_test, y_pred))

#Primero podemos analizar la importancia de las características con Eli5:

eli5.show_weights(rf_model.named_steps["model"], 
                  feature_names=all_features)
                  
#Podemos explicar a grandes rasgos en qué parece centrarse principalmente nuestro modelo. También obtenemos la desviación estándar de la importancia de las características en los distintos árboles de nuestro conjunto.

#Entrenaremos también nuestro modelo XGB.
gs = GridSearchCV(xgb_model, {"model__max_depth": [5, 10],
                              "model__min_child_weight": [5, 10],
                              "model__n_estimators": [25]},
                  n_jobs=-1, cv=5, scoring="accuracy")

gs.fit(X_train, y_train)

#Veamos nuestros mejores parámetros y puntuación

print(gs.best_params_)
print(gs.best_score_)
xgb_model.set_params(**gs.best_params_)
xgb_model.fit(X_train, y_train)

#Generar predicciones

y_pred = xgb_model.predict(X_test)
accuracy_score(y_test, y_pred)

print(classification_report(y_test, y_pred))
"""
Crear un explicador
Para explicar por qué el modelo clasifica observaciones individuales como clase 0 o 1, utilizaremos el explicador tabular de la biblioteca Lime. Este es el explicador principal para datos tabulares. Lime también proporciona explicadores para datos de texto, imágenes y series temporales.

Al usar el explicador tabular, debemos proporcionar nuestro conjunto de entrenamiento como parámetro para que Lime pueda calcular estadísticas para cada característica: la media y la desviación estándar para características numéricas, o la frecuencia de los valores para características categóricas. Estas estadísticas se utilizan para escalar los datos y generar nuevos datos perturbados con los que entrenar nuestros modelos lineales locales.
"""
from lime.lime_tabular import LimeTabularExplainer
"""Los parámetros que se pasan al explicador son:

Nuestro conjunto de entrenamiento. Debemos asegurarnos de usar el conjunto de entrenamiento sin codificación one-hot.
Modo: El explicador puede usarse para clasificación o regresión.
Nombres de características: Lista de etiquetas para nuestras características.
Características categóricas: Lista de índices de características categóricas.
Nombres categóricos: Diccionario que asigna a cada índice de característica categórica una lista de etiquetas correspondientes.
Discretizar continuo: Discretizará los valores numéricos en intervalos que se pueden usar para la explicación. Por ejemplo, puede indicarnos que la decisión se tomó porque la distancia está en el intervalo [5 km, 10 km], en lugar de decirnos que la distancia es una característica importante.

Primero, para obtener el parámetro `nombres categóricos`, necesitamos crear un diccionario con los índices de los valores categóricos del conjunto de datos original como claves y listas de posibles categorías como valores.
"""
categorical_names = {}
for col in cat_features:
    categorical_names[X_train.columns.get_loc(col)] = [new_col.split("__")[1] 
                                                       for new_col in new_ohe_features 
                                                       if new_col.split("__")[0] == col]
categorical_names

#Lime necesita que el conjunto de datos proporcionado tenga los valores categóricos convertidos a etiquetas enteras que se correspondan con los valores en `categorical_names`. Por ejemplo, la etiqueta 0 para la columna 2 se corresponderá con "divorciado/a". Para ello, utilizaremos una función auxiliar personalizada que convierte los datos del formato original a LIME y viceversa.

#Esta función recorre todas las características categóricas y reemplaza las cadenas por las etiquetas enteras correctas. Puedes consultar `helpers.py`.

def convert_to_lime_format(X, categorical_names, col_names=None, invert=False):
    #Convierte datos con valores categóricos como cadenas de texto al formato correcto para LIME, con valores categóricos como etiquetas enteras.

    #Requiere `categorical_names`, el mismo diccionario que debe pasarse a LIME para garantizar la coherencia.

    #`col_names` e `invert` permiten reconstruir el dataframe original a partir de un array NumPy en formato LIME para pasarlo a un Pipeline o a un OneHotEncoder de scikit-learn."""

    # Si los datos no son un dataframe, necesitamos poder construirlo.
    if not isinstance(X, pd.DataFrame):
        X_lime = pd.DataFrame(X, columns=col_names)
    else:
        X_lime = X.copy()

    for k, v in categorical_names.items():
        if not invert:
            label_map = {
                str_label: int_label for int_label, str_label in enumerate(v)
            }
        else:
            label_map = {
                int_label: str_label for int_label, str_label in enumerate(v)
            }

        X_lime.iloc[:, k] = X_lime.iloc[:, k].map(label_map)

    return X_lime
#Comprobemos que funcionó:

convert_to_lime_format(X_train, categorical_names).head()

explainer = LimeTabularExplainer(convert_to_lime_format(X_train, categorical_names).values,
                                 mode="classification",
                                 feature_names=X_train.columns.tolist(),
                                 categorical_names=categorical_names,
                                 categorical_features=categorical_names.keys(),
                                 discretize_continuous=True,
                                 random_state=42)
#¡Genial! Nuestro explicador está listo. Ahora, seleccionemos una observación que queramos explicar.

#Explicar nuevas observaciones
#Crearemos una variable llamada `observación` que contendrá la i-ésima observación del conjunto de datos de prueba.

i = 2
X_observation = X_test.iloc[[i], :]
X_observation

print(f"""\
* True label: {y_test.iloc[i]}
* LR: {lr_model.predict_proba(X_observation)[0]}
* DT: {dt_model.predict_proba(X_observation)[0]}
* RF: {rf_model.predict_proba(X_observation)[0]}
* XGB: {xgb_model.predict_proba(X_observation)[0]}""")

#Convirtamos nuestra observación al formato Lime y luego a una matriz NumPy.

observation = convert_to_lime_format(X_test.iloc[[i], :],categorical_names).values[0]
observation

#Para explicar una predicción, utilizamos el método `explain_instance` de nuestro explicador. Este método generará nuevos datos con características perturbadas alrededor de la observación y aprenderá un modelo lineal local. Necesita recibir:

#Nuestra observación como un array de NumPy.
#Una función que utilice nuestro modelo para predecir probabilidades a partir de los datos (en el mismo formato que le pasamos al explicador). Esto significa que no podemos pasar directamente `rf_model.predict_proba` porque nuestro pipeline espera etiquetas de cadena para valores categóricos. Necesitaremos crear una función personalizada `rf_predict_proba` que primero convierta las etiquetas enteras a cadenas y luego llame a `rf_model.predict_proba`.

#`num_features`: número de características a considerar en la explicación.
#Escribamos una función `predict_proba` personalizada para nuestros modelos:
from functools import partial

def custom_predict_proba(X, model):
    X_str = convert_to_lime_format(X, categorical_names, col_names=X_train.columns, invert=True)
    return model.predict_proba(X_str)
#lr_predict_proba = partial(custom_predict_proba, model=lr_model)
dt_predict_proba = partial(custom_predict_proba, model=dt_model)
rf_predict_proba = partial(custom_predict_proba, model=rf_model)
xgb_predict_proba = partial(custom_predict_proba, model=xgb_model)
#Vamos a probar nuestra función personalizada para asegurarnos de que genera las probabilidades correctamente.

num_cols = X_train.select_dtypes(include=["int64", "float64"]).columns
cat_cols = X_train.select_dtypes(include=["object", "category"]).columns

def predict_proba_fn(x):
    import pandas as pd
    
    x_df = pd.DataFrame(x, columns=X_train.columns)
    
    # Tipos correctos
    x_df[num_cols] = x_df[num_cols].astype(float)
    x_df[cat_cols] = x_df[cat_cols].astype(str)
    
    return lr_model.predict_proba(x_df)

categorical_features = [
    X_train.columns.get_loc(col) 
    for col in cat_cols
]

# 🔥 usar datos transformados (solo números)
preprocessor = lr_model.named_steps['preprocessor']
def predict_proba_fn(x):
    return lr_model.predict_proba(x)

X_train_transformed = preprocessor.transform(X_train)


# =========================
# LIME EXPLAINABLE AI
# =========================
import lime
import lime.lime_tabular
import numpy as np
import pandas as pd

# 1. Obtener el preprocessor del pipeline
preprocessor = lr_model.named_steps["preprocessor"]

# 2. Transformar datos de entrenamiento (esto los convierte en numéricos)
X_train_transformed = preprocessor.transform(X_train)
X_test_transformed = preprocessor.transform(X_test)

# 3. Obtener nombres de features después del OneHotEncoder
ohe_categories = preprocessor.named_transformers_["categorical"].categories_
new_ohe_features = [
    f"{col}__{val}"
    for col, vals in zip(cat_features, ohe_categories)
    for val in vals
]

all_features = num_features + new_ohe_features

# 4. Crear explainer LIME
explainer = lime.lime_tabular.LimeTabularExplainer(
    training_data=np.array(X_train_transformed),
    feature_names=all_features,
    class_names=['No', 'Yes'],
    mode='classification'
)

# 5. Función predict_proba para LIME (MUY IMPORTANTE)
def predict_proba_lime(data):
    data_df = pd.DataFrame(data, columns=all_features)
    return lr_model.named_steps["model"].predict_proba(data_df)

# 6. Explicar una observación
i = 5  # cambiar por la observación que quieras

exp = explainer.explain_instance(
    X_test_transformed[i],
    predict_proba_lime
)

# Mostrar explicación
exp.as_list()
print(exp.as_list())

