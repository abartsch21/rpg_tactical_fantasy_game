import pygame as pg
from lxml import etree

from src.constants import TILE_SIZE


class Entity:
    def __init__(self, name, pos, sprite):
        self.name = name
        self.pos = pos
        self.sprite = pg.transform.scale(pg.image.load(sprite).convert_alpha(), (TILE_SIZE, TILE_SIZE))

    def display(self, screen):
        screen.blit(self.sprite, self.pos)

    def get_pos(self):
        return self.pos

    def set_pos(self, pos):
        self.pos = pos

    def get_rect(self):
        return self.sprite.get_rect(topleft=self.pos)

    def get_name(self):
        return self.name

    def get_formatted_name(self):
        return self.name.replace('_', ' ').title()

    def get_max_moves(self):
        return 0

    def get_sprite(self):
        return self.sprite

    def is_on_pos(self, pos):
        return self.get_rect().collidepoint(pos)

    def save(self):
        # Build XML tree
        tree = etree.Element('entity')

        # Save name
        name = etree.SubElement(tree, 'name')
        name.text = self.name

        # Save position
        pos = etree.SubElement(tree, 'position')
        x = etree.SubElement(pos, 'x')
        x.text = str(self.pos[0] // TILE_SIZE)
        y = etree.SubElement(pos, 'y')
        y.text = str(self.pos[1] // TILE_SIZE)

        return tree

