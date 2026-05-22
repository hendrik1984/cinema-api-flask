from flask.cli import AppGroup
from app.extensions import db
from app.models.user import User
from app.models.movie import Movie

seed_cli = AppGroup("seed")


@seed_cli.command("admin")
def seed_admin():
    """Create default admin user"""

    email = "admin@gmail.com"
    username = "admin"
    password = "password"

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        print("Admin already exists")
        return

    admin = User(
        email=email,
        username=username,
        role="admin"
    )
    admin.set_password(password)

    db.session.add(admin)
    db.session.commit()

    print("Admin user created:")
    print(f"Email: {email}")
    print(f"Password: {password}")

@seed_cli.command("user")
def seed_user():
    print("Create user")
    email = "john.wick1@gmail.com"
    username = "john.wick1"
    password = "password"

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        print("User already exists")
        return

    admin = User(
        email=email,
        username=username,
        role="admin"
    )
    admin.set_password(password)

    db.session.add(admin)
    db.session.commit()

@seed_cli.command("movies")
def seed_movies():
    movies = [
        {
            "title": "Shadows of the Past",
            "description": "A detective confronts his own forgotten crime while hunting a serial killer.",
            "duration": 112
        },
        {
            "title": "Echoes of Tomorrow",
            "description": "A time traveler gets stuck in a loop, reliving the day Earth receives an alien signal.",
            "duration": 128
        },
        {
            "title": "The Last Signal",
            "description": "Astronauts on a dying space station race to send a warning to Earth.",
            "duration": 105
        },
        {
            "title": "Fractured Mind",
            "description": "A man with dissociative identity disorder is the only witness to a political assassination.",
            "duration": 118
        },
        {
            "title": "Silent Thunder",
            "description": "In a world without sound, a young warrior must defeat a storm that devours memories.",
            "duration": 122
        },
        {
            "title": "Crimson Tide Rising",
            "description": "A rogue submarine captain threatens to start World War III.",
            "duration": 135
        },
        {
            "title": "The Forgotten Kingdom",
            "description": "A peasant discovers she is the lost heir to a magical kingdom buried under ice.",
            "duration": 140
        },
        {
            "title": "Neon Skies",
            "description": "In a cyberpunk future, a hacker fights to free human consciousness from a corporate grid.",
            "duration": 115
        },
        {
            "title": "Whispers in the Dark",
            "description": "A journalist investigates a cult that speaks to the dead via radio frequencies.",
            "duration": 108
        },
        {
            "title": "The Velvet Cage",
            "description": "A ballerina is trapped in a theater that feeds on dancers' souls.",
            "duration": 125
        },
        {
            "title": "Ashes of Eden",
            "description": "After a failed utopia, two siblings wander a desert searching for the last tree.",
            "duration": 130
        },
        {
            "title": "Midnight Express",
            "description": "Passengers on a train to nowhere must solve a murder before they all disappear.",
            "duration": 119
        },
        {
            "title": "The Obsidian Heart",
            "description": "A thief steals a cursed gem that slowly turns her into stone.",
            "duration": 113
        },
        {
            "title": "Ghosts of the Red Moon",
            "description": "On a lunar colony, astronauts are haunted by apparitions of extinct Earth animals.",
            "duration": 126
        },
        {
            "title": "Beneath the Frost",
            "description": "A climate scientist uncovers a prehistoric predator frozen in the Arctic.",
            "duration": 110
        },
        {
            "title": "The Clockwork Man",
            "description": "In Victorian London, an automaton detective hunts a rogue inventor.",
            "duration": 132
        },
        {
            "title": "Rivers of Rust",
            "description": "In a post-apocalyptic swamp, a scavenger builds a raft to find the sea.",
            "duration": 117
        },
        {
            "title": "Starlight Fugitives",
            "description": "Two aliens crash-land on Earth and must evade a government hit squad.",
            "duration": 121
        },
        {
            "title": "The Ivory Labyrinth",
            "description": "A maze appears every night in a small town, and a girl gets lost inside.",
            "duration": 109
        },
        {
            "title": "Phantom Circuit",
            "description": "A programmer discovers a hidden AI that wants to become human.",
            "duration": 124
        },
        {
            "title": "The Gilded Noose",
            "description": "A corrupt billionaire is blackmailed by his own butler.",
            "duration": 114
        },
        {
            "title": "Wolves at the Gate",
            "description": "During a siege, a young archer must protect her village from werewolves.",
            "duration": 127
        },
        {
            "title": "The Obsidian Tear",
            "description": "A single tear from a stone angel can bring back the dead — for a price.",
            "duration": 135
        },
        {
            "title": "Cobalt Dream",
            "description": "A factory worker injects a drug that lets him live inside paintings.",
            "duration": 106
        },
        {
            "title": "The Last Astronomer",
            "description": "In a city that banned the night sky, a man builds a secret telescope.",
            "duration": 118
        },
        {
            "title": "Serpentine",
            "description": "A con artist poses as a snake priestess to rob a jungle temple.",
            "duration": 123
        },
        {
            "title": "The Hollow King",
            "description": "A king without a shadow discovers his reflection is alive and evil.",
            "duration": 131
        },
        {
            "title": "Iron Blossom",
            "description": "In a steampunk world, a flower made of metal starts a revolution.",
            "duration": 115
        },
        {
            "title": "Glass Inferno",
            "description": "Firefighters battle a blaze in a skyscraper made entirely of glass.",
            "duration": 129
        },
        {
            "title": "The Vermilion Gate",
            "description": "A warrior must pass through seven deadly doors to save her sister.",
            "duration": 140
        },
        {
            "title": "Echo Chamber",
            "description": "A podcaster discovers that every lie she tells becomes real.",
            "duration": 104
        },
        {
            "title": "Saffron Rain",
            "description": "A strange yellow rain falls, turning people into living statues.",
            "duration": 117
        },
        {
            "title": "The Copper Child",
            "description": "A couple builds a robot child, but it begins to feel jealousy.",
            "duration": 125
        },
        {
            "title": "Midnight Carnival",
            "description": "A traveling carnival arrives at midnight and grants cursed wishes.",
            "duration": 112
        },
        {
            "title": "The Obsidian Fleet",
            "description": "Pirates sail on a black glass ship that can cross between worlds.",
            "duration": 136
        },
        {
            "title": "Frozen Chorus",
            "description": "A choir in a remote abbey sings a hymn that freezes time.",
            "duration": 108
        },
        {
            "title": "The Rusted Compass",
            "description": "A lost traveler finds a compass that points to his past mistakes.",
            "duration": 119
        },
        {
            "title": "Violet Dusk",
            "description": "At sunset every day, the dead can walk among the living for one hour.",
            "duration": 130
        },
        {
            "title": "The Bone Harp",
            "description": "A musician makes a harp from dragon bones and awakens an ancient evil.",
            "duration": 124
        },
        {
            "title": "Ashwalkers",
            "description": "Nomads traverse a volcanic wasteland, hunted by ash monsters.",
            "duration": 115
        },
        {
            "title": "The Silver Plague",
            "description": "A virus turns people into living silver statues that still breathe.",
            "duration": 128
        },
        {
            "title": "Crimson Lullaby",
            "description": "A mother sings a cursed lullaby to save her son from a witch.",
            "duration": 110
        },
        {
            "title": "The Clock Tower",
            "description": "A tower appears every 100 years; whoever enters it lives backwards.",
            "duration": 133
        },
        {
            "title": "Ember & Bone",
            "description": "Two rival alchemists must combine their arts to stop a plague.",
            "duration": 122
        },
        {
            "title": "The Shadow Market",
            "description": "An underground market sells shadows, and a man buys his own.",
            "duration": 116
        },
        {
            "title": "White Noise",
            "description": "A radio host's voice makes listeners forget their worst memories.",
            "duration": 107
        },
        {
            "title": "The Gargoyle's Kiss",
            "description": "A gargoyle comes to life and falls in love with a nun.",
            "duration": 125
        },
        {
            "title": "Molten Sky",
            "description": "The sky rains fire, and a family builds a boat to sail on lava.",
            "duration": 131
        },
        {
            "title": "The Last Calligrapher",
            "description": "In a world without writing, a man's ink brings stories to life.",
            "duration": 118
        },
        {
            "title": "Night Heron",
            "description": "A blind assassin uses sound to hunt corrupt officials.",
            "duration": 127
        },
        {
            "title": "The Porcelain War",
            "description": "Two armies fight with living china dolls as soldiers.",
            "duration": 113
        },
        {
            "title": "Sulfur & Honey",
            "description": "A demon and an angel open a bakery together in a small town.",
            "duration": 120
        },
        {
            "title": "The Hollow Glacier",
            "description": "Explorers find a city inside a glacier where time stands still.",
            "duration": 134
        },
        {
            "title": "Raven's Gambit",
            "description": "A chess master plays a game against Death for her husband's soul.",
            "duration": 109
        },
        {
            "title": "The Amber Room",
            "description": "A woman inherits a room made of amber that shows the future.",
            "duration": 126
        },
        {
            "title": "Cinder & Silk",
            "description": "A seamstress sews uniforms for soldiers, unaware they are ghosts.",
            "duration": 114
        },
        {
            "title": "The Obsidian Tide",
            "description": "A black wave rises from the ocean and swallows islands whole.",
            "duration": 129
        },
        {
            "title": "Phantom Orchid",
            "description": "A rare flower only blooms in the presence of a lie.",
            "duration": 111
        },
        {
            "title": "The Brass Leviathan",
            "description": "A mechanical whale hunts a captain who sold his soul for oil.",
            "duration": 138
        },
        {
            "title": "Midnight Sun",
            "description": "In an Arctic town, the sun never sets — and neither do the dead.",
            "duration": 123
        },
        {
            "title": "The Velvet Razor",
            "description": "A barber slits throats of tyrants, leaving roses on their chests.",
            "duration": 117
        },
        {
            "title": "Ash & Amber",
            "description": "A girl made of ash falls in love with a prince made of amber.",
            "duration": 122
        },
        {
            "title": "The Clockwork Forest",
            "description": "Trees made of gears grow in a forest where animals are automatons.",
            "duration": 130
        },
        {
            "title": "Stained Glass Souls",
            "description": "A cathedral's windows trap sinners' souls; a thief tries to free one.",
            "duration": 115
        },
        {
            "title": "The Iron Tide",
            "description": "Magnetic storms pull metal from the ground, forming walking forts.",
            "duration": 128
        },
        {
            "title": "Emberveil",
            "description": "A city hides under a dome of ash; a girl finds a crack to the sun.",
            "duration": 119
        },
        {
            "title": "The Last Lighthouse",
            "description": "A lighthouse keeper guides souls of drowned sailors to the afterlife.",
            "duration": 124
        },
        {
            "title": "Rust & Roses",
            "description": "A robot falls in love with a gardener in a post-human world.",
            "duration": 112
        },
        {
            "title": "The Obsidian Compass",
            "description": "A compass points not north, but toward your greatest fear.",
            "duration": 135
        },
        {
            "title": "Crimson Snow",
            "description": "Red snow falls every winter, hiding a predator underneath.",
            "duration": 108
        },
        {
            "title": "The Gilded Cage",
            "description": "A singer is held captive in a floating opera house above clouds.",
            "duration": 131
        },
        {
            "title": "Phantom Engine",
            "description": "A train runs on ghostly coal and can travel through memories.",
            "duration": 126
        },
        {
            "title": "The Copper Veil",
            "description": "A bride wears a copper mask; underneath is nothing but gears.",
            "duration": 113
        },
        {
            "title": "Salt & Bone",
            "description": "On a salt desert, skeletons rise and ask riddles to pass.",
            "duration": 120
        },
        {
            "title": "The Velvet Abyss",
            "description": "A submarine descends into a trench where light has a physical form.",
            "duration": 137
        },
        {
            "title": "Midnight Glass",
            "description": "Mirrors show alternate selves; one of them escapes into our world.",
            "duration": 116
        },
        {
            "title": "The Ash Princess",
            "description": "A princess cursed to turn to ash at dawn is saved by a dragon.",
            "duration": 129
        },
        {
            "title": "Ironweave",
            "description": "Cloth made of iron threads can stop bullets but not betrayal.",
            "duration": 114
        },
        {
            "title": "The Last Rainmaker",
            "description": "In a drought, a man who can cry rain is hunted by warlords.",
            "duration": 122
        },
        {
            "title": "Obsidian Rain",
            "description": "Shards of black glass fall from the sky instead of rain.",
            "duration": 110
        },
        {
            "title": "The Clockwork Sun",
            "description": "An artificial sun breaks down, and a mechanic must repair it.",
            "duration": 134
        },
        {
            "title": "Ember Dogs",
            "description": "Fiery dogs roam the plains, loyal only to children.",
            "duration": 118
        },
        {
            "title": "The Copper Crown",
            "description": "A king's copper crown rusts, revealing he is immortal.",
            "duration": 125
        },
        {
            "title": "Silk & Steel",
            "description": "A spy uses poisoned silk ribbons to assassinate nobles.",
            "duration": 111
        },
        {
            "title": "The Hollow Mountain",
            "description": "A mountain is hollow and contains a sleeping giant.",
            "duration": 139
        },
        {
            "title": "Crimson Petals",
            "description": "Flowers bloom wherever blood is spilled in a war-torn land.",
            "duration": 123
        },
        {
            "title": "The Last Mirror",
            "description": "The final mirror on Earth shows not your reflection but your soul.",
            "duration": 117
        },
        {
            "title": "Rustheart",
            "description": "A robot replaces her heart with a rusted one and starts dreaming.",
            "duration": 130
        },
        {
            "title": "The Velvet Storm",
            "description": "A storm made of rose petals buries entire villages.",
            "duration": 109
        },
        {
            "title": "Phantom Feast",
            "description": "A dinner party where guests eat memories instead of food.",
            "duration": 124
        },
        {
            "title": "The Obsidian Rose",
            "description": "A black rose grants immortality but kills love with every touch.",
            "duration": 132
        },
        {
            "title": "Midnight Alchemy",
            "description": "An alchemist turns regret into gold at midnight only.",
            "duration": 115
        },
        {
            "title": "The Gilded Tomb",
            "description": "A pharaoh's tomb is made of gold but curses all who enter.",
            "duration": 128
        },
        {
            "title": "Cinderfall",
            "description": "A city built on cinders sinks deeper each day.",
            "duration": 121
        },
        {
            "title": "The Iron Orchard",
            "description": "Trees bear iron fruit; whoever eats it becomes a soldier.",
            "duration": 114
        },
        {
            "title": "Ember & Ivory",
            "description": "A war between fire wizards and ice wizards ends in a frozen volcano.",
            "duration": 136
        },
        {
            "title": "The Last Candle",
            "description": "A single candle keeps the darkness away; it is starting to melt.",
            "duration": 110
        },
        {
            "title": "Rust & Starlight",
            "description": "A spaceship made of rusted iron flies to a dying star.",
            "duration": 127
        },
        {
            "title": "The Copper Labyrinth",
            "description": "A maze under a city changes every night with copper walls.",
            "duration": 133
        }
    ]

    print("Preparing...")
    for m in movies:
        movie = Movie(
            title=m["title"],
            description=m["description"],
            duration=m["duration"],
            is_active=True
        )
        print(f"Add {movie.title}...")
        db.session.add(movie)
        db.session.commit()
        print("done")
    