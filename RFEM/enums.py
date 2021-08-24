from enum import Enum

class MemberType(Enum):
    '''
    Member Type | Enum
    '''
    TYPE_BEAM, TYPE_BUCKLING, TYPE_CABLE, TYPE_COMPRESSION, TYPE_COUPLING_HINGE_HINGE,\
    TYPE_COUPLING_HINGE_RIGID, TYPE_COUPLING_RIGID_HINGE, TYPE_COUPLING_RIGID_RIGID,\
    TYPE_DEFINABLE_STIFFNESS, TYPE_RIB, TYPE_RIGID, TYPE_TENSION, TYPE_TRUSS, TYPE_TRUSS_ONLY_N = range(14)


class NodalSupportType(Enum):
    '''
    Nodal Support Type | Enum
    '''
    FIXED, HINGED, ROLLER, ROLLER_IN_X, ROLLER_IN_Y, ROLLER_IN_Z = range(6)


class StaticAnalysisType(Enum):
    '''
    Static Analysis Type | Enum
    '''
    GEOMETRICALLY_LINEAR, LARGE_DEFORMATIONS, LARGE_DEFORMATIONS_POSTRCRITICAL, SECOND_ORDER_P_DELTA = range(4)


class AnalysisType(Enum):
    '''
    Analysis Type | Enum
    '''
    ANALYSIS_TYPE_CREEP_AND_SHRINKAGE, ANALYSIS_TYPE_CUTTING_PATTERN, ANALYSIS_TYPE_MODAL, ANALYSIS_TYPE_RESPONSE_SPECTRUM,\
    ANALYSIS_TYPE_STATIC, ANALYSIS_TYPE_TIME_DEPENDENT, ANALYSIS_TYPE_TIME_HISTORY, ANALYSIS_TYPE_WIND_SIMULATION = range(8)


class LoadDirectionType(Enum):
    '''
    Load Direction Type | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U, LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V, LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W,\
    LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z = range(6)

class MemberLoadDirection(Enum):
    '''
    Member Load Direction | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_PROJECTED, LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE,\
    LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_PROJECTED, LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE,\
    LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_PROJECTED, LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,\
    LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z, LOAD_DIRECTION_PRINCIPAL_U,\
    LOAD_DIRECTION_PRINCIPAL_V = range(11)

class MemberLoadType(Enum):
    '''
    Member Load Type | Enum
    '''
    E_TYPE_MASS, LOAD_TYPE_AXIAL_DISPLACEMENT, LOAD_TYPE_AXIAL_STRAIN, LOAD_TYPE_DISPLACEMENT, LOAD_TYPE_FORCE,\
    LOAD_TYPE_FORM_FINDING, LOAD_TYPE_INITIAL_PRESTRESS, LOAD_TYPE_MOMENT, LOAD_TYPE_PIPE_CONTENT_FULL,\
    LOAD_TYPE_PIPE_CONTENT_PARTIAL, LOAD_TYPE_PIPE_INTERNAL_PRESSURE, LOAD_TYPE_PRECAMBER, LOAD_TYPE_ROTARY_MOTION,\
    LOAD_TYPE_ROTATION, LOAD_TYPE_TEMPERATURE, LOAD_TYPE_TEMPERATURE_CHANGE = range(16)


class MemberLoadDistribution(Enum):
    '''
    Member Load Distribution | Enum
    '''
    LOAD_DISTRIBUTION_CONCENTRATED_1, LOAD_DISTRIBUTION_CONCENTRATED_2, LOAD_DISTRIBUTION_CONCENTRATED_2x2,\
    LOAD_DISTRIBUTION_CONCENTRATED_N, LOAD_DISTRIBUTION_CONCENTRATED_VARYING, LOAD_DISTRIBUTION_PARABOLIC,\
    LOAD_DISTRIBUTION_TAPERED, LOAD_DISTRIBUTION_TRAPEZOIDAL, LOAD_DISTRIBUTION_UNIFORM, LOAD_DISTRIBUTION_UNIFORM_TOTAL,\
    LOAD_DISTRIBUTION_VARYING, LOAD_DISTRIBUTION_VARYING_IN_Z = range(12)

class MemberHingeAxialRelease(Enum):
    '''
    Member Hinge Axial Release | Enum
    '''
    NONLINEARITY_TYPE_DIAGRAM, NONLINEARITY_TYPE_FAILURE_ALL_IF_NEGATIVE, NONLINEARITY_TYPE_FAILURE_ALL_IF_POSITIVE,\
    NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE, NONLINEARITY_TYPE_FAILURE_IF_POSITIVE, NONLINEARITY_TYPE_FRICTION_DIRECTION_1,\
    NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2, NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2, NONLINEARITY_TYPE_FRICTION_DIRECTION_2,\
    NONLINEARITY_TYPE_NONE, NONLINEARITY_TYPE_PARTIAL_ACTIVITY, NONLINEARITY_TYPE_STIFFNESS_DIAGRAM = range(12)

class LineLoadType(Enum):
    '''
    Line Load Type | Enum
    '''
    E_TYPE_MASS, LOAD_TYPE_FORCE, LOAD_TYPE_MOMENT = range(3)

class LineLoadDistribution(Enum):
    '''
    Line Load Distribution | Enum
    '''
    LOAD_DISTRIBUTION_CONCENTRATED_1, LOAD_DISTRIBUTION_CONCENTRATED_2, LOAD_DISTRIBUTION_CONCENTRATED_2x2,\
    LOAD_DISTRIBUTION_CONCENTRATED_N, LOAD_DISTRIBUTION_CONCENTRATED_VARYING, LOAD_DISTRIBUTION_PARABOLIC,\
    LOAD_DISTRIBUTION_TAPERED, LOAD_DISTRIBUTION_TRAPEZOIDAL, LOAD_DISTRIBUTION_UNIFORM, LOAD_DISTRIBUTION_UNIFORM_TOTAL,\
    LOAD_DISTRIBUTION_VARYING = range(11)
    
class SurfaceLoadDistribution(Enum):
    '''
    Surface Load Distribution | Enum
    '''
    LOAD_DISTRIBUTION_LINEAR, LOAD_DISTRIBUTION_LINEAR_IN_X, LOAD_DISTRIBUTION_LINEAR_IN_Y, LOAD_DISTRIBUTION_LINEAR_IN_Z,\
    LOAD_DISTRIBUTION_RADIAL, LOAD_DISTRIBUTION_UNIFORM, LOAD_DISTRIBUTION_VARYING_IN_Z = range(7)

class SurfaceLoadDirection(Enum):
    '''
    Surface Load Direction | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_PROJECTED, LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE,\
    LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_PROJECTED, LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE,\
    LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_PROJECTED, LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,\
    LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z = range(9)

class SurfaceLoadType(Enum):
    '''
    Surface Load Type | Enum
    '''
    LOAD_TYPE_AXIAL_STRAIN, LOAD_TYPE_FORCE, LOAD_TYPE_FORM_FINDING, LOAD_TYPE_MASS, LOAD_TYPE_PRECAMBER,\
    LOAD_TYPE_ROTARY_MOTION, LOAD_TYPE_TEMPERATURE = range(7)

class SetType(Enum):
    '''
    Line, Member, Surface, and Solid Set Type | Enum
    '''
    SET_TYPE_CONTINUOUS, SET_TYPE_GROUP = range(2)

class NodalLoadType(Enum):
    '''
    Nodal Load Type | Enum
    '''

    LOAD_TYPE_COMPONENTS, LOAD_TYPE_FORCE, LOAD_TYPE_MASS, LOAD_TYPE_MOMENT = range(4)

class NodalLoadSpecificDirectionType(Enum):
    '''
    Nodal Load Specific Direction Type | Enum
    '''

    DIRECTION_TYPE_DIRECTED_TO_NODE, DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE, DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER, DIRECTION_TYPE_PARALLEL_TO_TWO_NODES, DIRECTION_TYPE_ROTATED_VIA_3_ANGLES = range(5)

class NodalLoadAxesSequence(Enum):
    '''
    Nodal Load Axes Sequence | Enum
    '''

    SEQUENCE_XYZ, SEQUENCE_XZY, SEQUENCE_YXZ, SEQUENCE_YZX, SEQUENCE_ZXY, SEQUENCE_ZYX = range(6)

class NodalLoadMassAxisRotation(Enum):
    '''
    Nodal Load Mass Axis Rotation | Enum
    '''

    AXIS_OF_ROTATION_X_NEGATIVE, AXIS_OF_ROTATION_X_POSITIVE, AXIS_OF_ROTATION_Y_NEGATIVE, AXIS_OF_ROTATION_Y_POSITIVE, AXIS_OF_ROTATION_Z_NEGATIVE, AXIS_OF_ROTATION_Z_POSITIVE = range(6)


class MemberLoadEccentricityHorizontalAlignment(Enum):
    '''
    Member Load Eccentricity Horizontal Alignment
    '''

    ALIGN_LEFT, ALIGN_MIDDLE, ALIGN_NONE, ALIGN_TOP = range(4)


class MemberLoadEccentricityVerticalAlignment(Enum):
    '''
    Member Load Eccentricity Vertical Alignment
    '''

    ALIGN_LEFT, ALIGN_MIDDLE, ALIGN_NONE, ALIGN_TOP = range(4)

class MemberLoadEccentricitySectionMiddle(Enum):
    '''
    Member Load Eccentricity Section Middle
    '''

    LOAD_ECCENTRICITY_SECTION_MIDDLE_CENTER_OF_GRAVITY, LOAD_ECCENTRICITY_SECTION_MIDDLE_NONE, LOAD_ECCENTRICITY_SECTION_MIDDLE_SHEAR_CENTER = range(3)

class MemberLoadFormFindingDefinitonType(Enum):
    '''
    Member Load Form Finding Definiton Type
    '''

    FORM_FINDING_TYPE_FORCE, FORM_FINDING_TYPE_GEOMETRIC = range(2)

class MemberLoadFormFindingForceDefinition(Enum):
    '''
    Member Load Form Finding Force Definition
    '''

    FORM_FINDING_FORCE_INPUT_PARAMETER_AVERAGE, FORM_FINDING_FORCE_INPUT_PARAMETER_DENSITY, FORM_FINDING_FORCE_INPUT_PARAMETER_HORIZONTAL_TENSION_COMPONENT, \
    FORM_FINDING_FORCE_INPUT_PARAMETER_MAXIMUM_FORCE_IN_MEMBER, FORM_FINDING_FORCE_INPUT_PARAMETER_MINIMAL_TENSION_AT_I_END, \
    FORM_FINDING_FORCE_INPUT_PARAMETER_MINIMAL_TENSION_AT_J_END, FORM_FINDING_FORCE_INPUT_PARAMETER_MINIMUM_FORCE_IN_MEMBER,\
    FORM_FINDING_FORCE_INPUT_PARAMETER_TENSION_AT_I_END, FORM_FINDING_FORCE_INPUT_PARAMETER_TENSION_AT_J_END = range(9)

class MemberLoadFormFindingGeometryDefinition(Enum):
    '''
    Member Load Form Finding Geometry Definition
    '''

    FORM_FINDING_GEOMETRIC_INPUT_PARAMETER_LENGTH, FORM_FINDING_GEOMETRIC_INPUT_PARAMETER_LOW_POINT_VERTICAL_SAG, \
    FORM_FINDING_GEOMETRIC_INPUT_PARAMETER_MAXIMUM_VERTICAL_SAG, FORM_FINDING_GEOMETRIC_INPUT_PARAMETER_SAG, \
    FORM_FINDING_GEOMETRIC_INPUT_PARAMETER_UNSTRESSED_LENGTH = range(5)

class MemberLoadFormFindingInternalForce(Enum):
    '''
    Member Load Form Finding Internal Force
    '''

    FORM_FINDING_INTERNAL_FORCE_COMPRESSION, FORM_FINDING_INTERNAL_FORCE_TENSION = range(2)

class MemberLoadDirectionOrientation(Enum):
    '''
    Member Load Direction Orientation
    '''
    LOAD_DIRECTION_FORWARD, LOAD_DIRECTION_REVERSED = range(2)

class MemberLoadAxisDefinitionType(Enum):
    '''
    Member Load Axis Definition
    '''
    AXIS_DEFINITION_POINT_AND_AXIS, AXIS_DEFINITION_TWO_POINTS = range(2)

class MemberLoadAxisDefinition(Enum):
    '''
    Member Load Axis Definition
    '''
    AXIS_X, AXIS_Y, AXIS_Z = range(3)

class MemberLoadAxisDefinitionAxisOrientation(Enum):
    '''
    Member Load Axis Definition Axis Orientation
    '''

    AXIS_NEGATIVE, AXIS_POSITIVE = range(2)


    




