import os
import sys
import numpy as np
import SimpleITK as sitk
from gvxrPython3 import gvxr
from gvxrPython3.utils import plotScreenshot
import matplotlib.pyplot as plt

def runSim(patientNumber, view):
    inputMeshPath = f"input_files\\pacient_{patientNumber}\\stl\\pacient{patientNumber}PanevMesh.stl"

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
    minX, minY, minZ, maxX, maxY, maxZ = gvxr.getNodeAndChildrenBoundingBox("panev", "mm")

    centerX = (minX + maxX) / 2.
    centerY = (minY + maxY) / 2.
    centerZ = (minZ + maxZ) / 2.
    gvxr.translateNode("panev", -centerX, -centerY, -centerZ, "mm")

    # gvxr.translateNode("panev", -centerX, -centerY, -centerZ, "mm")

    gvxr.moveToCenter("panev")
    gvxr.setMixture("panev", [1, 6, 7, 8, 11, 12, 15, 16, 20],
                    [0.034, 0.155, 0.042, 0.435, 0.001, 0.002, 0.103, 0.003, 0.225])
    gvxr.setDensity("panev", 1.920, "g/cm3")

    xrayImage = np.array(gvxr.computeXRayImage()).astype(np.float32)
    xrayImageFlipped = np.fliplr(xrayImage)
    xrayImageReshaped = np.reshape(xrayImageFlipped, (1, 1000, 1000))
    imageInverse = sitk.InvertIntensity(sitk.GetImageFromArray(xrayImageReshaped), maximum=1)
    imageInverse.SetOrigin((0., 0., 0.))

    print(imageInverse.GetOrigin(), imageInverse.GetDirection(), imageInverse.GetSpacing())
    plt.imshow(sitk.GetArrayViewFromImage(imageInverse)[0, ...], cmap="gray")
    plt.show()

    outputImagePath = os.path.join(os.getcwd(),
                                   f"input_files\\pacient_{patientNumber}\\registration\\pacient{patientNumber}Intraop"
                                   f"{view.upper()}.mha")
    sitk.WriteImage(imageInverse, outputImagePath)
    plotScreenshot()

if __name__ == "__main__":
    patienNum = sys.argv[1]
    viewAngle = sys.argv[2]
    runSim(patienNum, viewAngle)