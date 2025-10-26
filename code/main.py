class Graph:
    """
    Classe para representar um grafo (orientado ou não orientado)
    usando uma lista de adjacência.
    """

    def __init__(self, num_vertices, directed=False):
        self.V = num_vertices
        self.directed = directed
        # Dicionário para armazenar a lista de adjacência
        self.graph = {i: [] for i in range(self.V)}

    def add_edge(self, u, v):
        """Adiciona uma aresta entre os vértices u e v."""
        if 0 <= u < self.V and 0 <= v < self.V:
            self.graph[u].append(v)

            if not self.directed:
                self.graph[v].append(u)
        else:
            print(
                f"Erro: Vértices {u} ou {v} estão fora do intervalo [0, {self.V-1}]")

    def _solve_hamiltonian_util(self, current_v, path, visited):
        """
        Função auxiliar recursiva (backtracking) para encontrar o caminho.
        """
        # Caso base: Se o caminho contém todos os vértices, encontramos
        # um Caminho Hamiltoniano.
        if len(path) == self.V:
            return True

        # Itera sobre todos os vizinhos do vértice atual
        for neighbor in self.graph[current_v]:
            # Se o vizinho ainda não foi visitado
            if neighbor not in visited:
                # 1. Escolha: Adiciona o vizinho ao caminho
                path.append(neighbor)
                visited.add(neighbor)

                # 2. Explore: Chama recursivamente a partir do vizinho
                if self._solve_hamiltonian_util(neighbor, path, visited):
                    return True  # Solução encontrada

                # 3. Retroceda (Backtrack): Se a exploração falhou,
                # remove o vizinho para tentar outro caminho.
                visited.remove(neighbor)
                path.pop()

        # Se nenhum vizinho levou a uma solução a partir deste vértice
        return False

    def find_hamiltonian_path(self):
        """
        Tenta encontrar um Caminho Hamiltoniano no grafo.
        Retorna o caminho (lista) se encontrado, ou None se não existir.
        """
        for start_node in range(self.V):
            path = [start_node]
            visited = {start_node}

            if self._solve_hamiltonian_util(start_node, path, visited):
                return path

        return None


# --- Exemplos de Uso ---
print("--- Exemplo 1: Grafo NÃO orientado (Possui caminho) ---")
g1 = Graph(5, directed=False)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
g1.add_edge(3, 4)
g1.add_edge(1, 3)
g1.add_edge(1, 4)

path1 = g1.find_hamiltonian_path()
if path1:
    print(f"Caminho Hamiltoniano encontrado: {path1}")
else:
    print("Nenhum Caminho Hamiltoniano encontrado.")


print("\n--- Exemplo 2: Grafo Orientado (Possui caminho) ---")
g2 = Graph(4, directed=True)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
g2.add_edge(3, 0)
g2.add_edge(1, 3)

path2 = g2.find_hamiltonian_path()
if path2:
    print(f"Caminho Hamiltoniano encontrado: {path2}")
else:
    print("Nenhum Caminho Hamiltoniano encontrado.")


print("\n--- Exemplo 3: Grafo NÃO Orientado (NÃO possui caminho) ---")
g3 = Graph(6, directed=False)
g3.add_edge(0, 1)
g3.add_edge(1, 2)
g3.add_edge(2, 0)
g3.add_edge(3, 4)
g3.add_edge(4, 5)
g3.add_edge(5, 3)
g3.add_edge(2, 3)

path3 = g3.find_hamiltonian_path()
if path3:
    print(f"Caminho Hamiltoniano encontrado: {path3}")
else:
    print("Nenhum Caminho Hamiltoniano encontrado.")
