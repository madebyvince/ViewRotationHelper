bl_info = {
    "name": "View Rotation Helper",
    "author": "Vince",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > View",
    "description": "Quick access to orthogonal views with rotation control",
    "category": "3D View",
}

import bpy
import math


class VIEW3D_OT_set_view_axis_custom(bpy.types.Operator):
    """Set view to specific orthogonal axis"""
    bl_idname = "view3d.set_view_axis_custom"
    bl_label = "Set View Axis"
    bl_options = {'REGISTER', 'UNDO'}
    
    axis: bpy.props.EnumProperty(
        items=[
            ('TOP', "Top", "Top view"),
            ('BOTTOM', "Bottom", "Bottom view"),
            ('FRONT', "Front", "Front view"),
            ('BACK', "Back", "Back view"),
            ('LEFT', "Left", "Left view"),
            ('RIGHT', "Right", "Right view"),
        ]
    )
    
    def execute(self, context):
        bpy.ops.view3d.view_axis(type=self.axis, align_active=False)
        return {'FINISHED'}


class VIEW3D_OT_rotate_view_90(bpy.types.Operator):
    """Rotate current view by 90 degrees"""
    bl_idname = "view3d.rotate_view_90"
    bl_label = "Rotate View 90°"
    bl_options = {'REGISTER', 'UNDO'}
    
    angle: bpy.props.FloatProperty(
        name="Angle",
        default=90.0,
        description="Rotation angle in degrees"
    )
    
    def execute(self, context):
        bpy.ops.view3d.view_roll(angle=math.radians(self.angle))
        return {'FINISHED'}


class VIEW3D_PT_view_rotation_helper(bpy.types.Panel):
    """Panel for view rotation helper"""
    bl_label = "View Rotation Helper"
    bl_idname = "VIEW3D_PT_view_rotation_helper"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'View'
    
    def draw(self, context):
        layout = self.layout
        
        # Orthogonal views section
        box = layout.box()
        box.label(text="Orthogonal Views:", icon='ORIENTATION_VIEW')
        
        # Top row: Top and Bottom
        row = box.row(align=True)
        row.scale_y = 1.5
        op = row.operator("view3d.set_view_axis_custom", text="Top", icon='TRIA_UP')
        op.axis = 'TOP'
        op = row.operator("view3d.set_view_axis_custom", text="Bottom", icon='TRIA_DOWN')
        op.axis = 'BOTTOM'
        
        # Middle row: Front and Back
        row = box.row(align=True)
        row.scale_y = 1.5
        op = row.operator("view3d.set_view_axis_custom", text="Front", icon='FORWARD')
        op.axis = 'FRONT'
        op = row.operator("view3d.set_view_axis_custom", text="Back", icon='BACK')
        op.axis = 'BACK'
        
        # Bottom row: Left and Right
        row = box.row(align=True)
        row.scale_y = 1.5
        op = row.operator("view3d.set_view_axis_custom", text="Left", icon='TRIA_LEFT')
        op.axis = 'LEFT'
        op = row.operator("view3d.set_view_axis_custom", text="Right", icon='TRIA_RIGHT')
        op.axis = 'RIGHT'
        
        # Separator
        layout.separator()
        
        # Rotation section
        box = layout.box()
        box.label(text="Rotate Current View:", icon='FILE_REFRESH')
        
        row = box.row(align=True)
        row.scale_y = 1.5
        op = row.operator("view3d.rotate_view_90", text="-90°", icon='LOOP_BACK')
        op.angle = -90.0
        op = row.operator("view3d.rotate_view_90", text="+90°", icon='LOOP_FORWARDS')
        op.angle = 90.0


# Registration
classes = (
    VIEW3D_OT_set_view_axis_custom,
    VIEW3D_OT_rotate_view_90,
    VIEW3D_PT_view_rotation_helper,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()