import os

def global_vars(request):
    social_media_names = os.environ.get("SOCIAL_MEIDA_NAMES", "").split(",")
    social_media_links = os.environ.get("SOCIAL_MEIDA_LINKS", "").split(",")
    social_media_icons = os.environ.get("SOCIAL_MEIDA_ICONS", "").split(",")

    social_medias = [
        {"name": n, "link": a, "icon": c}
        for n, a, c in zip(social_media_names, social_media_links, social_media_icons)
    ]

    return {
        "SITE_TITLE": os.environ.get("SITE_TITLE"),
        "EMAIL_ADDRESS": os.environ.get("EMAIL_ADDRESS"),
        "SOCIAL_MEDIAS": social_medias
    }