import os
import pygame

def import_sprite(path):
    surface_list = []

    if not os.path.exists(path):
        print(f"[ERROR] La ruta '{path}' no existe.")
        return surface_list

    try:
        # Filtra y ordena solo archivos de imagen válidos
        files = sorted([
            file for file in os.listdir(path)
            if file.lower().endswith(('.png', '.jpg', '.jpeg'))
        ])

        if not files:
            print(f"[ADVERTENCIA] No se encontraron imágenes en '{path}'.")

        for file in files:
            full_path = os.path.join(path, file)
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)

        print(f"[INFO] {len(surface_list)} sprites cargados desde '{path}'")

    except Exception as e:
        print(f"[ERROR] al cargar sprites desde '{path}': {e}")

    return surface_list
