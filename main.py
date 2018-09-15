import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "hackaturing.dsv"
dtype = {'base_hackaturing.cnpj': str,
         'base_hackaturing.prestador': str,
         'base_hackaturing.uf': str,
         'base_hackaturing.id_beneficiario': str,
         'base_hackaturing.sexo': str,
         'base_hackaturing.data_nascimento': str,
         'base_hackaturing.id_conta': str,
         'base_hackaturing.crm_solicitante': str,
         'base_hackaturing.cbos_solicitante': str,
         'base_hackaturing.cbos_executante': str,
         'base_hackaturing.data_entrada': str,
         'base_hackaturing.data_saida': str,
         'base_hackaturing.data_item': str,
         'base_hackaturing.senha': str,
         'base_hackaturing.tipo_guia': str,
         'base_hackaturing.tipo_item': str,
         'base_hackaturing.carater_atendimento': str,
         'base_hackaturing.servico': str,
         'base_hackaturing.quantidade': float,
         'base_hackaturing.valor_item': float,
         'base_hackaturing.valor_cobrado': float,
         'base_hackaturing.valor_pago': float,
         'base_hackaturing.ano_mes': str,
         'base_hackaturing.cid': str}
dataset = pandas.read_csv(url, sep = '|', dtype = dtype)
names = {old: old[17:] for old in dtype.keys()}
new_columns = [old_name[17:] for old_name in dataset.columns]
dataset.columns = new_columns


print(dataset.columns)
# print(dataset.shape)
# print(dataset.head(20))
# print(dataset.describe())

# dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)

# scatter plot matrix
# scatter_matrix(dataset)
# plt.show()


# # split array
# array = dataset.values
# X = array[:,0:4]
# Y = array[:,4]
# validation_size = 0.20
# seed = 7
# X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# # Test options and evaluation metric
# seed = 7
# scoring = 'accuracy'

# knn = KNeighborsClassifier()
# knn.fit(X_train, Y_train)
# predictions = knn.predict(X_validation)
# print(accuracy_score(Y_validation, predictions))
# print(confusion_matrix(Y_validation, predictions))
# print(classification_report(Y_validation, predictions))
