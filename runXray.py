import os
import sys
import numpy as np
import SimpleITK as sitk
from gvxrPython3 import gvxr
import matplotlib.pyplot as plt


def runSim(patientNumber):
    inputMeshPath = f"input_files\\pacient_{patientNumber}\\stl\\pacient{patientNumber}PanevMesh.stl"
    inputPinPath = f"input_files\\pacient_{patientNumber}\\stl\\pacient{patientNumber}Zavadec.stl"

    gvxr.createOpenGLContext()

    # configure x-ray source
    gvxr.setSourcePosition(0., -1000., 0., "mm")
    gvxr.usePointSource()
    # gvxr.addFilter("Al", 1., "mm")
    # gvxr.addFilter("Cu", 0.1, "mm")
    gvxr.setMonoChromatic(80., "keV", 1000)

    # configure detector/output image
    gvxr.setDetectorPosition(0., 0., 0., "mm")
    gvxr.setDetectorUpVector(0, 0, -1)
    gvxr.setDetectorNumberOfPixels(1000, 1000)
    gvxr.setDetectorPixelSize(0.4, 0.4, "mm")
    #gvxr.setDetectorPixelSize(0.3048, 0.3048, "mm")
    # gvxr.setScintillator("CsI", 600, "um")

    # load mesh files
    gvxr.loadMeshFile("panev", inputMeshPath, "mm")
    gvxr.loadMeshFile("drat", inputPinPath, "mm")

    # set material properties of meshes
    gvxr.moveToCenter()
    gvxr.translateNode("panev", 0, -100, 0, "mm")
    gvxr.translateNode("drat", 0, -100, 0, "mm")
    # gvxr.setMixture("panev", [1, 6, 7, 8, 11, 12, 15, 16, 20],
    #                 [0.034, 0.155, 0.042, 0.435, 0.001, 0.002, 0.103, 0.003, 0.225])
    gvxr.setCompound("panev", "HCNONaMgPSCa")
    # gvxr.setCompound("panev", "Ca10(PO4)6(OH)2")
    gvxr.setDensity("panev", 1.920, "g/cm3")
    gvxr.setCompound("drat", "FeCrNi")
    gvxr.setDensity("drat", 8., "g/cm3") # 316L medical grade stainless steel density

    # compute x-ray image
    xrayImage = np.array(gvxr.computeXRayImage()).astype(np.float32)

    # flat-field correction
    totalEnergyInMeV = gvxr.getTotalEnergyWithDetectorResponse()
    white = np.ones(xrayImage.shape) * totalEnergyInMeV
    dark = np.zeros(xrayImage.shape)
    xrayImageFlat = (xrayImage - dark) / (white - dark)

    # convert grayscale values with log LUT
    xrayImageFlipped = -np.log(np.fliplr(xrayImageFlat))
    xraySitkImage = sitk.GetImageFromArray(xrayImageFlipped)
    xraySitkImage.SetOrigin((0., 0.))

    print(xraySitkImage.GetOrigin(), xraySitkImage.GetDirection(),
          xraySitkImage.GetSpacing(), xraySitkImage.GetSize())
    plt.imshow(xrayImageFlipped, cmap="gray")
    plt.axis("off")
    plt.show()
    
    # outputImagePath = os.path.join(os.getcwd(),
    #                                f"input_files\\pacient_{patientNumber}\\registration\\"
    #                                f"pacient{patientNumber}Preop.mha")
    # sitk.WriteImage(xraySitkImage, outputImagePath)
    gvxr.renderLoop()


if __name__ == "__main__":
    patienNum = sys.argv[1]
    # viewAngle = sys.argv[2]
    runSim(patienNum)