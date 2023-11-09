<<<<<<< HEAD
# Applications-of-Networks
University of Pittsburgh
=======
## Discrete Event Simulator

This is a Python-based packet queue simulator that allows you to study the behavior of a packet queue with different  
combinations of arrival rates, departure rates, and buffer sizes.


There are two programs implemented to handle the two experiment for the constant inputs  of for every 1000000 events.  
It is the `constant_rate_queue_simulator.py` and the `variable_rate_queue_simulator..py` for the constant departure rate  
and buffer size, but the variable arrival rate for variable rate of events for 1000000 events


1. Download the  

     a)`constant_rate_queue_simulator.py`
     b)`variable_rate_queue_simulator.py`


2. Install the required libraries (if not already installed) using pip:

   ```bash
   pip install matplotlib
   
## 1. constant_rate_queue_simulator.py 

**Run it with the following command-line arguments:**

--arrival_rates: Arrival rates as a single value or comma-separated values.  
--departure_rates: Departure rates as a single value or comma-separated values.  
--buffer_sizes: Buffer sizes as a single value or comma-separated values.  
--num_events: Number of events to simulate.

### For a single combination of values:

```bash

python3 constant_rate_queue_simulator.py --arrival_rates 25 --departure_rates 60 --buffer_sizes 60 --num_events 100000
```
### For multiple combinations of values:

```bash

python3 constant_rate_queue_simulator.py --arrival_rates 25,75,125 --departure_rates 60,100,125 --buffer_sizes 60,100,125 --num_events 100000
````
## 2. variable_rate_queue_simulator.py 

**Run it with the following command-line arguments:**

--arrival_rates: Arrival rates as a single value or multiple.  
--departure_rates: Departure rates as a single value.  
--buffer_sizes: Buffer sizes as a single value.  
--num_events: Number of events to simulate.  
--event_rate: Event percentage fro every arrival rate.

**cmd code**
``` bash
python3 variable_rate_queue_simulator.py --arrival_rates 70 200 130 120 70 --departure_rate 125 --buffer_size 100 --num_events 1000000 --event_rates "10-70" "70-80" "80-90" "90-100"
```

#### The simulator will generate plots showing the behavior of the packet queue for the specified parameter combinations.

#### You can customize the parameters, such as the number of events and the range of values, to study different scenarios.

#### Application of Networks - Project 1 
#### Jeeva Krishnasamy
>>>>>>> 3876fde (Initial commit)
