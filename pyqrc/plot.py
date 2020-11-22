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
            if format == "Gaussian:":
                for i in range(0, len(outlines)):
                    if outlines[i].find("SCF Done") > -1:
                        print("Found SCF Results!!")
                        self.SPENERGY = outlines[i].split()[3]

        outfile = open(file, "r")
        outlines = outfile.readlines()
        getJOBTYPE(self, outlines, "Gaussian")
        getTERMINATION(self, outlines, "Gaussian")

        if self.TERMINATION != "normal":
            print("Wrong Termination!!")

        getSPenergy(self, outlines, "Gaussian")


def main():
    _path = "/home/lhes30412/TTA/Code/NDIC2/No15/631Gdp/B3LYP-D3BJ/freq_scan/mode_5/minus/"
    energies = []

    for i in range(1, 21):
        print("No " + str(i) + ":")
        file = _path + str(i) + "/output.log"
        _sp = getoutData(file)
        energies.append(_sp.SPENERGY)
        print()

    _path = "/home/lhes30412/TTA/Code/NDIC2/No15/631Gdp/B3LYP-D3BJ/freq_scan/mode_5/positive/"

    for i in range(1, 21):
        file = _path + str(i) + "/output.log"
        print("No" + str(i+20) + ":")
        _sp = getoutData(file)
        energies.append(_sp.SPENERGY)
        print()

    print(energies)


if __name__ == "__main__":
    main()
