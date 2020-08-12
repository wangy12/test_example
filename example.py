Class PathExtraction3D():
    def __init__(self):
        pass
		
    def process(self, **kwargs):
        return traj3D
		
Class ObjectDetection():
    def __init__(self):
        pass
		
    def process(self, **kwargs):
        return object3D
		
import PathExtraction3D, ObjectDetection

PathExtractor = PathExtraction3D()
ObjectDetector = ObjectDetection()

for _ in range(100):
    # for each data piece, pass image + lidar data to path extraction and object detection functions
    sensorData = [] # lidar or camera
    traj3d = PathExtractor.process(sensorData)
    object3d = ObjectDetector.process(sensorData)
