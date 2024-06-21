volume = int(input())
pipe1_flow_rate = int(input())
pipe2_flow_rate = int(input())
hours_absent = float(input())

total_flow_rate = pipe1_flow_rate + pipe2_flow_rate
total_filled_volume = total_flow_rate * hours_absent

if total_filled_volume <= volume:
    percent_filled = total_filled_volume / volume * 100
    percent_pipe1 = pipe1_flow_rate / total_flow_rate * 100
    percent_pipe2 = pipe2_flow_rate / total_flow_rate * 100
    print(f"The pool is {percent_filled:.2f}% full. Pipe 1: {percent_pipe1:.2f}%. Pipe 2: {percent_pipe2:.2f}%.")
else:
    overflow_volume = total_filled_volume - volume
    print(f"For {hours_absent:.2f} hours the pool overflows with {overflow_volume:.2f} liters.")