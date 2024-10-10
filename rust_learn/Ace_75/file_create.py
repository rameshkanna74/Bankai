import os

# Define the topics and their respective notebook names
structure = {
    "01_Array_or_String": [
        "01-Merge-Strings-Alternately.ipynb",
        "02-Greatest-Common-Divisor-of-Strings.ipynb",
        "03-Kids-With-the-Greatest-Number-of-Candies.ipynb",
        "04-Can-Place-Flowers.ipynb",
        "05-Reverse-Vowels-of-a-String.ipynb",
        "06-Reverse-Words-in-a-String.ipynb",
        "07-Product-of-Array-Except-Self.ipynb",
        "08-Increasing-Triplet-Subsequence.ipynb",
        "09-String-Compression.ipynb",
    ],
    "02_Two_Pointers": [
        "10-Move-Zeroes.ipynb",
        "11-Is-Subsequence.ipynb",
        "12-Container-With-Most-Water.ipynb",
        "13-Max-Number-of-K-Sum-Pairs.ipynb",
    ],
    "03_Sliding_Window": [
        "14-Maximum-Average-Subarray-I.ipynb",
        "15-Maximum-Number-of-Vowels-in-a-Substring-of-Given-Length.ipynb",
        "16-Max-Consecutive-Ones-III.ipynb",
        "17-Longest-Subarray-of-1's-After-Deleting-One-Element.ipynb",
    ],
    "04_Prefix_Sum": [
        "18-Find-the-Highest-Altitude.ipynb",
        "19-Find-Pivot-Index.ipynb",
    ],
    "05_Hash_Map_Set": [
        "20-Find-the-Difference-of-Two-Arrays.ipynb",
        "21-Unique-Number-of-Occurrences.ipynb",
        "22-Determine-if-Two-Strings-Are-Close.ipynb",
        "23-Equal-Row-and-Column-Pairs.ipynb",
    ],
    "06_Stack": [
        "24-Removing-Stars-From-a-String.ipynb",
        "25-Asteroid-Collision.ipynb",
        "26-Decode-String.ipynb",
    ],
    "07_Queue": [
        "27-Number-of-Recent-Calls.ipynb",
        "28-Dota2-Senate.ipynb",
    ],
    "08_Linked_List": [
        "29-Delete-the-Middle-Node-of-a-Linked-List.ipynb",
        "30-Odd-Even-Linked-List.ipynb",
        "31-Reverse-Linked-List.ipynb",
        "32-Maximum-Twin-Sum-of-a-Linked-List.ipynb",
    ],
    "09_Binary_Tree_DFS": [
        "33-Maximum-Depth-of-Binary-Tree.ipynb",
        "34-Leaf-Similar-Trees.ipynb",
        "35-Count-Good-Nodes-in-Binary-Tree.ipynb",
        "36-Path-Sum-III.ipynb",
        "37-Longest-ZigZag-Path-in-a-Binary-Tree.ipynb",
        "38-Lowest-Common-Ancestor-of-a-Binary-Tree.ipynb",
    ],
    "10_Binary_Tree_BFS": [
        "39-Binary-Tree-Right-Side-View.ipynb",
        "40-Maximum-Level-Sum-of-a-Binary-Tree.ipynb",
    ],
    "11_Binary_Search_Tree": [
        "41-Search-in-a-Binary-Search-Tree.ipynb",
        "42-Delete-Node-in-a-BST.ipynb",
    ],
    "12_Graphs_DFS": [
        "43-Keys-and-Rooms.ipynb",
        "44-Number-of-Provinces.ipynb",
        "45-Reorder-Routes-to-Make-All-Paths-Lead-to-the-City-Zero.ipynb",
        "46-Evaluate-Division.ipynb",
    ],
    "13_Graphs_BFS": [
        "47-Nearest-Exit-from-Entrance-in-Maze.ipynb",
        "48-Rotting-Oranges.ipynb",
    ],
    "14_Heap_Priority_Queue": [
        "49-Kth-Largest-Element-in-an-Array.ipynb",
        "50-Smallest-Number-in-Infinite-Set.ipynb",
        "51-Maximum-Subsequence-Score.ipynb",
        "52-Total-Cost-to-Hire-K-Workers.ipynb",
        "53-Binary-Search-Guess-Number-Higher-or-Lower.ipynb",
        "54-Successful-Pairs-of-Spells-and-Potions.ipynb",
        "55-Find-Peak-Element.ipynb",
        "56-Koko-Eating-Bananas.ipynb",
    ],
    "15_Backtracking": [
        "57-Letter-Combinations-of-a-Phone-Number.ipynb",
        "58-Combination-Sum-III.ipynb",
    ],
    "16_DP_1D": [
        "59-N-th-Tribonacci-Number.ipynb",
        "60-Min-Cost-Climbing-Stairs.ipynb",
        "61-House-Robber.ipynb",
        "62-Domino-and-Tromino-Tiling.ipynb",
    ],
    "17_DP_Multidimensional": [
        "63-Unique-Paths.ipynb",
        "64-Longest-Common-Subsequence.ipynb",
        "65-Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee.ipynb",
        "66-Edit-Distance.ipynb",
    ],
    "18_Bit_Manipulation": [
        "67-Counting-Bits.ipynb",
        "68-Single-Number.ipynb",
        "69-Minimum-Flips-to-Make-a-OR-b-Equal-to-c.ipynb",
    ],
    "19_Trie": [
        "70-Implement-Trie-(Prefix-Tree).ipynb",
        "71-Search-Suggestions-System.ipynb",
    ],
    "20_Intervals": [
        "72-Non-overlapping-Intervals.ipynb",
        "73-Minimum-Number-of-Arrows-to-Burst-Balloons.ipynb",
    ],
    "21_Monotonic_Stack": [
        "74-Daily-Temperatures.ipynb",
        "75-Online-Stock-Span.ipynb",
    ],
}

# Create directories and files
for topic, notebooks in structure.items():
    # Create the topic folder
    os.makedirs(topic, exist_ok=True)
    for notebook in notebooks:
        # Create the .ipynb file in the corresponding folder
        file_path = os.path.join(topic, notebook)
        with open(file_path, "w") as f:
            f.write(
                '{"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 4}'
            )  # Basic notebook structure

print("Folders and notebooks created successfully!")
