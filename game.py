import pygame
from pytmx.util_pygame import load_pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

pygame.init()
ds = pygame.display.set_mode((1280, 720))
tmx_data = load_pygame("assets/data/tmx/basic.tmx")
sprite_group = pygame.sprite.Group()

# cycle through all layers
for layer in tmx_data.visible_layers:
    # if layer.name in ('Floor', 'Plants and rocks', 'Pipes'):
    if hasattr(layer, 'data'):
        for x, y, surf in layer.tiles():
            pos = (x * 128, y * 128)
            Tile(pos = pos, surf = surf, groups = sprite_group)

for obj in tmx_data.objects:
    pos = obj.x, obj.y
    if obj.type in ('Building', 'Vegetation'):
        Tile(pos = pos, surf = obj.image, groups = sprite_group)




# # get all layers
# print(tmx_data.layers)

# # get visible layers
# for layer in tmx_data.visible_layers:
#     print(layer)

# # get layer names
# print(tmx_data.layernames)

# # get layer by name
# print(tmx_data.get_layer_by_name('Ground'))

# # get object groups
# for obj in tmx_data.objectgroups: # get object layers
#     print(obj)

# get tiles
# layer = tmx_data.get_layer_by_name('Floor')
# for x,y,surf in layer.tiles(): # get all the information
#     print(x * 128)
#     print(y * 128)
#     print(surf)

# print(layer.data)
# print(layer.id)

# get objects
# object_layer = tmx_data.get_layer_by_name('objects')
# for obj in object_layer:
#     print(obj)

# for obj in tmx_data.objects:
#     # print(obj.x)
#     # print(obj.y)
#     # print(obj.image)

#     print(obj.type)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    ds.fill("black")
    sprite_group.draw(ds)
        
    for obj in tmx_data.objects:
        pos = obj.x, obj.y
        if obj.type == 'Shape':
            if obj.name == 'Marker':
                pygame.draw.circle(ds, 'red', (obj.x, obj.y), 5)

            if obj.name == 'Rectangle':
                rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                pygame.draw.rect(ds, 'yellow', rect)

            if obj.name == 'Ellipse':
                rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                pygame.draw.ellipse(ds, 'blue', rect)

            if obj.name == 'Polygon':
                points = [(point.x, point.y) for point in obj.points]
                pygame.draw.polygon(ds, 'green', points)




    pygame.display.update()

pygame.quit()