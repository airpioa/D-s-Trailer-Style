import os

def remap_controls():
    options_path = '/Users/zylermillet/Library/Application Support/ModrinthApp/profiles/D_s Trailer Style/options.txt'
    
    if not os.path.exists(options_path):
        print(f"Error: {options_path} not found.")
        return

    with open(options_path, 'r') as f:
        lines = f.readlines()

    # Mapping for currently 'unknown' modded keys
    mapping = {
        # Shaders
        'key_iris.keybind.toggleShaders': 'key.keyboard.o',
        'key_iris.keybind.reload': 'key.keyboard.r',
        'key_iris.keybind.shaderPackSelection': 'key.keyboard.y',
        'key_iris.keybind.wireframe': 'key.keyboard.backslash',
        
        # Mod Menu
        'key_key.modmenu.open_menu': 'key.keyboard.m',
        
        # Audio
        'key_key.presencefootsteps.toggle': 'key.keyboard.u',
        'key_key.stfu.toggle_music': 'key.keyboard.f7',
        'key_key.stfu.skip_music': 'key.keyboard.f8',
        'key_key.stfu.narrator_hotkey': 'key.keyboard.f9',
        
        # Gameplay / Culling
        'key_key.entityculling.toggle': 'key.keyboard.f12',
        'key_key.entityculling.toggleBoxes': 'key.keyboard.right.bracket',
        'key_keybinds.bettercombat.feint': 'key.keyboard.comma',
        'key_keybinds.bettercombat.toggle_mine_with_weapons': 'key.keyboard.period',
        
        # FBP (Fancy Block Particles)
        'key_key.fbp.toggle_mod': 'key.keyboard.semicolon',
        'key_key.fbp.toggle_animations': 'key.keyboard.grave',
        'key_key.fbp.open_settings': 'key.keyboard.home',
        'key_key.fbp.freeze_particles': 'key.keyboard.page.up',
        'key_key.fbp.kill_particles': 'key.keyboard.page.down',
        'key_key.fbp.add_to_blacklist': 'key.keyboard.insert',
        'key_key.fbp.reload_config': 'key.keyboard.f13',
        
        # Utility
        'key_key.dynamic_fps.toggle_forced': 'key.keyboard.f14',
        'key_key.dynamic_fps.toggle_disabled': 'key.keyboard.f15',
        'key_tab.bettertab.keybind.toggle_mod': 'key.keyboard.f16',
        'key_lambdynlights.key.toggle_fps_dynamic_lighting': 'key.keyboard.f17',
        'key_zoomify.key.zoom.secondary': 'key.keyboard.f18',
        'key_key.optigui.inspect': 'key.keyboard.f19',
        
        # Jade Profiles
        'key_key.jade.profile.0': 'key.keyboard.keypad.6',
        'key_key.jade.profile.1': 'key.keyboard.keypad.7',
        'key_key.jade.profile.2': 'key.keyboard.keypad.8',
        'key_key.jade.profile.3': 'key.keyboard.keypad.9',
        
        # Flashback markers
        'key_flashback.keybind.create_marker_1': 'key.keyboard.f20',
        'key_flashback.keybind.create_marker_2': 'key.keyboard.f21',
        'key_flashback.keybind.create_marker_3': 'key.keyboard.f22',
        'key_flashback.keybind.create_marker_4': 'key.keyboard.f23',
    }

    # Vanilla prefixes to protect
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

    new_lines = []
    for line in lines:
        if line.startswith('key_'):
            parts = line.split(':', 1)
            if len(parts) == 2:
                key_name = parts[0]
                # Check if it's vanilla or a debug key
                is_vanilla = key_name in vanilla_keys or key_name.startswith('key_key.debug.') or key_name.startswith('key_hotbar.')
                
                if not is_vanilla and 'key.keyboard.unknown' in parts[1]:
                    if key_name in mapping:
                        line = f"{key_name}:{mapping[key_name]}\n"
        new_lines.append(line)

    with open(options_path, 'w') as f:
        f.writelines(new_lines)
    
    print("Controls remapped successfully.")

if __name__ == "__main__":
    remap_controls()
