# Algorithmic Approaches to the Travelling Salesman Problem (TSP)

Dự án thực nghiệm và tối ưu hóa bài toán Người đi du lịch (TSP) thuộc học phần Toán rời rạc. Dự án triển khai các phương pháp tiếp cận từ thuật toán Tham lam (Greedy) cho đến các chiến lược Tìm kiếm cục bộ (Local Search) trên các bộ dữ liệu chuẩn từ thư viện TSPLIB.

---

## Cấu trúc thư mục (Project Structure)

├── data/                  # Nơi lưu trữ các file dữ liệu cấu hình .tsp
│   ├── eil51.tsp          # Bộ dữ liệu cơ sở 51 thành phố
│   ├── kroA100.tsp        # Bộ dữ liệu 100 thành phố
│   └── ch150.tsp          # Bộ dữ liệu 150 thành phố
├── src/                   # Thư mục chứa mã nguồn thuật toán
│   ├── __init__.py        # Kích hoạt Python package
│   ├── utils.py           # Bộ công cụ (Đọc file, lập ma trận, tính tổng quãng đường, validate)
│   ├── greedy.py          # Thuật toán tham lam (Cheapest Insertion & Nearest Neighbor)
│   └── local_search.py    # Thuật toán tối ưu (Node Swap & 2-opt)
├── main.py                # File điều phối chính và xuất báo cáo thực nghiệm
└── README.md              # File hướng dẫn tổng quan dự án

---

## Hướng dẫn thực thi (How to Run)

1. Cài đặt và chuẩn bị
Đảm bảo máy tính đã cài đặt Python (Phiên bản khuyến nghị >= 3.8). Di chuyển vào thư mục dự án trên Terminal:
Lệnh chạy: cd TSP-Discrete-Math

2. Khởi chạy chương trình
Chạy file điều khiển trung tâm để hệ thống tự động quét qua tất cả các bộ dữ liệu và xuất báo cáo thực nghiệm đồng bộ:
Lệnh chạy: python main.py

---

## Các thuật toán đã cài đặt (Features)

1. Khởi tạo lộ trình (Greedy Heuristics):
   * Cheapest Insertion (Nhiệm vụ bắt buộc): Kiến tạo chu trình từ lõi dựa trên chi phí hình học tăng thêm tối thiểu.
   * Nearest Neighbor (Nhiệm vụ mở rộng): Chiến lược tham lam ngắn hạn tìm đỉnh lân cận gần nhất.

2. Tối ưu hóa lộ trình (Local Search):
   * Node Swap (Nhiệm vụ bắt buộc): Chiến lược đổi chỗ cặp đỉnh để tìm tối ưu cục bộ.
   * 2-opt (Nhiệm vụ mở rộng): Thuật toán gỡ phẳng chu trình bằng cách cắt và đảo ngược phân đoạn cạnh đan chéo.

3. Cơ chế kiểm soát an toàn (Validation):
   * Tích hợp bộ lọc hậu kiểm định dạng chu trình, tự động phát hiện và ngăn chặn hiện tượng chu trình con (Sub-tour) hoặc bỏ sót đỉnh.

---

## Kết quả thực nghiệm thực tế (Experimental Results)

Dưới đây là bảng số liệu hiệu suất thực tế thu được khi hệ thống chạy kiểm thử đồng bộ trên máy cục bộ:

### 1. Dataset: EIL51.TSP (51 Cities)
Cách tiếp cận (Approach)            | Tổng quãng đường | Thời gian (ms) | Valid?
--------------------------------------------------------------------------------
Greedy 1 (Cheapest Insertion)       | 478.00           | 6.65           | YES
Greedy 1 + Local Search (Swap)      | 471.00           | 23.55          | YES
Greedy 1 + Local Search (2-opt)     | 471.00           | 24.07          | YES
Greedy 2 (Nearest Neighbor)         | 511.00           | 0.20           | YES
Greedy 2 + Local Search (Swap)      | 502.00           | 22.70          | YES
Greedy 2 + Local Search (2-opt)     | 453.00           | 124.75         | YES

### 2. Dataset: KROA100.TSP (100 Cities)
Cách tiếp cận (Approach)            | Tổng quãng đường | Thời gian (ms) | Valid?
--------------------------------------------------------------------------------
Greedy 1 (Cheapest Insertion)       | 25230.00         | 88.42          | YES
Greedy 1 + Local Search (Swap)      | 24403.00         | 1043.79        | YES
Greedy 1 + Local Search (2-opt)     | 24605.00         | 424.19         | YES
Greedy 2 (Nearest Neighbor)         | 27807.00         | 1.12           | YES
Greedy 2 + Local Search (Swap)      | 24155.00         | 2090.43        | YES
Greedy 2 + Local Search (2-opt)     | 23006.00         | 1616.84        | YES

### 3. Dataset: CH150.TSP (150 Cities)
Cách tiếp cận (Approach)            | Tổng quãng đường | Thời gian (ms) | Valid?
--------------------------------------------------------------------------------
Greedy 1 (Cheapest Insertion)       | 7853.00          | 160.16         | YES
Greedy 1 + Local Search (Swap)      | 7476.00          | 3289.90        | YES
Greedy 1 + Local Search (2-opt)     | 7424.00          | 2524.80        | YES
Greedy 2 (Nearest Neighbor)         | 8191.00          | 1.56           | YES
Greedy 2 + Local Search (Swap)      | 8061.00          | 1211.04        | YES
Greedy 2 + Local Search (2-opt)     | 6976.00          | 6859.39        | YES