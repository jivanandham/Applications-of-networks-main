import random
import matplotlib.pyplot as plt
import argparse
from itertools import product

# Define a class for the packet queue simulator
class PacketQueueSimulator:
    def __init__(self, arrival_rate, departure_rate, buffer_size, num_events):
        self.arrival_rate = arrival_rate
        self.departure_rate = departure_rate
        self.buffer_size = buffer_size
        self.num_events = num_events
        self.reset()

    def reset(self):
        # Reset simulation variables
        self.packets_in_queue = 0
        self.packets_dropped = 0
        self.time_steps = []
        self.queue_sizes = []
        self.dropped_events = []

    def simulate_event(self):
        # Simulate events based on arrival and departure rates
        for time_step in range(self.num_events):
            probability_arrival = self.arrival_rate / (self.departure_rate + self.arrival_rate)
            probability_departure = 1 - probability_arrival

            random_number = random.random()

            if random_number <= probability_arrival:
                if self.packets_in_queue < self.buffer_size:
                    self.packets_in_queue += 1
                else:
                    self.packets_dropped += 1
            else:
                if self.packets_in_queue > 0:
                    self.packets_in_queue -= 1

            # Collect data for plotting
            self.time_steps.append(time_step)
            self.queue_sizes.append(self.packets_in_queue)
            self.dropped_events.append(self.packets_dropped)

# Function to plot simulation results
def plot_simulation_results(simulator, title, combination_number):
    plt.figure(figsize=(10, 8))
    plt.plot(simulator.time_steps, simulator.queue_sizes, linestyle='--', color='green',
             label="Packets in the Queue")
    plt.plot(simulator.time_steps, simulator.dropped_events, linestyle='-', color='blue',
             label="Packets Dropped from Queue")
    plt.xlabel("Simulated Events")
    plt.ylabel("Number of Packets")
    plt.title(f"Combination {combination_number} - {title}")
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.savefig(f"Constant_input_{combination_number}.png")
    plt.close()

# Function to parse input arguments
def parse_arg_list(input_str):
    if ',' in input_str:
        return [int(x) for x in input_str.split(',')]
    return int(input_str)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Packet Queue Simulator")
    parser.add_argument("--arrival_rates", type=parse_arg_list, required=True,
                        help="Arrival rates as single value or comma-separated values")
    parser.add_argument("--departure_rates", type=parse_arg_list, required=True,
                        help="Departure rates as single value or comma-separated values")
    parser.add_argument("--buffer_sizes", type=parse_arg_list, required=True,
                        help="Buffer sizes as single value or comma-separated values")
    parser.add_argument("--num_events", type=int, required=True,
                        help="Number of events to simulate")
    args = parser.parse_args()

    if isinstance(args.arrival_rates, list):
        # If multiple input values are provided, create combinations
        arrival_rates = [int(rate) for rate in args.arrival_rates]
        departure_rates = [int(rate) for rate in args.departure_rates]
        buffer_sizes = [int(size) for size in args.buffer_sizes]

        combinations = list(product(arrival_rates, departure_rates, buffer_sizes))
        num_combinations = len(combinations)

        for idx, combo in enumerate(combinations, start=1):
            lambda_val, mu_val, buffer_size = combo
            simulator = PacketQueueSimulator(lambda_val, mu_val, buffer_size, args.num_events)
            simulator.simulate_event()
            plot_title = (f"Simulation Results - Arrival Rate={lambda_val}, Departure Rate={mu_val}, Buffer={buffer_size}")
            plot_simulation_results(simulator, plot_title, idx)
    else:
        # Run the simulation once for single values
        simulator = PacketQueueSimulator(args.arrival_rates, args.departure_rates, args.buffer_sizes, args.num_events)
        simulator.simulate_event()
        plot_title = f"Simulation Results - Arrival Rate={args.arrival_rates}, Departure Rate={args.departure_rates}, Buffer Size={args.buffer_sizes}"
        plot_simulation_results(simulator, plot_title, 1)


# For a single combination of values: run the below cmd
# python3 constant_rate_queue_cmd2.py --arrival_rate 25 --departure_rate 60 --buffer_size 60 --num_events 1000000

# For a multiple combination of values: run the below cmd
# python3 constant_rate_queue_cmd2.py --arrival_rate 25,75,125 --departure_rate 60,100,125 --buffer_size 60,100,150 --num_events 1000000
