import neurokit2 as nk
import numpy as np


def compute_segment(signals, start_metric, end_metric):
    # Extract the indices where start_metric and end_metric are not zero
    start_indices = np.where(signals[start_metric] != 0)[0]
    end_indices = np.where(signals[end_metric] != 0)[0]

    # Truncate the longer array to match the length of the shorter one
    min_length = min(len(start_indices), len(end_indices))
    start_indices = start_indices[:min_length]
    end_indices = end_indices[:min_length]

    return end_indices - start_indices

def generate_segments(duration=3600):
    sampling_rate = 1000

    ecg = nk.ecg_simulate(duration=duration, sampling_rate=sampling_rate)
    nk.signal_plot(ecg, sampling_rate=sampling_rate)

    signals, _ = nk.ecg_process(ecg, sampling_rate=sampling_rate)

    # COMPUTE PR SEGMENT
    PR_segment = compute_segment(signals, 'ECG_P_Onsets', 'ECG_R_Onsets')

    # COMPUTE QRS SEGMENT
    QRS_segment = compute_segment(signals, 'ECG_R_Onsets', 'ECG_R_Offsets')

    # COMPUTE ST SEGMENT
    ST_segment = compute_segment(signals, 'ECG_R_Offsets', 'ECG_T_Onsets')

    return {
            "PR_segment": PR_segment,
            "QRS_segment": QRS_segment,
            "ST_segment": ST_segment
        }

