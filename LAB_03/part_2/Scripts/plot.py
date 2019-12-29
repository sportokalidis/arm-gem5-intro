import matplotlib.pyplot as plt


########################################################### SPECBZIP #####################################################################

bzip_x = ['file 1', 'file 2', 'file 3', 'file 4', 'file 5']

area_y = [51, 52, 30, 1521, 41]
peak_power_y = [9.49383, 10.2015, 9.5333, 18.0372, 13.591]
EDAP_y = [854, 894, 501, 3634, 3677]

# plot area
plt.xlabel('file')
plt.ylabel('area (mm^2)')
plt.title('BZIP')
# plt.ylim(1.4, 1.77)
plt.bar(bzip_x, area_y)
plt.show()

# plot peak power
plt.xlabel('file')
plt.ylabel('peak_power (Watt)')
plt.title('BZIP')
# plt.ylim(1.4, 1.77)
plt.bar(bzip_x, peak_power_y)
plt.show()

# plot EDAP
plt.xlabel('file')
plt.ylabel('EDAP')
plt.title('BZIP')
# plt.ylim(1.4, 1.77)
plt.bar(bzip_x, EDAP_y)
plt.show()

########################################################### SPECHMMER #####################################################################

hmmer_x = ['file 1', 'file 2', 'file 4', 'file 5']

area_y = [50, 52, 35, 35]
peak_power_y = [9.91251 , 11.0655 , 11.0655 , 13.591]
EDAP_y = [677, 370, 666, 1343]


# plot area
plt.xlabel('file')
plt.ylabel('area (mm^2)')
plt.title('HMMER')
# plt.ylim(1.4, 1.77)
plt.bar(hmmer_x, area_y)
plt.show()

# plot peak power
plt.xlabel('file')
plt.ylabel('peak_power (Watt)')
plt.title('HMMER')
# plt.ylim(1.4, 1.77)
plt.bar(hmmer_x, peak_power_y)
plt.show()

# plot EDAP
plt.xlabel('file')
plt.ylabel('EDAP')
plt.title('HMMER')
# plt.ylim(1.4, 1.77)
plt.bar(hmmer_x, EDAP_y)
plt.show()

########################################################### SPECLIBM #####################################################################

libm_x = ['file 1', 'file 4', 'file 5', 'file 6']

area_y = [26, 99, 98, 99]
peak_power_y = [8.04241 , 31.5029 , 31.035 , 13.591]
EDAP_y = [677, 370, 666, 1343]


# plot area
plt.xlabel('file')
plt.ylabel('area (mm^2)')
plt.title('LIBM')
# plt.ylim(1.4, 1.77)
plt.bar(libm_x, area_y)
plt.show()

# plot peak power
plt.xlabel('file')
plt.ylabel('peak_power (Watt)')
plt.title('LIBM')
# plt.ylim(1.4, 1.77)
plt.bar(libm_x, peak_power_y)
plt.show()

# plot EDAP
plt.xlabel('file')
plt.ylabel('EDAP')
plt.title('LIBM')
# plt.ylim(1.4, 1.77)
plt.bar(libm_x, EDAP_y)
plt.show()

########################################################### SPECMCF #####################################################################

mcf_x = ['file 1', 'file 3', 'file 4', 'file 5']

area_y = [8, 35, 41, 38]
peak_power_y = [13.7281 , 11 , 13.5 , 13.591]
EDAP_y = [47, 638, 1885, 1748]


# plot area
plt.xlabel('file')
plt.ylabel('area (mm^2)')
plt.title('MCF')
# plt.ylim(1.4, 1.77)
plt.bar(mcf_x, area_y)
plt.show()

# plot peak power
plt.xlabel('file')
plt.ylabel('peak_power (Watt)')
plt.title('MCF')
# plt.ylim(1.4, 1.77)
plt.bar(mcf_x, peak_power_y)
plt.show()

# plot EDAP
plt.xlabel('file')
plt.ylabel('EDAP')
plt.title('MCF')
# plt.ylim(1.4, 1.77)
plt.bar(mcf_x, EDAP_y)
plt.show()



########################################################### SPECSJENG #####################################################################

jeng_x = ['file 2', 'file 5', 'file 8']

area_y = [26, 26, 29]
peak_power_y = [8.04241 , 8.7 , 10.3]
EDAP_y = [3738, 4695, 15153]


# plot area
plt.xlabel('file')
plt.ylabel('area (mm^2)')
plt.title('SPECSJENG')
# plt.ylim(1.4, 1.77)
plt.bar(jeng_x, area_y)
plt.show()

# plot peak power
plt.xlabel('file')
plt.ylabel('peak_power (Watt)')
plt.title('SPECSJENG')
# plt.ylim(1.4, 1.77)
plt.bar(jeng_x, peak_power_y)
plt.show()

# plot EDAP
plt.xlabel('file')
plt.ylabel('EDAP')
plt.title('SPECSJENG')
# plt.ylim(1.4, 1.77)
plt.bar(jeng_x, EDAP_y)
plt.show()
