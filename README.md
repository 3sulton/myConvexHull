# myConvexHull Library
> Sebuah pustaka dalam bahasa Python yang dapat mengembalikan convex hull dari kumpulan data 2 dimensi.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- Himpunan titik pada bidang planar disebut convex jika untuk sembarang dua titik pada bidang tersebut, seluruh segmen garis yang berakhir di dua titik berada pada himpunan tersebut.
- Pustaka ini bertujuan untuk mencari garis penghubung titik titik sehingga membentuk convex hull.


## Technologies Used
- Python - version 3.9.1


## Features

- `myConvexHull.simplices` mengembalikan list yang berisikan garis pembentuk convex hull.


## Setup
Agar dapat menjalankan test diperlukan
- Pandas - version 1.4.1
- Matplotlib - version 3.5.1
- Sklearn - version 1.0.2
- Scipy - version 1.8.0
- Jupyter Notebook atau Jupyter Extension jika kamu menggunakan Visual Studio Code

Instalasi library pendukung pada CMD ketik

```
    pip install pandas
    pip install matplotlib
    pip insall sklearn
    pip install scipy
```

Instalasi Jupiter Notebook di [sini](https://jupyter.org/install), sedangkan Jupiter Extension for Visual Studio Code di [sini](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)



## Usage
- clone repository github ini dengan mengetikkan di CMD

```
git clone https://github.com/3sulton/myConvexHull.git
```
- akan muncul folder myConvexHull. Arahkan path pada cmd ke dalam folder tersebut dengan menuliskan `cd myConvexHull`

Instalasi Pustaka myConvexHull
```
    pip install ./dist/myConvexHull-0.1.0-py3-none-any.whl
```

Terdapat file test_myConvexHull.ipynb sebagai contoh penggunaan pustaka ini yang dapat dijalankan dengan menggunakan Jupyter Notebook

## Project Status
Project is: _complete_


## Acknowledgements
Give credit here.
- Pustaka ini dibuat untuk memenuhi Tugas Kecil 2 IF2211 Strategi Algoritma
- Proyek ini didasarkan pada tutorial [ini](https://codecrucks.com/convex-hull-using-divide-and-conquer/) untuk pendekatan divide and conquer dan tutorial [ini](https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f) untuk pembuatan pustaka bahasa Python
- Many thanks to Pak Rinaldi Munir selaku pengajar K03 IF2211 Strategi Algoritma


## Contact
Created by [@3sulton](https://www.github.com/3sulton) - 13520033 / Tri Sulton Adila
