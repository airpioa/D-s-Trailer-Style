import os

def remap_controls_robust():
    options_path = '/Users/zylermillet/Library/Application Support/ModrinthApp/profiles/D_s Trailer Style/options.txt'
    
    if not os.path.exists(options_path):
        return

    with open(options_path, 'r') as f:
        lines = f.readlines()

    vanilla_keys = {
        'key_key.attack', 'key_key.use', 'key_key.forward', 'key_key.left', 
        'key_key.back', 'key_key.right', 'key_key.jump', 'key_key.sneak', 
        'key_key.sprint', 'key_key.drop', 'key_key.inventory', 'key_key.chat', 
        'key_key.playerlist', 'key_key.pickItem', 'key_key.command', 
        'key_key.socialInteractions', 'key_key.toggleGui', 'key_key.togglePerspective', 
        'key_key.screenshot', 'key_key.smoothCamera', 'key_key.fullscreen', 
        'key_key.spectatorOutlines', 'key_key.spectatorHotbar', 'key_key.swapOffhand', 
        'key_key.saveToolbarActivator', 'key_key.loadToolbarActivator', 'key_key.advancements', 
        'key_key.quickActions', 'key_key.toggleSpectatorShaderEffects'
    }

    mapping = {
        'key_iris.keybind.toggleShaders': 'key.keyboard.o',
        'key_iris.keybind.reload': 'key.keyboard.r',
        'key_iris.keybind.shaderPackSelection': 'key.keyboard.y',
        'key_iris.keybind.wireframe': 'key.keyboard.backslash',
        'key_key.modmenu.open_menu': 'key.keyboard.m',
        'key_key.presencefootsteps.toggle': 'key.keyboard.u',
        'key_key.stfu.toggle_music': 'key.keyboard.f7',
        'key_key.stfu.skip_music': 'key.keyboard.f8',
        'key_key.stfu.narrator_hotkey': 'key.keyboard.f9',
        'key_keybinds.bettercombat.feint': 'key.keyboard.comma',
        'key_keybinds.bettercombat.toggle_mine_with_weapons': 'key.keyboard.period',
    }

    used_keys = set()
    for line in lines:
        if ':' in line:
            val = line.split(':', 1)[1].strip()
            if val != 'key.keyboard.unknown':
                used_keys.add(val)

    # Pre-add manual mappings to used keys
    for k in mapping.values():
        used_keys.add(k)

    f_index = 12
    def get_next_available():
        nonlocal f_index
        while True:
            f_index += 1
            f_key = f'key.keyboard.f{f_index}'
            if f_key not in used_keys:
                return f_key

    new_lines = []
    for line in lines:
        if line.startswith('key_') and 'key.keyboard.unknown' in line:
            key_name = line.split(':', 1)[0]
            is_vanilla = key_name in vanilla_keys or key_name.startswith('key_key.debug.') or key_name.startswith('key_hotbar.')
            
            if not is_vanilla:
                target_key = mapping.get(key_name) or get_next_available()
                line = f"{key_name}:{target_key}\n"
                used_keys.add(target_key)
        new_lines.append(line)

    with open(options_path, 'w') as f:
        f.writelines(new_lines)
    
    print("Robust remapping complete.")

if __name__ == "__main__":
    remap_controls_robust()
