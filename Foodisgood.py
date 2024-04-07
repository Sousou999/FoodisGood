import streamlit as st
import pandas as pd
import random

# Beispiel Daten für Frühstücksrezepte
breakfast_recipes_data = {
    "Gericht": [
        "Haferflocken mit Beeren",
        "Avocado-Toast",
        "Joghurt mit Müsli und Früchten",
        "Omelett mit Gemüse",
        "Smoothie-Bowl",
        "Pancakes mit Ahornsirup",
        "Chia-Pudding mit Früchten",
        "Lachs-Sandwich",
        "Acai-Bowl",
        "Apfel-Nuss-Müsli",
        "Räucherlachs mit Rührei"
    ],
    "Zutaten": [
        "Haferflocken, Beeren (z.B. Himbeeren, Blaubeeren), Milch oder Joghurt, Honig",
        "Avocado, Vollkornbrot, Ei, Salz, Pfeffer",
        "Naturjoghurt, Müsli, Früchte (z.B. Banane, Erdbeeren)",
        "Eier, Gemüse (z.B. Paprika, Spinat), Salz, Pfeffer",
        "Gemischte gefrorene Früchte (z.B. Banane, Beeren), Mandelmilch, Toppings (z.B. Granola, Kokosraspeln)",
        "Mehl, Eier, Milch, Zucker, Backpulver, Ahornsirup",
        "Chiasamen, Mandelmilch, Früchte (z.B. Erdbeeren, Mango)",
        "Räucherlachs, Frischkäse, Gurke, Dill, Vollkornbrot",
        "Acai-Püree, Banane, Beeren (z.B. Blaubeeren, Erdbeeren), Granola, Kokosraspeln",
        "Haferflocken, Nüsse, Joghurt, Apfel, Honig",
        "Räucherlachs, Eier, Vollkornbrot, Salz, Pfeffer"
    
    ],
    "Schwierigkeitsgrad": [
        "Sehr leicht",
        "Leicht",
        "Sehr leicht",
        "Leicht",
        "Leicht",
        "Mittel",
        "Sehr leicht",
        "Leicht",
        "Leicht",
        "Sehr leicht",
        "Leicht"
    ],
    "Dauer": [
        "10 Minuten",
        "5 Minuten",
        "5 Minuten",
        "10 Minuten",
        "5 Minuten",
        "15 Minuten",
        "5 Minuten",
        "10 Minuten",
        "5 Minuten",
        "5 Minuten",
        "10 Minuten"
    ],
    "Bild": [
        "https://www.edeka.de/media/01-rezeptbilder/rezeptbilder-i-p/rez-edeka-porridge-mit-beeren-rezept-i-p-1-1.jpg",
        "https://mesbrouillonsdecuisine.fr/wp-content/uploads/2021/09/IMG_5475.jpg",
        "https://kochclub.schuhbeck.de/wp-content/uploads/2017/05/knuspermuesli.jpg",
        "https://www.paramediform.ch/app/uploads/2023/01/Gemueseomelette_gez-scaled-jpg-webp.webp",
        "https://zestysouthindiankitchen.com/wp-content/uploads/2019/02/Berry-smoothie-bowl-2.jpg",
        "https://www.spendwithpennies.com/wp-content/uploads/2021/01/Banana-Pancakes-SpendWithPennies-1.jpg",
        "https://www.linsfood.com/wp-content/uploads/2017/07/Quinoa-Breakfast-Bowl-3.jpg",
        "https://www.simplyrecipes.com/thmb/2Sd8OgRC1N7Yai-7C2WtZBXZoMg=/960x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/Simply-Recipes-Smoked-Salmon-and-Avocado-Tartine-LEAD-2-5b834e02ba61770036ec5ae1.jpg",
        "https://images.immediate.co.uk/production/volatile/sites/30/2021/03/Acai-Bowl-3d0780d.jpg",
        "https://wholeandheavenlyoven.com/wp-content/uploads/2019/09/Apple-Cinnamon-Granola-9.jpg",
        "https://www.olivemagazine.com/wp-content/uploads/2017/01/wholewheat-rasps-smoked-salmon-eggs.jpg"
    ],
    "Anleitung": [
        "1. Haferflocken mit Milch oder Joghurt in einer Schüssel vermengen. 2. Frische Beeren hinzufügen und mit Honig süßen. 3. Sofort servieren.",
        "1. Avocado halbieren, entkernen und das Fruchtfleisch auf Toastbrot streichen. 2. Ein Ei in einer Pfanne braten und auf die Avocado-Toast legen. 3. Mit Salz und Pfeffer würzen und servieren.",
        "1. Naturjoghurt in eine Schüssel geben. 2. Müsli und frische Früchte hinzufügen. 3. Nach Belieben mit Honig süßen und sofort genießen.",
        "1. Eier verquirlen und mit Salz und Pfeffer würzen. 2. Gemüse nach Wahl (z.B. Paprika, Spinat) in einer Pfanne anbraten. 3. Eier über das Gemüse gießen und stocken lassen. 4. Omelett vorsichtig falten und servieren.",
        "1. Gefrorene Früchte und Mandelmilch in einen Mixer geben und cremig mixen. 2. In einer Schüssel anrichten und mit Toppings (z.B. Granola, Kokosraspeln) garnieren.",
        "1. Mehl, Eier, Milch, Zucker und Backpulver zu einem Teig verrühren. 2. Pancakes in einer Pfanne goldbraun backen und mit Ahornsirup servieren.",
        "1. Chiasamen und Mandelmilch vermischen und über Nacht im Kühlschrank quellen lassen. 2. Am nächsten Morgen mit Früchten garnieren und genießen.",
        "1. Räucherlachs, Frischkäse, Gurke und Dill auf Vollkornbrot schichten. 2. Mit etwas Zitrone beträufeln und servieren.",
        "1. Acai-Püree in eine Schüssel geben. 2. Mit geschnittenen Bananen und Beeren belegen. 3. Mit Granola und Kokosraspeln toppen und sofort genießen.",
        "1. Haferflocken, Nüsse und Joghurt in eine Schüssel geben. 2. Apfel in Stücke schneiden und dazugeben. 3. Mit Honig süßen und gut durchmischen.",
        "1. Räucherlachs in eine Pfanne geben und leicht erhitzen. 2. Eier darüber gießen und zu Rührei stocken lassen. 3. Auf Vollkornbrot anrichten und servieren."
    ]
}

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
    "🍳 Rührei mit Räucherlachs ist ein klassisches, proteinreiches Frühstück für Feinschmecker!"
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
