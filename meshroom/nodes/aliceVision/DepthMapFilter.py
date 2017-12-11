from meshroom.core import desc

class DepthMapFilter(desc.CommandLineNode):
    internalFolder = '{cache}/{nodeType}/{uid0}/'
    commandLine = 'aliceVision_depthMapFiltering {allParams}'
    gpu = desc.Level.NORMAL
    size = desc.DynamicNodeSize('ini')
    parallelization = desc.Parallelization(blockSize=10)
    commandLineRange = '--rangeStart {rangeStart} --rangeSize {rangeBlockSize}'

    inputs = [
        desc.File(
            name="ini",
            label="MVS Configuration file",
            description="",
            value="",
            uid=[0],
            ),
        desc.File(
            name="depthMapFolder",
            label="Depth Map Folder",
            description="Input depth map folder",
            value="",
            uid=[0],
            ),
        desc.IntParam(
            name="nNearestCams",
            label="Number of Nearest Cameras",
            description="Number of nearest cameras used for filtering.",
            value=10,
            range=(0, 20, 1),
            uid=[0],
        ),
        desc.IntParam(
            name="minNumOfConsistensCams",
            label="Min Consistent Cameras",
            description="Min Number of Consistent Cameras",
            value=3,
            range=(0, 10, 1),
            uid=[0],
        ),
        desc.IntParam(
            name="minNumOfConsistensCamsWithLowSimilarity",
            label="Min Consistent Cameras Bad Similarity",
            description="Min Number of Consistent Cameras for pixels with weak similarity value",
            value=4,
            range=(0, 10, 1),
            uid=[0],
        ),
        desc.IntParam(
            name="pixSizeBall",
            label="Filtering Size in Pixels",
            description="Filtering size in pixels",
            value=0,
            range=(0, 10, 1),
            uid=[0],
        ),
        desc.IntParam(
            name="pixSizeBallWithLowSimilarity",
            label="Filtering Size in Pixels Bad Similarity",
            description="Filtering size in pixels",
            value=0,
            range=(0, 10, 1),
            uid=[0],
        ),
    ]

    outputs = [
        desc.File(
            name='output',
            label='Output',
            description='Output folder for generated depth maps.',
            value='{cache}/{nodeType}/{uid0}/',
            uid=[],
        ),
    ]
