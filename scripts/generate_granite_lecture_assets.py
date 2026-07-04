from pathlib import Path
import os

import cv2
import numpy as np

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-codex")

import matplotlib

matplotlib.use("Agg")
from matplotlib import pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "obrazki/duze/granite_1920.jpg"
OUT = ROOT / "lectures/assets"


def load_bgr():
    image = cv2.imread(str(SOURCE), cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(f"Cannot read image: {SOURCE}")
    return image


def save(fig, relpath):
    path = OUT / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, dpi=100)
    plt.close(fig)


def rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def hist_gray(image):
    return cv2.calcHist([image], [0], None, [256], [0, 256])


def intro_assets(image):
    g = gray(image)
    h, w = g.shape

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(rgb(image))
    ax.set_title("Granite")
    ax.axis("off")
    save(fig, "01_introduction/01_original_granite.png")

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(rgb(image))
    axes[0].set_title("RGB")
    axes[1].imshow(g, cmap="gray")
    axes[1].set_title("Skala szarości")
    axes[2].imshow(hsv)
    axes[2].set_title("HSV")
    for ax in axes:
        ax.axis("off")
    save(fig, "01_introduction/02_color_spaces_granite.png")

    _, _, red = cv2.split(image)
    zeros = np.zeros_like(red)
    red_only = cv2.merge([zeros, zeros, red])
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    axes[0].imshow(red, cmap="gray")
    axes[0].set_title("Kanał czerwony")
    axes[1].imshow(rgb(red_only))
    axes[1].set_title("Tylko czerwony")
    for ax in axes:
        ax.axis("off")
    save(fig, "01_introduction/03_red_channel_granite.png")

    y1, x1 = 0, 0
    y2, x2 = min(200, h), min(200, w)
    modified = image.copy()
    modified[y1:y2, x1:x2] = (123, 255, 45)
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    axes[0].imshow(rgb(image))
    axes[0].set_title("Oryginał")
    axes[1].imshow(rgb(modified))
    axes[1].set_title("ROI skopiowany")
    for ax in axes:
        ax.axis("off")
    save(fig, "01_introduction/05_roi_granite.png")


def threshold_assets(image):
    g = gray(image)
    methods = [
        ("BINARY", cv2.THRESH_BINARY),
        ("BINARY_INV", cv2.THRESH_BINARY_INV),
        ("TRUNC", cv2.THRESH_TRUNC),
        ("TOZERO", cv2.THRESH_TOZERO),
        ("TOZERO_INV", cv2.THRESH_TOZERO_INV),
    ]

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes[0, 0].imshow(g, cmap="gray")
    axes[0, 0].set_title("Oryginał")
    axes[0, 0].axis("off")
    for idx, (title, method) in enumerate(methods, start=1):
        _, result = cv2.threshold(g, 127, 255, method)
        ax = axes[(idx) // 3, (idx) % 3]
        ax.imshow(result, cmap="gray")
        ax.set_title(title)
        ax.axis("off")
    axes[1, 2].axis("off")
    save(fig, "02_thresholding/01_threshold_types_granite.png")

    _, global_thresh = cv2.threshold(g, 127, 255, cv2.THRESH_BINARY)
    _, otsu = cv2.threshold(g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    adaptive = cv2.adaptiveThreshold(
        g, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    for ax, img, title in zip(
        axes,
        [g, global_thresh, otsu, adaptive],
        ["Oryginał", "Globalne T=127", "Otsu", "Adaptacyjne Gauss"],
    ):
        ax.imshow(img, cmap="gray")
        ax.set_title(title)
        ax.axis("off")
    save(fig, "02_thresholding/02_otsu_compare_granite.png")


def filtering_assets(image):
    blur = cv2.blur(image, (5, 5))
    gauss = cv2.GaussianBlur(image, (5, 5), 0)
    median = cv2.medianBlur(image, 5)
    bilateral = cv2.bilateralFilter(image, 9, 75, 75)

    fig, axes = plt.subplots(1, 5, figsize=(25, 5))
    for ax, img, title in zip(
        axes,
        [image, blur, gauss, median, bilateral],
        ["Oryginał", "Averaging", "Gaussian", "Median", "Bilateral"],
    ):
        ax.imshow(rgb(img))
        ax.set_title(title)
        ax.axis("off")
    save(fig, "03_filtering_and_blurring/01_blur_methods_granite.png")

    sizes = [3, 7, 15, 31]
    fig, axes = plt.subplots(1, len(sizes) + 1, figsize=(20, 4))
    axes[0].imshow(rgb(image))
    axes[0].set_title("Oryginał")
    axes[0].axis("off")
    for i, k in enumerate(sizes, start=1):
        blurred = cv2.GaussianBlur(image, (k, k), 0)
        axes[i].imshow(rgb(blurred))
        axes[i].set_title(f"Gauss {k}×{k}")
        axes[i].axis("off")
    save(fig, "03_filtering_and_blurring/02_kernel_sizes_granite.png")

    blurred = cv2.GaussianBlur(image, (0, 0), 2.0)
    unsharp = cv2.addWeighted(image, 1.5, blurred, -0.5, 0)
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    axes[0].imshow(rgb(image))
    axes[0].set_title("Oryginał")
    axes[0].axis("off")
    axes[1].imshow(rgb(unsharp))
    axes[1].set_title("Unsharp Masking")
    axes[1].axis("off")
    save(fig, "03_filtering_and_blurring/03_unsharp_granite.png")

    kernel_emboss = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]], dtype=np.float32)
    kernel_edges_h = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)
    kernel_edges_v = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)

    emboss = cv2.filter2D(image, -1, kernel_emboss)
    edges_h = cv2.filter2D(image, -1, kernel_edges_h)
    edges_v = cv2.filter2D(image, -1, kernel_edges_v)

    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    for ax, img, title in zip(
        axes,
        [image, emboss, edges_h, edges_v],
        ["Oryginał", "Emboss", "Krawędzie poziome", "Krawędzie pionowe"],
    ):
        ax.imshow(rgb(img))
        ax.set_title(title)
        ax.axis("off")
    save(fig, "03_filtering_and_blurring/04_custom_kernels_granite.png")


def histogram_assets(image):
    g = gray(image)
    hist = hist_gray(g)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(hist, color="gray")
    ax.fill_between(range(256), hist.flatten(), alpha=0.3, color="gray")
    ax.set_title("Histogram jasności")
    ax.set_xlabel("Wartość piksela (0–255)")
    ax.set_ylabel("Liczba pikseli")
    ax.set_xlim([0, 256])
    ax.grid(True, alpha=0.3)
    save(fig, "04_histograms/01_histogram_gray_granite.png")

    fig, ax = plt.subplots(figsize=(10, 4))
    for channel, color, label in [
        (0, "blue", "Blue"),
        (1, "green", "Green"),
        (2, "red", "Red"),
    ]:
        h = cv2.calcHist([image], [channel], None, [256], [0, 256])
        ax.plot(h, color=color, label=label)
    ax.set_title("Histogram kanałów BGR")
    ax.set_xlabel("Wartość piksela")
    ax.set_ylabel("Liczba pikseli")
    ax.set_xlim([0, 256])
    ax.legend()
    ax.grid(True, alpha=0.3)
    save(fig, "04_histograms/02_histogram_bgr_granite.png")

    mask = np.zeros_like(g, dtype=np.uint8)
    h, w = g.shape
    y1, y2 = h // 6, min(h, h // 6 + 220)
    x1, x2 = w // 6, min(w, w // 6 + 300)
    mask[y1:y2, x1:x2] = 255
    hist_mask = cv2.calcHist([g], [0], mask, [256], [0, 256])
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(hist, label="Cały obraz", color="gray")
    ax.plot(hist_mask, label="Zamaskowany obszar", color="blue")
    ax.legend()
    ax.set_title("Histogram z maską vs pełny")
    save(fig, "04_histograms/03_histogram_mask_granite.png")

    eq = cv2.equalizeHist(g)
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes[0, 0].imshow(g, cmap="gray")
    axes[0, 0].set_title("Oryginał")
    axes[0, 1].imshow(eq, cmap="gray")
    axes[0, 1].set_title("Po equalizacji")
    hist_orig = hist
    hist_eq = hist_gray(eq)
    axes[1, 0].plot(hist_orig, color="gray")
    axes[1, 0].set_title("Histogram oryginału")
    axes[1, 0].set_xlim([0, 256])
    axes[1, 1].plot(hist_eq, color="blue")
    axes[1, 1].set_title("Histogram po equalizacji")
    axes[1, 1].set_xlim([0, 256])
    save(fig, "04_histograms/04_equalization_gray_granite.png")

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v_eq = cv2.equalizeHist(v)
    hsv_eq = cv2.merge([h, s, v_eq])
    result = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    axes[0].imshow(rgb(image))
    axes[0].set_title("Oryginał")
    axes[0].axis("off")
    axes[1].imshow(rgb(result))
    axes[1].set_title("Equalizacja HSV")
    axes[1].axis("off")
    save(fig, "04_histograms/05_equalization_hsv_granite.png")

    eq_global = cv2.equalizeHist(g)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    eq_clahe = clahe.apply(g)
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    for ax, img, title in zip(
        axes, [g, eq_global, eq_clahe], ["Oryginał", "Globalna equalizacja", "CLAHE"]
    ):
        ax.imshow(img, cmap="gray")
        ax.set_title(title)
        ax.axis("off")
    save(fig, "04_histograms/06_clahe_comparison_granite.png")


def morphology_assets(image):
    g = gray(image)
    _, binary = cv2.threshold(g, 127, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    erosion = cv2.erode(binary, kernel, iterations=1)
    dilation = cv2.dilate(binary, kernel, iterations=1)
    opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)
    tophat = cv2.morphologyEx(binary, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(binary, cv2.MORPH_BLACKHAT, kernel)

    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    images = [binary, erosion, dilation, opening, closing, gradient, tophat, blackhat]
    titles = [
        "Binarny",
        "Erozja",
        "Dylatacja",
        "Otwarcie",
        "Domknięcie",
        "Gradient",
        "Top Hat",
        "Black Hat",
    ]
    for ax, img, title in zip(axes.flatten(), images, titles):
        ax.imshow(img, cmap="gray")
        ax.set_title(title)
        ax.axis("off")
    save(fig, "05_morphology_and_edges/01_morphology_ops_granite.png")

    kernel = np.ones((3, 3), np.uint8)
    fig, axes = plt.subplots(1, 5, figsize=(20, 4))
    axes[0].imshow(binary, cmap="gray")
    axes[0].set_title("Oryginał")
    axes[0].axis("off")
    for i, n in enumerate([1, 2, 4, 8], start=1):
        eroded = cv2.erode(binary, kernel, iterations=n)
        axes[i].imshow(eroded, cmap="gray")
        axes[i].set_title(f"Erozja x{n}")
        axes[i].axis("off")
    save(fig, "05_morphology_and_edges/02_iterations_granite.png")

    noise = binary.copy()
    rng = np.random.default_rng(0)
    num_pixels = int(0.05 * g.size)
    coords = [rng.integers(0, i, num_pixels) for i in g.shape]
    noise[coords[0], coords[1]] = 255
    coords = [rng.integers(0, i, num_pixels) for i in g.shape]
    noise[coords[0], coords[1]] = 0
    cleaned = cv2.morphologyEx(noise, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    axes[0].imshow(noise, cmap="gray")
    axes[0].set_title("Z szumem")
    axes[0].axis("off")
    axes[1].imshow(cleaned, cmap="gray")
    axes[1].set_title("Po otwarciu")
    axes[1].axis("off")
    save(fig, "05_morphology_and_edges/03_opening_noise_granite.png")

    sobelx = cv2.Sobel(g, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(g, cv2.CV_64F, 0, 1, ksize=3)
    sobelx_abs = np.uint8(np.absolute(sobelx))
    sobely_abs = np.uint8(np.absolute(sobely))
    sobel_combined = cv2.bitwise_or(sobelx_abs, sobely_abs)
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    for ax, img, title in zip(
        axes,
        [g, sobelx_abs, sobely_abs, sobel_combined],
        ["Oryginał", "Sobel X (pionowe)", "Sobel Y (poziome)", "Połączone"],
    ):
        ax.imshow(img, cmap="gray")
        ax.set_title(title)
        ax.axis("off")
    save(fig, "05_morphology_and_edges/04_sobel_granite.png")

    blurred = cv2.GaussianBlur(g, (3, 3), 0)
    laplacian = np.uint8(np.absolute(cv2.Laplacian(blurred, cv2.CV_64F)))
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    axes[0].imshow(g, cmap="gray")
    axes[0].set_title("Oryginał")
    axes[0].axis("off")
    axes[1].imshow(laplacian, cmap="gray")
    axes[1].set_title("Laplacian")
    axes[1].axis("off")
    save(fig, "05_morphology_and_edges/05_laplacian_granite.png")

    blurred = cv2.GaussianBlur(g, (5, 5), 0)
    canny_low = cv2.Canny(blurred, 50, 150)
    canny_medium = cv2.Canny(blurred, 100, 200)
    canny_high = cv2.Canny(blurred, 150, 300)
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    for ax, img, title in zip(
        axes,
        [g, canny_low, canny_medium, canny_high],
        ["Oryginał", "Canny (50/150)", "Canny (100/200)", "Canny (150/300)"],
    ):
        ax.imshow(img, cmap="gray")
        ax.set_title(title)
        ax.axis("off")
    save(fig, "05_morphology_and_edges/06_canny_granite.png")

    blurred = cv2.GaussianBlur(g, (3, 3), 0)
    sobelX = cv2.Sobel(blurred, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(blurred, cv2.CV_64F, 0, 1)
    sobel = np.uint8(np.clip(np.sqrt(sobelX**2 + sobelY**2), 0, 255))
    lap = np.uint8(np.absolute(cv2.Laplacian(blurred, cv2.CV_64F)))
    canny = cv2.Canny(blurred, 100, 200)
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    for ax, img, title in zip(
        axes, [g, sobel, lap, canny], ["Oryginał", "Sobel", "Laplacian", "Canny"]
    ):
        ax.imshow(img, cmap="gray")
        ax.set_title(title)
        ax.axis("off")
    save(fig, "05_morphology_and_edges/07_edge_compare_granite.png")


def contour_assets(image):
    g = gray(image)
    _, binary = cv2.threshold(g, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(
        binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    contour_img = image.copy()
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(rgb(contour_img))
    ax.set_title("Kontury")
    ax.axis("off")
    save(fig, "06_contours_and_detection/01_contours_granite.png")

    img_copy = image.copy()
    for cnt in contours:
        if cv2.contourArea(cnt) < 500:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect).astype(np.int32)
        cv2.drawContours(img_copy, [box], 0, (0, 0, 255), 2)
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(rgb(img_copy))
    ax.set_title("Bounding Box")
    ax.axis("off")
    save(fig, "06_contours_and_detection/02_bounding_box_granite.png")

    img_copy = image.copy()
    for cnt in contours:
        if cv2.contourArea(cnt) < 500:
            continue
        (cx, cy), radius = cv2.minEnclosingCircle(cnt)
        cv2.circle(img_copy, (int(cx), int(cy)), int(radius), (255, 0, 0), 2)
        M = cv2.moments(cnt)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(img_copy, (cX, cY), 5, (0, 0, 255), -1)
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(rgb(img_copy))
    ax.set_title("Okrąg otaczający")
    ax.axis("off")
    save(fig, "06_contours_and_detection/03_enclosing_circle_granite.png")

    img_copy = image.copy()
    for cnt in contours:
        if cv2.contourArea(cnt) < 500:
            continue
        epsilon = 0.02 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        n = len(approx)
        if n == 3:
            shape = "Trojkat"
        elif n == 4:
            shape = "Czworobok"
        elif n == 5:
            shape = "Pieciokat"
        else:
            shape = "Okrag"
        x, y, _, _ = cv2.boundingRect(approx)
        cv2.drawContours(img_copy, [approx], -1, (0, 255, 0), 2)
        cv2.putText(
            img_copy,
            shape,
            (x, max(0, y - 10)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 255),
            1,
        )
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(rgb(img_copy))
    ax.set_title("Rozpoznawanie kształtów")
    ax.axis("off")
    save(fig, "06_contours_and_detection/04_shapes_granite.png")


def main():
    image = load_bgr()
    intro_assets(image)
    threshold_assets(image)
    filtering_assets(image)
    histogram_assets(image)
    morphology_assets(image)
    contour_assets(image)


if __name__ == "__main__":
    main()
