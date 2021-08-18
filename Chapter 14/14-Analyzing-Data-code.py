import numpy as np

ages = np.array(
    [40, 41, 39, 35, 42, 37, 45, 43, 42, 38, 39, 45, 37, 36,
     45, 41, 41, 31, 42, 40, 39, 38, 40, 39, 41, 46, 42, 44,
     46, 48, 45, 39, 46, 43, 35, 38, 43, 41, 36, 40, 34, 44,
     42, 44, 40, 49, 47, 51, 52, 45, 44, 47, 39, 38, 43, 39,
     45, 40, 36, 43, 38, 43, 32, 35, 36, 42, 40, 38, 37, 36,
     41, 41, 31, 39, 51, 38, 42, 36, 35, 36, 40, 40, 37, 43,
     39, 42, 44, 50, 39, 38, 37, 33, 52, 35, 44, 29, 42, 39,
     40, 42]
)

mean = np.mean(ages)
mean

np.sum(ages)/ages.size

np.max(ages), np.min(ages)

import matplotlib.pyplot as plt
plt.hist(ages, bins=33, color="lightgray", edgecolor="black")

plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Histogram of concert attendee ages")

mean = np.mean(ages)
plt.axvline(mean, color="black", linestyle="dotted")
plt.text(mean + 0.1, 11, "mean")

np.median(ages)

Q1 = np.quantile(ages, 0.25)

Q3 = np.quantile(ages, 0.75)
Q1, Q3

IQR = np.quantile(ages, 0.75) - np.quantile(ages, 0.25)

import matplotlib.pyplot as plt
import numpy as np
import math

ages = np.array(
    [40, 41, 39, 35, 42, 37, 45, 43, 42, 38, 39, 45, 37, 36,
     45, 41, 41, 31, 42, 40, 39, 38, 40, 39, 41, 46, 42, 44,
     46, 48, 45, 39, 46, 43, 35, 38, 43, 41, 36, 40, 34, 44,
     42, 44, 40, 49, 47, 51, 52, 45, 44, 47, 39, 38, 43, 39,
     45, 40, 36, 43, 38, 43, 32, 35, 36, 42, 40, 38, 37, 36,
     41, 41, 31, 39, 51, 38, 42, 36, 35, 36, 40, 40, 37, 43,
     39, 42, 44, 50, 39, 38, 37, 33, 52, 35, 44, 29, 42, 39,
     40, 42]
)

plt.title("Box plot of concert attendee ages")
plt.ylabel("Age in years")

# medianprops is a dict with the
# drawing options for the median line
plt.boxplot(ages, medianprops={"color": "black", "linewidth": 2})

quantiles = np.quantile(ages, [0.0, 0.25, 0.5, 0.75, 1.0])
labels = ["minimum", "Q1 = first quartile",
          "mean", "Q3 = third quartile", "maximum"]

for (q, label) in zip(quantiles, labels):
    plt.axhline(q, color="gray", linewidth=0.5)
    plt.text(0.55, q + 0.2, f"{label} = {q}", fontsize=9)

IQR = quantiles[3] - quantiles[1]

# Draw the lower whisker extreme. Below this are outliers.
q = math.ceil(quantiles[1] - 1.5 * IQR)
plt.axhline(q, color="gray", linewidth=0.5)
plt.text(0.55, q + 0.2, f"Q1 - 1.5 * IQR = {q}", fontsize=9)

# Draw the upper whisker extreme. Above this are outliers.
q = math.floor(quantiles[3] + 1.5 * IQR)
plt.axhline(q, color="gray", linewidth=0.5)
plt.text(0.55, q + 0.2, f"Q3 + 1.5 * IQR = {q}", fontsize=9)


data_1 = np.arange(1, 100)
data_2 = np.repeat(50, 99)
(np.mean(data_1), np.mean(data_2))

(np.std(data_1), np.std(data_2))

np.var(ages)

concerts_attended_in_1995 = np.array(
    [0, 0, 0, 0, 2, 0, 4, 4, 4, 0, 0, 4, 0, 0, 6, 0, 2, 0, 4, 0,
     0, 0, 0, 0, 0, 5, 4, 4, 5, 5, 4, 0, 5, 4, 0, 0, 4, 0, 0, 0,
     0, 4, 3, 4, 0, 7, 5, 6, 6, 4, 4, 5, 0, 0, 4, 0, 4, 0, 0, 4,
     0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 2, 0, 0, 0, 6, 0, 4, 0, 0, 0,
     1, 0, 0, 4, 0, 4, 3, 6, 0, 0, 0, 0, 6, 0, 4, 0, 6, 0, 0, 4] )

covariance_matrix = np.cov(ages, concerts_attended_in_1995)
covariance_matrix[0, 1]

correlation_coefficients = np.corrcoef(ages, concerts_attended_in_1995)
correlation_coefficients[0, 1]

cats = open("src/examples/registered-cats.csv", "rt")
print(cats.readline())

print(cats.readline())
cats.close()

import pandas as pd

df = pd.read_csv("src/examples/registered-cats.csv")

df.info()

df.head()

df.tail()

del df["Animal_Type"]

df.head()

new_column_names = {
    "Breed_Description": "Breed",
    "Colour_Description": "Colour",
    "GENDER": "Gender"
}

df.rename(columns=new_column_names).head()

df.head()

df.rename(columns=new_column_names, inplace=True)
df.head()

df.shape

df.nunique()

df["Locality"].value_counts()

df["Locality"].value_counts(normalize=True)

cat_data = df["Locality"].value_counts().sort_index()
cat_data

import matplotlib.pyplot as plt
plt.clf()
cat_data.plot(kind="bar")

plt.clf()

cat_data.plot(kind="bar", color="lightgray", edgecolor="black",
              rot=45, hatch="///")

plt.tick_params(axis='x', labelsize=7)

plt.xlabel("Locality")
plt.ylabel("Number of cats")
plt.title("Number of registered cats in 2021 per locality in the City of Greater Dandenong")

small_df = df.iloc[50:57].copy()
small_df

small_df.iloc[0]

small_df.loc[50]

small_df.drop([51], axis=0, inplace=True)
small_df

small_df.drop([53, 54], axis="index")

small_df[["Gender", "Breed"]]

small_df.loc[[54, 56], ["Breed", "Colour"]]

x = small_df[["Breed"]]
x

y = small_df["Breed"]
y

type(x), type(y)

x.shape, y.shape

x.loc[54]

type(x.loc[54])

y[54]

type(y[54])

concert_df = pd.DataFrame(
  {
    "Age": ages,
    "1995 Concerts": concerts_attended_in_1995
  }
)

concert_df.iloc[3:9]

concert_df.describe()

import random

random.seed(23)

num_rows = concert_df.shape[0]
concert_df["Id"] = random.sample(range(1000, 1001 + num_rows), num_rows)

concert_df.head(5)

concert_df.info()

concert_df = concert_df[["Id", "Age", "1995 Concerts"]]

concert_df.head(5)

concert_df.sort_values(by="Id", inplace=True)

concert_df.head(5)

concert_df.to_csv("work/concert-goers.csv", index=False)

with open("work/concert-goers.csv", "rt") as csv_file:
    for _ in range(6):
        print(csv_file.readline(), end="")

concert_df.to_excel("work/concert-goers.xlsx", index=False)

df['Gender'].value_counts()

df[df["Gender"] == "U"]

df.loc[611, ["Gender"]] = 'F'

df[df["Gender"] == "U"]

df = df[df["Gender"].str.contains("F|M")]
df['Gender'].value_counts()

df.reset_index(drop=True, inplace=True)

df[df["Breed"].isna()]

df[df["Colour"].isna()]

df[df["Locality"].isna()]

df.dropna(inplace=True)
df[df["Breed"].isna()]

df[df["Colour"].isna()]

concert_df.describe()

concert_df.mean()

concert_df["Age"].mean()

concert_df.describe().loc["mean", "Age"]

concert_df.mean()["Age"]

concert_df.std()["Age"]

concert_df.var()["Age"]

concert_df.quantile(q=0.25)["Age"]

concert_df.median()["Age"]

concert_df.quantile(q=0.75)["Age"]

concert_df.cov()

cc = concert_df.corr(method="pearson")
cc

cc.loc["Age", "1995 Concerts"]

df.head(2)

pd.get_dummies(df, columns=["Gender"]).head(2)

pd.get_dummies(df, columns=["Gender"], prefix="G").head(2)

df = pd.get_dummies(df, columns=["Gender"], prefix="", prefix_sep="")
df.head(2)

df.describe()

localities = df["Locality"].unique()
localities

type(localities)

localities.sort()
localities

number_of_male_cats = [
    df[df["Locality"] == locality]['M'].sum()
        for locality in localities
]

number_of_male_cats

number_of_female_cats = [
    df[df["Locality"] == locality]['F'].sum()
        for locality in localities
]

number_of_female_cats

localities = [locality.title() for locality in localities]
localities

df_cats = pd.DataFrame(
  {
      "Locality": localities,
      'F': number_of_female_cats,
      'M': number_of_male_cats
  }
)

df_cats

df_cats = df.groupby(["Locality"]).sum()
df_cats

df_cats = df.groupby(["Locality"])[['F', 'M']].sum()
df_cats

df_cats.reset_index(inplace=True)
df_cats

df_cats = df_cats.astype({'F': "int8", 'M': "int8"})

df_cats["Locality"] = df_cats["Locality"].str.title()
df_cats

plt.clf()

df_cats.plot.bar(
    x="Locality",
    y=['F', 'M'],
    color=["gray", "black"],
    title="Number of female and male cats per locality",
    xlabel="Locality",
    ylabel="Count"
)

colours = sorted(df["Colour"].unique())

for count, colour in enumerate(colours, start=1):
    print(f"{colour:<9}", end=("\n" if count % 8 == 0 else ""))

[colour for colour in colours if "TOR" in colour]

tor_df = df[df["Colour"].str.contains("TOR")]

tor_df.groupby("Colour")[['M', 'F']].sum()

df[df["Colour"].str.contains("CALI")].groupby("Colour")[['M', 'F']].sum()

import matplotlib.pyplot as plt
import squarify

grey_colours = [colour for colour in colours if "GRE" in colour]
print(*grey_colours)

tan_colours = [colour for colour in colours if "TAN" in colour]
print(*tan_colours)

white_colours = [colour for colour in colours if "WHI" in colour]
print(*white_colours)

squarify.plot(
    sizes=[len(colours), len(grey_colours),
           len(tan_colours), len(white_colours)],
    label=["total", "Grey Cats", "Tan Cats", "White Cats"],
    color=["#DDDDDD", "#BBBBBB", "#999999", "white"])

import matplotlib_venn

matplotlib_venn.venn3(
    subsets=(set(grey_colours), set(tan_colours), set(white_colours)),
    set_labels=("Grey", "Tan", "White")
)

