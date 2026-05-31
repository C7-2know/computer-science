class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for m in asteroids:
            if m>mass:
                return False
            mass+=m
        return True