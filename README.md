# Bulut bilişim final projesi - Arkadaşlar için anket
Proje GitHub Linki: https://github.com/otvaliuje/rrrfrr
## Kullanılan Teknolojiler
* **Uygulama Mimarisi:** Python, FastAPI, Jinja2, PyMongo
* **Konteynerizasyon:** Docker
* **Orkestrasyon:** Google Kubernetes Engine
* **CI/CD Pipeline:** GitHub Actions

## Kubernetes Mimarisi
1. **Deployment & StatefulSet:** Web uygulaması için 3 replicas sağlayan Deployment ve veritabanı bütünlüğü için StatefulSet kullanılmıştır
2. **Service:** Dış trafik için `LoadBalancer`, veritabanı içi iletişim için `Headless Service` yapılandırılmıştır
3. **PV/PVC:** Veritabanı podları silindiğinde veri kaybını önlemek için Google Cloud üzerinde PVC entegre edilmiştir
4. **NetworkPolicy & Secret:** MongoDB veritabanına sadece web uygulamasının erişebilmesi için NetworkPolicy uygulanmış ve şifreler `Secret` objesi ile şifrelenmiştir
5. **Otomasyon:** GitHuba yapılan her push işleminde imajı derleyip Docker Huba gönderen ve GKEde güncelleyen CI/CD akışı kurulmuştur