from collections import deque
import time

def load_words_from_file(file_path):
    """Load English words from a text file."""
    with open(file_path, 'r') as file:
        words = set(word.strip().lower() for word in file)
    return words

def is_valid_word(word, word_set):
    """Check if a word is valid (exists in the dictionary)."""
    return word.lower() in word_set

def get_neighbors(word, word_set):
    """Generate valid neighbors of a word by changing one letter."""
    neighbors = []
    for i in range(len(word)):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if char != word[i]:
                new_word = word[:i] + char + word[i+1:]
                if is_valid_word(new_word, word_set):
                    neighbors.append(new_word)
    return neighbors

def build_graph(words):
    """Build a graph where each word is a node and edges connect words that differ by one letter."""
    graph = {}
    for word in words:
        graph[word] = get_neighbors(word, words)
    return graph

def breadth_first_search(graph, start, target):
    """Perform breadth-first search to find the shortest path from start to target."""
    if start == target:
        return [start], 0

    frontier = deque([(start, [start])])  # Queue of (node, path) pairs
    explored = set()
    steps = 0

    while frontier:
        current_word, path = frontier.popleft()
        explored.add(current_word)

        for neighbor in graph[current_word]:
            steps += 1
            if neighbor == target:
                return path + [neighbor], steps  # Found the target word, return the path and steps
            if neighbor not in explored:
                frontier.append((neighbor, path + [neighbor]))

    return None, steps  # Target word not reachable

def print_shortest_path(graph, start, target):
    """Print the shortest path from start to target."""
    path, steps = breadth_first_search(graph, start, target)
    if path:
        print("Shortest path from", start, "to", target, ":")
        print(" -> ".join(path))
        print("Number of steps:", steps)
    else:
        print("No path found from", start, "to", target)

def check_length(start, target):
    """Check if the length of start and target words are the same."""
    return len(start) == len(target)

# Load English words from the text file
english_words = load_words_from_file('english_words.txt')

# Get initial and target words from the terminal input
initial_word = input("Enter the initial word: ").strip().lower()
target_word = input("Enter the target word: ").strip().lower()

# Check if the length of initial and target words are the same
if not check_length(initial_word, target_word):
    print("Initial and target words must have the same length.")
else:
    # Build the graph
    graph = build_graph(english_words)

    # Measure the runtime of the search algorithm
    start_time = time.time()
    # Print the shortest path and number of steps
    print_shortest_path(graph, initial_word, target_word)
    end_time = time.time()
    print("Runtime:", end_time - start_time, "seconds")