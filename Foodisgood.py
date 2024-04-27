import streamlit as st
import pandas as pd
import random
import streamlit_authenticator as stauth


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
        "Räucherlachs mit Rührei",
        "Quinoa-Pfannkuchen mit Blaubeeren und Mandeln",
        "Bircher Müsli mit Nüssen und Honig",
        "Frittata mit Spargel, Tomaten und Avocado",
        "Bagel-Sandwich mit Ei, Schinken und Käse",
        "Frühstücks-Burrito mit Gemüse und Salsa",
        "Vanille-Chia-Pudding mit frischem Obst",
        "Bananen-Pancakes mit Beerenkompott",
        "Rösti mit pochiertem Ei und Gemüse",
        "Tofu-Scramble mit schwarzen Bohnen und Avocado"
    ],
    "Zutaten": [
        "50g Haferflocken, 100g Beeren (z.B. Himbeeren, Blaubeeren), 200ml Milch oder Joghurt, 1 EL Honig",
        "1 Avocado, 2 Scheiben Vollkornbrot, 1 Ei, Salz, Pfeffer",
        "150g Naturjoghurt, 50g Müsli, 100g frische Früchte (z.B. Banane, Erdbeeren), 1 EL Honig",
        "3 Eier, 100g Gemüse (z.B. Paprika, Spinat), Salz, Pfeffer",
        "200g gemischte gefrorene Früchte (z.B. Banane, Beeren), 150ml Mandelmilch, Toppings (z.B. Granola, Kokosraspeln)",
        "100g Mehl, 1 Ei, 150ml Milch, 1 EL Zucker, 1 TL Backpulver, Ahornsirup",
        "3 EL Chiasamen, 250ml Mandelmilch, 100g Früchte (z.B. Erdbeeren, Mango)",
        "100g Räucherlachs, 50g Frischkäse, 1/2 Gurke, Dill, 2 Scheiben Vollkornbrot",
        "100g Acai-Püree, 1 Banane, 50g Beeren (z.B. Blaubeeren, Erdbeeren), 30g Granola, 1 EL Kokosraspeln",
        "50g Haferflocken, 30g gemischte Nüsse, 150g Joghurt, 1 Apfel, 1 EL Honig",
        "100g Räucherlachs, 3 Eier, 2 Scheiben Vollkornbrot, Salz, Pfeffer",
        "100g Quinoa-Mehl, 2 Eier, 150ml Milch (oder Mandelmilch), 50g Blaubeeren, 30g gehackte Mandeln, 1 EL Honig",
        "50g Haferflocken, 100g Joghurt, 50ml Milch, 1 Apfel, 30g gemischte Nüsse, 1 EL Honig",
        "4 Eier, 100g grüner Spargel, 50g Kirschtomaten, 1 Avocado, Salz, Pfeffer",
        "1 Bagel, 2 Eier, 50g Schinken, 50g Käse, Salz, Pfeffer",
        "2 Tortillas, 100g Gemüse (z.B. Paprika, Zwiebeln), 50g Salsa, 1 Avocado",
        "3 EL Chiasamen, 250ml Mandelmilch, 1 TL Vanilleextrakt, 100g frisches Obst",
        "100g Mehl, 1 reife Banane, 2 EL Erdnussbutter, 150ml Milch, 1 EL Honig, 100g gemischte Beeren",
        "2 große Kartoffeln, 2 Eier, 1 Zwiebel, 1 Paprika, Salz, Pfeffer",
        "200g Tofu, 100g schwarze Bohnen, 1 Paprika, 1 Zwiebel, 2 Knoblauchzehen, Salz, Pfeffer, 2 Tortillas"
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
        "Leicht",
        "Mittel",
        "Mittel",
        "Mittel",
        "Mittel",
        "Mittel",
        "Mittel",
        "Mittel",
        "Schwer",
        "Schwer"
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
        "10 Minuten",
        "30 Minuten",
        "10 Minuten",
        "20 Minuten",
        "15 Minuten",
        "15 Minuten",
        "5 Minuten",
        "20 Minuten",
        "20 Minuten",
        "25 Minuten"
    ],
    "Bild": [
        "https://www.edeka.de/media/01-rezeptbilder/rezeptbilder-i-p/rez-edeka-porridge-mit-beeren-rezept-i-p-1-1.jpg",
        "https://mesbrouillonsdecuisine.fr/wp-content/uploads/2021/09/IMG_5475.jpg",
        "https://kochclub.schuhbeck.de/wp-content/uploads/2017/05/knuspermuesli.jpg",
        "https://www.paramediform.ch/app/uploads/2023/01/Gemueseomelette_gez-scaled-jpg-webp.webp",
        "https://zestysouthindiankitchen.com/wp-content/uploads/2019/02/Berry-smoothie-bowl-2.jpg",
        "https://www.grillfuerst.de/magazin/wp-content/uploads/2020/03/Pancake-Ahornsirup-scaled.jpg?v=1665135735",
        "https://www.foodtempel.de/wp-content/uploads/2023/03/Veganer-Chiapudding-mit-Erdbeeren-und-Mandeln.jpg",
        "https://snackconnection-marktplatz.de/wp-content/uploads/2023/02/Lachs-Gurken-Sandwich-c-123rf-azurita.jpg",
        "https://www.twopeasandtheirpod.com/wp-content/uploads/2023/06/Acai-Bowl-10.jpg",
        "https://tribalance.de/cdn/shop/articles/tri.balance_Rezept-Tipp_Muesli.jpg?v=1700628257",
        "https://rezept-db.womenshealth.de/image/rezept-db/fullWidth/Ulrike-Holsten_RuehreiRaeucherlachs_800x462.jpg.webp",
        "https://images.eatsmarter.de/sites/default/files/styles/max_size/public/quinoa-pancakes-641304-1.jpg",
        "https://www.oma-kocht.de/wp-content/uploads/2022/03/bircher-musli.jpg",
        "https://www.koch-mit.de/app/uploads/2019/05/Gruene_Spargelfrittata.jpeg",
        "https://media02.stockfood.com/largepreviews/Mzg0ODQwOTc1/12414225-Bagel-belegt-mit-Ei-Kaese-und-Speck.jpg",
        "https://files.vegan-taste-week.de/1/Burrito-Wrap_Timolina_fotolia-1036x414.jpg",
        "https://img.over-blog-kiwi.com/1/45/44/32/20150730/ob_b97941_dsc-1800.JPG",
        "https://klaraslife.com/wp-content/uploads/2017/01/DSC01951.jpg",
        "https://media01.stockfood.com/largepreviews/NDE4MDI5Mjk2/13484816-Roesti-mit-pochierten-Eiern.jpg",
        "https://www.lowcarb.de/files/styles/mainimage_normal/public/assets/image/2021/06/17/tofu-scramble_mit_avocado_portrait.jpg?itok=TcQj08iX&t=1632710627"
    ],
    "Anleitung": [
        "1. Haferflocken in einer Schüssel mit Milch oder Joghurt vermengen. 2. Frische Beeren hinzufügen und mit Honig süßen. 3. Sofort servieren.",
        "1. Avocado halbieren, entkernen und das Fruchtfleisch auf Toastbrot streichen. 2. Ein Ei in einer Pfanne braten und auf die Avocado-Toast legen. 3. Mit Salz und Pfeffer würzen und servieren.",
        "1. Naturjoghurt in eine Schüssel geben. 2. Müsli und frische Früchte hinzufügen. 3. Nach Belieben mit Honig süßen und sofort genießen.",
        "1. Eier verquirlen und mit Salz und Pfeffer würzen. 2. Gemüse nach Wahl (z.B. Paprika, Spinat) in einer Pfanne anbraten. 3. Eier darüber gießen und stocken lassen. 4. Omelett vorsichtig falten und servieren.",
        "1. Gefrorene Früchte und Mandelmilch in einen Mixer geben und cremig mixen. 2. In einer Schüssel anrichten und mit Toppings (z.B. Granola, Kokosraspeln) garnieren.",
        "1. Mehl, Eier, Milch, Zucker und Backpulver zu einem Teig verrühren. 2. Pancakes in einer Pfanne goldbraun backen und mit Ahornsirup servieren.",
        "1. Chiasamen und Mandelmilch vermischen und über Nacht im Kühlschrank quellen lassen. 2. Am nächsten Morgen mit Früchten garnieren und genießen.",
        "1. Räucherlachs, Frischkäse, Gurke und Dill auf Vollkornbrot schichten. 2. Mit etwas Zitrone beträufeln und servieren.",
        "1. Acai-Püree in eine Schüssel geben. 2. Mit geschnittenen Bananen und Beeren belegen. 3. Mit Granola und Kokosraspeln toppen und sofort genießen.",
        "1. Haferflocken, Nüsse und Joghurt in eine Schüssel geben. 2. Apfel in Stücke schneiden und dazugeben. 3. Mit Honig süßen und gut durchmischen.",
        "1. Räucherlachs in eine Pfanne geben und leicht erhitzen. 2. Eier darüber gießen und zu Rührei stocken lassen. 3. Auf Vollkornbrot anrichten und servieren.",
        "1. In einer Schüssel das Quinoa-Mehl, Eier und Milch zu einem glatten Teig verrühren. 2. Eine Pfanne leicht einfetten und erhitzen. Den Teig portionsweise in die Pfanne geben und Blaubeeren darauf streuen. 3. Von beiden Seiten goldbraun backen, bis die Pfannkuchen durchgegart sind. 4. Mit gehackten Mandeln bestreuen und mit Honig servieren.",
        "1. Haferflocken, Joghurt, Milch, Apfelstücke, Nüsse und Honig in einer Schüssel mischen. 2. Über Nacht im Kühlschrank ziehen lassen und am nächsten Morgen mit frischen Früchten und Honig garnieren.",
        "1. Eier verquirlen und mit Salz und Pfeffer würzen. 2. Spargel, Tomaten und Avocado in Stücke schneiden. 3. Eier darüber gießen und in der Pfanne stocken lassen. 4. Frittata aus der Pfanne nehmen und in Stücke schneiden.",
        "1. Bagel halbieren und leicht toasten. 2. Eier in einer Pfanne braten und auf den Bagel legen. 3. Schinken und Käse auf das Ei legen und den Bagel zuklappen. 4. Mit Salz und Pfeffer würzen und servieren.",
        "1. Tortillas leicht erwärmen. 2. Gemüse in einer Pfanne anbraten und auf die Tortillas geben. 3. Salsa und Avocado hinzufügen, Tortillas aufrollen und servieren.",
        "1. Chiasamen mit Mandelmilch und Vanilleextrakt vermengen. 2. Über Nacht im Kühlschrank quellen lassen. 3. Am nächsten Morgen mit frischem Obst garnieren und servieren.",
        "1. Mehl, zerdrückte Banane, Erdnussbutter, Milch und Honig zu einem Teig verrühren. 2. Pancakes in einer Pfanne goldbraun backen. 3. Mit Beerenkompott und Honig servieren.",
        "1. Kartoffeln reiben und abtropfen lassen. 2. Zwiebel fein hacken. 3. Kartoffeln und Zwiebeln in einer Pfanne goldbraun braten. 4. Pochierte Eier zubereiten und auf den Rösti legen. 5. Mit Salz und Pfeffer würzen und servieren.",
        "1. Tofu zerbröseln und in einer Pfanne anbraten. 2. Schwarze Bohnen, Paprika, Zwiebeln und Knoblauch hinzufügen. 3. Alles gut vermischen und mit Salz und Pfeffer würzen. 4. Auf Tortillas verteilen und mit Avocado servieren."
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
