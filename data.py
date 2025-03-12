import csv


def display(options):
    for i in range(0, len(options)):
        print(options[i], "(", i, ") ", sep="")


genres = [
    "Documentaries",
    "International TV Shows",
    "TV Dramas",
    "TV Mysteries",
    "Crime TV Shows",
    "TV Action & Adventure",
    "Docuseries",
    "Reality TV",
    "Romantic TV Shows",
    "TV Comedies",
    "TV Horror",
    "Children & Family Movies",
    "Dramas",
    "Independent Movies",
    "International Movies",
    "British TV Shows",
    "Comedies",
    "Spanish-Language TV Shows",
    "Thrillers",
    "Romantic Movies",
    "Music & Musicals",
    "Horror Movies",
    "Sci-Fi & Fantasy",
    "TV Thrillers",
    "Kids' TV",
    "Action & Adventure",
    "TV Sci-Fi & Fantasy",
    "Classic Movies",
    "Anime Features",
    "Sports Movies",
    "Anime Series",
    "Korean TV Shows",
    "Science & Nature TV",
    "Teen TV Shows",
    "Cult Movies",
    "TV Shows",
    "Faith & Spirituality",
    "LGBTQ Movies",
    "Stand-Up Comedy",
    "Movies",
    "Stand-Up Comedy & Talk Shows",
    "Classic & Cult TV"
]

gnums = []

display(genres)
chosen = 0
while chosen != -1:
    chosen = int(input("\nEnter choice: "))
    if chosen != -1:
        gnums.append(chosen)
        print(genres[chosen])


genre_list = []
possible_titles = []
possible_desc = []

with open('netflix_dataset.csv', newline='', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        valid = True
        txt = row['listed_in'].split(", ")
        for g in gnums:
            if genres[g] not in txt:
                valid = False
        if valid:
            possible_titles.append(row['title'])
            possible_desc.append(row['description'])


add_up = {}

for poss in possible_titles:
    add_up[poss] = 0

# 1, 8, 33

n = 4

for i in range(0, n):
    for j in range(i+1, n):
        print()
        print(possible_titles[i])
        print(possible_desc[i])
        print("OR")
        print(possible_titles[j])
        print(possible_desc[j])
        print()
        choice = int(input("Which would you prefer to watch? (0 or 1) "))
        if choice == 0:
            add_up[possible_titles[i]] += 1
        else:
            add_up[possible_titles[j]] += 1

print("Recommendations for you!")

done = sorted(add_up.items(), key=lambda x: x[1], reverse=True)

for i in range(0, n):
    print((i+1), ". ", done[i], sep="")
