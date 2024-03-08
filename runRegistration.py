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


def runMain():

    global metric_values, multires_iterations
    metric_values = []
    multires_iterations = []

    print("Loading files...")
    preopDrrPath = os.path.join(baseDir,
                                f"input_files\\pacient_{patientNumber}\\pacient{patientNumber}Preop{view.upper()}.mha")
    intraopDrrPath = os.path.join(baseDir,
                                  f"input_files\\pacient_{patientNumber}\\pacient{patientNumber}Intraop{view.upper()}.mha")
    print(preopDrrPath, intraopDrrPath)
    preopImage = sitk.ReadImage(preopDrrPath, sitk.sitkFloat32)
    intraopImage = sitk.ReadImage(intraopDrrPath, sitk.sitkFloat32)

    intraopImageInverted = sitk.InvertIntensity(intraopImage, maximum=1)
    print(f"moving: {preopImage.GetSize()}, fixed: {intraopImageInverted.GetSize()}")

    print("Starting registration...")
    fixedImage = intraopImageInverted
    movingImage = preopImage[:, :, 0]
    movingImage.SetOrigin(fixedImage.GetOrigin())
    movingImage.SetSpacing(fixedImage.GetSpacing())
    print(f"Fixed image, spacing: {fixedImage.GetSpacing()}, size: {fixedImage.GetSize()}, "
          f"direction: {fixedImage.GetDirection()}, origin: {fixedImage.GetOrigin()}")
    print(f"Moving image, spacing: {movingImage.GetSpacing()}, size: {movingImage.GetSize()}, "
          f"direction: {movingImage.GetDirection()}, origin: {movingImage.GetOrigin()}")

    initialTransform = sitk.CenteredTransformInitializer(fixedImage, movingImage,
                                                         sitk.AffineTransform(2))

    registration = sitk.ImageRegistrationMethod()
    registration.SetMetricAsMattesMutualInformation()
    registration.SetOptimizerScalesFromPhysicalShift()
    registration.SetInitialTransform(initialTransform)
    registration.SetInterpolator(sitk.sitkLinear)
    registration.AddCommand(sitk.sitkIterationEvent, lambda: get_metric(registration))

    shrink_factors = []
    smoothing_sigmas = []
    if multires_level > 1:
        print(f"Registering with multiresolution level {multires_level}")

        shrink_factors = [shrink for shrink in range(2, (2 * multires_level), 2)]
        shrink_factors.insert(0, 1)
        smoothing_sigmas = [smooth for smooth in range(0, multires_level, 1)]

        registration.SetShrinkFactorsPerLevel(shrinkFactors=shrink_factors[::-1])
        registration.SetSmoothingSigmasPerLevel(smoothingSigmas=smoothing_sigmas[::-1])
        registration.SmoothingSigmasAreSpecifiedInPhysicalUnitsOn()
        registration.AddCommand(sitk.sitkMultiResolutionIterationEvent, update_multires_iterations)

    if regoptim == "gradient":
        outTransform = runGradientDescent(registration, fixedImage, movingImage)
    else:
        pass

    final_iter = registration.GetOptimizerIteration()
    print("Resampling transformed image...")
    movingImageResampled = sitk.Resample(movingImage, fixedImage, outTransform,
                                         sitk.sitkLinear, 0.0, movingImage.GetPixelID())

    saveDir = os.path.join(baseDir, f"input_files\\pacient_{patientNumber}\\registration\\{regoptim}")
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)

    print("Saving images...")
    fixedPath = os.path.join(saveDir, f"pacient{patientNumber}fixedImage{view.upper()}")
    movingPath = os.path.join(saveDir, f"pacient{patientNumber}movingImage{view.upper()}.npy")
    resampledPath = os.path.join(saveDir, f"pacient{patientNumber}resampledImage{view.upper()}.npy")
    metricsPath = os.path.join(saveDir, f"pacient{patientNumber}registrationInfo.npz")

    np.save(fixedPath, sitk.GetArrayViewFromImage(fixedImage))
    np.save(movingPath, sitk.GetArrayViewFromImage(movingImage))
    np.save(resampledPath, sitk.GetArrayViewFromImage(movingImageResampled))
    np.savez(metricsPath, metricValues=metric_values, finaliter=final_iter, multiresIters=multires_iterations,
             shrink_factors=shrink_factors, smoothing_sigmas=smoothing_sigmas)


def get_metric(registration_method):
    global metric_values, multires_iterations

    metric_values.append(registration_method.GetMetricValue())


def update_multires_iterations():
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


if __name__ == "__main__":
    global metric_values, multires_iterations
    baseDir = os.getcwd()
    if len(sys.argv[1:]) == 4:
        patientNumber = sys.argv[1]
        view = sys.argv[2]
        regoptim = sys.argv[3]
        multires_level = int(sys.argv[4])
    else:
        print("Použití souboru:\n"
              "argument 1: číslo pacinet - 01, 02, ...\n"
              "argument 2: pohled - ap, lat, pi\n"
              "argument 3: optimalizátor - gradient, \n"
              "argument 4: multires level - 2, 3, ...\n")
        sys.exit(1)
    runMain()
