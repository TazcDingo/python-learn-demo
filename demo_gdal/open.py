"""这块主要学习gdal打开文件并读取信息的方法"""
from osgeo import gdal

data_path = "path/to/xxx.tiff"
dataset = gdal.Open(data_path, gdal.GA_ReadOnly)

print("Driver: {}/{}".format(dataset.GetDriver().ShortName,
                            dataset.GetDriver().LongName))
print("Size is {} x {} x {}".format(dataset.RasterXSize,
                                    dataset.RasterYSize,
                                    dataset.RasterCount))
print("Projection is {}".format(dataset.GetProjection()))
geotransform = dataset.GetGeoTransform()
if geotransform:
    print("Origin = ({}, {})".format(geotransform[0], geotransform[3]))
    print("Pixel Size = ({}, {})".format(geotransform[1], geotransform[5]))
band = dataset.GetRasterBand(1)
print("Band Type={}".format(gdal.GetDataTypeName(band.DataType)))

min_band = band.GetMinimum()
max_band = band.GetMaximum()
if not min_band or not max_band:
    (min_band, max_band) = band.ComputeRasterMinMax(True)
print("Min={:.3f}, Max={:.3f}".format(min_band, max_band))

if band.GetOverviewCount() > 0:
    print("Band has {} overviews".format(band.GetOverviewCount()))

if band.GetRasterColorTable():
    print("Band has a color table with {} entries".format(band.GetRasterColorTable().GetCount()))

print(gdal.__version__)
dataset = None
