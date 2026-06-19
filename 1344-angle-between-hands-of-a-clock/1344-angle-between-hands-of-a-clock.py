class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle=(hour%12)*30+(minutes/60)*30
        min_angle=minutes*6
        bn_angle=abs(hour_angle-min_angle)
        return min(bn_angle, 360-bn_angle)