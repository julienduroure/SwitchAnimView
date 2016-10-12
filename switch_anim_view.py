#====================== BEGIN GPL LICENSE BLOCK ======================
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#======================= END GPL LICENSE BLOCK ========================
bl_info = {
	"name": "Switch Anim View",
	"author": "Julien Duroure, based on Hjalti Hjalmarsson idea",
	"version": (1, 0, 0),
	"blender": (2,78, 0),
	"description": "Switch between Graph Editor & DopeSheet",
	"wiki_url": "http://blerifa.com/tools/SwitchAnimView/",
	"tracker_url": "https://github.com/julienduroure/SwitchAnimView/issues/",
	"category": "Animation",
}

import bpy


def main(context):
	if context.area.type == "DOPESHEET_EDITOR":
		context.area.type = "GRAPH_EDITOR"
	else:
		context.area.type = "DOPESHEET_EDITOR"

class SwitchAnimView(bpy.types.Operator):
	"""Graph Editor & DopeSheet > Use Z to switch"""
	bl_idname = "wm.switch_anim_view"
	bl_label = "Switch Anim view"

	@classmethod
	def poll(cls, context):
		return context.area.type in ["DOPESHEET_EDITOR","GRAPH_EDITOR"]

	def execute(self, context):
		main(context)
		return {'FINISHED'}


addon_keymaps = []

def register():
	bpy.utils.register_class(SwitchAnimView)

	wm = bpy.context.window_manager

	if wm.keyconfigs.addon:
		km = wm.keyconfigs.addon.keymaps.new(name='Animation')
		kmi = km.keymap_items.new('wm.switch_anim_view', 'Z', 'PRESS')

		addon_keymaps.append(km)


def unregister():
	bpy.utils.unregister_class(SwitchAnimView)

	wm = bpy.context.window_manager

	if wm.keyconfigs.addon:
		for km in addon_keymaps:
			for kmi in km.keymap_items:
				km.keymap_items.remove(kmi)

			wm.keyconfigs.addon.keymaps.remove(km)

	# clear the list
	del addon_keymaps[:]

if __name__ == "__main__":
    print("register")
    register()
