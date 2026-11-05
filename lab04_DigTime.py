# Digital Time and Resource Calculator

total_seconds = 10000

# Convert seconds into days, hr, min and sec
days = total_seconds // 86400
remaining_seconds = total_seconds % 86400

hours = remaining_seconds // 3600
remaining_seconds = remaining_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# Cal complete 45-min lab sessions
session_time = 45 * 60

complete_sessions = total_seconds // session_time
leftover_time = total_seconds % session_time

# Cal time required for the next session
remaining_for_next = session_time - leftover_time

# Display output
print("----- Digital Time and Resource Calculator -----")

print(f"Total Seconds: {total_seconds}")
print(f"Equivalent Time: {days} Days, {hours} Hours, {minutes} Minutes, {seconds} Seconds")

print(f"Complete Lab Sessions: {complete_sessions}")
print(f"Unused Time: {leftover_time} Seconds")
print(f"Time Required for Next Session: {remaining_for_next} Seconds")
