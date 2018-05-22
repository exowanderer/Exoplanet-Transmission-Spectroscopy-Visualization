from pylab import *;ion()
from matplotlib.colors import Normalize

rcParams['figure.dpi'] = 300
rcParams['savefig.dpi'] = 300

# planet_spec_opt_waves, planet_spec_opt_spec = np.loadtxt('w6_1184_solarC,O_M,H0optical.txt').T
planet_spec_ir_waves , planet_spec_ir_spec  = np.loadtxt('w6_1184_solarC,O_M,H0IR.txt').T

wave_soss_min = 0.6
wave_soss_max = 2.8

# soss_waves_opt= (planet_spec_opt_waves>wave_soss_min) * (planet_spec_opt_waves<wave_soss_max)
soss_waves_ir = (planet_spec_ir_waves >wave_soss_min) * (planet_spec_ir_waves <wave_soss_max)

# planet_spec_opt_spec  = planet_spec_opt_spec[ soss_waves_opt]
# planet_spec_opt_waves = planet_spec_opt_waves[soss_waves_opt]

planet_spec_ir_spec   = planet_spec_ir_spec[  soss_waves_ir ]
planet_spec_ir_waves  = planet_spec_ir_waves[ soss_waves_ir ]

transpec_min = planet_spec_ir_spec.min() # min(planet_spec_opt_spec.min(), planet_spec_ir_spec.min())
transpec_max = planet_spec_ir_spec.max() # max(planet_spec_opt_spec.max(), planet_spec_ir_spec.max())

colormap = cm.BuPu #get_cmap('hsv')

# 0.0 works better for this colormap -- change depending on colormap
# 3.2 works better for this colormap -- change depending on colormap
norm     = Normalize(0.0, 3.2) 

# ax1 = fig.add_subplot(121)
# ax2 = fig.add_subplot(122)


fig = gcf()
clf()

left1, bottom1, width1, height1 = 0.025, 0.05, 0.450, 0.90
left2, bottom2, width2, height2 = 0.525, 0.1, 0.450, 0.85

ax1 = fig.add_axes([left1, bottom1, width1, height1])
ax2 = fig.add_axes([left2, bottom2, width2, height2])

ax2.plot(planet_spec_ir_waves , planet_spec_ir_spec , c='black', lw=2)
for tick in ax2.xaxis.get_major_ticks():
    tick.label.set_fontsize(0.0)
for tick in ax2.xaxis.get_minor_ticks():
    tick.label.set_fontsize(0.0)

ax2.set_ylabel('Fraction of Starlight Absorbed by Planet', )

k_ctr,k_height, k_width, k_bot = 0.78, 1e-5, 0.20, 0.0222
ax2.bar(k_ctr,k_height, k_width, k_bot, color='#880000')
ax2.annotate('K', xy=(k_ctr - 0.15*k_width, k_bot+2.5*k_height), color='#880000')

h2o_ctr, h2o_height, h2o_width, h2o_bot = 1.8, 1e-5, 1.45, 0.02245
ax2.bar(h2o_ctr, h2o_height, h2o_width, h2o_bot, color='#0000AA')
ax2.annotate('H$_2$O', xy=(h2o_ctr - 0.05*h2o_width, h2o_bot+2.5*h2o_height), color='#0000AA')

fig.suptitle('NIRISS Exoplanet Transmission Spectrum with Atmospheric Opacity Visualization', y=0.99)
ax2.annotate('Bluer',
            xy    = (planet_spec_ir_waves.mean(), planet_spec_ir_spec.mean()),  # wavelength, transit depth
            color = 'blue',
            textcoords='axes fraction',
            xytext= (-0.025, -0.04))#,  # fraction, fraction

ax2.annotate('', 
            xycoords='axes fraction', 
            textcoords='axes fraction', 
            xy=(0.85, -0.03), 
            xytext=(0.1, -0.03), 
            arrowprops=dict(arrowstyle="fancy", 
            facecolor='w'))
            
ax2.annotate('Redder',
            xy    = (planet_spec_ir_waves.mean(), planet_spec_ir_spec.mean()),  # wavelength, transit depth
            color = 'red',
            textcoords='axes fraction',
            xytext= (0.90, -0.04))#,  # fraction, fraction


ax2.annotate('Created by J. Fraine with Creative Inspiration from L. Kreidberg', 
            xycoords='axes fraction', 
            textcoords='axes fraction', 
            size  = 5,
            color='grey',
            xy=(0.85, -0.09), 
            xytext=(0.45, -0.09))

ax1.set_xlim(-1,1)
ax1.set_ylim(-1,1)
ax2.set_xlim(planet_spec_ir_waves.min(), planet_spec_ir_waves.max())
ax2.set_ylim(transpec_min*0.999, transpec_max*1.001)

ax1.set_xticks([])
ax1.set_yticks([])
ax2.set_xticks([])
ax2.set_yticks([])

ax1.annotate("Host Star",
            xy        = (.3,.7),  # x, y point
            xycoords  = 'data',
            xytext    = (-0.3,0.85), # x, y bubble
            textcoords= 'data',
            size      = 12, 
            va        = "center", 
            ha        = "center",
            bbox      = dict(boxstyle="round4", fc="w"),
            arrowprops= dict(#arrowstyle="-|>",
                             arrowstyle="fancy", 
                             connectionstyle="arc3,rad=-0.2",
                             relpos=(1., .5),
                             fc="w"), 
            )

ax1.annotate("Planet Atmosphere",
            xy        = (0.3,.225),  # x, y point
            xycoords  = 'data',
            xytext    = (-0.5,0.5), # x, y bubble
            textcoords= 'data',
            size      = 12, 
            va        = "center", 
            ha        = "center",
            bbox      = dict(boxstyle="round4", fc="w"),
            arrowprops= dict(#arrowstyle="-|>",
                             arrowstyle="fancy", 
                             connectionstyle="arc3,rad=-0.5",
                             relpos=(1., 0.5),
                             fc="w"), 
            )

ax1.annotate("Planet 'Core'",
            xy        = (0.00,-0.01),  # x, y point
            xycoords  = 'data',
            xytext    = (-0.6,0.1), # x, y bubble
            textcoords= 'data',
            size      = 12, 
            va        = "center", 
            ha        = "center",
            bbox      = dict(boxstyle="round4", fc="w"),
            arrowprops= dict(#arrowstyle="-|>",
                             arrowstyle="fancy", 
                             connectionstyle="arc3,rad=-0.3",
                             relpos=(1., 0.5),
                             fc="w"), 
            )

npts      = 1000
waves_use = linspace(wave_soss_min, wave_soss_max, npts)

plot_now  = False
save_now  = True

for kw, wave_now in enumerate(waves_use):
    tspec_now = planet_spec_ir_spec[abs(planet_spec_ir_waves - wave_now).argmin()]
    alpha_now = (tspec_now- transpec_min) / (transpec_max - transpec_min)* (0.75 - 0.25) + 0.25
    
    if len(ax1.collections) > 0:
        ax1.collections.pop()
        ax1.collections.pop()
        ax1.collections.pop()
    
    ax1.scatter(-2.75,-0.25, s=1.0e6, lw=0, alpha=1.0, c=wave_now,cmap=colormap, norm=norm)
    ax1.scatter( 0.25,-0.25, s=1.0e4, lw=0, c='black', alpha=1.0)
    ax1.scatter( 0.25,-0.25, s=2.0e4, lw=0, c='black', alpha=alpha_now)
    
    # ax2.plot(planet_spec_opt_waves, planet_spec_opt_spec, c='black')
    # ax2.plot(planet_spec_ir_waves , planet_spec_ir_spec , c='black')
    ax2.lines.pop() if len(ax2.lines) == 2 else None
    
    ax2.axvline(wave_now, color='black')
    
    plt.pause(1e-10) if plot_now else None
    
    i_str = '0'*(len(str(waves_use.size)) - len(str(kw))) + str(kw)
    
    fig.savefig('movie_saves/' + 'niriss_transmission_spec_example_hot_jupiter_'+i_str+'.png') if save_now else None

