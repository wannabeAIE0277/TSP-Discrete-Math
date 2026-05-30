def cheapest_insertion(distance_matrix):
    """
    Thuật toán Tham lam: Cheapest Insertion (Nhiệm vụ bắt buộc)
    Vào: Ma trận khoảng cách (Mảng 2 chiều)
    Ra: Lộ trình chu trình Hamilton (List các ID thành phố)
    """
    num_cities = len(distance_matrix)
    visited = [False] * num_cities
    
    #Khởi tạo chu trình ban đầu với 2 thành phố đầu tiên (0 và 1)
    tour = [0, 1]
    #Cho rằng 2 thành phố đầu tiên (0 và 1) đã được đi qua
    visited[0] = True   
    visited[1] = True
    
    #Vòng lặp chèn 49 thành phố còn lại vào chu trình
    for _ in range(num_cities - 2):
        best_city = None
        best_position = -1
        min_increment = float('inf')
        
        #Duyệt qua từng thành phố chưa đi (k)
        for k in range(num_cities):
            if not visited[k]:
                #Tìm vị trí chèn tối ưu trong chu trình hiện tại
                for i in range(len(tour)):
                    j = (i + 1) % len(tour) #Dùng modulo để kết nối city cuối và đầu
                    city_i = tour[i]
                    city_j = tour[j]
                    
                    #Tính chi phí phát sinh (quãng đường tăng thêm)
                    cost = distance_matrix[city_i][k] + distance_matrix[k][city_j] - distance_matrix[city_i][city_j]
                    
                    #Nếu quãng đường thêm hiện tại bé hơn thì sẽ cập nhật các biến best
                    if cost < min_increment:
                        min_increment = cost
                        best_city = k
                        best_position = i + 1
        
        #Chèn thành phố có chi phí thấp nhất vào vị trí tốt nhất tìm được
        tour.insert(best_position, best_city) #Thêm vị trí tốt nhất vào vị trí tốt nhất tìm được
        visited[best_city] = True   #Đánh dấu thành phố vừa đi qua
        
    return tour

def nearest_neighbor(distance_matrix, start_city=0):
    """
    Nhiệm vụ mở rộng: Thuật toán Kẻ cận thị
    Độ phức tạp thời gian: O(N^2)
    """
    num_cities = len(distance_matrix)
    visited = [False] * num_cities
    
    # Xuất phát từ thành phố được chỉ định (mặc định là thành phố 0)
    tour = [start_city]
    visited[start_city] = True
    current_city = start_city
    
    # Vòng lặp tìm N-1 thành phố còn lại
    for _ in range(num_cities - 1):
        nearest_city = None
        min_dist = float('inf')
        
        # Quét tìm thành phố chưa đi có khoảng cách ngắn nhất đến current_city
        for next_city in range(num_cities):
            if not visited[next_city] and distance_matrix[current_city][next_city] < min_dist:
                min_dist = distance_matrix[current_city][next_city]
                nearest_city = next_city
                
        # Di chuyển đến thành phố lân cận gần nhất đó
        tour.append(nearest_city)
        visited[nearest_city] = True
        current_city = nearest_city
        
    return tour