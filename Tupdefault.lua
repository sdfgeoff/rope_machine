-- tup.creategitignore()

gen_stls = tup.foreach_rule('*.stl.FCStd', 'python $(TOP)/tools/export_stl.py %f %o', '$(STL_FOLDER)/%B')

-- $(HIDE)$(PYTHON3) $(PROJECT_DIR)/tools/export_gcode.py $< $@
gen_gcode = tup.foreach_rule(gen_stls, 'python $(TOP)/tools/export_gcode.py %f %o', '$(GCODE_FOLDER)/%B.gcode')
