import os
import pygame

from utils.resource_loader import import_folder
from random import choice


class AnimationPlayer:
    def __init__(self):

        self.frames = {
            # Spells
            'flame': import_folder(os.path.join('graphics',
                                                'particles',
                                                'flame',
                                                'frames')),

            'aura': import_folder(os.path.join('graphics',
                                               'particles',
                                               'aura')),

            'heal': import_folder(os.path.join('graphics',
                                               'particles',
                                               'heal',
                                               'frames')),

            # Attacks
            'claw': import_folder(os.path.join('graphics',
                                               'particles',
                                               'claw')),

            'slash': import_folder(os.path.join('graphics',
                                                'particles',
                                                'slash')),

            'sparkle': import_folder(os.path.join('graphics',
                                                  'particles',
                                                  'sparkle')),

            'leaf_attack': import_folder(os.path.join('graphics',
                                                      'particles',
                                                      'leaf_attack')),
            'thunder': import_folder(os.path.join('graphics',
                                                  'particles',
                                                  'thunder')),

            # Monster Deaths
            'squid': import_folder(os.path.join('graphics',
                                                'particles',
                                                'smoke_orange')),

            'raccoon': import_folder(os.path.join('graphics',
                                                  'particles',
                                                  'raccoon')),

            'spirit': import_folder(os.path.join('graphics',
                                                 'particles',
                                                 'nova')),

            'bamboo': import_folder(os.path.join('graphics',
                                                 'particles',
                                                 'bamboo')),

            # Leafs
            'leaf': (
                import_folder(os.path.join('graphics',
                                           'particles',
                                           'leaf1')),

                import_folder(os.path.join('graphics',
                                           'particles',
                                           'leaf2')),

                import_folder(os.path.join('graphics',
                                           'particles',
                                           'leaf3')),

                import_folder(os.path.join('graphics',
                                           'particles',
                                           'leaf4')),

                import_folder(os.path.join('graphics',
                                           'particles',
                                           'leaf5')),

                import_folder(os.path.join('graphics',
                                           'particles',
                                           'leaf6')),

                self.reflect_images(
                    import_folder(os.path.join('graphics',
                                               'particles',
                                               'leaf1'))),

                self.reflect_images(
                    import_folder(os.path.join('graphics',
                                               'particles',
                                               'leaf2'))),

                self.reflect_images(
                    import_folder(
                        os.path.join('graphics',
                                     'particles',
                                     'leaf3'))),

                self.reflect_images(
                    import_folder(
                        os.path.join('graphics',
                                     'particles',
                                     'leaf4'))),

                self.reflect_images(
                    import_folder(
                        os.path.join('graphics',
                                     'particles',
                                     'leaf5'))),

                self.reflect_images(
                    import_folder(
                        os.path.join('graphics',
                                     'particles',
                                     'leaf6')))
            )
        }

    def reflect_images(self, frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames

    def create_grass_particles(self, position, groups):
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(position, animation_frames, groups)

    def generate_particles(self, animation_type, position, groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(position, animation_frames, groups)


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, position, animation_frames, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=position)
        self.sprite_type = 'magic'

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()
