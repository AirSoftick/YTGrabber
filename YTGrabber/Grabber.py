import os
import warnings
import locale
from pytube import YouTube

translations = {
    'en': {
        'available_qualities': 'Available Qualities:',
        'resolution': 'Resolution',
        'format': 'Format',
        'downloading_video': 'Downloading video...',
        'video_downloaded': 'Video downloaded successfully.',
        'enter_youtube_url': 'Enter the YouTube URL:',
        'select_quality': 'Select the desired quality (enter the corresponding number):',
        'invalid_choice': 'Invalid choice. Please try again.',
    },
    'ru': {
        'available_qualities': 'Доступные качества:',
        'resolution': 'Разрешение',
        'format': 'Формат',
        'downloading_video': 'Загрузка видео...',
        'video_downloaded': 'Видео успешно загружено.',
        'enter_youtube_url': 'Введите URL YouTube видео:',
        'select_quality': 'Выберите желаемое качество (введите соответствующую цифру):',
        'invalid_choice': 'Недопустимый выбор. Пожалуйста, попробуйте еще раз.',
    },
    'fr': {
        'available_qualities': 'Qualités disponibles :',
        'resolution': 'Résolution',
        'format': 'Format',
        'downloading_video': 'Téléchargement de la vidéo...',
        'video_downloaded': 'Vidéo téléchargée avec succès.',
        'enter_youtube_url': 'Entrez l\'URL YouTube :',
        'select_quality': 'Sélectionnez la qualité souhaitée (entrez le numéro correspondant) :',
        'invalid_choice': 'Choix invalide. Veuillez réessayer.',
    },
    'es': {
        'available_qualities': 'Calidades disponibles:',
        'resolution': 'Resolución',
        'format': 'Formato',
        'downloading_video': 'Descargando video...',
        'video_downloaded': 'Video descargado correctamente.',
        'enter_youtube_url': 'Ingrese la URL de YouTube:',
        'select_quality': 'Seleccione la calidad deseada (ingrese el número correspondiente):',
        'invalid_choice': 'Opción inválida. Por favor, intente nuevamente.',
    },
    'de': {
        'available_qualities': 'Verfügbare Qualitäten:',
        'resolution': 'Auflösung',
        'format': 'Format',
        'downloading_video': 'Video wird heruntergeladen...',
        'video_downloaded': 'Video erfolgreich heruntergeladen.',
        'enter_youtube_url': 'Geben Sie die YouTube-URL ein:',
        'select_quality': 'Wählen Sie die gewünschte Qualität aus (geben Sie die entsprechende Nummer ein):',
        'invalid_choice': 'Ungültige Auswahl. Bitte versuchen Sie es erneut.',
    },
    'it': {
        'available_qualities': 'Qualità disponibili:',
        'resolution': 'Risoluzione',
        'format': 'Formato',
        'downloading_video': 'Download del video in corso...',
        'video_downloaded': 'Video scaricato con successo.',
        'enter_youtube_url': 'Inserisci l\'URL di YouTube:',
        'select_quality': 'Seleziona la qualità desiderata (inserisci il numero corrispondente):',
        'invalid_choice': 'Scelta non valida. Per favore, riprova.',
    },
    'pt': {
        'available_qualities': 'Qualidades disponíveis:',
        'resolution': 'Resolução',
        'format': 'Formato',
        'downloading_video': 'Baixando vídeo...',
        'video_downloaded': 'Vídeo baixado com sucesso.',
        'enter_youtube_url': 'Digite a URL do YouTube:',
        'select_quality': 'Selecione a qualidade desejada (digite o número correspondente):',
        'invalid_choice': 'Escolha inválida. Por favor, tente novamente.',
    },
    'zh': {
        'available_qualities': '可用质量：',
        'resolution': '分辨率',
        'format': '格式',
        'downloading_video': '正在下载视频...',
        'video_downloaded': '视频下载成功。',
        'enter_youtube_url': '请输入 YouTube 视频的 URL：',
        'select_quality': '选择所需的质量（输入相应的数字）：',
        'invalid_choice': '选择无效，请重试。',
    },
    'ja': {
        'available_qualities': '利用可能な品質:',
        'resolution': '解像度',
        'format': 'フォーマット',
        'downloading_video': 'ビデオをダウンロードしています...',
        'video_downloaded': 'ビデオのダウンロードに成功しました。',
        'enter_youtube_url': 'YouTube の URL を入力してください:',
        'select_quality': '希望する品質を選択してください（対応する番号を入力）:',
        'invalid_choice': '無効な選択です。もう一度やり直してください。',
    },
    'ko': {
        'available_qualities': '사용 가능한 품질:',
        'resolution': '해상도',
        'format': '포맷',
        'downloading_video': '비디오 다운로드 중...',
        'video_downloaded': '비디오 다운로드 완료.',
        'enter_youtube_url': 'YouTube URL을 입력하세요:',
        'select_quality': '원하는 품질을 선택하세요 (해당하는 번호를 입력하세요):',
        'invalid_choice': '잘못된 선택입니다. 다시 시도해주세요.',
    },
    'ar': {
        'available_qualities': 'الجودات المتاحة:',
        'resolution': 'الدقة',
        'format': 'الصيغة',
        'downloading_video': 'جارٍ تحميل الفيديو...',
        'video_downloaded': 'تم تحميل الفيديو بنجاح.',
        'enter_youtube_url': 'أدخل رابط يوتيوب:',
        'select_quality': 'اختر الجودة المطلوبة (أدخل الرقم المقابل):',
        'invalid_choice': 'اختيار غير صالح. يرجى المحاولة مرة أخرى.',
    },
    'tr': {
        'available_qualities': 'Mevcut Kaliteler:',
        'resolution': 'Çözünürlük',
        'format': 'Format',
        'downloading_video': 'Video indiriliyor...',
        'video_downloaded': 'Video başarıyla indirildi.',
        'enter_youtube_url': 'YouTube URL\'sini girin:',
        'select_quality': 'İstenen kaliteyi seçin (ilgili numarayı girin):',
        'invalid_choice': 'Geçersiz seçim. Lütfen tekrar deneyin.',
    },
    'nl': {
        'available_qualities': 'Beschikbare kwaliteiten:',
        'resolution': 'Resolutie',
        'format': 'Formaat',
        'downloading_video': 'Video wordt gedownload...',
        'video_downloaded': 'Video succesvol gedownload.',
        'enter_youtube_url': 'Voer de YouTube URL in:',
        'select_quality': 'Selecteer de gewenste kwaliteit (voer het overeenkomstige nummer in):',
        'invalid_choice': 'Ongeldige keuze. Probeer het opnieuw.',
    },
    'sv': {
        'available_qualities': 'Tillgängliga kvaliteter:',
        'resolution': 'Upplösning',
        'format': 'Format',
        'downloading_video': 'Laddar ner video...',
        'video_downloaded': 'Video laddades ner framgångsrikt.',
        'enter_youtube_url': 'Ange YouTube URL:',
        'select_quality': 'Välj önskad kvalitet (ange motsvarande nummer):',
        'invalid_choice': 'Ogiltigt val. Försök igen.',
    },
    'pl': {
        'available_qualities': 'Dostępne jakości:',
        'resolution': 'Rozdzielczość',
        'format': 'Format',
        'downloading_video': 'Pobieranie filmu...',
        'video_downloaded': 'Film został pomyślnie pobrany.',
        'enter_youtube_url': 'Wprowadź URL filmu z YouTube:',
        'select_quality': 'Wybierz żądaną jakość (wprowadź odpowiadającą jej liczbę):',
        'invalid_choice': 'Nieprawidłowy wybór. Spróbuj ponownie.',
    },
}

warnings.filterwarnings("ignore", category=DeprecationWarning)

def get_system_language():
    system_language = locale.getdefaultlocale()
    return system_language[0].split('_')[0] if system_language[0] else 'en'

def translate(text, language):
    if language in translations and text in translations[language]:
        return translations[language][text]
    else:
        return translations['en'][text] if 'en' in translations and text in translations['en'] else text

def translated_print(text, language):
    print(translate(text, language))

def print_streams(streams, language):
    translated_print("available_qualities", language)
    for i, stream in enumerate(streams):
        print(f"{i+1}. {translate('resolution', language)}: {stream.resolution}, {translate('format', language)}: {stream.mime_type}")

def download_video(stream, output_path, language):
    translated_print("downloading_video", language)
    stream.download(output_path=output_path)
    translated_print("video_downloaded", language)

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    download_dir = os.path.join(current_dir, "Downloads")
    os.makedirs(download_dir, exist_ok=True)

    system_language = get_system_language()

    translated_print("enter_youtube_url", system_language)
    video_path = input()

    yt = YouTube(video_path)
    streams = yt.streams.filter(progressive=True)

    print_streams(streams, system_language)

    translated_print("select_quality", system_language)
    choice = int(input()) - 1

    try:
        selected_stream = streams[choice]
        download_video(selected_stream, output_path=download_dir, language=system_language)
    except IndexError:
        translated_print("invalid_choice", system_language)

if __name__ == "__main__":
    main()
