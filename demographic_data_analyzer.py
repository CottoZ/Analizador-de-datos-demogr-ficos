import pandas as pd

def calculate_demographic_data(print_data=True):
    # Leer los datos del archivo
    df = pd.read_csv('adult.data.csv')

    # Asegurarse de que los valores de edad sean numéricos y eliminar valores nulos
    average_age_men = round(df[df['sex'] == 'Male']['age'].dropna().mean(), 1)

    # Contar el número de cada raza
    race_count = df['race'].value_counts()

    # Calcular el porcentaje de personas con un título de licenciatura
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)

    # Calcular el porcentaje de personas con educación avanzada que ganan más de 50K
    higher_education_rich = round((df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')].shape[0] / df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0]) * 100, 1)

    lower_education_rich = round((df[(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')].shape[0] / df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0]) * 100, 1)

    # Asegurarse de que las horas trabajadas sean numéricas y eliminar valores no válidos
    df['hours-per-week'] = pd.to_numeric(df['hours-per-week'], errors='coerce')

    # Calcular el mínimo número de horas trabajadas por semana
    min_work_hours = df['hours-per-week'].min()

    # Calcular el porcentaje de personas que ganan más de 50K y trabajan el mínimo número de horas
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # Calcular el país con el mayor porcentaje de personas ricas
    highest_earning_country = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean()).idxmax()
    highest_earning_country_percentage = round(df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean()).max() * 100, 1)

    # Identificar la ocupación más popular para aquellos que ganan más de 50K en India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # Imprimir los resultados si es necesario
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
