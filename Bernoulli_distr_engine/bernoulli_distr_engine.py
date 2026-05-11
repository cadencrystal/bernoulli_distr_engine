'''
A simple statistical model builder and visualiser
for a bernoulli/boolean distrubution 
a user will input their sample size and perceived 
successes, then the program will simulate multiple 
samples of the data and calculate confidence intervals and
other important statistical values as well as display a
histogram of the data
'''
#i want to add more inference and experimental capability to this
#things like comparing two proportions of the same sample ie male and female
#responses to the same poll, hypothesis testing, etc
#would need to add to calc class the comparison math 
#could add second proportion to the same visualizer and be able to see both

import math 
import random
import matplotlib.pyplot as plt

class SampleData:
    #taking the raw sample data and calculating p hat and q hat 
    
    def __init__(self, x_observed, n):
        self.x_observed = x_observed
        self.n = n
        
    @property #success proportion calculation
    def p_hat(self):
        return self.x_observed / self.n
    
    @property #failure calculation
    def q_hat(self):
        return 1 - self.p_hat
    
    def __str__(self):
        return f"n = {self.n}, x = {self.x_observed}, p-hat = {self.p_hat:.3f}"

class StatsCalc:
    #calculating SE and CI
    
    @staticmethod #SE
    def standard_error(p_hat, q_hat, n):
        return math.sqrt((p_hat * q_hat) / n) 
    
    @staticmethod
    def get_z(confidence_level):
        z_table = {
            0.90: 1.645,
            0.95: 1.96,
            0.99: 2.576
        }
        return z_table.get(confidence_level, 1.96)
    
    @staticmethod #confidence interval 
    def confidence_interval(p_hat, n, confidence_level = 0.95):
        z = StatsCalc.get_z(confidence_level)
        q_hat = 1 - p_hat
        se = StatsCalc.standard_error(p_hat, q_hat, n)
        margin = z * se
        return (p_hat - margin, p_hat + margin)

class SimulationEngine:
    #Simulate the distribution and calculate p hat for each simulation
    
    def __init__(self, n, p, num_simulations):
        self.n = n
        self.p = p
        self.num_simulations = num_simulations
    
    def single_sim_data(self):
        x = 0
        for _ in range(self.n):
            if random.random() < self.p:
                x += 1
        return x/self.n
    
    def multiple_simulations(self):
        sim_phat_list = []
        for _ in range(self.num_simulations):
            result = self.single_sim_data()
            sim_phat_list.append(result)
        return sim_phat_list

class Visualizer:
    #visualize the sample data and draw lines at key dat points: p hat and ci upper and lower bounds
    
    def __init__(self, results, p_hat, ci):
        self.results = results
        self.p_hat = p_hat
        self.ci = ci
    
    def plot_data(self):
        #plot based on results of simulation and put lines at p hat and CI bounds
        plt.hist(self.results, 50, alpha = 0.6)
        plt.axvline(x = self.p_hat, color = 'green', label = "Observed P hat")
        lower_ci_bound = self.ci[0]
        upper_ci_bound = self.ci[1]
        plt.axvline(x = lower_ci_bound, color = 'blue', label = "Confidence Interval")
        plt.axvline(x = upper_ci_bound, color = 'blue')
        plt.xlabel("Sample Proportion (P Hat)")
        plt.ylabel("Frequency")
        plt.title("Sampling Distribution")
        plt.legend()
        plt.show()
        
def main():
    print("Welcome to the Burnoulli Distribution Engine!")
    print()
    #user input for original data x and n
    while True:
        try:
            x = int(input("Enter number of observed successes (x): "))
            n = int(input("Enter sample size (n): "))
            if n <= 0 or x < 0 or x > n:
                raise ValueError
            raw_data = SampleData(x, n)
            break
        except ValueError as e:
            print("Invalid input ", e)
            
    #confidence level choice and input
    CL_options = {
        "1": 0.90,
        "2": 0.95,
        "3": 0.99
    }
    print("\nChoose a confidence level:")
    print("(1) 90%")
    print("(2) 95%")
    print("(3) 99%")
    
    user_CL = input("Enter a choice (1-3): ")
    confidence_level = CL_options.get(user_CL, 0.95)
    
    ci = StatsCalc.confidence_interval(raw_data.p_hat, raw_data.n, confidence_level)
    print(raw_data)
    print(f"Sample CI: ({ci[0]:.4f}, {ci[1]:.4f})")
    
    #user input and display of simulations and simulator data
    print()
    print("Simulating multiple instances of Bernoulli Distribution based on prevciously entered data")
    while True:
        try:
            num_simulations = int(input("Enter number of simulations you would like to run: "))
            if num_simulations <= 0:
                raise ValueError("Number of simulations must be greater than 0")
            if num_simulations > 5000:
                print("Simulations capped at 5,000")
                num_simulations = 5000
            break
        except ValueError:
            print("Invalid input", e)
        
    simulation = SimulationEngine(raw_data.n, raw_data.p_hat, num_simulations)
    results = simulation.multiple_simulations()
    mean_p_hat = sum(results)/len(results)
    print(f"Mean P hat of simulations: {mean_p_hat:.4f}")
    
    #Visualize the data from the simulation
    print()
    print("Visualizing data.")    
    viz = Visualizer(results, raw_data.p_hat, ci)
    viz.plot_data()
    
if __name__ == "__main__":
    main()