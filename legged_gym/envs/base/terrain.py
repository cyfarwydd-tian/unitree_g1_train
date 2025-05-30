# legged_gym/envs/g1/terrain.py
import torch
from isaacgym import gymapi

class SimpleStairTerrain:
    def __init__(self, gym, sim, stair_height=0.25, stair_width=0.5, stair_depth=0.3, num_steps=1):
        self.gym = gym
        self.sim = sim
        self.stair_height = stair_height
        self.stair_width = stair_width
        self.stair_depth = stair_depth
        self.num_steps = num_steps
        self.terrain_bodies = []

    def create(self, env_origin):
        for i in range(self.num_steps):
            stair_pose = gymapi.Transform()
            stair_pose.p.x = env_origin[0] + (i + 1) * self.stair_depth
            stair_pose.p.y = env_origin[1]
            stair_pose.p.z = env_origin[2] + (i + 1) * self.stair_height / 2.0  # z是中心高

            stair_asset = self.gym.create_box(
                self.sim,
                self.stair_depth,
                self.stair_width,
                self.stair_height,
                gymapi.AssetOptions()
            )

            stair_actor = self.gym.create_actor(
                self.sim, stair_asset, stair_pose, f"stair_{i}", i + 1, 0, 0
            )

            self.terrain_bodies.append(stair_actor)
