from collections import deque

#TODO: update to is ask for the data file name at run
def main():
    print('\n\n========  Assigment 3  ========\n\n')
    print("\n\n")
    graph_mk = map('Magic_Kingdom.txt')
    print(f'Magic Kingdom: \n{graph_mk}')
    graph_epcot = map('Epcot.txt')
    print(f'Epcot: \n{graph_epcot}')

    print('\n\n')
    print(bfs(graph_mk))


#TODO: Figure out why there is a space before the values in the dictionary
# Is this converting graph to a map?
def map(data_file):
    with open(data_file, 'r') as file:
        first_line = file.readline().strip().split(',')
        first_line_key = first_line[0].replace(',', '').lower()
        first_line_values = []
        for line in first_line[1:]:
            first_line_values.append(line.lower())
        connections = {first_line_key: first_line_values}

        remaining_lines = file.readlines()[0:]
        for lines in remaining_lines:
            route = lines.split(',')
            key = route[0].replace(',', '').lower()
            values = []
            for value in route[1:]:
                values.append(value.replace('\n', '').lower())
            connections[key] = values

    return connections


# ask for start and end
# look at start
    # look at the attached nodes
    # add the nodes to the queue
    # add the start node to a list

    # pop the queue and then look at the next node
    # if the nodes are not already in the queue
        # queue the attacked nodes
    # add the current node to the list


def bfs(graph):
    start = ''
    end = ''
    while start not in graph and end not in graph:
        start = input("Where should the search START?: ")
        end = input("Where should the seach END?: ")
        if start not in graph:
            print("Sorry, that location is not in the graph, please input a new starting point. ")
            start = input("Where should the search START?: ")
        if end not in graph:
            print("Sorry, that location is not in the graph, please input a new ending point. ")
            end = input("Where should the search END?: ")

    # list of nodes we've visited
    visited = []
    # creates queue with the starting node
    queue = deque([start])

    # Currently just checking that we are viewing all the nodes in the path
    while queue != end:
        # gets the first element in the queue
        node = queue.popleft()
        # node not in the visited list, append the node
        if node not in visited:
            visited.append(node)
        # loop through for the specific node
        for i in graph[node]:
            #if the elements in that current node is not in visited, append it to the queue
            if i not in visited:
                queue.append(i)
    # retund the list of nodes we visited
    return visited

if __name__ == "__main__":
    main()