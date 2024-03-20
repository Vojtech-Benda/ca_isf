import os
import sys
import numpy as np
import SimpleITK as sitk
from gvxrPython3 import gvxr
from gvxrPython3.utils import plotScreenshot
import matplotlib.pyplot as plt

def runSim(patientNumber, view):
    inputMeshPath = f"input_files\\pacient_{patientNumber}\\stl\\pacient{patientNumber}PanevMesh.stl"
    inputPinPath = f"input_files\\pacient_{patientNumber}\\stl\\pacient{patientNumber}Zavadec.stl"

    gvxr.createOpenGLContext()
    gvxr.setSourcePosition(0., -1000., 0., "mm")
    gvxr.usePointSource()
    gvxr.addFilter("Al", 1., "mm")
    gvxr.addFilter("Cu", 0.1, "mm")

    gvxr.setMonoChromatic(80., "keV", 1000)
    gvxr.setDetectorPosition(0., -100., 0., "mm")
    gvxr.setDetectorUpVector(0, 0, -1)
    gvxr.setDetectorNumberOfPixels(1000, 1000)
    gvxr.setDetectorPixelSize(0.3048, 0.3048, "mm")
    gvxr.setScintillator("CsI", 600, "um")

    gvxr.loadMeshFile("panev", inputMeshPath, "mm")
    gvxr.loadMeshFile("pin", inputPinPath, "mm")

    rotationAngle = 0.0
    xVector = yVector = zVector = 0.0
    match view:
        case "ap":
            print("ap view")
        case "latL":
            rotationAngle = -90.0
            zVector = 1.0
        case "latR":
            rotationAngle = 90.0
            zVector = 1.0
        case "pi":
            rotationAngle = 45.0
            xVector = 1.0
        case _:
            print("unknown view")
            return None

    if view != "ap":
        gvxr.rotateNode("panev", rotationAngle, xVector, yVector, zVector)
    # gvxr.scaleNode()
    # minX, minY, minZ, maxX, maxY, maxZ = gvxr.getNodeAndChildrenBoundingBox("panev", "mm")
    # minX, minY, minZ, maxX, maxY, maxZ = gvxr.getNodeAndChildrenBoundingBox("panev", "mm")
    #
    # centerX = (minX + maxX) / 2.
    # centerY = (minY + maxY) / 2.
    # centerZ = (minZ + maxZ) / 2.
    # gvxr.translateNode("panev", -centerX, -centerY, -centerZ, "mm")

    # gvxr.translateNode("panev", -centerX, -centerY, -centerZ, "mm")

    gvxr.moveToCenter()
    gvxr.setMixture("panev", [1, 6, 7, 8, 11, 12, 15, 16, 20],
                    [0.034, 0.155, 0.042, 0.435, 0.001, 0.002, 0.103, 0.003, 0.225])
    gvxr.setDensity("panev", 1.920, "g/cm3")
    gvxr.setCompound("pin", "FeCrNi")
    gvxr.setDensity("pin", 8.01, "g/cm3") # 316L medical grade stainless steel density

    xrayImage = np.array(gvxr.computeXRayImage()).astype(np.float32)

    totalEnergyInMeV = gvxr.getTotalEnergyWithDetectorResponse()
    white = np.ones(xrayImage.shape) * totalEnergyInMeV
    dark = np.zeros(xrayImage.shape)
    xrayImageFlat = (xrayImage - dark) / (white - dark)

    xrayImageFlipped = -np.log(np.fliplr(xrayImageFlat))
    xrayImageReshaped = np.reshape(xrayImageFlipped, (1, 1000, 1000))
    xraySitkImage = sitk.GetImageFromArray(xrayImageReshaped)
    xraySitkImage.SetOrigin((0., 0., 0.))

    xraySitkImageExp = sitk.Expand(xraySitkImage, (1, 1, 4))

    print(xraySitkImageExp.GetOrigin(), xraySitkImageExp.GetDirection(),
          xraySitkImageExp.GetSpacing(), xraySitkImageExp.GetSize())
    plt.imshow(xrayImageFlipped, cmap="gray")
    plt.show()

    outputImagePath = os.path.join(os.getcwd(),
                                   f"input_files\\pacient_{patientNumber}\\registration\\pacient{patientNumber}Preop"
                                   f"{view.upper()}.mha")
    sitk.WriteImage(xraySitkImageExp, outputImagePath)
    # gvxr.renderLoop()

if __name__ == "__main__":
    patienNum = sys.argv[1]
    viewAngle = sys.argv[2]
    runSim(patienNum, viewAngle)