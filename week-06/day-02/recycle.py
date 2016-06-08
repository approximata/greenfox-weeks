# def drawcanvas(self):
#     mapcoords = self.creatmapvalues()
#     size = 72
#     for i in range(len(mapcoords)):
#         if mapcoords[i]['type'] == 'floor':
#             self.canvas.create_image(mapcoords[i]['x'] * size, mapcoords[i]['y'] * size, anchor = NW, image = self.floor)
#         elif mapcoords[i]['type'] == 'wall':
#             self.canvas.create_image(mapcoords[i]['x'] * size, mapcoords[i]['y'] * size, anchor = NW, image = self.wall)
