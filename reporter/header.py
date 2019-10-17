# Import modules
import datetime
import locale

def create_header(authors_list, city="Paris"):
    """ Creates the header text.
    
    Params
    ------
    authors_list: a list of dict
        Each dictionary should contain a "first" and "last".
    city: str, optional, default "Paris"
        City where the report is emitted
        
    Returns
    -------
    header_text : str
        The header text
    
    """
    
    if(city == ''):
        print ("Merci d'indiquer une ville en paramètre de la fonction")
    
    # On va chercher la data du jour
    date_string = datetime.date.today()
    # On set l'environnement en FR ou EN    
    if(city == 'Paris'):
        locale.setlocale(locale.LC_ALL, 'fr_FR')
    elif(city == 'New York'):
        locale.setlocale(locale.LC_ALL, 'en_EN')
    else:
        locale.setlocale(locale.LC_ALL, 'fr_FR')
        
    # On set les valeurs voulues pour la data référence ici : https://docs.python.org/fr/3/library/datetime.html)
    date_string = date_string.strftime("%A %d %B %Y")
    author_strings = [f'{city}, {date_string} \n', '### Authors', '\n']

    for author in authors_list:
        # Methode get pour le dictionnaire recommandée
        firstname = author.get("first", "")
        lastname = author.get("last", "")
        
#         try:
#             lastname = author["last"]
#         except KeyError:
#             print(f'Champ "lastname" manquant pour "{firstname}"\n')
#             lastname = ""
        # bonne syntaxe de formatage : on met le f avant la chaine et on met les variables entre { }
    
        author_string = f'- {firstname} {lastname}'
        author_strings.append(author_string)
        
    # join ajoute des \n - dans cet exemple - entre chaque élément de la liste et transforme en une chaine de caractères
    return '\n'.join(author_strings)