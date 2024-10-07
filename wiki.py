import wikipediaapi
import time

user_agent = "wiki_game (masonwhispi@gmail.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")




#function to return list of links
def fetch_links(page):
    links_list = []
    links = page.links

    for title in links.keys():
        links_list.append(title)

    return links_list


def wikipedia_game_solver(start_page, target_page):
    fetch_links(page)
    links = fetch_links(start_page)
    
    for i in links_list():
        if links_list == "Minos":
            print("link found")
            


start_page = wiki.page("Ultrakill")
target_page = wiki.page("Minos")

#print(fetch_links(start_page))

