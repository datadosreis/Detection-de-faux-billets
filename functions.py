def data_analyse(df):
    """
    Permet de réaliser une analyse des données (infos, outliers, valeurs manquantes et doublons)
    """
    print("Structure du dataframe:")
    print("-"*20)
    print(df.info())
    print("\n")
    print("Vérification des valeurs uniques:")
    print("-"*20)
    print(df.nunique())
    print("\n")
    print("Valeurs manquantes:")
    print("-"*20)
    print(df.isna().sum())
    print("\n")
    print("% Valeurs manquantes:")
    print("-"*20)
    print(df.isna().mean().round(2))
    print("\n")
    print("Vérification des doublons:")
    print("-"*20)
    print(df.duplicated().sum(), 'doublons détectés.')
    print("\n")
    print("Vérification des outliers:")
    print("-"*20)
    return df.describe()

def make_autopct(values):
    """
    Permet d'afficher les valeurs sur un pie chart
    """
    def my_autopct(pct):
        total = sum (values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct