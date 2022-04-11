import matplotlib
import matplotlib.pyplot as plt


def condition_1_hop_freq():
    x_c1 = ['hop', 'not hop']
    y_c1 = [0.9792, 1.0]

    # plt.figure(figsize=(4, 4))
    plt.bar(x=x_c1, height=y_c1, width=0.4)

    for _x, _y in zip(x_c1, y_c1):
        plt.text(_x, _y + 0.01, str(_y), ha='center', va='bottom', fontsize=10, rotation=0)

    plt.title('Condition 1: Hop Freq')
    plt.xlabel('Hop')
    plt.ylabel('Accuracy')
    plt.show()


def condition_2_rotation_level():
    x_c1 = ['level 1', 'level 2', 'level 3', 'level 4']
    y_c1 = [1.0, 1.0, 1.0, 1.0]

    # plt.figure(figsize=(4, 4))
    plt.bar(x=x_c1, height=y_c1, width=0.4)

    for _x, _y in zip(x_c1, y_c1):
        plt.text(_x, _y + 0.01, str(_y), ha='center', va='bottom', fontsize=10, rotation=0)

    plt.title('Condition 2: Rotation Level')
    plt.xlabel('Rotation Level')
    plt.ylabel('Accuracy')
    plt.show()


def condition_3_object_distance():
    x_c1 = ['distance 1', 'distance 2', 'distance 3', 'distance 4']
    y_c1 = [1.0, 0.8194, 1.0, 0.8347]

    # plt.figure(figsize=(4, 4))
    plt.bar(x=x_c1, height=y_c1, width=0.4)

    for _x, _y in zip(x_c1, y_c1):
        plt.text(_x, _y + 0.01, str(_y), ha='center', va='bottom', fontsize=10, rotation=0)

    plt.title('Condition 3: Object Distance')
    plt.xlabel('Object Distance')
    plt.ylabel('Accuracy')
    plt.show()


def condition_5_tag_type():
    x_c1 = ['type 1', 'type 2']
    y_c1 = [1.0, 0.8347]

    # plt.figure(figsize=(4, 4))
    plt.bar(x=x_c1, height=y_c1, width=0.4)

    for _x, _y in zip(x_c1, y_c1):
        plt.text(_x, _y + 0.01, str(_y), ha='center', va='bottom', fontsize=10, rotation=0)

    plt.title('Condition 5: Tag Type')
    plt.xlabel('Tag Type')
    plt.ylabel('Accuracy')
    plt.show()


def condition_6_interfer_tag_numbers():
    x_c1 = ['interfer 1', 'interfer 2', 'interfer 3', 'interfer 4']
    y_c1 = [1.0, 1.0, 1.0, 1.0]

    # plt.figure(figsize=(4, 4))
    plt.bar(x=x_c1, height=y_c1, width=0.4)

    for _x, _y in zip(x_c1, y_c1):
        plt.text(_x, _y + 0.01, str(_y), ha='center', va='bottom', fontsize=10, rotation=0)

    plt.title('Condition 6: Interfer Tag Numbers')
    plt.xlabel('Interfer Tag Numbers')
    plt.ylabel('Accuracy')
    plt.show()


if __name__ == '__main__':
    condition_6_interfer_tag_numbers()
