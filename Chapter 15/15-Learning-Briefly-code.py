import pandas as pd

df = pd.read_csv("src/examples/registered-cats.csv")
del df["Animal_Type"]
del df["Postcode"]

new_column_names = {
    "Breed_Description": "Breed",
    "Colour_Description": "Colour",
    "GENDER": "Gender"
}

df.rename(columns=new_column_names, inplace=True)

df.loc[611, ["Gender"]] = 'F'
df = df[df["Gender"].str.contains("F|M")]
df.reset_index(drop=True, inplace=True)
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)
df = pd.get_dummies(df, columns=["Gender"], prefix="", prefix_sep="")
df = df.astype({"F": "int8", "M": "int8"})
df.info()

import numpy as np

breed_dict = dict()

for count, breed in enumerate(np.sort(df["Breed"].unique())):
    breed_dict[breed] = count

breed_dict["DOMSH"]

colour_dict = dict()

for count, colour in enumerate(np.sort(df["Colour"].unique())):
    colour_dict[colour] = count

locality_dict = dict()

for count, locality in enumerate(np.sort(df["Locality"].unique())):
    locality_dict[locality] = count

for n in range(df.shape[0]):
    breed, colour, locality = df.loc[n, ["Breed", "Colour", "Locality"]]
    df.at[n, "Breed"] = breed_dict[breed]
    df.at[n, "Colour"] = colour_dict[colour]
    df.at[n, "Locality"] = locality_dict[locality]

df = df.astype({"Breed": "int16", "Colour": "int16", "Locality": "int16"})
df.info()

df.head()

pd.set_option("display.float_format", lambda x: "%.4f" % x)

np_float_formatter = "{:.4f}".format
np.set_printoptions(formatter={'float_kind':np_float_formatter})

df.describe()

from sklearn.preprocessing import minmax_scale

new_locality = minmax_scale(df["Locality"].values)
new_locality[:10]

from sklearn.preprocessing import StandardScaler

new_locality = StandardScaler().fit_transform(df[["Locality"]])
pd.Series(new_locality.flatten()).describe()

locality = df["Locality"].values
mu = locality.mean()
sigma = locality.std()

new_locality = (locality - mu)/sigma
pd.Series(new_locality).describe()

max_minus_min = locality.max() - locality.min()

assert max_minus_min != 0.0

new_locality = (locality - mu) / max_minus_min
pd.Series(new_locality).describe()

df[['F', 'M']].corr(method="pearson")

def standardize_DataFrame_column(df, column_label):
    data = df[column_label].values
    mu = data.mean()
    sigma = data.std()
    assert sigma != 0  # don't forget this!
    df[column_label] = (data - mu)/sigma

for label in df.columns.values:
    standardize_DataFrame_column(df, label)

df.describe()

from sklearn.decomposition import PCA

pca = PCA(n_components=5)
pca.fit(df)

pca.explained_variance_ratio_

pca = PCA(n_components=3)
pca.fit(df)

pca.explained_variance_ratio_

del df['M']
df.head(2)

xy_df = pd.read_csv("src/examples/clustering-xy.csv")
xy_df.describe()

xy_df.head()

from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=3, random_state=0).fit(xy_df)

k_means.labels_

k_means.cluster_centers_

k_means.predict([[14, 3]])

center_point = np.mean(k_means.cluster_centers_, axis=0)
center_point

df = pd.read_csv("src/examples/clustering-xy-labels.csv")
df = df[df["label"] != 0]
df.head()

from sklearn import svm

classifier = svm.SVC(kernel="linear")
classifier.fit(df[['x', 'y']], df["label"])

classifier.predict([[14, 3]])

classifier.support_vectors_

a = classifier.support_vectors_[0]
b = classifier.support_vectors_[1]
slope = (a[1] - b[1]) / (a[0] - b[0])
slope

import pandas as pd

df = pd.read_csv("src/examples/baseball-xy.csv")
df = df.astype({"label": "int16"})

df.info()

df.iloc[2]

df.iloc[63]

position_A = [3.8, 7.5]
position_B = [9.5, 3.6]
position_C = [13, 6.8]

from sklearn.neighbors import KNeighborsClassifier

k_neighbors = KNeighborsClassifier(n_neighbors=1)
k_neighbors.fit(df[['x', 'y']], df["label"])

k_neighbors.predict([position_A])

k_neighbors.predict_proba([position_A])

def fan_predictor(name, position):
    teams = ("Mets", "Yankees")
    team = k_neighbors.predict([position])[0]
    probability = k_neighbors.predict_proba([position])[0]

    print(f"'{name}' is a {teams[team]} fan with " +
          f"probability {probability[team]}")

fan_predictor('A', position_A)

fan_predictor('B', position_B)

fan_predictor('C', position_C)

k_neighbors = KNeighborsClassifier(n_neighbors=5)
k_neighbors.fit(df[['x', 'y']], df["label"])

fan_predictor('A', position_A)
fan_predictor('B', position_B)
fan_predictor('C', position_C)

for j in range(0, 120, 20):
    k_neighbors = KNeighborsClassifier(n_neighbors=j + 1)
    k_neighbors.fit(df[['x', 'y']], df["label"])
    fan_predictor('B', position_B)

def simple_linear_regression(xs, ys):
    # return the slope and y-intercept of the simple
    # linear regression line

    n = xs.size
    assert n == ys.size

    numer = n * (xs * ys).sum() - xs.sum() * ys.sum()
    denom = n * (xs * xs).sum() - (xs.sum())**2
    slope = numer / denom
    y_intercept = ys.mean() - slope * xs.mean()
    return slope, y_intercept

xs = np.array([2.0, 4.0, 8.0])
ys = np.array([2.0, 5.0, 5.0])

simple_linear_regression(xs, ys)

from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(pd.DataFrame({'x': xs}), ys)

lin_reg.coef_

lin_reg.intercept_

lin_reg.predict([[6]])

lin_reg.predict([[10]])

