v_pool = int(input())
pipe_1_per_hour = int(input())
pipe_2_per_hour = int(input())
hours_without_worker = float(input())

debit_pipe_1 = hours_without_worker * pipe_1_per_hour
debit_pipe_2 = hours_without_worker * pipe_2_per_hour

total_debit = debit_pipe_1 + debit_pipe_2
total_percent = (total_debit * 100) / v_pool
pipe_1_percent = (debit_pipe_1 * 100) / total_debit
pipe_2_percent = (debit_pipe_2 * 100) / total_debit
overflow_pool = total_debit - v_pool

if v_pool >= total_debit:
    print(f"The pool is {total_percent:.2f}% full. Pipe 1: {pipe_1_percent:.2f}%. Pipe 2: {pipe_2_percent:.2f}%.")
elif v_pool < total_debit:
    print(f"For {hours_without_worker:.2f} hours the pool overflows with {overflow_pool:.2f} liters.")
