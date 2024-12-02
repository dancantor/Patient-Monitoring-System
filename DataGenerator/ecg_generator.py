import neurokit2 as nk  # Load the package

# simulated_ecg = nk.ecg_simulate(duration=8, sampling_rate=200, heart_rate=80)
#
# nk.signal_plot(simulated_ecg, sampling_rate=200)  # Visualize the signal
#
# processed_ecg = nk.ecg_process(simulated_ecg, sampling_rate=200)  # Process the signal

simulated_ecg = nk.ecg_simulate(duration=8, sampling_rate=200, method="daubechies")

nk.signal_plot(simulated_ecg, sampling_rate=200)