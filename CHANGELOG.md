# Changelog

All notable changes to the View Rotation Helper add-on will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-02

### Added
- Initial release of View Rotation Helper
- Six orthogonal view buttons (Top, Bottom, Front, Back, Left, Right)
- View rotation functionality with +90° and -90° buttons
- Sidebar panel in 3D View under "View" tab
- Icon support for better visual clarity
- Organized layout with separate sections for views and rotations
- Undo/Redo support for all operations

### Features
- Quick access to all standard orthogonal views
- Ability to rotate locked orthogonal views by 90-degree increments
- Clean and intuitive user interface
- Larger buttons (1.5x scale) for easy clicking
- Grouped layout with visual separators

### Technical Details
- Compatible with Blender 3.0+
- Uses native Blender operators (`view3d.view_axis` and `view3d.view_roll`)
- Proper operator registration and unregistration
- Full undo/redo integration

---

## Release Notes

### Version 1.0.0
This is the first stable release of View Rotation Helper. The add-on addresses a common workflow need in Blender: the ability to rotate orthogonal views, which is not natively available in Blender's default view controls.

**Target Users**: 3D artists, modelers, and designers who frequently work with orthogonal views and need precise control over view angles.

**Future Posible Plans**: 
- Custom rotation angles (e.g., 45°, 180°)
- Keyboard shortcuts for quick access
- View presets and saved configurations
- Additional view alignment tools

---

[1.0.0]: https://github.com/yourusername/view-rotation-helper/releases/tag/v1.0.0
