import sys
import random
import statistics

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python simulator.py num_points")
    
    try:
        num = int(sys.argv[1])
        if num <= 0:
            raise ValueError
    except ValueError:
        sys.exit("Invalid number")
    
    data = []
    for _ in range(num):
        sales = random.randint(10, 100)
        category = random.choice(["low", "medium", "high"])
        data.append({"sales": sales, "category": category})
    
    # Write to file
    with open("data.txt", "w") as file:
        for item in data:
            file.write(f"{item['sales']},{item['category']}\n")
    
    # Read back
    read_data = []
    with open("data.txt", "r") as file:
        for line in file:
            try:
                sales_str, cat = line.strip().split(",")
                sales = int(sales_str)
                read_data.append(sales)
            except:
                print("Invalid line, skipping")
    
    if read_data:
        avg = statistics.mean(read_data)
        print(f"Average sales: {round(avg, 2)}")
        
        # Sorted and categorize with match (Python 3.10+)
        sorted_data = sorted(read_data)
        for val in sorted_data:
            match val:
                case v if v < 30:
                    print(f"{v}: Low")
                case v if v < 70:
                    print(f"{v}: Medium")
                case _:
                    print(f"{v}: High")

if __name__ == "__main__":
    main()
