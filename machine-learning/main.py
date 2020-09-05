from imageai.Prediction import ImagePrediction
from pathlib import Path

def main():
    working_dir = Path.cwd().joinpath('machine-learning')
    prediction = ImagePrediction()
    
    # SqueezeNet model
    # prediction.setModelTypeAsSqueezeNet()
    # prediction.setModelPath(working_dir.joinpath('./model/squeezenet_weights_tf_dim_ordering_tf_kernels.h5'))
    
    # ResNet model
    prediction.setModelTypeAsResNet()
    prediction.setModelPath(working_dir.joinpath('./model/resnet50_weights_tf_dim_ordering_tf_kernels.h5'))
    
    prediction.loadModel()

    predictions, probabilities = prediction.predictImage(working_dir.joinpath("./img/giraffe.jpg"), result_count=5 )
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)
    
    return 0


if __name__ == "__main__":
    main()