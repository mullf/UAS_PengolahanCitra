import numpy as np
import matplotlib.pyplot as plt
import cv2

# Read the image (use an image path that you have)
image = cv2.imread('samping1.jpg')

# Check if the image was successfully loaded
if image is None:
    print("Error: Image not found or unable to load.")
else:
    # Change color to RGB (from BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Display the original image
    plt.imshow(image)
    plt.title('Original Image')
    plt.axis('off')  # Hide axis
    plt.show()

    # Reshape the image to a 2D array of pixels and 3 color values (RGB)
    pixel_vals = image.reshape((-1, 3))

    # Convert to float type
    pixel_vals = np.float32(pixel_vals)

    # Step 1: Pilih jumlah cluster yang ingin dicari yaitu k.
    k = 4

    # Step 2: Tetapkan titik data secara acak ke salah satu k cluster.
    # cv2.kmeans will handle the random assignment internally

    # Define criteria for the algorithm to stop running, which is either 100 iterations
    # or the required accuracy (epsilon) reached at 85%
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)

    # Perform k-means clustering with the number of clusters specified as k
    # Random centers are initially chosen for k-means clustering
    retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Step 3: Kemudian hitung pusat clusternya.
    # (cv2.kmeans computes the initial centers and updates them in the loop)
    # centers now contains the center of each cluster

    # Step 4: Hitung jarak titik data dari pusat masing-masing cluster.
    # (cv2.kmeans handles this internally by computing the distance of each point to the centers)
    
    # Step 5: Bergantung pada jarak setiap titik data dari klaster, tetapkan kembali titik data ke klaster terdekat.
    # (cv2.kmeans reassigns each point to the nearest cluster center)

    # Step 6: Hitung lagi pusat cluster yang baru.
    # (cv2.kmeans recomputes the centers based on the new assignments)

    # Step 7: Ulangi langkah 4, 5 dan 6 hingga titik data tidak mengubah cluster, atau hingga mencapai jumlah iterasi yang ditetapkan.
    # (cv2.kmeans repeats the process until convergence or max iterations)

    # Convert data into 8-bit values
    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]

    # Reshape data into the original image dimensions
    segmented_image = segmented_data.reshape((image.shape))

    # Display the segmented image
    plt.imshow(segmented_image)
    plt.title('Segmented Image with K-Means Clustering')
    plt.axis('off')  # Hide axis
    plt.show()
