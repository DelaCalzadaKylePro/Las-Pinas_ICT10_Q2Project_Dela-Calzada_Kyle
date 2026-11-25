from js import document

nicknames = {
    "kyle": {"name": "Kyle", "origin": "Scottish origin", "meaning": "A name associated with a narrow channel or strait, often linked with strength and determination."},
    "mia": {"name": "Mia", "origin": "Latin and Scandinavian origin", "meaning": "A warm and friendly name meaning “mine” or “beloved.”"},
    "noah": {"name": "Noah", "origin": "Hebrew origin", "meaning": "A timeless name meaning “rest” or “comfort.”"},
    "sofia": {"name": "Sofia", "origin": "Greek origin", "meaning": "A graceful name meaning “wisdom.”"}
}

elements = {
    "h": {"symbol": "H", "name": "Hydrogen", "number": "1", "mass": "1.008", "group": "Nonmetal", "state": "Gas"},
    "hydrogen": {"symbol": "H", "name": "Hydrogen", "number": "1", "mass": "1.008", "group": "Nonmetal", "state": "Gas"},
    "he": {"symbol": "He", "name": "Helium", "number": "2", "mass": "4.0026", "group": "Noble gas", "state": "Gas"},
    "li": {"symbol": "Li", "name": "Lithium", "number": "3", "mass": "6.94", "group": "Alkali metal", "state": "Solid"},
    "c": {"symbol": "C", "name": "Carbon", "number": "6", "mass": "12.011", "group": "Nonmetal", "state": "Solid"},
    "carbon": {"symbol": "C", "name": "Carbon", "number": "6", "mass": "12.011", "group": "Nonmetal", "state": "Solid"},
    "o": {"symbol": "O", "name": "Oxygen", "number": "8", "mass": "15.999", "group": "Nonmetal", "state": "Gas"},
    "oxygen": {"symbol": "O", "name": "Oxygen", "number": "8", "mass": "15.999", "group": "Nonmetal", "state": "Gas"},
    "na": {"symbol": "Na", "name": "Sodium", "number": "11", "mass": "22.990", "group": "Alkali metal", "state": "Solid"},
    "mg": {"symbol": "Mg", "name": "Magnesium", "number": "12", "mass": "24.305", "group": "Alkaline earth", "state": "Solid"},
    "fe": {"symbol": "Fe", "name": "Iron", "number": "26", "mass": "55.845", "group": "Transition metal", "state": "Solid"},
    "iron": {"symbol": "Fe", "name": "Iron", "number": "26", "mass": "55.845", "group": "Transition metal", "state": "Solid"},
    "cu": {"symbol": "Cu", "name": "Copper", "number": "29", "mass": "63.546", "group": "Transition metal", "state": "Solid"},
    "ag": {"symbol": "Ag", "name": "Silver", "number": "47", "mass": "107.868", "group": "Transition metal", "state": "Solid"},
    "au": {"symbol": "Au", "name": "Gold", "number": "79", "mass": "196.967", "group": "Transition metal", "state": "Solid"},
    "gold": {"symbol": "Au", "name": "Gold", "number": "79", "mass": "196.967", "group": "Transition metal", "state": "Solid"}
}

members = [
    {"name": "Kyle Dela Calzada", "club": "Coding Club", "role": "Member"},
    {"name": "Angela Cruz", "club": "Science Club", "role": "President"},
    {"name": "Miguel Santos", "club": "Debate Team", "role": "Captain"},
    {"name": "Lara Reyes", "club": "Arts Club", "role": "Member"},
    {"name": "Nathan Flores", "club": "Coding Club", "role": "Member"},
    {"name": "Sofia Lim", "club": "Science Club", "role": "Secretary"},
    {"name": "Paolo Garcia", "club": "Debate Team", "role": "Member"},
    {"name": "Ivy Mendoza", "club": "Arts Club", "role": "Treasurer"},
    {"name": "Rico Torres", "club": "Coding Club", "role": "Vice President"}
]

def escape_text(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

nickname_input = document.getElementById("nicknameInput")
if nickname_input:
    def check_nickname(*args):
        key = nickname_input.value.strip().lower()
        result = document.getElementById("nicknameResult")
        if key in nicknames:
            item = nicknames[key]
            initial = escape_text(item["name"][0])
            result.innerHTML = (
                '<div class="nickname-card">'
                f'<div class="name-monogram">{initial}</div>'
                '<div class="name-details">'
                f'<h2>{escape_text(item["name"])}</h2>'
                f'<span class="origin">{escape_text(item["origin"])}</span>'
                f'<p>{escape_text(item["meaning"])}</p>'
                '</div></div>'
            )
        else:
            result.innerHTML = '<div class="error-message"><strong>Name not found</strong><span>Try Kyle, Mia, Noah, or Sofia.</span></div>'

    document.getElementById("nicknameButton").addEventListener("click", check_nickname)
    nickname_input.addEventListener("keypress", lambda event: check_nickname() if event.key == "Enter" else None)
    for button in document.querySelectorAll(".quick-name"):
        button.addEventListener("click", lambda event, b=button: (setattr(nickname_input, "value", b.dataset.name), check_nickname()))

element_input = document.getElementById("elementInput")
if element_input:
    def check_element(*args):
        key = element_input.value.strip().lower()
        result = document.getElementById("elementResult")
        if key in elements:
            item = elements[key]
            result.innerHTML = (
                '<div class="element-card">'
                '<div class="element-symbol-box">'
                f'<strong>{escape_text(item["symbol"])}</strong><span>Atomic number {escape_text(item["number"])}</span>'
                '</div>'
                '<div class="element-details">'
                f'<h2>{escape_text(item["name"])}</h2>'
                f'<div class="element-property"><span>Atomic mass</span><strong>{escape_text(item["mass"])}</strong></div>'
                f'<div class="element-property"><span>Category</span><strong>{escape_text(item["group"])}</strong></div>'
                f'<div class="element-property"><span>Standard state</span><strong>{escape_text(item["state"])}</strong></div>'
                f'<div class="element-property"><span>Atomic number</span><strong>{escape_text(item["number"])}</strong></div>'
                '</div></div>'
            )
        else:
            result.innerHTML = '<div class="error-message"><strong>Element not found</strong><span>Try a name or symbol such as H or Oxygen.</span></div>'

    document.getElementById("elementButton").addEventListener("click", check_element)
    element_input.addEventListener("keypress", lambda event: check_element() if event.key == "Enter" else None)
    for button in document.querySelectorAll(".quick-element"):
        button.addEventListener("click", lambda event, b=button: (setattr(element_input, "value", b.dataset.element), check_element()))

club_select = document.getElementById("clubSelect")
if club_select:
    def render_clubs(*args):
        selected = club_select.value
        visible = members if selected == "all" else [member for member in members if member["club"] == selected]
        stats = document.getElementById("clubStats")
        grid = document.getElementById("clubGrid")
        stats.innerHTML = f"Showing {len(visible)} member{'s' if len(visible) != 1 else ''}"
        cards = []
        for member in visible:
            parts = member["name"].split()
            initials = "".join(part[0] for part in parts[:2]).upper()
            cards.append(
                '<article class="member-card">'
                f'<div class="member-avatar">{escape_text(initials)}</div>'
                '<div>'
                f'<h3>{escape_text(member["name"])}</h3>'
                f'<span>{escape_text(member["club"])}</span> &middot; '
                f'<span>{escape_text(member["role"])}</span>'
                '</div></article>'
            )
        grid.innerHTML = "".join(cards)

    club_select.addEventListener("change", render_clubs)
    render_clubs()
