from arm.logicnode.arm_nodes import *


class DrawRectNode(ArmLogicTreeNode):
    """Draws a rectangle.

    @input Draw: Activate to draw the rectangle on this frame. The input must
        be (indirectly) called from an `On Render2D` node.
    @input Color: The color of the rectangle.
    @input Filled: Whether the rectangle is filled or only the outline is drawn.
    @input Strength: The line strength if the rectangle is not filled.
    @input X/Y: Position of the rectangle, in pixels from the top left corner.
    @input Width/Height: Size of the rectangle in pixels. The rectangle
        grows towards the bottom right corner.

    @output Out: Activated after the rectangle has been drawn.

    @see [`kha.graphics2.Graphics.drawRect()`](http://kha.tech/api/kha/graphics2/Graphics.html#drawRect).
    @see [`kha.graphics2.Graphics.fillRect()`](http://kha.tech/api/kha/graphics2/Graphics.html#fillRect).
    """
    bl_idname = 'LNDrawRectNode'
    bl_label = 'Draw Rect'
    arm_section = 'draw'
    arm_version = 1

    def arm_init(self, context):
        self.add_input('ArmNodeSocketAction', 'Draw')
        self.add_input('ArmColorSocket', 'Color', default_value=[1.0, 1.0, 1.0, 1.0])
        self.add_input('ArmBoolSocket', 'Filled', default_value=False)
        self.add_input('ArmFloatSocket', 'Strength', default_value=1.0)
        self.add_input('ArmFloatSocket', 'X')
        self.add_input('ArmFloatSocket', 'Y')
        self.add_input('ArmFloatSocket', 'Width')
        self.add_input('ArmFloatSocket', 'Height')

        self.add_output('ArmNodeSocketAction', 'Out')
