
LISTING_INFORMATION = {'kategori' : {'tag' : 'a', 'class' : '._3YDLCj', 'get' : 'style'},
                           'nama_produk' : {'tag' : 'div', 'class' : '.attM6y'},
                           'deskripsi_produk' : {'tag' : 'div', 'class' : '._3yZnxJ'},
                           'nama_variasi1' : {'tag' : 'label', 'class' : '._2IW_UG', 'order' : 0},
                           'varian_variasi1' : {'tag' : 'div', 'class' : 'flex.items.center._2oeDUI', 'order' : 0},
                           'foto_variasi1' : {'tag' : 'div', 'class' : '._3Q7kBy._2GchKS', 'get' : 'style'},
                           'nama_variasi2' : {'tag' : 'div', 'class' : '_2IW_UG', 'order' : 1},
                           'varian_variasi2' : {'tag' : 'div', 'class' : 'flex.items.center._2oeDUI', 'order' : 1},
                           'harga' : {'tag' : 'div', 'class' : '._3e_UQT'},
                           'stok' : {'tag' : 'div', 'class' : '.flex.items.center._90fTvx'}}

for i in LISTING_INFORMATION:
    if 'class' and 'get' in LISTING_INFORMATION[i]:
        print(LISTING_INFORMATION[i]['class'] + " [" + LISTING_INFORMATION[i]['get'] + ']')
        print('{} : Ya'.format(i))
    else:
        print('{} : Tidak'.format(i))

import itertools
import os
d = 9
a = [1, 2, 3]
b = [3, 5, 6]
c = [6, 9, 8]

for i in itertools.product( [[1, 2, 3]], [1, 3],[[1]], [2, 4], repeat = 1):
    print(list(i))

print(os.cpu_count())
._3e_UQT
deselect_by_index(0)
'.flex.items-center._90fTvx'
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
your_element = WebDriverWait(your_driver, some_timeout,ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.ID, my_element_id)))