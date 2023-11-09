import random
import matplotlib.pyplot as plt
import argparse

class PacketQueueSimulator:
    def __init__(self, arrival_rates, departure_rate, buffer_size, num_events):
        self.arrival_rates = arrival_rates
        self.departure_rate = departure_rate
        self.buffer_size = buffer_size
        self.packets_in_queue = 0
        self.packets_dropped = 0
        self.time_steps = []  # To track time steps
        self.queue_sizes = []  # To track queue sizes
        self.dropped_events = []  # To track dropped events
        self.num_events = num_events

    def simulate_event(self, event_rate_range):
        max_rate = event_rate_range
        for time_step in range(self.num_events):
            # Determine the current event percentage
            current_event_percentage = (time_step / self.num_events) * 100

            # Check if the current event rate falls within the specified range
            if current_event_percentage <= max_rate:
                # Calculate arrival rate based on the current event percentage
                arrival_rate = self.get_arrival_rate(current_event_percentage)

                probability_arrival = arrival_rate / (self.departure_rate + arrival_rate)
                probability_departure = 1 - probability_arrival

                random_number = random.random()

                if random_number <= probability_arrival:
                    # Packet arrival event
                    if self.packets_in_queue < self.buffer_size:
                        self.packets_in_queue += 1
                    else:
                        self.packets_dropped += 1
                else:
                    # Packet departure event
                    if self.packets_in_queue > 0:
                        self.packets_in_queue -= 1

            self.time_steps.append(time_step)
            self.queue_sizes.append(self.packets_in_queue)
            self.dropped_events.append(self.packets_dropped)

    def get_arrival_rate(self, event_percentage):
        if event_percentage < 10:
            return self.arrival_rates[0]
        elif event_percentage < 70:
            return self.arrival_rates[1]
        elif event_percentage < 80:
            return self.arrival_rates[2]
        elif event_percentage < 90:
            return self.arrival_rates[3]
        else:
            return self.arrival_rates[4]

def plot_simulation_results(simulator, title):
    plt.figure(figsize=(10, 8))
    plt.plot(simulator.time_steps, simulator.queue_sizes, linestyle='--', color='green',
             label=f"Packets in the Queue")

    # Plot the time steps when packets were dropped as a solid blue line
    plt.plot(simulator.time_steps, simulator.dropped_events, linestyle='-', color='blue',
             label=f"Packets Dropped from Queue")

    plt.xlabel("Simulated Events")
    plt.ylabel("Number of Packets")
    plt.title(f"{title}")
    plt.legend()
    plt.grid(True)
    plt.show()  # Display the plot on the screen
    plt.savefig("Variable_input_event.png")  # Save the plot to a file
    plt.close()  # Close the plot window



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Packet Queue Simulator")

    parser.add_argument("--arrival_rates", nargs="+", type=int, required=True,
                        help="List of arrival rates for different event percentages")
    parser.add_argument("--departure_rate", type=int, required=True,
                        help="Departure rate (μ)")
    parser.add_argument("--buffer_size", type=int, required=True,
                        help="Buffer size (n)")
    parser.add_argument("--num_events", type=int, required=True,
                        help="Number of events to simulate")
    parser.add_argument("--event_rates", nargs="+", type=str, required=True,
                        help="List of event rate ranges (e.g., '10-70 70-80 80-90 90-100')")

    args = parser.parse_args()

    arrival_rates = args.arrival_rates
    departure_rate = args.departure_rate
    buffer_size = args.buffer_size
    num_events = args.num_events
    event_ranges = [max(int(rate.split('-')[1]) for rate in args.event_rates)]


    for event_range in event_ranges:
        simulator = PacketQueueSimulator(arrival_rates, departure_rate, buffer_size, num_events)
        simulator.simulate_event(event_range)
        plot_title = (f"Simulation Results - Variable input with Events"
                      f"\nArrival Rates={arrival_rates},Departure Rate={departure_rate}, Buffer Size={buffer_size}")
        plot_simulation_results(simulator, plot_title)

# command line program to run the program.
# python3 variable_rate_queue_simulator.py --arrival_rates 70 200 130 120 70 --departure_rate 125 --buffer_size 100 --num_events 1000000 --event_rates "10-70" "70-80" "80-90" "90-100"