import numpy as np
import matplotlib.pyplot as plt

# Hareketli nesne parametreleri
num_steps = 100
motion_noise = 0.1
measurement_noise = 0.1

# Hareketli nesne başlangıç konumu
true_position = np.array([2.0, 2.0])

# Hareket modeli
def motion_model(x, dt):
    return x + np.random.normal(0, motion_noise, size=2)

# Hareketli nesne gerçek hareketi ve ölçümler
true_path = [true_position]
num_landmarks = 5  # Örnek olarak 5 nesne olsun
landmarks = np.random.rand(num_landmarks, 2) * 10
measurements = []

for _ in range(num_steps):
    true_position = motion_model(true_position, 1)
    true_path.append(true_position)
    measured_distances = np.linalg.norm(landmarks - true_position, axis=1)
    measurements.append(measured_distances + np.random.normal(0, measurement_noise, num_landmarks))

# UKF algoritması
def unscented_kalman_filter(motion_model, measurements):
    num_states = 2

    # Hesaplamaları saklamak için matrisler
    P = np.eye(num_states)  # Başlangıç tahmin hata kovaryans matrisi

    estimated_path = [true_path[0]]  # İlk konumu ekliyoruz

    for i in range(num_steps):
        # Hareket modelini kullanarak tahmin
        predicted_position = motion_model(estimated_path[-1], 1)
        
        # Hata kovaryansı güncelleme
        P = np.eye(num_states) * motion_noise  # Basitçe güncellendi, gerçek uygulamada daha karmaşık olmalıdır
        
        # Gözlem
        H = np.eye(num_landmarks, num_states)  # Ölçüm matrisi
        R = np.eye(num_landmarks) * measurement_noise ** 2
        
        # Kalman kazancı
        K = P @ H.T @ np.linalg.inv(H @ P @ H.T + R)
        
        # Gözlemi entegre etme
        z = measurements[i]
        estimated_position = predicted_position + K @ (z - np.linalg.norm(landmarks - predicted_position, axis=1))
        estimated_path.append(estimated_position)
    
    return np.array(estimated_path)

# UKF uygulamasını çağırma
estimated_path = unscented_kalman_filter(motion_model, measurements)

# Sonuçları çizdirme
true_path = np.array(true_path)
estimated_path = np.array(estimated_path)

plt.scatter(true_path[:, 0], true_path[:, 1], color='green', label='True Path')
plt.plot(estimated_path[:, 0], estimated_path[:, 1], color='red', label='Estimated Path')
plt.scatter(landmarks[:, 0], landmarks[:, 1], color='blue', label='Landmarks')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D SLAM Simulation with Unscented Kalman Filter')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
