

cdef int i, j, k, N

cdef _compute_descendant_matrix(o, cellLine, ligand):
    """communication from Steven Hill, June 2013
    # Simon Spencer (2012)
    # Adaptation of Warshall's algorithm for finding transitive closure of a
    # graph
    """
    path = o.edge_scores[cellLine][ligand].copy()
    N = o.valid_length[cellLine]
    for k in range(0,N):
        for i in range(0,N):
            for j in range(0,N):
                path[i][j] = max(path[i][j], min(path[i][k],path[k][j]))
    o.descendancy_matrices[cellLine][ligand] = path.copy()


def compute_descendant_matrix(o, cellLine, ligand):
    _compute_descendant_matrix(o, cellLine, ligand)


