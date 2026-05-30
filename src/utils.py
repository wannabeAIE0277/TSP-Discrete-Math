import math
#Khởi tạo hàm đọc các file .tsp
def read_tsp_file(filepath):
    #Khởi tạo kho chứa coordinates
    coords = {}

    #Mở file và đưa toàn bộ các dòng vào kho chứa
    with open(filepath, 'r') as file: #Tham số filepath ứng với (tên file).tsp
        lines = file.readlines()    #đưa tất cả các dòng vào 1 list "lines", mỗi dòng là 1 phần tử

    #Duyệt từng dòng
    node_coord_start = False    #Check xem đã đến phần số liệu chính chưa
    for line in lines:      #Đi qua tất cả các dòng trong list "lines" vừa khởi tạo
        line = line.strip() #Xóa khoảng trống đầu cuối
        
        #Bỏ qua dòng trống
        if not line: continue
            
        #Tìm "lệnh mở cửa" để bật cờ hiệu
        if "NODE_COORD_SECTION" in line:    #Báo hiệu sau dòng "NODE_COORD_SECTION" sẽ là số liệu cần xử lí
            node_coord_start = True
            continue
            
        #Gặp chữ EOF thì dừng
        if "EOF" in line: break
            
        #Khi tín hiệu đã là True, bắt đầu xử lí dòng chứa số liệu
        if node_coord_start:
            parts = line.split()    #Chia dòng số liệu làm 3 phần: [id,x,y]
            node_id = int(parts[0]) - 1  #Đổi về chỉ số từ 0
            x = float(parts[1])      #Giá trị x về dạng float
            y = float(parts[2])      #Giá trị y về dạng float
            
            #Cất vào kho chứa
            coords[node_id] = (x, y)
            
    return coords

#Khởi tạo hàm tính khoảng cách giữa các điểm
def calculate_distance_matrix(coords):
    num_cities = len(coords)

    #Tạo một lưới vuông toàn số 0 kích thước N*N
    matrix = [[0.0] * num_cities for _ in range(num_cities)]
    
    #Hai vòng lặp lồng nhau để tính khoảng cách giữa từng thành phố
    for i in range(num_cities):
        for j in range(i+1,num_cities):
            if i != j:
                x1, y1 = coords[i]
                x2, y2 = coords[j]
                
                # Công thức Euclid tính khoảng cách hình học
                distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                
                # Làm tròn thành số nguyên theo chuẩn TSPLIB
                matrix[i][j] = round(distance)
                matrix[j][i] = round(distance)
    return matrix

#Khởi tạo hàm tính tổng đường đi
def calculate_total_distance(tour, distance_matrix):
    total = 0
    num_cities = len(tour)
    
    for i in range(num_cities):
        city_from = tour[i]
        city_to = tour[(i + 1) % num_cities] #Sử dụng modulo này để khi i = 50 thì sẽ tính khoảng cách giữa thành phố cuối và thành phố đầu
        total += distance_matrix[city_from][city_to]
        
    return total

#Khởi tạp hàm kiểm tra tính chính xác của thuật toán
def validate_tour(tour, num_cities):
    #ĐK1: Kiểm tra tổng số lượng phần tử
    if len(tour) != num_cities:
        print(f"Validation Failed: Tour length ({len(tour)}) does not match number of cities ({num_cities}).")
        return False
        
    #ĐK2: Kiểm tra trùng lặp bằng Set để đảm bảo không chứa chu trình con
    unique_cities = set(tour)
    if len(unique_cities) != num_cities:
        print("Validation Failed: Tour contains duplicate cities or missing cities.")
        return False
        
    #ĐK3: Kiểm tra xem có bỏ sót thành phố cụ thể nào không
    for city in range(num_cities):
        if city not in unique_cities:
            print(f"Validation Failed: City {city} is missing from the tour.")
            return False
            
    return True