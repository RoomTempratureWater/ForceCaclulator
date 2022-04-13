import numpy as np
import math as mt
import matplotlib.pyplot as plt

def Res_unknown(raw_inp, show_plot=True):


    force_vectors = []
    unit_vectors = []
    magnitude_vectors = []
    raw = []
    for i in raw_inp:
        mag = i[0]
        direc = i[1]
        raw.append([mag, direc])
        direc = mt.radians(direc)
        unit_vectors.append([mt.cos(direc), mt.sin(direc)])
        magnitude_vectors.append([mag])
        force_vectors.append([mag*mt.cos(direc),mag*mt.sin(direc)])

    unit_vectors = np.array(unit_vectors)
    magnitude_vectors = np.array(magnitude_vectors)



    res = np.dot(unit_vectors.T,magnitude_vectors)
    force_vectors = np.array(force_vectors)

    resdirec = mt.atan(res[1][0]/res[0][0])
    resmag = res[0][0]/mt.cos(resdirec)
#    print('--------------------\n')
#    print("Resultant force: {}".format(resmag))
#    print("Resultant Direc: {}".format(mt.degrees(resdirec)))
#    print('\n--------------------\n')

    if show_plot == True:

        M = force_vectors


        rows,cols = M.T.shape

        #Get absolute maxes for axis ranges to center origin
        #This is optional
        maxes = 1.1*np.amax(abs(M), axis = 0)

        for i,l in enumerate(range(0,cols)):
            xs = M[i,0]
            ys = M[i,1]
            plt.arrow(0,0,xs,ys,color="b",label="Force{}".format(i+1))
            plt.annotate("{}N, {} deg".format(raw[i][0], raw[i][1]),[M[i,0],M[i,1]])
        plt.arrow(0,0,res[0][0],res[1][0],color="r",label='Resultant')
        plt.annotate("{}N, {} deg".format(resmag, mt.degrees(resdirec)), [res[0][0],res[1][0]])
        plt.plot(0,0,'ok') #<-- plot a black point at the origin
        plt.axis('equal')  #<-- set the axes to the same scale
        plt.xlim([-maxes[0],maxes[0]]) #<-- set the x axis limits
        plt.ylim([-maxes[1],maxes[1]]) #<-- set the y axis limits
        plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left",
                   mode="expand", borderaxespad=0, ncol=3)
        plt.grid(b=True, which='major')  # <-- plot grid lines
        plt.autoscale()
        fig = plt.gcf()
        fig.set_size_inches(10, 8)
        fig.savefig("plots/temp/tempplot.jpeg", dpi=1000, bbox_inches='tight')
        plt.show()

    return [resmag,mt.degrees(resdirec)]

#for resultant known and magnitude of forces wanted
def Res_known(raw_inp, show_plot=True):
    force_vectors = []
    unit_vectors = []
    magnitude_vectors = []
    raw = []
    resmag = 0
    resdirec = 0
    resvec = []
    mag = 0
    truex, truey = 0,0
    direc = 0

    for i, j in enumerate(raw_inp):
        if i == 0:
            resumag = j[0]
            resudirec = j[1]
            truex = resumag * mt.cos(mt.radians(resudirec))
            truey = resumag * mt.sin(mt.radians(resudirec))
            resvec.append([truex, truey])
        else:
            mag = j[0]
            direc = j[1]
            raw.append([mag , mt.degrees(direc)])
        unit_vectors.append([mt.cos(direc), mt.sin(direc)])
        magnitude_vectors.append([mag])
        force_vectors.append([mag*mt.cos(direc),mag*mt.sin(direc)])

    unit_vectors = np.array(unit_vectors)
    magnitude_vectors = np.array(magnitude_vectors)

    res = np.dot(unit_vectors.T, magnitude_vectors)
    force_vectors = np.array(force_vectors)
    resvec = np.array(resvec)
    req = np.subtract(resvec,res.T)

    force_vectors = np.append(resvec.T, force_vectors.T, axis=1)

    resdirec = (mt.atan(req[0][1] / req[0][0]))
    resmag = req[0][0] / mt.cos(resdirec)

#    print('--------------------\n')
#    print("Required force: {}".format(resmag))
#    print("Required force Direc: {}".format(resdirec))
#    print('\n--------------------\n')
    if show_plot == True:

        M = force_vectors.T


        rows,cols = M.T.shape

        #Get absolute maxes for axis ranges to center origin
        #This is optional
        maxes = 1.1*np.amax(abs(M), axis = 0)
        for i,l in enumerate(range(0,cols)):
            xs = M[i,0]
            ys = M[i,1]
            if i == 0:
                xs = -M[i, 0]
                ys = M[i, 1]
                plt.arrow(0, 0, truex, truey,color="g",label="Resultant")
                plt.annotate("{}N, {} deg".format(resumag, resudirec), [truex, truey])
            elif i == 1:
                continue
            else:
                plt.arrow(0, 0, xs, ys, color="b", label="Force {}".format(str(i)))
                plt.annotate("{}N, {} deg".format(raw[i-2][0], raw[i-2][1]), [xs, ys])

        plt.arrow(0, 0, req[0,0], req[0,1], color="r",label='Required Force')
        plt.annotate("{}N, {} deg".format(resmag, mt.degrees(resdirec)), [req[0][0], req[0][1]])
        plt.plot(0,0,'ok') #<-- plot a black point at the origin
        plt.axis('equal')  #<-- set the axes to the same scale
        plt.xlim([-maxes[0],maxes[0]]) #<-- set the x axis limits
        plt.ylim([-maxes[1],maxes[1]]) #<-- set the y axis limits
        plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left",
                   mode="expand", borderaxespad=0, ncol=3)
        plt.grid(b=True, which='major') #<-- plot grid lines
        plt.autoscale()
        fig = plt.gcf()
        fig.set_size_inches(10, 8)
        fig.savefig("plots/temp/tempplot.jpeg", dpi=1000, bbox_inches='tight')
        plt.show()

    return [resmag, mt.degrees(resdirec)]

