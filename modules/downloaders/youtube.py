from os import path

from yt_dlp import YoutubeDL

from modules.config import DURATION_LIMIT
from modules.helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio/best",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)
    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"🛑 Video ini terlalu panjang goblok {DURATION_LIMIT} Menit (s) Ditolak , Harusnya {duration} Menit(s)",
        )
    try:
        ydl.download([url])
    except:
        raise DurationLimitError(
            f"🛑 Video ini terlalu panjang goblok {DURATION_LIMIT} Menit(s) Ditolak , Harusnya {duration} Menit(s)",
        )
    return path.join("downloads", f"{info['id']}.{info['ext']}")
