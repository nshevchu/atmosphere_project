import numpy as np
import matplotlib.pyplot as plt

#кол-во точек по широте долготе высоте
nx = 360
ny = 180
nz = 100

#создаем массивы широт долгот высот
lonlist = np.linspace(0, 360, nx)
latlist = np.linspace(-90, 90, ny)
zlist = np.linspace(0, 100, nz)

#задаем пока рандомный массив
value = np.random.rand(nx, ny, nz)

#функция для поиска ближайшего расстояния до центра гауссианы)
def myfunc(lon, m_x):
    return min([(lon - m_x) ** 2, (m_x + (360 - lon)) ** 2, (lon + (360 - m_x)) ** 2])

#векторизуем эту функцию
nearest_sqlon = np.vectorize(myfunc)


# параметры для рассчета широты\долготы\высоты зная индекс
lon0=0
lat0=-90
lev0=0
dlon=1
dlat=1
dlev=1

# параметры гауссианы
sigma_x = 30
m_x = 30
sigma_y = 10
m_y = 45

#функция для рассчета двумерной гауссианы
def gaussian_2D(i, j, k):
    # рассчет широты долготы высоты по индексу
    lon=lon0+i*dlon
    lat=lat0+j*dlat
    lev=lev0+k*dlev

    # квадрат ближайшего расстояния от точки lon до центра гауссианы
    lonb=nearest_sqlon(lon,m_x)

    # собственно гауссиана
    gauss = 1/(2*np.pi*sigma_x*sigma_y)*np.exp((-1)*lonb/(2*sigma_x**2)-(lat-m_y)**2/(2*sigma_y**2))
    return gauss

#создание нампай массива из функции задавая размерность
value = np.fromfunction(gaussian_2D, (nx,ny,nz))

#функция для рассчета частных производных по координатам - пока в процессе
#hhh= np.gradient(value)
#print(hhh.shape)

# создание мешгрида для рисования контура
Y, X = np.meshgrid(latlist, lonlist)
#рисуем контур для первой высота
cont = plt.contourf(X, Y, value[:, :, 0])
#показываем
plt.show()

