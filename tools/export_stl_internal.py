import FreeCAD
import sys
import os
import MeshPart
import Mesh

try:
    args = sys.argv[sys.argv.index("--")+1:]

    input_filename = args[0]
    output_filename = args[1]

    print("Opening {}".format(input_filename))
    doc = FreeCAD.open(input_filename)

    clean_filename = os.path.basename(input_filename).replace(".FCStd", "")

    stl_objects = []
    for obj in doc.Objects:
        if obj.Label.endswith("_stl") or obj.Label.endswith(".stl"):
            stl_objects.append(obj)

    if len(stl_objects) == 0:
        raise Exception("No objects ending in '_stl' present in file")
#    if len(stl_objects) != 1:
#        raise Exception(f"For build reproducibility, there can only be exactly one object ending in '_stl' in the freecad file. Found {list(o.Label for o in stl_objects)}")

    # Combine all objects ending into one mesh
    meshes = []

    for obj in stl_objects:
        shape = obj.Shape

        # Would be nice to just export the file as STL but this uses (inconsistent)
        # view settings, so isn't reliable at producing smooth arcs etc.
        # shape.exportStl(output_filename)
        msh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "Mesh")

        msh.Mesh = MeshPart.meshFromShape(
            Shape=shape, 
            LinearDeflection=0.01, 
            AngularDeflection=0.0872665
        )
        meshes.append(msh)
    print("Exporting to {}".format(output_filename))
    Mesh.export(meshes, output_filename)

            
    exit(0)
except Exception as e:
    print(e)
    exit(1)
