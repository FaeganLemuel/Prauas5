from django.shortcuts import render, HttpResponse
from pabrik.models import Sensor, Actuator
from django.http import JsonResponse
from django.template import loader
from pabrik.MQTT import run_mqtt


run_mqtt()


def main_page(request):
    kandang_temperatur = Sensor.objects.get(name="kandang/temperatur")
    kandang_kelembaban = Sensor.objects.get(name="kandang/kelembaban")
    kandang_pakan = Sensor.objects.get(name="kandang/pakan")
    kandang_kondisi = Actuator.objects.get(name="kandang/kondisi")

    wagyu_berat = Sensor.objects.get(name="wagyu/berat")
    wagyu_kualitas = Sensor.objects.get(name="wagyu/kualitas")
    wagyu_lemak = Sensor.objects.get(name="wagyu/lemak")
    wagyu_harga = Actuator.objects.get(name="wagyu/harga")

    ikan_berat = Sensor.objects.get(name="ikan/berat")
    ikan_lemak = Sensor.objects.get(name="ikan/lemak")
    ikan_panjang = Sensor.objects.get(name="ikan/panjang")
    ikan_harga = Actuator.objects.get(name="ikan/harga")

    kondisi_farm = Actuator.objects.get(name="farm")

    beras_berat = Sensor.objects.get(name="beras/berat")
    beras_aroma = Sensor.objects.get(name="beras/aroma")
    beras_air = Sensor.objects.get(name="beras/air")
    beras_harga = Actuator.objects.get(name="beras/harga")

    sayur_berat = Sensor.objects.get(name="sayur/berat")
    sayur_warna = Sensor.objects.get(name="sayur/warna")
    sayur_keasaman = Sensor.objects.get(name="sayur/keasaman")
    sayur_harga = Actuator.objects.get(name="sayur/harga")

    buah_berat = Sensor.objects.get(name="buah/berat")
    buah_warna = Sensor.objects.get(name="buah/warna")
    buah_keasaman = Sensor.objects.get(name="buah/keasaman")
    buah_harga = Actuator.objects.get(name="buah/harga")

    musim_angin = Sensor.objects.get(name="musim/angin")
    musim_suhu = Sensor.objects.get(name="musim/suhu")
    musim_kelembaban = Sensor.objects.get(name="musim/kelembaban")
    musim_musim = Actuator.objects.get(name="musim/musim")

    jual_makanan = Sensor.objects.get(name="jual/makanan")
    jual_minuman = Sensor.objects.get(name="jual/minuman")
    jual_service = Sensor.objects.get(name="jual/service")
    jual_harga = Actuator.objects.get(name="jual/harga")

    pengunjung_kepuasan = Sensor.objects.get(name="pengunjung/kepuasan")
    pengunjung_jumlah = Sensor.objects.get(name="pengunjung/jumlah")
    pengunjung_promosi = Sensor.objects.get(name="pengunjung/promosi")
    pengunjung_kondisi = Actuator.objects.get(name="pengunjung/kondisi")


    template = loader.get_template('index.html')
    context = {
        'kandang_temperatur': kandang_temperatur.value,
        'kandang_kelembaban': kandang_kelembaban.value,
        'kandang_pakan': kandang_pakan.value,
        'kandang_kondisi': kandang_kondisi.value,
        'wagyu_berat': wagyu_berat.value,
        'wagyu_kualitas': wagyu_kualitas.value,
        'wagyu_lemak': wagyu_lemak.value,
        'wagyu_harga': wagyu_harga.value,
        'ikan_berat': ikan_berat.value,
        'ikan_lemak': ikan_lemak.value,
        'ikan_panjang': ikan_panjang.value,
        'ikan_harga': ikan_harga.value,
        'kondisi_farm': kondisi_farm.value,
        'beras_berat': beras_berat.value,
        'beras_aroma': beras_aroma.value,
        'beras_air': beras_air.value,
        'beras_harga': beras_harga.value,
        'sayur_berat': sayur_berat.value,
        'sayur_warna': sayur_warna.value,
        'sayur_keasaman': sayur_keasaman.value,
        'sayur_harga': sayur_harga.value,
        'buah_berat': buah_berat.value,
        'buah_warna': buah_warna.value,
        'buah_keasaman': buah_keasaman.value,
        'buah_harga': buah_harga.value,
        'jual_makanan': jual_makanan.value,
        'jual_minuman': jual_minuman.value,
        'jual_service': jual_service.value,
        'jual_harga': jual_harga.value,
        'pengunjung_kepuasan': pengunjung_kepuasan.value,
        'pengunjung_jumlah': pengunjung_jumlah.value,
        'pengunjung_promosi': pengunjung_promosi.value,
        'pengunjung_kondisi': pengunjung_kondisi.value,
        'musim_angin': musim_angin.value,
        'musim_suhu': musim_suhu.value,
        'musim_kelembaban': musim_kelembaban.value,
        'musim_musim': musim_musim.value,
    }
    return HttpResponse(template.render(context, request))
