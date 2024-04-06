from .Arithmetic import IntMultiplication, FloatMultiplication, IntSubtraction
from .Numeral import NumeralToString, TwoFloats, FourFloats, SixFloats, EightFloats, StepsAndCfg, StepsAndCfgAndWH
from .Util import CanvasCreatorAdvanced, CanvasCreatorSimple, CanvasCreatorBasic, RandomLayouts, SeedGenerator
from .Mask import CreateRegionalPNGMask, PngColorMasksToString, PngColorMasksToRGB, PngColorMasksToStringList, PngColorMasksToMaskList, PngRectanglesToMask, PngRectanglesToMaskList, CreateMaskWithCanvas, CreateWatermarkRemovalMask
from .Text import TextBox, TextWithBooleanSwitchAndCommonTextInput, TextCombinerSix, TextCombinerTwo
from .Logic import SingleBooleanTrigger, TwoBooleanTrigger, FourBooleanTrigger, SixBooleanTrigger, LogicNot, EvenOrOdd
def __init__(self):
    pass
    
# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "IntMultiplication"         : IntMultiplication,
    "FloatMultiplication"       : FloatMultiplication,
    "IntSubtraction"            : IntSubtraction,
    
    "NumeralToString"           : NumeralToString,
    "TwoFloats"                 : TwoFloats,
    "FourFloats"                : FourFloats,
    "SixFloats"                 : SixFloats,
    "EightFloats"               : EightFloats,
    "StepsAndCfg"               : StepsAndCfg,
    "StepsAndCfgAndWH"          : StepsAndCfgAndWH,
        
    "CanvasCreatorAdvanced"     : CanvasCreatorAdvanced,
    "CanvasCreatorSimple"       : CanvasCreatorSimple,
    "CanvasCreatorBasic"        : CanvasCreatorBasic,
    "RandomLayouts"             : RandomLayouts,
    "SeedGenerator"             : SeedGenerator,
    
    "CreateRegionalPNGMask"     : CreateRegionalPNGMask,
    "PngColorMasksToString"     : PngColorMasksToString,
    "PngColorMasksToRGB"        : PngColorMasksToRGB,
    "PngColorMasksToStringList" : PngColorMasksToStringList,
    "PngColorMasksToMaskList"   : PngColorMasksToMaskList,
    "PngRectanglesToMask"       : PngRectanglesToMask,
    "PngRectanglesToMaskList"   : PngRectanglesToMaskList,
    "CreateMaskWithCanvas"      : CreateMaskWithCanvas,
    "CreateWatermarkRemovalMask": CreateWatermarkRemovalMask,
    
    "SingleBooleanTrigger"      : SingleBooleanTrigger,
    "TwoBooleanTrigger"         : TwoBooleanTrigger,
    "FourBooleanTrigger"        : FourBooleanTrigger,
    "SixBooleanTrigger"         : SixBooleanTrigger,
    "LogicNot"                  : LogicNot,
    "EvenOrOdd"                 : EvenOrOdd,
    
    "TextBox"                                   : TextBox,
    "TextWithBooleanSwitchAndCommonTextInput"   : TextWithBooleanSwitchAndCommonTextInput,
    "TextCombinerSix"                           : TextCombinerSix,
    "TextCombinerTwo"                           : TextCombinerTwo,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "IntMultiplication"         : "Integer Multiplication",
    "FloatMultiplication"       : "Float Multiplication",
    "IntSubtraction"            : "Int Subtraction",
    
    "NumeralToString"           : "Convert Numeral to String",
    "TwoFloats"                 : "2 Floats",
    "FourFloats"                : "4 Floats",
    "SixFloats"                 : "6 Floats",
    "EightFloats"               : "8 Floats",
    "StepsAndCfg"               : "Steps & Cfg",
    "StepsAndCfgAndWH"          : "Steps & Cfg & WH",
    
    "CanvasCreatorAdvanced"     : "Create Canvas Advanced",
    "CanvasCreatorSimple"       : "Create Canvas",
    "CanvasCreatorBasic"        : "Create Canvas H/W only",
    "RandomLayouts"             : "Random Layouts",
    "SeedGenerator"             : "Seed Generator",
    
    "CreateRegionalPNGMask"     : "Create PNG Mask",
    "PngColorMasksToString"     : "PngColor Mask to HEX String",
    "PngColorMasksToRGB"        : "PngColor Mask to INT RGB",
    "PngColorMasksToStringList" : "PngColor Masks to List",
    "PngColorMasksToMaskList"   : "PngColor Masks to Masks",
    "PngRectanglesToMask"       : "PngRectangles to Mask",
    "PngRectanglesToMaskList"   : "PngRectangles to Masks",
    "CreateMaskWithCanvas"      : "Create Mask With Canvas",
    "CreateWatermarkRemovalMask": "Create Watermark Removal Mask",
    
    "SingleBooleanTrigger"      : "1 Bool",
    "TwoBooleanTrigger"         : "2 Bool",
    "FourBooleanTrigger"        : "4 Bool",
    "SixBooleanTrigger"         : "6 Bool",
    "LogicNot"                  : "Not",
    "EvenOrOdd"                 : "Even or Odd",
    
    "TextBox"                                   : "Text Box",
    "TextWithBooleanSwitchAndCommonTextInput"   : "Text Switcher",
    "TextCombinerSix"                           : "Text Combiner 6",
    "TextCombinerTwo"                           : "Text Combiner 2",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

