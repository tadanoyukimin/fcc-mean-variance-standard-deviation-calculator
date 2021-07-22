import numpy as np



def calculate(calculate_list):
    if len(calculate_list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
    # make 3x3 matrix
        output_array = np.array(calculate_list).reshape(3, 3)

    output_dict = {
        "mean": [np.mean(output_array, axis=0).tolist(), np.mean(output_array, axis=1), np.mean(calculate_list)],
        "variance": [np.var(output_array, axis=0).tolist(), np.var(output_array, axis=1), np.var(calculate_list)],
        "standard deviation": [np.std(output_array, axis=0).tolist(), np.std(output_array, axis=1).tolist(), np.std(calculate_list)],
        "max": [np.max(output_array, axis=0).tolist(), np.max(output_array, axis=1).tolist(), np.max(calculate_list)],
        "min": [np.min(output_array, axis=0).tolist(), np.min(output_array, axis=1).tolist(), np.min(calculate_list)],
        "sum": [np.sum(output_array, axis=0).tolist(), np.sum(output_array, axis=1).tolist(), np.sum(calculate_list)],
    }

    # first attempt
    # mean_output_axis1 = np.mean(output_array, axis=0).tolist()
    # mean_output_axis2 = np.mean(output_array, axis=1).tolist()
    # mean_output_flattened = np.mean(calculate_list).tolist()
    # output_dict["mean"].append(mean_output_axis1)
    # output_dict["mean"].append(mean_output_axis2)
    # output_dict["mean"].append(mean_output_flattened)

    # variance_output_axis1 = np.var(output_array, axis=0).tolist()
    # variance_output_axis2 = np.var(output_array, axis=1).tolist()
    # variance_output_flattened = np.var(calculate_list).tolist()
    # output_dict["variance"].append(variance_output_axis1)
    # output_dict["variance"].append(variance_output_axis2)
    # output_dict["variance"].append(variance_output_flattened)

    # sd_output_axis1 = np.std(output_array, axis=0).tolist()
    # sd_output_axis2 = np.std(output_array, axis=1).tolist()
    # sd_output_flattened = np.std(calculate_list).tolist()
    # output_dict["standard deviation"].append(sd_output_axis1)
    # output_dict["standard deviation"].append(sd_output_axis2)
    # output_dict["standard deviation"].append(sd_output_flattened)

    # max_output_axis1 = np.max(output_array, axis=0).tolist()
    # max_output_axis2 = np.max(output_array, axis=1).tolist()
    # max_output_flattened = np.max(calculate_list).tolist()
    # output_dict["max"].append(max_output_axis1)
    # output_dict["max"].append(max_output_axis2)
    # output_dict["max"].append(max_output_flattened)

    # min_output_axis1 = np.min(output_array, axis=0).tolist()
    # min_output_axis2 = np.min(output_array, axis=1).tolist()
    # min_output_flattened = np.min(calculate_list).tolist()
    # output_dict["min"].append(min_output_axis1)
    # output_dict["min"].append(min_output_axis2)
    # output_dict["min"].append(min_output_flattened)

    # sum_output_axis1 = np.sum(output_array, axis=0).tolist()
    # sum_output_axis2 = np.sum(output_array, axis=1).tolist()
    # sum_output_flattened = np.sum(calculate_list).tolist()
    # output_dict["sum"].append(sum_output_axis1)
    # output_dict["sum"].append(sum_output_axis2)
    # output_dict["sum"].append(sum_output_flattened)

    return output_dict


print(calculate([2,6,2,8,4,0,1,5,2]))