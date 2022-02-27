class myConvexHull:
    """
    Instantiate a convex hull from a given set of points.
    """

    EPSILON = 1e-10

    def __init__(self, ndarray):
        self.simplices = [] # himpunan solusi yang nantinya berisi garis dari dua titik pembentuk convex hull
        self.array = ndarray.tolist()
        self.array.sort() # convert array to sorted list
        self.convex_hull()

    def convex_hull(self):
        """
        I.S. : himpunan solusi masih kosong
        Proses: mencari titik pembentuk convex hull
        F.S. : himpunan solusi berisi garis dari dua titik pembentuk convex hull
        """
        # dua titik ekstrem terkiri dan terkanan misalkan A dan B
        left_point = self.array[0]
        right_point = self.array[len(self.array) - 1]
        # masukkan garis AB dan BA ke dalam himpunan solusi
        self.simplices.append([left_point, right_point])
        self.simplices.append([right_point, left_point])
        # membagi array menjadi dua partisi yang berisi titik yang berada di kiri dan kanan garis AB dan BA
        left_partition = self.partisi(left_point, right_point, self.array)
        right_partition = self.partisi(right_point, left_point, self.array)
        # cari titik pembentuk convex hull dari setiap partisi
        self.find_hull(left_partition, left_point, right_point)
        self.find_hull(right_partition, right_point, left_point)

    def find_hull(self, array, pangkal, ujung):
        """
        I.S. : array berisi titik yang berada di kiri / atas garis relatif terhadap pangkal dan ujungnya misalkan pangkal A dan ujung B
        Proses: mencari titik terjauh dari garis relatif tersebut misalkan titik terjauh C lalu garis AC dan CB ditambahkan ke himpunan solusi
                lalu melakukan partisi untuk titik yang berada pada kiri garis AC dan CB, pencarian convex hull selanjutnya
                dilakukan dengan rekursif untuk setiap partisi
        F.S. : himpunan solusi telah berisi semua garis pembentuk convex hull

        :param array: titik titik yang berada di kiri / atas garis relatif terhadap pangkal dan ujungnya
        :param pangkal: titik pangkal garis
        :param ujung: titik ujung garis
        """
        if(len(array) == 0):    # base case, titik C sebelum pemanggilan fungsi ini merupakan titik pembentuk convex hull terakhir pada partisi
            return
        else:
            # titik terjauh dari garis relatif tersebut misalkan C
            farrest_point = self.farrest_point(array, pangkal, ujung)
            # ganti garis AB dengan AC dan CB
            self.simplices = [x for x in self.simplices if x != [pangkal, ujung]]
            self.simplices.append([pangkal, farrest_point]) # garis AC
            self.simplices.append([farrest_point, ujung])   # garis CB
            # hapus titik C sebelum di partisi karena sudah merupakan titik pembentuk convex hull
            array = [x for x in array if x != farrest_point]
            # partisi array
            left_partition = self.partisi(pangkal, farrest_point, array) # titik titik di kiri garis AC
            right_partition = self.partisi(farrest_point, ujung, array) # titik titik di kanan garis BC atau di kiri CB
            # rekursif untuk setiap partisi
            self.find_hull(left_partition, pangkal, farrest_point)
            self.find_hull(right_partition, farrest_point, ujung)

    def farrest_point(self, array, p1, p2):
        """
        :param array: array 2 dimensi berisi banyak titik
        :param p1: titik p1
        :param p2: titik p2
        :return: titik terjauh yang berada di array dari garis p1p2
        """
        max_distance = 0
        farrest_point = None
        for p in array:
            d = self.distance(p, p1, p2)
            if(d > max_distance):
                max_distance = d
                farrest_point = p
        return farrest_point

    def partisi(self, pangkal, ujung, array):
        """
        :param pangkal: titik pangkal garis misalkan A
        :param ujung: titik ujung garis misalkan B
        :param array: array 2 dimensi berisi banyak titik di antara garis AB

        mengembalikan array 2 dimensi yang berisi titik yang berada di kiri / atas garis relatif terhadap AB
        """
        partition_array = []
        for i in range(len(array)):
            det = self.determinant(pangkal, ujung, array[i])
            if(det > 0 and abs(det) > self.EPSILON):
                partition_array.append(array[i])
        return partition_array

    def distance(self, p0, p1, p2):
        """
        return distance from p0 to line formed by p1 and p2
        """
        X = 0
        Y = 1  
        return abs((p2[X] - p1[X]) * (p1[Y] - p0[Y]) - (p1[X] - p0[X]) * (p2[Y] - p1[Y])) / (((p2[X] - p1[X]) ** 2 + (p2[Y] - p1[Y]) ** 2) ** 0.5)

    def determinant(self, p1, p2, p3):
        """
        :param p1: array 2 dimensi
        :param p2: array 2 dimensi
        :param p3: array 2 dimensi
        :return: determinant
        """
        X = 0
        Y = 1
        return (p1[X] * p2[Y] + p2[X] * p3[Y] + p3[X] * p1[Y]) - (p1[Y] * p2[X] + p2[Y] * p3[X] + p3[Y] * p1[X])