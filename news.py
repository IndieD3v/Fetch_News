import requests
import pyfiglet # pip install pyfiglet


print("""       \n
                Choose Category-

                1] buisness
                2] entertainment
                3] general
                4] health              
                5] technology 
                \n
""")


choose_category = int(input("Enter the number of category >> "))
category = ''

# ALL INPUT CHECKING

if choose_category == 1:
    category = 'buisness'
elif choose_category == 2:
    category = 'entertainment'
elif choose_category == 3:
    category = 'general'
elif choose_category == 4:
    category = 'health'   
elif choose_category == 5:
    category = 'technology'

# API FUNCTION
def main():

    api_key = 'YOUR API'

    # URL TO FETCH DATA
    URL = f'https://newsapi.org/v2/everything?q={category}&apiKey={api_key}'

    res = requests.get(URL)
    data = res.json() # DATA IN JSON


    for items in range(10):
        # ITERATING FROM THE LIST

        author = data['articles'][items]['author']
        title = data['articles'][items]['title']
        description = data['articles'][items]['description']

        print(pyfiglet.figlet_format(author))
        
        print(f'TITLE- \n {title} \n')
        print(f'DESCRIPTION- \n {description} \n')


main()