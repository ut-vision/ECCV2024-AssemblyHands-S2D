# ECCV HANDS2024: AssemblyHands-S2D
This repository offers a submission guidance for the [ECCV 2024 HANDS challenge - AssemblyHands-S2D](https://hands-workshop.org/challenge2024.html).
The task is adapting a single-view 3D hand pose estimator to dual-view settings.

## Release notes
Aug 2, 2024: Update test files (v1-1).  Please check the ``test_pair_stats `` in `challenge_submit.py`.

## Test image and metadata
You can find test images and files (including image path, bbox): \
[[test images]](https://drive.google.com/drive/folders/1sbZcZMIKS2lk2zBxfa47cWA2KDZXPwVE?usp=sharing) 
[[test files]](https://drive.google.com/drive/folders/1ell5eDp86D5GXm8Gy4PbGskPZ52rUwsb?usp=sharing) \
Please place the `template/` folder under this directory. \
Code for baseline method (you can develop based on it): https://github.com/ut-vision/S2DHand_HANDS2024

## Evaluation details
We will evaluate 3D predictions in camera coordinates. We will calculate the error after aligning the predictions with ground-truth labels.

The data file `test_HANDS2024/assemblyhands_test_ego_data-${version}.json` defines the input images that can be used for test dataloader.
The final submission format is specified by `template/asßsemblyhands_test_joint_3d_eccv24_${version}_pred_template.json`. \
```angular2html
- info
- annotations
    - camera pair name
        - sequence name
            - camera name
                - frame id: 3D joint list (21 * 3)
```
Note: we've filtered out images that are not suitable for evaluation (e.g., the hand is partially out-of-view). 
This results in less frame indices than those in the test image folder.

Before submission, please make sure the following notes:
- Hand joint format (21 keypoints are defined for each frame)
- Frame indices match the template json
- Leave the prediction blank (fill in 0s) if the hand bbox is not provided in the data file

## How to convert to camera coordinates and visualization
As we only allow to use the provided pre-trained weights for adaptation, those model's predictions are under camera coordinate by default.
Please refer to the example [S2DHand Toolkit](https://github.com/MickeyLLG/S2DHand_HANDS2024)'s dataloader and pre-trained weights.

Please refer to the `visualize.py` of the example [S2DHand Toolkit](https://github.com/MickeyLLG/S2DHand_HANDS2024) for visialization.
## Submission instructions
The script `challenge_submit.py` will create your own json file using the template file.
Please custom the `get_pred(.)` function to register in your results.
By default, the function fills in ones and saves them to `assemblyhands_test_joint_3d_eccv24_pred.jso`.
Finally, please upload your prediction file as a zip file to the evaluation server.

## References
- [AssemblyHands Toolkit](https://github.com/facebookresearch/assemblyhands-toolkit)
- [S2DHand Toolkit](https://github.com/MickeyLLG/S2DHand_HANDS2024)
- [ECCV 2024 HANDS Workshop](https://hands-workshop.org/workshop2024.html)

## Acknowledgment
We thank Dr. Linlin Yang, Prof. Angela Yao (NUS), Dr. Kun He (Meta), and Prof. Yoichi Sato (UTokyo) for helpful discussions on the design of the challenge. This dataset is based on the work at Meta Reality Labs, and thanks go to Dr. Fadime Sener, Dr. Tomas Hodan, Dr. Luan Tran, and Dr. Cem Keskin (Meta). 
