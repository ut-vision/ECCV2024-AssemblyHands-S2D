ECCV HANDS2024: Single-to-Dual-View Adaptation Challenge
---

This is submission guidance for the **ECCV HANDS2024: AssemblyHands-S2D Challenge**. 

Please follow the template `template/assemblyhands_test_joint_3d_eccv24_pred_template.json` for submission, which has the following structure
```angular2html
- info
- annotations
    - camera pair name
        - sequence name
            - camera name
                - frame id: 3D joint list (21 * 3)
```
Note that the 3D joints should be in camera coordinate systems. We will calculate the error after align the predictions with ground-truth labels.  

## Submission code
Please implement the `get_pred` function in `challenge_submit.py` to return the 3D joint prediction given the camera pair, sequence name, camera name, and frame id.

Then, please upload the generated json file to our challenge website.

## Contact

For any questions, including algorithms and datasets, feel free to contact us via the hands group email.
