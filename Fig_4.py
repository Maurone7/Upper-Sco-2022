import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

from Fig_1 import flux_list_2_87mm, flux_list_0_88mm_garrett, source_list_garrett

indices = []

#set thickness axis
plt.setp(ax.spines.values(), linewidth=2)

#avoid axis labels being cut
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

def index(flux_0_88, flux_2_87):
    return np.log(flux_0_88/flux_2_87)/np.log(2.87/0.88)

for i in range(len(flux_list_0_88mm_garrett)):
    indices.append(index(flux_list_0_88mm_garrett[i], flux_list_2_87mm[i]))

for x in range(len(indices)):
    print(source_list_garrett[x], indices[x])
# Creating dataset
a = indices

bins = []

for i in range(45):
    bins.append(1 + i/20)

# Creating histogram
fig, ax = plt.subplots(figsize=(10, 7))
ax.hist(a, bins=bins, ec='k', linewidth = 2, label='Upper Sco discs')

# Show plot
plt.ylabel("$Frequency$", fontsize=12), plt.xlabel(r"$\alpha_{obs}$", fontsize=12)
plt.grid()
plt.legend()
plt.savefig('Fig 4')
plt.show()