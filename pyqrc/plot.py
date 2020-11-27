from __future__ import print_function, absolute_import
import numpy as np
import matplotlib.pyplot as plt
import os


# Read data from an output file
class getoutData:
    def __init__(self, file):
        self.TERMINATION = None
        self.SPENERGY = None
        if not os.path.exists(file):
            print(("\nFATAL ERROR: Output file [ %s ] does not exist" % file))

        def getJOBTYPE(self, outlines, format):
            if format == "Gaussian":
                level = "none"
                bs = "none"
                for i in range(0, len(outlines)):
                    if outlines[i].strip().find('----------') > -1:
                        if outlines[i + 1].strip().find('#') > -1:
                            self.JOBTYPE = outlines[i + 1].strip().split('#')[1]
                            break

        def getTERMINATION(self, outlines, format):
            if format == "Gaussian":
                for i in range(0, len(outlines)):
                    if outlines[i].find("Normal termination") > -1:
                        self.TERMINATION = "normal"

        def getSPenergy(self, outlines, format):
            if format == "Gaussian":
                for i in range(0, len(outlines)):
                    if outlines[i].find("SCF Done:") > -1:
                        self.SPENERGY = float(outlines[i].split()[4])

        outfile = open(file, "r")
        outlines = outfile.readlines()
        getJOBTYPE(self, outlines, "Gaussian")
        getTERMINATION(self, outlines, "Gaussian")

        if self.TERMINATION != "normal":
            print("Wrong Termination!!")

        getSPenergy(self, outlines, "Gaussian")
        outfile.close()


def main():
    _path = "/home/lhes30412/TTA/Code/NDIC2/No13/631Gdp/freq_scan/mode_5/"
    energies = []

    for i in range(20, 0, -1):
        file = _path + "minus/" + str(i) + "/output.log"
        _sp = getoutData(file)
        energies.append(_sp.SPENERGY * 27.2107)

    for i in range(1, 21):
        file = _path + "positive/" + str(i) + "/output.log"
        _sp = getoutData(file)
        energies.append(_sp.SPENERGY * 27.2107)

    Q_points = np.linspace(-2, 2, 40, endpoint=True)

    fig = plt.figure()
    plt.plot(Q_points, energies, 'o-')
    plt.title("NDIC2_13 PES along normal mode 5")
    plt.ylabel("Energy (eV)")
    plt.xlabel("Q")
    plt.show()


if __name__ == "__main__":
    main()
