import maze_env
from algorithms.dfs import dfs
from algorithms.bfs import bfs
from algorithms.aStar import aStar
from algorithms.valIteration import valIteration
from algorithms.polIteration import polIteration


def main():
    maze = maze_env.MazeEnv(maze_size=(10, 10), mode="plus")
    maze.render()

    input(" - Press enter to see DFS")
    maze.reset()
    dfs(maze)
    input(" - Press enter to see BFS")
    maze.reset()
    bfs(maze)
    input(" - Press enter to see A*")
    maze.reset()
    aStar(maze)
    input(" - Press enter to see MDP Value Iteration")
    maze.reset()
    valIteration(maze)
    input(" - Press enter to see MDP Policy Iteration")
    maze.reset()
    polIteration(maze)
    input("press enter to quit")

main()
