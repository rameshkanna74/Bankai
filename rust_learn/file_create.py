import os

# Define the topics and their respective notebook names
structure = {
    "Graph General": [
        "89-Number-of-Islands.ipynb",
        "90-Surrounded-Regions.ipynb",
        "91-Clone-Graph.ipynb",
        "92-Evaluate-Division.ipynb",
        "93-Course-Schedule.ipynb",
        "94-Course-Schedule-II.ipynb",
    ],
    "Graph BFS": [
        "95-Snakes-and-Ladders.ipynb",
        "96-Minimum-Genetic-Mutation.ipynb",
        "97-Word-Ladder.ipynb",
    ],
    "Trie": [
        "98-Implement-Trie-(Prefix-Tree).ipynb",
        "99-Design-Add-and-Search-Words-Data-Structure.ipynb",
        "100-Word-Search-II.ipynb",
    ],
    "Backtracking": [
        "101-Letter-Combinations-of-a-Phone-Number.ipynb",
        "102-Combinations.ipynb",
        "103-Permutations.ipynb",
        "104-Combination-Sum.ipynb",
        "105-N-Queens-II.ipynb",
        "106-Generate-Parentheses.ipynb",
        "107-Word-Search.ipynb",
    ],
    "Divide & Conquer": [
        "108-Convert-Sorted-Array-to-Binary-Search-Tree.ipynb",
        "109-Sort-List.ipynb",
        "110-Construct-Quad-Tree.ipynb",
        "111-Merge-k-Sorted-Lists.ipynb",
    ],
    "Kadane's Algorithm": [
        "112-Maximum-Subarray.ipynb",
        "113-Maximum-Sum-Circular-Subarray.ipynb",
    ],
    "Binary Search": [
        "114-Search-Insert-Position.ipynb",
        "115-Search-a-2D-Matrix.ipynb",
        "116-Find-Peak-Element.ipynb",
        "117-Search-in-Rotated-Sorted-Array.ipynb",
        "118-Find-First-and-Last-Position-of-Element-in-Sorted-Array.ipynb",
        "119-Find-Minimum-in-Rotated-Sorted-Array.ipynb",
        "120-Median-of-Two-Sorted-Arrays.ipynb",
    ],
    "Heap": [
        "121-Kth-Largest-Element-in-an-Array.ipynb",
        "122-IPO.ipynb",
        "123-Find-K-Pairs-with-Smallest-Sums.ipynb",
        "124-Find-Median-from-Data-Stream.ipynb",
    ],
    "Bit Manipulation": [
        "125-Add-Binary.ipynb",
        "126-Reverse-Bits.ipynb",
        "127-Number-of-1-Bits.ipynb",
        "128-Single-Number.ipynb",
        "129-Single-Number-II.ipynb",
        "130-Bitwise-AND-of-Numbers-Range.ipynb",
    ],
    "Math": [
        "131-Palindrome-Number.ipynb",
        "132-Plus-One.ipynb",
        "133-Factorial-Trailing-Zeroes.ipynb",
        "134-Sqrt(x).ipynb",
        "135-Pow(x,n).ipynb",
        "136-Max-Points-on-a-Line.ipynb",
    ],
    "1D DP": [
        "137-Climbing-Stairs.ipynb",
        "138-House-Robber.ipynb",
        "139-Word-Break.ipynb",
        "140-Coin-Change.ipynb",
        "141-Longest-Increasing-Subsequence.ipynb",
    ],
    "Multidimensional DP": [
        "142-Triangle.ipynb",
        "143-Minimum-Path-Sum.ipynb",
        "144-Unique-Paths-II.ipynb",
        "145-Longest-Palindromic-Substring.ipynb",
        "146-Interleaving-String.ipynb",
        "147-Edit-Distance.ipynb",
        "148-Best-Time-to-Buy-and-Sell-Stock-III.ipynb",
        "149-Best-Time-to-Buy-and-Sell-Stock-IV.ipynb",
        "150-Maximal-Square.ipynb",
    ],
}

# Create directories and files
for topic, notebooks in structure.items():
    # Create the topic folder
    os.makedirs(topic, exist_ok=True)
    for notebook in notebooks:
        # Create the .ipynb file in the corresponding folder
        file_path = os.path.join(topic, notebook)
        with open(file_path, 'w') as f:
            f.write('{"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 4}')  # Basic notebook structure

print("Folders and notebooks created successfully!")
