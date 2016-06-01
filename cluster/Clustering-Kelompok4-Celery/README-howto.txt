Langkah-langkah :
1. Jalankan RabbitMQ Server (run rabbitmq-server)
2. lalu, buat kode untuk worker (tasks.py)
3. Setelah itu, jalankan worker menggunakan celery dengan cara
   > celery -A tasks worker --loglevel=info --pool=solo
4. Ketika worker sudah siap digunakan, jalankan manager dengan cara 
   > python manager.py
5. Result disimpan dalam variabel result, dan terdapat command untuk mendapatkan informasi lainnya, diantaranya :
   - result.ready() : mengetahui apakah task sudah selesai atau belum
   - result.get() : mendapatkan hasil dari penghitungan worker
   - lengkapnya, bisa dilihat disini : http://docs.celeryproject.org/en/latest/reference/celery.result.html#module-celery.result

Tugas yang perlu dikerjakan :
1. Membuat workernya agar menjadi Log Parser (code)
2. Membuat manager agar dapat menghitung TOP 10 Log Terbanyak (code)
3. Memperbanyak worker dengan metode Clustering menggunakan Celery (sedikit code + cara implementasi)
4. Implementasi secara real (implementasi sebelum demo/Demo Ready)