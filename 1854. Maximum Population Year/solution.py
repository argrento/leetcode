class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = collections.defaultdict(int)
        
        for (birth_year, death_year) in logs:
            for year in range(birth_year, death_year):
                population[year] += 1
                
        return max(sorted(population), key=population.get)
