import streamlit as st
import pandas as pd
import random
import streamlit_authenticator as stauth
import csv

# Define the path to your CSV file
csv_file_path = "Rezepte.csv"
# Dictionary to store data
breakfast_recipes_data = {}
# Read the CSV file
with open(csv_file_path, "r", encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Get the header row
    # Initialize the dictionary with empty lists for each header column
    for column_name in header:
        breakfast_recipes_data[column_name] = []
    # Iterate through each row in the CSV file
    for row in reader:
        for i, value in enumerate(row):
            # Check if the index exists in the header list
            if i < len(header):
                # Append each value to its respective column in the dictionary
                breakfast_recipes_data[header[i]].append(value)
# Convert the data dictionary to the desired format
breakfast_recipes_data_formated = "{\n"
for key, values in breakfast_recipes_data.items():
    breakfast_recipes_data_formated += f'"{key}": [\n'
    for value in values:
        breakfast_recipes_data_formated += f'"{value}",\n'
    breakfast_recipes_data_formated = breakfast_recipes_data_formated[:-2]  # Remove the trailing comma
    breakfast_recipes_data_formated += "\n],\n"
# Remove the trailing comma and newline
breakfast_recipes_data_formated = breakfast_recipes_data_formated[:-2] + "\n}"

# load list of passwords and logins (login_password_list.csv)
df = pd.read_csv("login_password_list.csv")
df.head()

# add column with hashed passwords
passwords = df['password']
df['hash'] = stauth.utilities.hasher.Hasher(passwords).generate()
df.head()

# save logins and hashed passwords to file
columns = ['username', 'name','hash']
df[columns].rename(columns={'hash':'password'}).to_csv("login_hashed_password_list.csv", index=False)

# DataFrame für Frühstücksrezepte erstellen
breakfast_recipes_df = pd.DataFrame(breakfast_recipes_data)
# Seitentitel festlegen
st.title("Willkommen bei FoodisGood")
st.subheader("Entdecke eine Welt voller gesunder und schmackhafter Frühstücksrezepte für ein energiegeladenes Studium!")
# Rezeptsuche nach Frühstücksrezepten
search_term = st.text_input("Suche nach einem Frühstücksrezept:")
if search_term:
    filtered_recipes = breakfast_recipes_df[breakfast_recipes_df["Gericht"].str.contains(search_term, case=False)]
else:
    filtered_recipes = breakfast_recipes_df
# Dropdown-Menü für Rezeptauswahl
selected_recipe = st.selectbox("Wähle ein Frühstücksrezept aus:", filtered_recipes["Gericht"])
# Informationen zum ausgewählten Rezept anzeigen
st.subheader(f"Rezept für {selected_recipe}:")
selected_recipe_info = filtered_recipes[filtered_recipes["Gericht"] == selected_recipe].iloc[0]
st.markdown(f"<div style='font-size: 18px'><b>Zutaten:</b> {selected_recipe_info['Zutaten']}</div>", unsafe_allow_html=True)
st.markdown(f"<div style='font-size: 18px'><b>Schwierigkeitsgrad:</b> {selected_recipe_info['Schwierigkeitsgrad']}</div>", unsafe_allow_html=True)
st.markdown(f"<div style='font-size: 18px'><b>Dauer:</b> {selected_recipe_info['Dauer']}</div>", unsafe_allow_html=True)
st.image(selected_recipe_info["Bild"], caption=selected_recipe, use_column_width=True)
st.markdown(f"<div style='font-size: 18px'><b>Anleitung:</b><br>{selected_recipe_info['Anleitung']}</div>", unsafe_allow_html=True)
# Einkaufsliste anzeigen
ingredients_list = selected_recipe_info["Zutaten"].split(", ")
st.subheader("Einkaufsliste:")
for ingredient in ingredients_list:
    st.checkbox(ingredient)
# Emoji-Überraschungen zum Thema Frühstück
emoji_surprises = {
    "🍓 Beeren sind voller Antioxidantien und passen perfekt zu Müsli und Joghurt!",
    "🥑 Avocados sind reich an gesunden Fetten und machen jedes Frühstück cremig und sättigend!",
    "🥚 Eier sind eine hervorragende Proteinquelle und können vielseitig in Frühstücksgerichten verwendet werden!",
    "🥛 Mandelmilch ist eine köstliche pflanzliche Milchalternative für Smoothies und Müsli!",
    "🍌 Bananen sind reich an Kalium und ein perfekter natürlicher Süßstoff für Smoothies und Oatmeal!",
    "🥞 Pancakes sind ein klassisches Frühstücksgericht und lassen sich vielseitig kombinieren!",
    "🥣 Chia-Pudding ist eine gesunde und sättigende Option für einen guten Start in den Tag!",
    "🍣 Lachs ist reich an Omega-3-Fettsäuren und passt perfekt zu einem herzhaften Frühstück!",
    "🍇 Acai-Bowls sind eine leckere Möglichkeit, viele Vitamine und Antioxidantien zu genießen!",
    "🍏 Äpfel sind gesund, knackig und eine perfekte Ergänzung für jedes Müsli oder Joghurt!",
    "🍳 Rührei mit Räucherlachs ist ein klassisches, proteinreiches Frühstück für Feinschmecker!",
    "🥯 Bagels sind eine köstliche Basis für herzhafte Frühstückssandwiches!",
    "🥔 Rösti ist eine knusprige Kartoffelbeilage und perfekt für ein herzhaftes Frühstück!",
    "🌱 Tofu-Scramble ist eine vegane Alternative zu Rührei und reich an pflanzlichem Protein!"
}
# Knopf für eine zufällige Emoji-Überraschung zum Thema Frühstück
if st.button("Klicke hier für eine Frühstücksüberraschung!"):
    random_surprise = random.choice(list(emoji_surprises))
    st.write(" Klicke erneut für eine andere Überraschung ;)")
    st.write(random_surprise)

# Sidebar mit Nahrungsergänzungsmitteln
st.sidebar.title("Nahrungsergänzungsmittel")
st.sidebar.markdown("""
- **Vitamin D:** Wichtig für die Knochengesundheit und das Immunsystem. Produktempfehlung: [Burgerstein Vitamin D3 600 IE](https://www.burgerstein.ch/de-DE/produkte/burgerstein-vitamin-d3-600-ie)
- **Omega-3-Fettsäuren:** Unterstützen die Herzgesundheit und fördern die Gehirnfunktion. Produktempfehlung: [Burgerstein Omega-3 Liquid](https://www.burgerstein.ch/de-DE/produkte/burgerstein-omega-3-liquid)
- **Probiotika:** Gut für die Darmgesundheit und die Verdauung. Produktempfehlung: [Burgerstein Biotics G](https://www.burgerstein.ch/de-DE/produkte/burgerstein-biotics-g)
- **Magnesium:** Kann helfen, Muskelkrämpfe zu reduzieren und hilft bei Müdigkeit. Produktempfehlung: [Burgerstein Magnesiumvital Direct](https://www.burgerstein.ch/de-DE/produkte/burgerstein-magnesiumvital-direct)
""")
# Footer
st.markdown("---")
st.markdown("Erstellt von FoodisGood 🍳 Genieße deine Mahlzeiten und dein Studium! 😊")