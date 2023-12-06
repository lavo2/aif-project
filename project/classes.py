from utils import random_nsteps, actions_from_path, wrong_actions, path_from_actions, is_wall, valid_actions_bitmap, count_loops
from gen_utils import fitness_function

class Map:
    def __init__(self, map, start, target):
        self.map = map
        self.start = start
        self.target = target
        # generate a matrix with the same size of the map where each cell is 1 if it is a wall and 0 otherwise
        self.map_matrix = [[1 if is_wall(cell) else 0 for cell in row] for row in self.map]

    def __str__(self):
        return f'Map: {self.map}\nStart: {self.start}\nTarget: {self.target}'

class Path:
    def __init__(self, path, game_map, start, target):
        if path is None:
            self.path = random_nsteps(game_map, start, target)
        self.path = path
        self.game_map = game_map
        self.start = start
        self.target = target
        self.actions = actions_from_path(self.start, self.path) # cosa succede se il path ha due posizioni uguali di fila?
    
    def __str__(self):
        return f'Path: {self.path}\nActions: {self.actions}'

class Individual:
    def __init__(self, actions, generation: int, map: Map):
        self.actions = actions
        self.generation = generation
        self.path= path_from_actions(map.map, map.start, self.actions)
        self.wrong_actions = wrong_actions(self.path)
        self.fitness = fitness_function(self.path, self.generation, map)
        self.valid_actions_bitmap = valid_actions_bitmap(map.start, self.path)
        self.loops = count_loops(self.path)

    def __str__(self):
        return f'{self.path}\nFitness: {self.fitness}\nGeneration: {self.generation}\nWrong actions: {self.wrong_actions}'

    def __repr__(self):
        return self.__str__()

