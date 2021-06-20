import matplotlib.pyplot as plt

# names of the assemblers
flye = "Flye"
canu = "Canu"
masurca = "MaSuRCA"

# data

# nga50 values for the assemblers
nga50_f = [6349]
nga50_c = [2870]
nga50_m = [3812]
# reference percentage values for the assemblers
ref_perc_f = [99.70]
ref_perc_c = [99.49]
ref_perc_m = [99.84]
# misassemblies values for the assemblers
misassemblies_f = [879]
misassemblies_c = [1200]
misassemblies_m = [1500]
# reference coverage
ref_cov_f = [96.4]
ref_cov_c = [95.4]
ref_cov_m = [95.1]


# define colors
red = "#bf616a"
grey = "#434c5e"
light_grey = "#d8dee9"

fig, (ax1, ax2, ax3,ax4) = plt.subplots(1, 4)
#fig.suptitle('Comparison of Assemblers for Human Genome', fontsize = 14)

ax1.bar(flye, nga50_f, color = red, label = flye)
ax1.bar(canu, nga50_c, color = grey, label = canu)
ax1.bar(masurca, nga50_m, color = light_grey, label = masurca)
ax1.set_title("NGA50")
ax1.legend()
ax1.xaxis.set_ticklabels([])

ax2.bar(flye, ref_perc_f, color = red)
ax2.bar(canu, ref_perc_c, color = grey)
ax2.bar(masurca, ref_perc_m, color = light_grey)
ax2.set_ylim([99, 99.9999])
ax2.set_title("Reference identity %")
ax2.xaxis.set_ticklabels([])

ax3.bar(flye, ref_cov_f, color = red)
ax3.bar(canu, ref_cov_c, color = grey)
ax3.bar(masurca, ref_cov_m, color = light_grey)
ax3.set_title("Reference coverage %")
ax3.set_ylim([94, 97.999])
ax3.xaxis.set_ticklabels([])

ax4.bar(flye, misassemblies_f, color = red)
ax4.bar(canu, misassemblies_c, color = grey)
ax4.bar(masurca, misassemblies_m, color = light_grey)
ax4.set_title("Misassemblies")
ax4.xaxis.set_ticklabels([])


fig.set_size_inches(15, 9)
plt.savefig("presentation/images/results_HUMAN.png")
plt.savefig("poster/images/results_HUMAN.png")
