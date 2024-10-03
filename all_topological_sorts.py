def all_topological_sorts(jobs, dependencies):
    # Create a graph using a dictionary
    graph = {job: [] for job in jobs}
    indegree = {job: 0 for job in jobs}

    for u, v in dependencies:
        graph[u].append(v)
        indegree[v] += 1

    # To keep track of visited nodes and results
    visited = set()
    result = []

    def backtrack():
        # If the result size is equal to the number of jobs, we found a valid sort
        if len(result) == len(jobs):
            print(result[:])  # Print a copy of the result
            return

        # Try all nodes with zero indegree
        for job in jobs:
            if job not in visited and indegree[job] == 0:
                # Mark the job as visited
                visited.add(job)
                result.append(job)

                # Decrease the indegree of neighbors
                for neighbor in graph[job]:
                    indegree[neighbor] -= 1

                # Recur to find the next job
                backtrack()

                # Backtrack
                visited.remove(job)
                result.pop()

                # Restore the indegree of neighbors
                for neighbor in graph[job]:
                    indegree[neighbor] += 1

    backtrack()

# Example usage
jobs = [1, 2, 3, 4]
dependencies = [[1, 2], [1, 3], [2, 3], [4, 2], [4, 3]]

all_topological_sorts(jobs, dependencies)
