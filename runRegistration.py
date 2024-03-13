import SimpleITK as sitk
import numpy as np
import os
import sys


def getMetricAndErrorsStart():
    global metric_values, multires_iterations
    global min_values, max_values, mean_values, std_values, error_values
    global current_iteration

    metric_values = []
    multires_iterations = []
    mean_values = []
    min_values = []
    max_values = []
    std_values = []
    error_values = []
    current_iteration = -1


def getMetricAndErrorsEnd():
    global metric_values, multires_iterations
    global min_values, max_values, mean_values, std_values, error_values
    global current_iteration


def getMetricAndErrors(registration_method, fixed_points, moving_points):
    global metric_values, multires_iterations
    global min_values, max_values, mean_values, std_values, error_values
    global current_iteration

    if registration_method.GetOptimizerIteration() == current_iteration:
        return

    current_iteration = registration_method.GetOptimizerIteration()
    metric_values.append(registration_method.GetMetricValue())

    current_transform = sitk.CompositeTransform(registration_method.GetInitialTransform())
    current_transform.SetParameters(registration_method.GetOptimizerPosition())
    current_transform.AddTransform(registration_method.GetMovingInitialTransform())
    current_transform.AddTransform(registration_method.GetFixedInitialTransform().GetInverse())

    mean_error, std_error, min_error, max_error, error = getRegistrationErrors(current_transform,
                                                                               fixed_points,
                                                                               moving_points)

    mean_values.append(mean_error)
    min_values.append(min_error)
    max_values.append(max_error)
    std_values.append(std_error)
    error_values.append(error_values)


def updateMultiresIterations():
    global metric_values, multires_iterations

    multires_iterations.append(len(metric_values))


def getRegistrationErrors(transform, fixed_points, moving_points):
    inverseTransform = transform.GetInverse()
    transformed_points = [inverseTransform.TransformPoint(p) for p in moving_points]
    errors = [np.linalg.norm(np.array(p_fixed) - np.array(p_moving))
              for p_fixed, p_moving in zip(fixed_points, transformed_points)]

    return np.mean(errors), np.std(errors), np.min(errors), np.max(errors), errors


def runGradientDescent(reg_method, fixed_image, moving_image):
    reg_method.SetOptimizerAsGradientDescent(learningRate=1.0,
                                             numberOfIterations=200,
                                             convergenceMinimumValue=1e-5,
                                             convergenceWindowSize=5)

    out_transform = reg_method.Execute(fixed_image, moving_image)
    print(f"Optimizer stop condition: {reg_method.GetOptimizerStopConditionDescription()}")
    print(f" Iteration: {reg_method.GetOptimizerIteration()}")
    print(f" Metric value: {reg_method.GetMetricValue()}")

    return out_transform


def getPoints(path):
    pointList = []
    with open(path, "r") as pointsFile:
        [pointList.append(line.split(",")[1:4]) for line in pointsFile.readlines()[1:]]
        pointList = [float(coords) for sublist in pointList for coords in sublist]
        return pointList


def runMain():
    global metric_values, multires_iterations
    global min_values, max_values, mean_values, std_values, error_values
    global current_iteration
    metric_values = []
    multires_iterations = []

    print("Loading files...")
    preopDrrPath = os.path.join(inputDir, f"pacient{patientNumber}Preop{view.upper()}.mha")
    intraopDrrPath = os.path.join(inputDir, f"pacient{patientNumber}Intraop{view.upper()}.mha")

    print(preopDrrPath, intraopDrrPath)
    preopImage = sitk.ReadImage(preopDrrPath, sitk.sitkFloat32)
    intraopImage = sitk.ReadImage(intraopDrrPath, sitk.sitkFloat32)

    fixedPoints = getPoints(os.path.join(inputDir, f"pacient{patientNumber}FixedPoints{view.upper()}.csv"))
    movingPoints = getPoints(os.path.join(inputDir, f"pacient{patientNumber}MovingPoints{view.upper()}.csv"))

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
    registration.AddCommand(sitk.sitkStartEvent, getMetricAndErrorsStart)
    registration.AddCommand(sitk.sitkEndEvent, getMetricAndErrorsEnd)
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

    outTransformInverse = outTransform.GetInverse()
    movingFinalPoints = [outTransformInverse.TransformPoint(p) for p in movingPoints]

    patientDir = os.path.join(inputDir, f"registration\\{regOptim}")
    if not os.path.exists(patientDir):
        os.makedirs(patientDir)

    print("Saving images, metrics, errors, points...")
    fixedPath = os.path.join(patientDir, f"pacient{patientNumber}fixedImage{view.upper()}")
    movingPath = os.path.join(patientDir, f"pacient{patientNumber}movingImage{view.upper()}.npy")
    resampledPath = os.path.join(patientDir, f"pacient{patientNumber}resampledImage{view.upper()}.npy")
    metricsPath = os.path.join(patientDir, f"pacient{patientNumber}registrationInfo{view.upper()}.npy")
    errorsPath = os.path.join(patientDir, f"pacient{patientNumber}ErrorsInfo{view.upper()}.npz")
    pointsPath = os.path.join(patientDir, f"pacient{patientNumber}PointsInfo{view.upper()}.npz")

    np.save(fixedPath, sitk.GetArrayViewFromImage(fixedImage))
    np.save(movingPath, sitk.GetArrayViewFromImage(movingImage))
    np.save(resampledPath, sitk.GetArrayViewFromImage(movingImageResampled))
    np.savez(metricsPath, metricValues=metric_values, finalIter=final_iter, multiresIters=multires_iterations,
             shrinkFactors=shrink_factors, smoothingSigmas=smoothing_sigmas)
    np.savez(errorsPath, errorValues=error_values, meanValues=mean_values, stdValues=std_values,
             minValues=min_values, maxValues=max_values)
    np.savez(pointsPath, fixedPoints=fixedPoints, movingPoints=movingPoints,
             movingInitialPoints=movingInitialPoints, movingFinalPoints=movingFinalPoints)


if __name__ == "__main__":
    global metric_values, multires_iterations
    global min_values, max_values, mean_values, std_values, error_values
    global current_iteration

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

    inputDir = os.path.join(os.getcwd(), f"input_files\\pacient_{patientNumber}\\")
    runMain()
