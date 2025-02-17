import yt
# Load a dataset
ds = yt.load('output_00001/info_00001.txt')
print(ds)
# This is to make a slice plot and a projection plot
#p = yt.SlicePlot(ds, 'z', 'density')
#p.save()  # save it as a png

# Do a projection plot (actually integrate over the l.o.s.)
#p = yt.ProjectionPlot(ds, 'z', 'density', weight_field='ones')
#p.save()  # save it as a png