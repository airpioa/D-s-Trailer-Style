# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.9] - 2026-02-18

### Changed

- **Controls**: Completely remapped controls to a standard 100% keyboard layout.
  - Assigned **Crawl** to `C` and **Zoomify** to `Z`.
  - Resolved all modded keybind conflicts and UI overlaps.
  - **Fixed mod configurations and shaders** keybind stability.
  - Restored Minecraft **F3 Debug Sub-Keys** (Hitboxes, Chunk Reload, etc.) to their default assignments.
  - Unmapped redundant or overlapping utility keys (Creative Toolbar, Zume, FBP settings) to ensure a conflict-free "Key Binds" menu.
- **Documentation**: Added a detailed `CONTROL_MAPPING.md` chart for user reference.

## [1.0.8] - 2026-02-17

### Added

- **Optimization**: Distant Horizons, VMP, Noisium, Alternate Current, Bad Optimizations, Immersive Optimization.
- **Visuals**: Default Dark Mode, Tectonic, Geophilic v3, Serene Seasons, Bare Bones Moon Fix.
- **Features**: Controlify, Diagonal Fences, Immersive UI, Reactive Music, Stoneworks, Better Tab, Collision Fix, Drip Sounds.
- **Configuration**: Detailed modpack description in `README.md`, CC BY-NC 4.0 license, and Dependency Review workflow.
- **Branding**: Customized Crash Assistant for "D's Trailer Style" with GitHub Issues integration.

### Changed

- **Mod Updates**:
  - Ambient Sounds (v6.3.1 -> v6.3.5)
  - Not Enough Animations (v1.11.1 -> v1.11.2)
  - entity_texture_features (v7.0.8 -> v7.0.9)
  - More Culling (v1.6.1 -> v1.6.2)
  - polytone (v5.4.9 -> v5.4.11)
  - skyboxify (v2.4 -> v2.5)
  - BSL Shaders (v10.1 -> v10.1.1)
- **Repository**: Relocated project files to new profile directory and removed Git LFS.

### Fixed

- Resolved diverging branches in the Git repository.

### Removed

- **Voxy**: Replaced with Distant Horizons.
- **Untracked Folders**: Removed `.fabric/`, `screenshots/`, `logs/`, and `local/` from Git tracking.
- Removed legacy `Bare Bones x Fresh Animations 1.10.1.zip` in favor of `1.10.3`.
