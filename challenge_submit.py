import numpy as np
import json

JNUM = 21
# NOTE: the number of samples in each camera pair.
test_pair_stats = {
    "HMC_84346135+HMC_84355350": 1108,
    "HMC_21176875+HMC_21179183": 12882,
    "HMC_84347414+HMC_84358933": 1592,
    "HMC_84347414+HMC_84355350": 2782,
    "HMC_84346135+HMC_84358933": 1810,
    "HMC_21176623+HMC_21110305": 2626,
    "HMC_84346135+HMC_84347414": 362,
    "HMC_21176623+HMC_21179183": 2110,
    "HMC_21176875+HMC_21110305": 9140,
    "HMC_84355350+HMC_84358933": 14648,
    "HMC_21110305+HMC_21179183": 35896,
    "HMC_21176875+HMC_21176623": 542,
}


def get_pred():
    """ 
    Custom your algorithm to get 3D joint coordinates from a given sample.
    input: custom by yourself
    output: 3D pose of two hands in world coordinates (21, 3)
    """
    joint_3d = np.ones((JNUM, 3))
    return joint_3d


if __name__ == '__main__':

    with open('template/assemblyhands_test_joint_3d_eccv24_pred_template.json', 'r') as f:
        kpt_pred = json.load(f)  # fill in 1.0 by default

    total_samples = 0
    for cam_pair in test_pair_stats.keys():
        camera_id_list = cam_pair.split('+')
        seq_list = kpt_pred['annotations'][cam_pair].keys()
        for seq_name in seq_list:
            for camera_id in camera_id_list:
                frame_id_list = kpt_pred['annotations'][cam_pair][seq_name][camera_id].keys()
                for frame_id in frame_id_list:
                    pts_3d_pred = get_pred()  # get your prediction
                    kpt_pred['annotations'][cam_pair][seq_name][camera_id][
                        frame_id] = pts_3d_pred.tolist()  # update the item in kpt_pred
                    total_samples += 1

    # n_samples check
    assert total_samples == sum(
        test_pair_stats.values()), "The total number of samples is not correct: {} vs {}".format(
        total_samples, sum(test_pair_stats.values()))

    output_path = 'assemblyhands_test_joint_3d_eccv24_pred.json'
    with open(output_path, 'w') as f:
        json.dump(kpt_pred, f)
    print('Dumped %d joints to %s' % (total_samples, output_path))
