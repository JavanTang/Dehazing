
from non_learning import histogram_stretching

algorithm_list = {'Grayscale-Histogram-Stretching': histogram_stretching.GrayscaleHistogramStretching(),
                  'RGB-Histogram-Stretching': histogram_stretching.RGBHistogramStretching()}

class AlgorithmFactory:
    def __init__(self):
        self.algorithm_list = algorithm_list

    def get_algorithm(self, name):
        return self.algorithm_list[name]


if __name__ == '__main__':
    
    input_images = ['./source/fog_image_1.jpg', './source/fog_image_2.png', './source/fog_image_3.png']

    # Grayscale-Histogram-Stretching 
    algorithm_factory = AlgorithmFactory()
    algorithm = algorithm_factory.get_algorithm('Grayscale-Histogram-Stretching')
    for image in input_images:
        algorithm.run(image, './output/Grayscale-' + image.split('/')[-1])


    # RGB-Histogram-Stretching
    algorithm = algorithm_factory.get_algorithm('RGB-Histogram-Stretching')
    for image in input_images:
        algorithm.run(image, './output/RGB-' + image.split('/')[-1])
    