
# Getting data from a text box
from pyscript import display, document


def get_name(e):
    document.getElementById('div1').innerHTML = ''

    ict_candidates = [
        'arkin san agustin',
        'liam lao',
        'lara estrada',
        'denise villostas',
        'athena alfaro',
        'pocholo commanda'
    ]

    f_name = document.getElementById('f_name').value
    l_name = document.getElementById('l_name').value

    candidates = f_name.strip() + " " + l_name.strip()

    member_checker = candidates.lower() in ict_candidates

    display_message = ( f"Sorry, {candidates}, your name is not on the list.", f"Congratulations, {candidates}! You are now part of the ICT club.")

    display(display_message[member_checker], target="div1")
