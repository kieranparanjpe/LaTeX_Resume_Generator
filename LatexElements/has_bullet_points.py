from abc import ABC, abstractmethod


class HasBulletPoints(ABC):
    @abstractmethod
    def update_bullet_points(self, *bullet_points: str):
        pass
