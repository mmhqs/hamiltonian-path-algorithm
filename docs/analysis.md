## Complexity analysis

### Classes P, NP, NP-Complete, and NP-Hard
The Hamiltonian Path problem is classified as NP-Complete. A problem is NP-Complete if it satisfies two conditions:

- It is in NP (Nondeterministic Polynomial time): a problem is in the NP class if a candidate solution (a "certificate") can be verified in polynomial time.
- It is NP-Hard: a problem is NP-Hard if it is "at least as hard as" any problem in NP.

NP-Complete problems are considered the "hardest" problems within the NP class. The Traveling Salesperson Problem (TSP), for example, is a generalization of the Hamiltonian Path/Cycle problem, and this relationship is key to understanding its difficulty. Because the NP-Complete Hamiltonian problem can be solved using a TSP algorithm, it proves that the TSP is NP-Hard. It is at least as difficult as the Hamiltonian problem.

### Analysis of asymptotic time complexity
The time complexity is `O(V * V!)` (fatorial complexity), where `V` is the number of vertices.This was determined by Recursion Tree Analysis (not the Master Theorem).
- `O(V!)`: the recursive backtracking function, in the worst case (a complete graph).
- `O(V * ...)`: the main function runs this `O(V!)` algorithm once for every possible starting vertex (`V` times in total).

### Application of the Master Theorem
The Master Theorem **cannot be applied to the Hamiltonian Path algorithm**. The Master Theorem is a specific tool used only for analyzing divide-and-conquer algorithms whose runtime recurrence fits the precise formula:

`T(n) = a * T(n/b) + f(n)`

This formula requires:
- `a`: constant number of subproblems.
- `b`: each subproblem must be a fractional size of the original.

The Hamiltonian Path algorithm fails to meet these criteria for two main reasons:

1. **Subproblem Size (Subtractive vs. Divisive)**: the algorithm is a backtracking search, not a divide-and-conquer one. It reduces the problem by a constant amount (one vertex), not a fraction.
2. **Number of subproblems (Not constant)**: the number of recursive calls (`a`) is not constant. It depends on the number of unvisited neighbors for the current vertex, which can be different at every step of the execution.

In summary, the Master Theorem is the wrong tool because this algorithm's complexity is defined by a state-space search tree, not by a divide-and-conquer recurrence.

### Analysis of complexity cases
- Best case: `O(V)` (Linear): the algorithm finds the path on its first attempt with zero backtracking (e.g., in a simple line graph 0-1-2-3). Performance is extremely fast.
- Worst case: `O(V * V!)` (Factorial): the algorithm must explore all (or nearly all) possible path permutations. This happens when no path exists, or in a highly-connected (complete) graph, forcing it to try every `V` starting node and backtrack extensively. Performance is slow.
- Average case (Exponential): the algorithm does some backtracking but cuts off many dead-end search branches. It is faster than the worst-case but still too slow for large graphs. Performance is highly dependent on the graph's structure.