from collections import deque

#TODO: update to is ask for the data file name at run
def main():
    print('\n\n========  Assigment 3  ========\n\n')
    print("\n\n")

    graph_mk = map('Magic_Kingdom.txt')
    print(f'Magic Kingdom: \n{graph_mk}')


    graph_hollywood_studios = map("hollywood studios.txt")
    print(graph_hollywood_studios)

    print('\n\n')
    #print(bfs(graph_mk))
    print(bfs(graph_hollywood_studios))



def map(data_file):
    with open(data_file, 'r') as file:
        first_line = file.readline().strip().split(',')
        first_line_key = first_line[0].replace(',', '').lower()
        first_line_values = []
        for line in first_line[1:]:
            first_line_values.append(line.lower().strip())
        connections = {first_line_key: first_line_values}

        remaining_lines = file.readlines()[0:]
        for lines in remaining_lines:
            route = lines.split(',')
            key = route[0].replace(',', '').lower()
            values = []
            for value in route[1:]:
                values.append(value.replace('\n', '').strip().lower())
            connections[key] = values

    return connections

def bfs(graph):
    start = ''
    end = ''
    while start not in graph or end not in graph:
        start = input("Where should the search START?: ").lower()
        end = input("Where should the search END?: ").lower()
        if start not in graph:
            print("Sorry, that location is not in the graph, please input a new starting point. ")
            start = input("Where should the search START?: ").lower()

        if end not in graph:
            print("Sorry, that location is not in the graph, please input a new ending point. ")
            end = input("Where should the search END?: ").lower()

    # list of nodes we've visited
    visited = []
    # creates queue with the starting node
    queue = deque([start])

    # Currently just checking that we are viewing all the nodes in the path
    # while queue.popleft() != end:
    while queue:
        #print(f'The current queue: {queue}\n')

        # gets the first element in the queue
        node = queue.popleft()
        #print(f'The current node: {node}\n')


        # if you reached the end, ends the while loop
        if node == end:
            visited.append(node)
            return visited


        # node not in the visited list, append the node
        if node not in visited:
            visited.append(node)


        # loop through for the specific node
        for i in graph[node]:
            #print(f'the current item: {i}\n')
            #if the elements in that current node is not in visited, append it to the queue
            if i not in visited:
                queue.append(i)



    # return the list of nodes we visited
    return visited

if __name__ == "__main__":
    main()