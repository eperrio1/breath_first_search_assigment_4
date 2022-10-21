from collections import deque

def main():
    print('\n\n========  Breadth-first search  ========\n\n')

    again = True

    while again == True:
        file = input("Select data file: Magic Kingdom.txt or Hollywood Studios.txt: ")
        while file != "Magic Kingdom.txt" and file != "Hollywood Studios.txt":
            file = input("Select data file: Magic Kingdom.txt or Hollywood Studios.txt: ")

        graph = map(file)

        print(f'Map: {graph}')
        print(bfs(graph))

        again = (input('Would you like to fine another path? Yes or No: ').lower())
        if again == "no":
            again = False
        if again == "yes":
            again = True



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
        if start not in graph:
            print("Sorry, that location is not in the graph, please input a new starting point. ")
            start = input("Where should the search START?: ").lower()

        if end not in graph:
            print("Sorry, that location is not in the graph, please input a new ending point. ")
            end = input("Where should the search END?: ").lower()

    # list of nodes we've seen
    seen = []
    # creates queue with the starting node
    queue = deque([start])

    # Currently just checking that we are viewing all the nodes in the path
    while queue:
        # gets the first element in the queue
        node = queue.popleft()
        # if you reached the end, ends the while loop
        if node == end:
            seen.append(node)
            return seen
        # node not in the seen list, append the node
        if node not in seen:
            seen.append(node)
        # loop through for the specific node
        for i in graph[node]:
            #if the elements in that current node is not in seen, append it to the queue
            if i not in seen:
                queue.append(i)

    # return the list of nodes we seen
    return seen

if __name__ == "__main__":
    main()