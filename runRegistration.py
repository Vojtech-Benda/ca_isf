import SimpleITK as sitk
import numpy as np
import os
import sys


# def start_plot():
#     global metric_values, multires_iterations
#
#     metric_values = []
#     multires_iterations = []


# Callback invoked when the EndEvent happens, do cleanup of data and figure.
# def end_plot():
#
#     # with open("metric_values.txt", 'w') as fp:
#     #     for value in metric_values:
#     #         fp.write(f"{value}\n")





def get_metric(registration_method):
    global metric_values, multires_iterations

    metric_values.append(registration_method.GetMetricValue())


def updateMultiresIterations():
    global metric_values, multires_iterations

    multires_iterations.append(len(metric_values))


def runGradientDescent(regmethod, fixedImage, movingImage):
    regmethod.SetOptimizerAsGradientDescent(learningRate=1.0,
                                            numberOfIterations=200,
                                            convergenceMinimumValue=1e-5,
                                            convergenceWindowSize=5)

    outtransform = regmethod.Execute(fixedImage, movingImage)
    print(f"Optimizer stop condition: {regmethod.GetOptimizerStopConditionDescription()}")
    print(f" Iteration: {regmethod.GetOptimizerIteration()}")
    print(f" Metric value: {regmethod.GetMetricValue()}")

    return outtransform


def getPoints(path):
    pointList = []
    with open(path, "r") as pointsFile:
        [pointList.append(line.split(",")[1:4]) for line in pointsFile.readlines()[1:]]
        pointList = [[float(coords) for coords in sublist] for sublist in pointList]
        return pointList


def runMain():
    global metric_values, multires_iterations
    metric_values = []
    multires_iterations = []

    print("Loading files...")
    preopDrrPath = os.path.join(inputDir,
                                f"input_files\\pacient_{patientNumber}\\pacient{patientNumber}"
                                f"Preop{view.upper()}.mha")
    intraopDrrPath = os.path.join(inputDir,
                                  f"input_files\\pacient_{patientNumber}\\pacient{patientNumber}"
                                  f"Intraop{view.upper()}.mha")

    print(preopDrrPath, intraopDrrPath)
    preopImage = sitk.ReadImage(preopDrrPath, sitk.sitkFloat32)
    intraopImage = sitk.ReadImage(intraopDrrPath, sitk.sitkFloat32)

    fixedPoints = getPoints(os.path.join(inputDir, f"pacient{patientNumber}\\pacient{patientNumber}"
                                                   f"FixedPoints{view.upper()}.csv"))
    movingPoints = getPoints(os.path.join(inputDir, f"pacient{patientNumber}\\pacient{patientNumber}"
                                                   f"MovingPoints{view.upper()}.csv"))

    # intraopImageInverted = sitk.InvertIntensity(intraopImage, maximum=1)
    print(f"moving: {preopImage.GetSize()}, fixed: {intraopImage.GetSize()}")

    print("Starting registration...")
    fixedImage = intraopImage
    movingImage = preopImage
    # movingImage.SetOrigin(fixedImage.GetOrigin())
    # movingImage.SetSpacing(fixedImage.GetSpacing())
    print(f"Fixed image, spacing: {fixedImage.GetSpacing()}, size: {fixedImage.GetSize()}, "
          f"direction: {fixedImage.GetDirection()}, origin: {fixedImage.GetOrigin()}")
    print(f"Moving image, spacing: {movingImage.GetSpacing()}, size: {movingImage.GetSize()}, "
          f"direction: {movingImage.GetDirection()}, origin: {movingImage.GetOrigin()}")

    initialTransform = sitk.CenteredTransformInitializer(fixedImage, movingImage,
                                                         sitk.AffineTransform(3))

    initialImage = sitk.Resample(movingImage, fixedImage, initialTransform, sitk.sitkLinear, 0.0,
                                 movingImage.GetPixelID())

    initialTransformInverse = initialTransform.GetInverse()
    movingInitialPoints = [initialTransformInverse.TransformPoint(p) for p in movingPoints]

    registration = sitk.ImageRegistrationMethod()
    registration.SetMetricAsMattesMutualInformation()
    registration.SetOptimizerScalesFromPhysicalShift()
    registration.SetInitialTransform(initialTransform)
    registration.SetInterpolator(sitk.sitkLinear)
    registration.AddCommand(sitk.sitkMultiResolutionIterationEvent, updateMultiresIterations)
    registration.AddCommand(sitk.sitkIterationEvent, lambda: getMetricAndErrors(registration,
                                                                                fixedPoints,
                                                                                movingPoints))
    shrink_factors = []
    smoothing_sigmas = []
    if multiresLevel > 1:
        print(f"Registering with multiresolution level {multiresLevel}")

        shrink_factors = [shrink for shrink in range(2, (2 * multiresLevel), 2)]
        shrink_factors.insert(0, 1)
        smoothing_sigmas = [smooth for smooth in range(0, multiresLevel, 1)]

        registration.SetShrinkFactorsPerLevel(shrinkFactors=shrink_factors[::-1])
        registration.SetSmoothingSigmasPerLevel(smoothingSigmas=smoothing_sigmas[::-1])
        registration.SmoothingSigmasAreSpecifiedInPhysicalUnitsOn()

    if regOptim == "gradient":
        outTransform = runGradientDescent(registration, fixedImage, movingImage)
    else:
        pass

    final_iter = registration.GetOptimizerIteration()
    print("Resampling transformed image...")
    movingImageResampled = sitk.Resample(movingImage, fixedImage, outTransform,
                                         sitk.sitkLinear, 0.0, movingImage.GetPixelID())

    patientDir = os.path.join(inputDir, f"pacient_{patientNumber}\\registration\\{regOptim}")
    if not os.path.exists(patientDir):
        os.makedirs(patientDir)

    print("Saving images...")
    fixedPath = os.path.join(patientDir, f"pacient{patientNumber}fixedImage{view.upper()}")
    movingPath = os.path.join(patientDir, f"pacient{patientNumber}movingImage{view.upper()}.npy")
    resampledPath = os.path.join(patientDir, f"pacient{patientNumber}resampledImage{view.upper()}.npy")
    metricsPath = os.path.join(patientDir, f"pacient{patientNumber}registrationInfo{view.upper()}.npy")
    errorsPath = os.path.join(patientDir, f"pacient{patientNumber}ErrorsInfo{view.upper()}.npz")

    np.save(fixedPath, sitk.GetArrayViewFromImage(fixedImage))
    np.save(movingPath, sitk.GetArrayViewFromImage(movingImage))
    np.save(resampledPath, sitk.GetArrayViewFromImage(movingImageResampled))
    np.savez(metricsPath, metricValues=metric_values, finalIter=final_iter, multiresIters=multires_iterations,
             shrinkFactors=shrink_factors, smoothingSigmas=smoothing_sigmas)
    np.savez(errorsPath, )


if __name__ == "__main__":
    global metric_values, multires_iterations
    inputDir = os.path.join(os.getcwd(), "input_files\\")
    if len(sys.argv[1:]) == 4:
        patientNumber = sys.argv[1]
        view = sys.argv[2]
        regOptim = sys.argv[3]
        multiresLevel = int(sys.argv[4])
    else:
        print("Použití souboru:\n"
              "argument 1: číslo pacinet - 01, 02, ...\n"
              "argument 2: pohled - ap, lat, pi\n"
              "argument 3: optimalizátor - gradient, \n"
              "argument 4: multires level - 2, 3, ...\n")
        sys.exit(1)
    runMain()
