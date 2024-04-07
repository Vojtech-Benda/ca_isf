import time

import SimpleITK as sitk
import numpy as np
import os
import sys
import matplotlib.pyplot as plt


def getMetricAndErrorsStart():
    global metric_values, multires_iterations, min_values, max_values, median_values, std_values, error_values, \
        current_iteration

    metric_values = []
    multires_iterations = []
    median_values = []
    min_values = []
    max_values = []
    std_values = []
    error_values = []
    current_iteration = -1


def getMetricAndErrorsEnd(registration_method, fixed_points, moving_points):
    global metric_values, multires_iterations, min_values, max_values, median_values, std_values, error_values, \
        current_iteration

    current_iteration = registration_method.GetOptimizerIteration()
    metric_values.append(registration_method.GetMetricValue())

    current_transform = sitk.CompositeTransform(registration_method.GetInitialTransform())
    current_transform.SetParameters(registration_method.GetOptimizerPosition())
    current_transform.AddTransform(registration_method.GetMovingInitialTransform())
    # current_transform.AddTransform(registration_method.GetFixedInitialTransform().GetInverse())

    median_error, std_error, min_error, max_error, error = getRegistrationErrors(current_transform,
                                                                               fixed_points,
                                                                               moving_points)

    median_values.append(median_error)
    min_values.append(min_error)
    max_values.append(max_error)
    std_values.append(std_error)
    error_values.append(error)


def getMetricAndErrors(registration_method, fixed_points, moving_points, moving_image, fixed_image):
    global metric_values, multires_iterations, min_values, max_values, \
        median_values, std_values, error_values, current_iteration

    if registration_method.GetOptimizerIteration() == current_iteration:
        return

    current_iteration = registration_method.GetOptimizerIteration()
    metric_values.append(registration_method.GetMetricValue())

    current_transform = sitk.CompositeTransform(registration_method.GetInitialTransform())
    current_transform.SetParameters(registration_method.GetOptimizerPosition())
    current_transform.AddTransform(registration_method.GetMovingInitialTransform())
    # current_transform.AddTransform(registration_method.GetFixedInitialTransform().GetInverse())

    median_error, std_error, min_error, max_error, error = getRegistrationErrors(current_transform,
                                                                               fixed_points,
                                                                               moving_points)

    median_values.append(median_error)
    min_values.append(min_error)
    max_values.append(max_error)
    std_values.append(std_error)
    error_values.append(error)


def updateMultiresIterations():
    global metric_values, multires_iterations

    multires_iterations.append(len(metric_values))


def getRegistrationErrors(transform, fixed_points, moving_points):
    inverseTransform = transform.GetInverse()
    transformed_points = [transform.TransformPoint(p) for p in fixed_points] # inverseTransform
    errors = [np.linalg.norm(np.array(p_fixed) - np.array(p_moving))
              for p_fixed, p_moving in zip(transformed_points, moving_points)]

    return np.median(errors), np.std(errors), np.min(errors), np.max(errors), errors


def getPoints(path):
    pointList = []
    with open(path, "r") as pointsFile:
        [pointList.append(line.split(",")[1:4]) for line in pointsFile.readlines()[1:]]
        return [[float(coords) for coords in sublist] for sublist in pointList]


def plotRegistrationErrors():
    figMetric, axMetric = plt.subplots(1, 1)
    axMetric.plot(np.arange(0, len(metric_values)), metric_values, "#1f77b4")
    axMetric.plot(multires_iterations, [metric_values[index] for index in multires_iterations], marker="o",
                  label="Registrační úroveň", linestyle="none",
                  markeredgecolor="none", markersize=6., c="#ff7f0e")
    axMetric.set_xlabel("Počet iterací [-]", fontsize=11)
    axMetric.set_ylabel("Vzájemná informace [-]", fontsize=11)
    axMetric.legend()
    axMetric.set_title("Optimalizace podobnostní metriky")

    # Plot the TRE median value and the [min-max] range.
    figTre, axTre = plt.subplots(1, 1)
    axTre.plot(median_values, color="black", label="Průměr")
    axTre.fill_between(range(len(median_values)), min_values, max_values,
                       facecolor="red", alpha=0.5)
    axTre.set_xlabel("Počet iterací", fontsize=11)
    axTre.set_ylabel("Rozdíl vzdáleností (TRE) [mm]", fontsize=11)
    axTre.set_title("Míra nepřesnosti registrace")
    axTre.legend()

    # Adjust the spacing between subplots so that the axis labels don't overlap.
    plt.show()


def runMain():
    global metric_values, multires_iterations, min_values, max_values, median_values, std_values, error_values, \
        current_iteration

    # create registration directory if there isn't
    if not os.path.exists(inputDir):
        os.makedirs(inputDir)

    print("Loading files...")
    preopDrrPath = os.path.join(inputDir, f"pacient{patientNumber}Preop.mha")
    intraopDrrPath = os.path.join(inputDir, f"pacient{patientNumber}IntraopST.mha")

    print(f"Moving Image: {preopDrrPath}\nFixed image: {intraopDrrPath}")
    # load images
    movingImage = sitk.ReadImage(preopDrrPath, sitk.sitkFloat32) # preop image
    fixedImage = sitk.ReadImage(intraopDrrPath, sitk.sitkFloat32) # intraop image
    movingImage = movingImage[..., 0]
    fixedImage = fixedImage[..., 0]

    # load points
    movingPoints = getPoints(os.path.join(inputDir, f"pacient{patientNumber}PreopPoints.csv"))
    fixedPoints = getPoints(os.path.join(inputDir, f"pacient{patientNumber}IntraopPoints.csv"))
    movingPoints = [sublist[:-1] for sublist in movingPoints]
    fixedPoints = [sublist[:-1] for sublist in fixedPoints]

    print(f"Fixed image, spacing: {fixedImage.GetSpacing()}, size: {fixedImage.GetSize()}, "
          f"direction: {fixedImage.GetDirection()}, origin: {fixedImage.GetOrigin()}")
    print(f"Moving image, spacing: {movingImage.GetSpacing()}, size: {movingImage.GetSize()}, "
          f"direction: {movingImage.GetDirection()}, origin: {movingImage.GetOrigin()}")

    print("Initializing images...")
    # initialization to center image centroids -> better results
    initialTransform = sitk.CenteredTransformInitializer(fixedImage, movingImage,
                                                         sitk.AffineTransform(2),
                                                         sitk.CenteredTransformInitializerFilter.MOMENTS)

    # get resampled moving image with initial transform
    movingInitialImage = sitk.Resample(movingImage, fixedImage, initialTransform, sitk.sitkLinear, 0.0,
                                       movingImage.GetPixelID())

    # get points with initial transform
    initialTransformInverse = initialTransform.GetInverse()
    movingInitialPoints = [initialTransformInverse.TransformPoint(p) for p in movingPoints]

    # instantiate registration method and set parameters
    registration = sitk.ImageRegistrationMethod()
    registration.SetMetricAsMattesMutualInformation() # similarity metric
    registration.SetOptimizerScalesFromPhysicalShift()
    registration.SetMetricSamplingStrategy(sitk.ImageRegistrationMethod.NONE)
    registration.SetMetricSamplingPercentage(percentage=0.01, seed=42) # disable randomisation -> reproducible results
    registration.SetInterpolator(sitk.sitkLinear)

    # optimized transform for ITKv4 registration framework
    optimizedTransform = sitk.AffineTransform(2)
    registration.SetMovingInitialTransform(initialTransform)
    registration.SetInitialTransform(optimizedTransform)

    # set up observers
    registration.AddCommand(sitk.sitkStartEvent, getMetricAndErrorsStart)
    registration.AddCommand(sitk.sitkEndEvent, lambda: getMetricAndErrorsEnd(registration,
                                                                                   fixedPoints,
                                                                                   movingPoints))
    registration.AddCommand(sitk.sitkIterationEvent, lambda: getMetricAndErrors(registration,
                                                                                      fixedPoints,
                                                                                      movingPoints,
                                                                                      movingImage,
                                                                                      fixedImage))
    # set up multiresolution pyramid
    shrinkFactor = []
    smoothSigmas = []
    if multiresLevel > 1:
        levels = multiresLevel
        shrinkFactor = [4 * factor for factor in range(0, levels)][::-1]  # 2 ** factor, range(0, levels)
        shrinkFactor[-1] = 1
        smoothSigmas = [3 * factor for factor in range(0, levels)][::-1]  # range(0, levels)
        #smoothSigmas = [(factor / 2) for factor in shrinkFactor]  # range(0, levels)

        registration.SetShrinkFactorsPerLevel(shrinkFactors=shrinkFactor)
        registration.SetSmoothingSigmasPerLevel(smoothingSigmas=smoothSigmas)
        registration.SmoothingSigmasAreSpecifiedInPhysicalUnitsOn()
        registration.AddCommand(sitk.sitkMultiResolutionIterationEvent, updateMultiresIterations)

    match regOptim:
        case "gradient":
            registration.SetOptimizerAsGradientDescent(learningRate=1.0,
                                                       numberOfIterations=100,
                                                       convergenceMinimumValue=1e-6,
                                                       convergenceWindowSize=2,
                                                       estimateLearningRate=registration.EachIteration)

        case "gradientline":
            registration.SetOptimizerAsGradientDescentLineSearch(learningRate=1.0,
                                                                 numberOfIterations=15,
                                                                 convergenceMinimumValue=1e-4,
                                                                 convergenceWindowSize=2,
                                                                 lineSearchMaximumIterations=3,
                                                                 lineSearchEpsilon=0.1,
                                                                 lineSearchLowerLimit=0.0,
                                                                 lineSearchUpperLimit=3.0,
                                                                 estimateLearningRate=registration.EachIteration)
        case "gradientlbf":
            registration.SetOptimizerAsLBFGS2(numberOfIterations=30,
                                              hessianApproximateAccuracy=4,
                                              lineSearchAccuracy=1e-4,
                                              lineSearchMinimumStep=1e-20,
                                              lineSearchMaximumStep=1e20,
                                              lineSearchMaximumEvaluations=10,
                                              deltaConvergenceDistance=0,
                                              deltaConvergenceTolerance=1e-5)
        case _:
            print(f"Optimizer {regOptim} is not recognized,\nallowed types are gradient, gradientline, gradientlbf")
            return

    print(f"Registering with {regOptim} and multiresolution level {multiresLevel}: {shrinkFactor, smoothSigmas}...")

    try:
        start_time = time.time()
        registration.Execute(fixedImage, movingImage)
        exec_time = time.time() - start_time
    except RuntimeError as runtimeError:
        print(runtimeError)
        return

    finalTransform = sitk.CompositeTransform([optimizedTransform, initialTransform])

    print(f"Optimizer stop condition: {registration.GetOptimizerStopConditionDescription()}")
    print(f" Iteration: {registration.GetOptimizerIteration()}")
    print(f" Metric value: {registration.GetMetricValue():.3f}")
    print(f"Registration time: {exec_time:.3f} seconds")

    final_iter = registration.GetOptimizerIteration()

    print("Resampling transformed image...")
    # get resampled moving image with final transform
    movingFinalImage = sitk.Resample(movingImage, fixedImage, finalTransform,
                                     sitk.sitkLinear, 0.0, movingImage.GetPixelID())

    # get points with final transform
    finalTransformInverse = finalTransform.GetInverse()
    movingFinalPoints = [finalTransformInverse.TransformPoint(p) for p in movingPoints]

    # get errors before initialization
    (pre_median, pre_std,
     pre_min, pre_max, pre_errors) = getRegistrationErrors(sitk.Transform(2, sitk.sitkIdentity),
                                                           fixedPoints,
                                                           movingPoints)
    # get errors after initialization
    (initial_median, initial_std,
     initial_min, initial_max, initial_errors) = getRegistrationErrors(sitk.Transform(2, sitk.sitkIdentity),
                                                                       fixedPoints,
                                                                       movingInitialPoints)
    # get errors after registration
    (final_median, final_std,
     final_min, finall_max, final_errors) = getRegistrationErrors(sitk.Transform(2, sitk.sitkIdentity),
                                                                  fixedPoints,
                                                                  movingFinalPoints)

    print(f"median errors pre, initial, final: {pre_median:.3f}, {initial_median:.3f}, {final_median:.3f}")
    """
    plt.imshow(sitk.GetArrayViewFromImage(movingInitialImage), cmap="gray")
    plt.imshow(sitk.GetArrayViewFromImage(fixedImage), cmap="gray", alpha=0.5)
    plt.scatter(list(np.array(fixedPoints).T)[0], list(np.array(fixedPoints).T)[1],
                c="#1f77b4", label="fixed", s=20)
    plt.scatter(list(np.array(movingInitialPoints).T)[0], list(np.array(movingInitialPoints).T)[1],
                c="#ff7f0e", label="moving", s=20)
    plt.show()
    """

    plt.imshow(sitk.GetArrayViewFromImage(movingFinalImage), cmap="gray")
    plt.imshow(sitk.GetArrayViewFromImage(fixedImage), cmap="gray", alpha=0.5)
    plt.scatter(list(np.array(fixedPoints).T)[0], list(np.array(fixedPoints).T)[1],
                c="#1f77b4", label="fixed", s=20)
    plt.scatter(list(np.array(movingFinalPoints).T)[0], list(np.array(movingFinalPoints).T)[1],
                c="#ff7f0e", label="moving", s=20)
    plt.legend()
    plt.axis("off")
    plt.show()

    plotRegistrationErrors()

    patientDir = os.path.join(inputDir, f"{regOptim}\\")

    if not os.path.exists(patientDir): # create optimizer directory if there isn't
        os.makedirs(patientDir)

    print("Saving images, metrics, errors, points...")
    imagePath = os.path.join(patientDir, f"pacient{patientNumber}Images.npz")
    metricsPath = os.path.join(patientDir, f"pacient{patientNumber}RegParams.npz")
    preErrorsPath = os.path.join(patientDir, f"pacient{patientNumber}PreErrors.npz")
    initialErrorsPath = os.path.join(patientDir, f"pacient{patientNumber}InitialErrors.npz")
    regErrorsPath = os.path.join(patientDir, f"pacient{patientNumber}RegErrors.npz")
    pointsPath = os.path.join(patientDir, f"pacient{patientNumber}Points.npz")

    np.savez(imagePath, movingImage=sitk.GetArrayFromImage(movingImage),
             fixedImage=sitk.GetArrayFromImage(fixedImage),
             movingInitialImage=sitk.GetArrayFromImage(movingInitialImage),
             movingFinalImage=sitk.GetArrayFromImage(movingFinalImage))

    np.savez(metricsPath, metricValues=metric_values, finalIter=final_iter, multiresIters=multires_iterations,
             shrinkFactors=shrinkFactor, smoothingSigmas=smoothSigmas, execTime=exec_time)

    np.savez(preErrorsPath, preErrors=pre_errors, preMedians=pre_median, preStds=pre_std,
             preMins=pre_min, preMaxs=pre_max)
    np.savez(initialErrorsPath, initialErrors=initial_errors, initialMedians=initial_median, initialStds=initial_std,
             initialMins=initial_min, initialMaxs=initial_max)
    np.savez(regErrorsPath, regErrors=error_values, regMedians=median_values, regStds=std_values,
             regMins=min_values, regMaxs=max_values)

    np.savez(pointsPath, fixedPoints=np.array(fixedPoints), movingPoints=np.array(movingPoints),
             movingInitialPoints=movingInitialPoints, movingFinalPoints=movingFinalPoints)
    print(f"Saved to {patientDir}")
    print("Finished...")


if __name__ == "__main__":

    if len(sys.argv[1:]) == 3:
        patientNumber = sys.argv[1]
        regOptim = sys.argv[2]
        multiresLevel = int(sys.argv[3])
    else:
        print("File usage:\n"
              "argument 1: patient number - 01, 02, ...\n"
              "argument 3: optimizer - gradient, gradientline, gradientlbf\n"
              "argument 4: multiressolution level - 2, 3, ...\n")
        sys.exit(1)

    inputDir = os.path.join(os.getcwd(), f"input_files\\pacient_{patientNumber}\\registration\\")
    runMain()
