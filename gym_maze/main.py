import maze_env

def main(): 
    maze = maze_env.MazeEnv(maze_size=(10,10))
    maze.render()

    # max = 10
    # for m in range(max):
    #     maze.step("E")
    #     print(maze.maze_size[0])
    #     print(maze.maze_view)
    #     maze.render()
    #     max -= 1

    maze.hop(5,5)
    maze.render()

    input("press enter to quit")

main()