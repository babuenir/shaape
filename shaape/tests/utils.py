import Image
import ImageChops
import math
import operator

class TestUtils(object):
    EXPORT_TEST_FILE = 'shaape/tests/generated_images/export_test.png'
    BLUR_INPUT = 'shaape/tests/input/lena.png'
    BLUR_GENERATED_IMAGE = 'shaape/tests/generated_images/blur.png'
    BLUR_EXPECTED_IMAGE = 'shaape/tests/expected_images/blur.png'
    EMPTY_CANVAS_GENERATED_IMAGE = 'shaape/tests/generated_images/empty_canvas.png'
    EMPTY_CANVAS_EXPECTED_IMAGE = 'shaape/tests/expected_images/empty_canvas.png'
    POLYGON_GENERATED_IMAGE = 'shaape/tests/generated_images/polygon.png'
    POLYGON_EXPECTED_IMAGE = 'shaape/tests/expected_images/polygon.png'
    POLYGON_SHADOW_GENERATED_IMAGE = 'shaape/tests/generated_images/polygon_shadow.png'
    POLYGON_SHADOW_EXPECTED_IMAGE = 'shaape/tests/expected_images/polygon_shadow.png'
    OPEN_GRAPH_GENERATED_IMAGE = 'shaape/tests/generated_images/open_graph.png'
    OPEN_GRAPH_EXPECTED_IMAGE = 'shaape/tests/expected_images/open_graph.png'
    OPEN_GRAPH_EMPTY_GENERATED_IMAGE = 'shaape/tests/generated_images/open_graph_empty.png'
    OPEN_GRAPH_EMPTY_EXPECTED_IMAGE = 'shaape/tests/expected_images/open_graph_empty.png'
    OPEN_GRAPH_SHADOW_GENERATED_IMAGE = 'shaape/tests/generated_images/open_graph_shadow.png'
    OPEN_GRAPH_SHADOW_EXPECTED_IMAGE = 'shaape/tests/expected_images/open_graph_shadow.png'
    OPEN_GRAPH_SHADOW_EMPTY_GENERATED_IMAGE = 'shaape/tests/generated_images/open_graph_shadow_empty.png'
    OPEN_GRAPH_SHADOW_EMPTY_EXPECTED_IMAGE = 'shaape/tests/expected_images/open_graph_shadow_empty.png'
    TEXT_GENERATED_IMAGE = 'shaape/tests/generated_images/text.png'
    TEXT_EXPECTED_IMAGE = 'shaape/tests/expected_images/text.png'
    ACCEPTABLE_RMS = 0
    
    @staticmethod
    def imagesEqual(image1, image2):
        try:
            img1 = Image.open(image1)
            img2 = Image.open(image2)
        except:
            return False
        diff = ImageChops.difference(img1, img2)
        h = ImageChops.difference(img1, img2).histogram()
        sq = (value*((idx%256)**2) for idx, value in enumerate(h))
        sum_of_squares = sum(sq)
        rms = math.sqrt(sum_of_squares/float(img1.size[0] * img1.size[1]))
        print(rms)
        return rms <= TestUtils.ACCEPTABLE_RMS
