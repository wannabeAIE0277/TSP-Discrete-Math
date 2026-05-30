import os
import time
from src.utils import read_tsp_file, calculate_distance_matrix, calculate_total_distance, validate_tour
from src.greedy import cheapest_insertion, nearest_neighbor

def main():
    data_path = os.path.join("data", "eil51.tsp")
    coords = read_tsp_file(data_path)
    distance_matrix = calculate_distance_matrix(coords)
    num_cities = len(coords)
    
    print("==================================================")
    print("      COMPARING GREEDY TSP APPROACHES             ")
    print("==================================================\n")
    
    #Chạy thuật toán được giao: Cheapest Insertion
    t0 = time.time()
    t_cheapest = cheapest_insertion(distance_matrix)
    dt_cheapest = (time.time() - t0) * 1000
    dist_cheapest = calculate_total_distance(t_cheapest, distance_matrix)
    v_cheapest = "YES" if validate_tour(t_cheapest, num_cities) else "NO"
    
    #Chạy Mở rộng thuật toán mở rộng: Nearest Neighbor
    t1 = time.time()
    t_nearest = nearest_neighbor(distance_matrix)
    dt_nearest = (time.time() - t1) * 1000
    dist_nearest = calculate_total_distance(t_nearest, distance_matrix)
    v_nearest = "YES" if validate_tour(t_nearest, num_cities) else "NO"
    
    # In bảng so sánh hiệu suất
    print(f"{'Approach':<25} | {'Total Distance':<15} | {'Time (ms)':<10} | {'Valid?':<6}")
    print("-" * 65)
    print(f"{'Cheapest Insertion':<25} | {dist_cheapest:<15.2f} | {dt_cheapest:<10.2f} | {v_cheapest:<6}")
    print(f"{'Nearest Neighbor':<25} | {dist_nearest:<15.2f} | {dt_nearest:<10.2f} | {v_nearest:<6}")

if __name__ == "__main__":
    main()