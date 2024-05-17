from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get('/')
async def root():
    return {"status": 200, "message": ["Server is Running!"]}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get('/api/get-latest-news')
async def getLatestNews():
    latestNews = {
        "status": 200,
        "message": [],
        "data": [
            {
                "id": "00001",
                "title": "Pengakuan Sopir Terpaksa Menabrakkan Bus SMK Lingga Kencana Depok ke Tiang Listrik Saat Kecelakaan Maut di Subang, Jika Tak Dilakukan...",
                "image_url": "https://thumb.tvonenews.com/thumbnail/2024/05/14/66426db4bad50-kondisi-bus-rombongan-smk-lingga-kencana-depok-yang-alami-kecelakaan-maut-di-wilayah-subang-jawa-barat_1265_711.jpg",
                "liked": False,
                "original_url": "https://www.tvonenews.com/berita/nasional/209899-pengakuan-sopir-terpaksa-menabrakkan-bus-smk-lingga-kencana-depok-ke-tiang-listrik-saat-kecelakaan-maut-di-subang-jika-tak-dilakukan",
                "tag": [
                    "News",
                    "Nasional",
                ],
                "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            {
                "id": "00002",
                "title": "Pengakuan Sopir Terpaksa Menabrakkan Bus SMK Lingga Kencana Depok ke Tiang Listrik Saat Kecelakaan Maut di Subang, Jika Tak Dilakukan...",
                "image_url": "https://thumb.tvonenews.com/thumbnail/2024/05/14/66426db4bad50-kondisi-bus-rombongan-smk-lingga-kencana-depok-yang-alami-kecelakaan-maut-di-wilayah-subang-jawa-barat_1265_711.jpg",
                "liked": False,
                "original_url": "https://www.tvonenews.com/berita/nasional/209899-pengakuan-sopir-terpaksa-menabrakkan-bus-smk-lingga-kencana-depok-ke-tiang-listrik-saat-kecelakaan-maut-di-subang-jika-tak-dilakukan",
                "tag": [
                    "News",
                    "Nasional",
                ],
                "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            {
                "id": "00003",
                "title": "Pengakuan Sopir Terpaksa Menabrakkan Bus SMK Lingga Kencana Depok ke Tiang Listrik Saat Kecelakaan Maut di Subang, Jika Tak Dilakukan...",
                "image_url": "https://thumb.tvonenews.com/thumbnail/2024/05/14/66426db4bad50-kondisi-bus-rombongan-smk-lingga-kencana-depok-yang-alami-kecelakaan-maut-di-wilayah-subang-jawa-barat_1265_711.jpg",
                "liked": False,
                "original_url": "https://www.tvonenews.com/berita/nasional/209899-pengakuan-sopir-terpaksa-menabrakkan-bus-smk-lingga-kencana-depok-ke-tiang-listrik-saat-kecelakaan-maut-di-subang-jika-tak-dilakukan",
                "tag": [
                    "News",
                    "Nasional",
                ],
                "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            {
                "id": "00004",
                "title": "Pengakuan Sopir Terpaksa Menabrakkan Bus SMK Lingga Kencana Depok ke Tiang Listrik Saat Kecelakaan Maut di Subang, Jika Tak Dilakukan...",
                "image_url": "https://thumb.tvonenews.com/thumbnail/2024/05/14/66426db4bad50-kondisi-bus-rombongan-smk-lingga-kencana-depok-yang-alami-kecelakaan-maut-di-wilayah-subang-jawa-barat_1265_711.jpg",
                "liked": False,
                "original_url": "https://www.tvonenews.com/berita/nasional/209899-pengakuan-sopir-terpaksa-menabrakkan-bus-smk-lingga-kencana-depok-ke-tiang-listrik-saat-kecelakaan-maut-di-subang-jika-tak-dilakukan",
                "tag": [
                    "News",
                    "Nasional",
                ],
                "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            {
                "id": "00005",
                "title": "Pengakuan Sopir Terpaksa Menabrakkan Bus SMK Lingga Kencana Depok ke Tiang Listrik Saat Kecelakaan Maut di Subang, Jika Tak Dilakukan...",
                "image_url": "https://thumb.tvonenews.com/thumbnail/2024/05/14/66426db4bad50-kondisi-bus-rombongan-smk-lingga-kencana-depok-yang-alami-kecelakaan-maut-di-wilayah-subang-jawa-barat_1265_711.jpg",
                "liked": False,
                "original_url": "https://www.tvonenews.com/berita/nasional/209899-pengakuan-sopir-terpaksa-menabrakkan-bus-smk-lingga-kencana-depok-ke-tiang-listrik-saat-kecelakaan-maut-di-subang-jika-tak-dilakukan",
                "tag": [
                    "News",
                    "Nasional",
                ],
                "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            {
                "id": "00006",
                "title": "Pengakuan Sopir Terpaksa Menabrakkan Bus SMK Lingga Kencana Depok ke Tiang Listrik Saat Kecelakaan Maut di Subang, Jika Tak Dilakukan...",
                "image_url": "https://thumb.tvonenews.com/thumbnail/2024/05/14/66426db4bad50-kondisi-bus-rombongan-smk-lingga-kencana-depok-yang-alami-kecelakaan-maut-di-wilayah-subang-jawa-barat_1265_711.jpg",
                "liked": False,
                "original_url": "https://www.tvonenews.com/berita/nasional/209899-pengakuan-sopir-terpaksa-menabrakkan-bus-smk-lingga-kencana-depok-ke-tiang-listrik-saat-kecelakaan-maut-di-subang-jika-tak-dilakukan",
                "tag": [
                    "News",
                    "Nasional",
                ],
                "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            {
                "id": "00007",
                "title": "Pengakuan Sopir Terpaksa Menabrakkan Bus SMK Lingga Kencana Depok ke Tiang Listrik Saat Kecelakaan Maut di Subang, Jika Tak Dilakukan...",
                "image_url": "https://thumb.tvonenews.com/thumbnail/2024/05/14/66426db4bad50-kondisi-bus-rombongan-smk-lingga-kencana-depok-yang-alami-kecelakaan-maut-di-wilayah-subang-jawa-barat_1265_711.jpg",
                "liked": False,
                "original_url": "https://www.tvonenews.com/berita/nasional/209899-pengakuan-sopir-terpaksa-menabrakkan-bus-smk-lingga-kencana-depok-ke-tiang-listrik-saat-kecelakaan-maut-di-subang-jika-tak-dilakukan",
                "tag": [
                    "News",
                    "Nasional",
                ],
                "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            {
                "id": "00008",
                "title": "Pengakuan Sopir Terpaksa Menabrakkan Bus SMK Lingga Kencana Depok ke Tiang Listrik Saat Kecelakaan Maut di Subang, Jika Tak Dilakukan...",
                "image_url": "https://thumb.tvonenews.com/thumbnail/2024/05/14/66426db4bad50-kondisi-bus-rombongan-smk-lingga-kencana-depok-yang-alami-kecelakaan-maut-di-wilayah-subang-jawa-barat_1265_711.jpg",
                "liked": False,
                "original_url": "https://www.tvonenews.com/berita/nasional/209899-pengakuan-sopir-terpaksa-menabrakkan-bus-smk-lingga-kencana-depok-ke-tiang-listrik-saat-kecelakaan-maut-di-subang-jika-tak-dilakukan",
                "tag": [
                    "News",
                    "Nasional",
                ],
                "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            {
                "id": "00009",
                "title": "Pengakuan Sopir Terpaksa Menabrakkan Bus SMK Lingga Kencana Depok ke Tiang Listrik Saat Kecelakaan Maut di Subang, Jika Tak Dilakukan...",
                "image_url": "https://thumb.tvonenews.com/thumbnail/2024/05/14/66426db4bad50-kondisi-bus-rombongan-smk-lingga-kencana-depok-yang-alami-kecelakaan-maut-di-wilayah-subang-jawa-barat_1265_711.jpg",
                "liked": False,
                "original_url": "https://www.tvonenews.com/berita/nasional/209899-pengakuan-sopir-terpaksa-menabrakkan-bus-smk-lingga-kencana-depok-ke-tiang-listrik-saat-kecelakaan-maut-di-subang-jika-tak-dilakukan",
                "tag": [
                    "News",
                    "Nasional",
                ],
                "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            {
                "id": "00010",
                "title": "Pengakuan Sopir Terpaksa Menabrakkan Bus SMK Lingga Kencana Depok ke Tiang Listrik Saat Kecelakaan Maut di Subang, Jika Tak Dilakukan...",
                "image_url": "https://thumb.tvonenews.com/thumbnail/2024/05/14/66426db4bad50-kondisi-bus-rombongan-smk-lingga-kencana-depok-yang-alami-kecelakaan-maut-di-wilayah-subang-jawa-barat_1265_711.jpg",
                "liked": False,
                "original_url": "https://www.tvonenews.com/berita/nasional/209899-pengakuan-sopir-terpaksa-menabrakkan-bus-smk-lingga-kencana-depok-ke-tiang-listrik-saat-kecelakaan-maut-di-subang-jika-tak-dilakukan",
                "tag": [
                    "News",
                    "Nasional",
                ],
                "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            }
        ],
        "pagination": {
            "page": 0,
            "total_items": 10,
        }
    }
    return latestNews

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)