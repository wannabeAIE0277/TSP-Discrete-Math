from src.utils import calculate_total_distance
def node_swap(tour, distance_matrix):
    """
    Thuật toán được giao:Node Swap (Thuật toán Hoán đổi 2 Đỉnh) 
    """
    best_tour = tour.copy()
    best_dist = calculate_total_distance(best_tour, distance_matrix)
    improved = True
    
    #Vòng lặp chạy liên tục cho đến khi KHÔNG tối ưu thêm được nữa
    while improved:
        improved = False
        num_cities = len(best_tour)
        
        #Duyệt qua mọi cặp vị trí (i, j) bất kỳ trong lộ trình
        for i in range(num_cities):
            for j in range(i + 1, num_cities):
                new_tour = best_tour.copy()
                
                #Đổi chỗ vị trí của 2 thành phố
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                
                #Tính tổng quãng đường sau khi đổi chỗ
                new_dist = calculate_total_distance(new_tour, distance_matrix)
                
                #Nếu lộ trình mới ngắn hơn, giữ lại ngay lập tức
                if new_dist < best_dist:
                    best_tour = new_tour
                    best_dist = new_dist
                    improved = True  # Đặt cờ báo hiệu đã tìm thấy đường tốt hơn
                    break            # Phá vòng lặp trong để bắt đầu quét lại từ đầu
            if improved:
                break
                
    return best_tour


def two_opt(tour, distance_matrix):
    """
    Thuật toán mở rộng: 2-opt (Thuật toán gỡ chéo cạnh)
    """
    best_tour = tour.copy()
    best_dist = calculate_total_distance(best_tour, distance_matrix)
    improved = True
    
    while improved:
        improved = False
        num_cities = len(best_tour)
        
        #Duyệt tìm 2 cạnh không kề nhau để cắt
        for i in range(1, num_cities - 1):
            for j in range(i + 1, num_cities):
                if j - i == 1: #kề nhau thì hiệu vị chí sẽ = 1
                    continue  # Bỏ qua các cạnh kề nhau
                
                new_tour = best_tour.copy()
                #Cắt và đảo ngược đoạn đường nằm giữa i và j
                new_tour[i:j+1] = reversed(new_tour[i:j+1])
                
                new_dist = calculate_total_distance(new_tour, distance_matrix)
                
                if new_dist < best_dist:
                    best_tour = new_tour
                    best_dist = new_dist
                    improved = True
                    break
            if improved:
                break
                
    return best_tour