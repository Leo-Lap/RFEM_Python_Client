from RFEM.initModel import Model
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.section import Section
from RFEM.enums import MemberType

# Initialize the model
Model()

# Define nodes for a 20 m span Bailey bridge
span_length = 20000  # in mm
depth = 2000         # in mm (vertical distance between top and bottom chords)
num_panels = 10      # Number of panels in the bridge
delta_x = span_length / num_panels  # Panel length

top_nodes = []       # Nodes for the top chord
bottom_nodes = []    # Nodes for the bottom chord
vertical_nodes = []  # Nodes for verticals

# Create nodes
for i in range(num_panels + 1):
    x_coord = i * delta_x

    # Top chord node
    top_node = Node(no=i + 1, coordinate_X=x_coord, coordinate_Y=depth, coordinate_Z=0)
    top_nodes.append(i + 1)

    # Bottom chord node
    bottom_node = Node(no=i + 1 + num_panels + 1, coordinate_X=x_coord, coordinate_Y=0, coordinate_Z=0)
    bottom_nodes.append(i + 1 + num_panels + 1)

# Define sections
Section(no=1, name="IPE 300")  # Steel profile for all members

# Create members for top and bottom chords
for i in range(num_panels):
    # Top chord member
    Member.Beam(
        no=i + 1,
        start_node_no=top_nodes[i],
        end_node_no=top_nodes[i + 1],
        start_section_no=1,
        end_section_no=1,
        comment="Top chord"
    )

    # Bottom chord member
    Member.Beam(
        no=i + 1 + num_panels,
        start_node_no=bottom_nodes[i],
        end_node_no=bottom_nodes[i + 1],
        start_section_no=1,
        end_section_no=1,
        comment="Bottom chord"
    )

# Create vertical and diagonal members
member_no = 2 * num_panels + 1
for i in range(num_panels):
    # Vertical member
    Member.Beam(
        no=member_no,
        start_node_no=top_nodes[i],
        end_node_no=bottom_nodes[i],
        start_section_no=1,
        end_section_no=1,
        comment="Vertical"
    )
    member_no += 1

    # Diagonal member
    if i < num_panels - 1:  # Avoid connecting diagonals on the last panel
        Member.Beam(
            no=member_no,
            start_node_no=top_nodes[i + 1],
            end_node_no=bottom_nodes[i],
            start_section_no=1,
            end_section_no=1,
            comment="Diagonal"
        )
        member_no += 1

# Finish modifications and save
Model.clientModel.service.finish_modification()

# Save the model
Model.clientModel.service.save("Bailey_Bridge.rf6")
print("Bailey bridge model created and saved as Bailey_Bridge.rf6")
