import os
import time
from src.utils import read_tsp_file, calculate_distance_matrix, calculate_total_distance, validate_tour
from src.greedy import cheapest_insertion, nearest_neighbor
from src.local_search import node_swap, two_opt

def main():
    tsp_files = ["eil51.tsp", "kroA100.tsp", "ch150.tsp"]
    
    #Danh sách cấu hình tự động: Tên hiển thị, Hàm Greedy, Hàm Local Search
    configs = [
        ('Greedy 1 (Cheapest Insertion)', cheapest_insertion, None),
        ('Greedy 1 + Local Search (Swap)', cheapest_insertion, node_swap),
        ('Greedy 1 + Local Search (2-opt)', cheapest_insertion, two_opt),
        ('Greedy 2 (Nearest Neighbor)', nearest_neighbor, None),
        ('Greedy 2 + Local Search (Swap)', nearest_neighbor, node_swap),
        ('Greedy 2 + Local Search (2-opt)', nearest_neighbor, two_opt)
    ]
    
    for filename in tsp_files:
        data_path = os.path.join("data", filename)
        if not os.path.exists(data_path):
            continue
            
        coords = read_tsp_file(data_path)
        num_cities = len(coords)
        if num_cities < 2:
            continue
            
        distance_matrix = calculate_distance_matrix(coords)
        
        print("\n" + "="*80)
        print(f"      EXPERIMENTAL RESULTS FOR DATASET: {filename.upper()} ({num_cities} Cities)")
        print("="*80)
        print(f"{'Cách tiếp cận (Approach)':<35} | {'Tổng quãng đường':<16} | {'Thời gian (ms)':<14} | {'Valid?'}")
        print("-" * 80)
        
        #Vòng lặp tự động chạy qua từng cấu hình thuật toán
        for name, tour_builder, local_search in configs:
            start_time = time.time()
            
            #Khởi tạo và tối ưu hóa lộ trình
            tour = tour_builder(distance_matrix)
            if local_search:
                tour = local_search(tour, distance_matrix)
                
            exec_time = (time.time() - start_time) * 1000
            dist = calculate_total_distance(tour, distance_matrix)
            valid = "YES" if validate_tour(tour, num_cities) else "NO"
            
            print(f"{name:<35} | {dist:<16.2f} | {exec_time:<14.2f} | {valid}")
        print("="*80)

if __name__ == "__main__":
    main()