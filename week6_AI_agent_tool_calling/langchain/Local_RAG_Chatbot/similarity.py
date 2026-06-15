import numpy as np


def cosine_similarity(
        vector1,
        vector2):

    v1 = np.array(
        vector1
    )

    v2 = np.array(
        vector2
    )

    numerator = np.dot(
        v1,
        v2
    )

    denominator = (
        np.linalg.norm(v1)
        *
        np.linalg.norm(v2)
    )

    if denominator == 0:

        return 0.0

    return (
        numerator
        / denominator
    )