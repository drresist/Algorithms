from collections import deque

graph = {}

graph["you"] = [ "alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search_queue = deque() # Очередь
search_queue += graph["you"] # добавляем соседей в очередь


def person_is_seller(name):
    return name[-1] == 'm'



def search(name):
    search_queue = deque()

    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person is searched:
            if person_is_seller(person):
                print(F"{person} is seller")
            else:
                search_queue += graph[person]
                searched.append(person)


search('you')
