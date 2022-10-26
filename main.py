from collections import deque

def main():
    print('\n\n========  Breadth-First Search  ========\n\n')

    bool = True
    while bool == True:
        file = input("Select data file: Magic Kingdom.txt or Hollywood Studios.txt: ")
        while file != "Magic Kingdom.txt" and file != "Hollywood Studios.txt":
            file = input("Select data file: Magic Kingdom.txt or Hollywood Studios.txt: ")

        graph = map(file)

        print(f'\nList of nodes:\n{list_nodes(file)}\n ')
        print(f'\nThe path from start to finish:\n{bfs(graph)}\n')

        play_again = ''
        while play_again != "no" and play_again != "yes":
            play_again = (input('Would you like to find another path? Yes or No: ').lower())
            if play_again == "no":
                bool = False
            if play_again == "yes":
                bool = True

def list_nodes(data_file):
    with open(data_file, 'r') as file:
        nodes_list = []
        data = file.readlines()
        for line in data:
            line_list = line.strip().split(',')
            for node in line_list:
                node = node.strip()
                if node not in nodes_list:
                    nodes_list.append(node)
        return nodes_list


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


#TODO: Update so it keeps track of a clear path from start to finish

def bfs(graph):
    start = ''
    end = ''
    while start not in graph or end not in graph:
        start = input("Where should the search START?: ").lower()
        end = input("Where should the search END?: ").lower()
        while start not in graph:
            print("Sorry, that location is not in the graph, please input a new starting point. ")
            start = input("Where should the search START?: ").lower()
        while end not in graph:
            print("Sorry, that location is not in the graph, please input a new ending point. ")
            end = input("Where should the search END?: ").lower()



    # list of nodes we've seen
    seen = []

    # creates queue with the starting node
    queue = deque([start])

    # display the map of connections

    # Currently just checking that we are viewing all the nodes in the path
    while queue:
        # display the queue
        # gets the first element in the queue
        node = queue.popleft()
        print(f'The current node: {node}')



        # if you reached the end, ends the while loop
        if node == end:
            seen.append(node)
            return seen



        # node not in the seen list, append the node
        if node not in seen:
            seen.append(node)
            print(f'The current seen: {seen}')



        # loop through for the specific node
        for link in graph[node]:
            #print(f'The node attached to the current node: {graph[node]}')
            #print()

            #if the elements in that current node is not in seen, append it to the queue
            if link not in seen:
                queue.append(link)
                #print(f"The current queue: {queue}\n")


    return f'A path does not exist'




if __name__ == "__main__":
    main()