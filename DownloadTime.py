
try:
    size_gb = float(input("Enter the size of the file in gigabytes: "))
    speed_mb_per_s = float(input("Enter your download speed in MB per second: "))
    
    if size_gb <= 0 or speed_mb_per_s <= 0:
        raise ValueError("Size and speed must be positive numbers.")

    
    size_mb = size_gb * 1024

    
    time_minutes = size_mb / speed_mb_per_s /60
    
    
    hours = int(time_minutes / 60)
    minutes = int(time_minutes % 60)
    seconds = int((time_minutes * 60) % 60)  

    # Print the result
    print(f"Estimated download time: {hours} hour(s), {minutes} minute(s), and {seconds} second(s)")

except ValueError as e:
    print(f"Error: {e}")
