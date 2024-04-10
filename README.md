# ComfyUI_Mira
A custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI/) to improve all those custom nodes I feel not comfortable in my workflow.

------

## Installation
`Clone` the repository to custom_nodes in your `ComfyUI\custom_nodes` directory:
```
git clone https://github.com/mirabarukaso/ComfyUI_Mira.git
```

------

## Functions   
### Mask
#### Create Tilling PNG Mask 
Create a `Tilling` PNG image with Color Mask stack for regional conditioning mask.   
Ideas from [sd-webui-regional-prompter](https://github.com/hako-mikan/sd-webui-regional-prompter)

| Inputs | Description |
| --- | --- |
| `Width`  `Height` | Image size, could be difference with cavan size, but recommended to connect them together. |
| `Colum_first` | A boolean trigger, when enabled, will treat default cut as a horizontal cut. |
| `Rows`  `Colums` |  Define how many `Blocks` you want, all `Blocks` are the same weight. (Blocks = Rows x Colums) <br />  ***Low prority, only works when Layout is incorrect.*** |
| `Layout` | Customized `Blocks` with layouts input. e.g. `1,2,1,1;2,4,6`<br /> `0-9` `,` `;` Check Examples section for more detail. <br />***High prority, in case you don't need custom layout, simply put `#` here.*** |   

| Outputs | Description |
| --- | --- |
| `Image` | Visualisation Image of your Layout. |
| `PngColorMasks` | A List contains all your Blocks' color information.  <br />Connect to `Create PNG Mask ` `Color Mask to HEX String` `Color Mask to INT RGB` `Color Masks List` |
| `PngRectangles` | A List contains all PNG Blocks' rectangle informationm, last one is the whole Image's Width and Height. |
| `Debug` | Debug information as String. |

| Examples | Description |
| --- | --- |
| `0-9` | Block weights |
| `,` | A normal segmentation. Let's call it `N` cut|
| `;` | A high-priority segmentation perpendicular to the normal direction. Let's call it `G` cut|
| `1,2,1,1;2,4,6` <br /> `Colum_first ENABLED`| When combining `,` and `;`, the first and the following `;` elements are treated as the weight of `G` for current cavans. Node will first split the canvas with weight `1` and `;2` as `G` cuts. Then split the following parts with `2,1,1` and `4,6` as `N` cuts.  <br />***NOTE: The arithmetic logic here are different from WebUI, please use "Colum_first" if you need to change the direction, don't replace `,` and `;` directly.*** |
| `1,2,3,2,1` <br /> `Colum_first DISABLED`| A simple horizontal `N` cut with weights. |
| `1,2,3,2,1` <br /> `Colum_first ENABLED`| A simple vertical `N` cut with weights. |

| ***1,2,1,1;2,4,6 with Colum_first*** | ***1,2,3,2,1*** | ***1,2,3,2,1 with Colum_first*** |
| --- | --- | --- |
| <img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/example_mask2rgb.png" width=35% height=35%> | <img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/example_mask2rgb_12321_f.png" width=35% height=35%> | <img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/example_mask2rgb_12321_t.png" width=35% height=35%> |

------
#### Create Nested Rectangles PNG Mask 
Create a `Nested Rectangles` PNG image with Color Mask stack for regional conditioning mask.   
Ideas from [Watermark Removal](https://github.com/mirabarukaso/ComfyUI_Mira?tab=readme-ov-file#create-watermark-removal-mask)   

| Inputs | Description |
| --- | --- |
| `Width`  `Height` | Image size, could be difference with cavan size, but recommended to connect them together. |
| `X`, `Y` |  Center point (`X`,`Y`) of all Rectangles. |    
| `unlimit_top` | When `ENABLED`, all `masks` will create from the top of Image. |
| `unlimit_bottom` | When `ENABLED`, all `masks` will create till the bottom of Image. |
| `unlimit_left` | When `ENABLED`, all `masks` will create from the left of Image. |
| `unlimit_right` | When `ENABLED`, all `masks` will create till the right of Image. |        
| `Layout` | Customized `Blocks` with layouts input. e.g. `2,4,1` <br /> `0-9` `,` `;` Check Examples section for more detail. |
        
| Outputs | Description |
| --- | --- |
| `Image` | Visualisation Image of your Layout. |
| `PngColorMasks` | A List contains all your Blocks' color information.  <br />Connect to `Create PNG Mask ` `Color Mask to HEX String` `Color Mask to INT RGB` `Color Masks List` |
| `PngRectangles` | A List contains all PNG Blocks' rectangle informationm, last one is the whole Image's Width and Height. |
| `Debug` | Debug information as String. |


| Examples | Description |
| --- | --- |
| `0-9` | Block weights |
| `,` | A normal segmentation.  `;` will treat as same as `,` |
| `;` | Ignored in `,  ;` |

| ***2,4,1*** | ***2,4,1 unlimit bottom*** | ***2,4,1 unlimit bottom and right and blur 16*** |
| --- | --- | --- |
| <img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/example_createnestedpng.png" width=35% height=35%> | <img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/example_createnestedpng_ub.png" width=35% height=35%> | <img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/example_createnestedpng_ubr_b16.png" width=35% height=35%> |

------
#### PngColor Masks to Mask List
Convert ranged `PngColorMasks` to Masks with(or without) Blur. **Dunno if there is a proper way to solve the output problem.**   
Ideas from [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials)

| Inputs | Description |
| --- | --- |
| `Image` | Image from ` Mira/Mask/Create PNG Mask` |
| `PngColorMasks` | List from ` Mira/Mask/Create PNG Mask` |
| `Blur` | The intensity of blur around the edge of Mask, set to `0` for a solid edge. |
| `Start_At_Index` | The first block index number you want. |

| Outputs | Description |
| --- | --- |
| `mask_[0-9]` | The Mask for `Regional Conditioning` or ***Anything*** who need a Mask. |

| ***Solid*** | ***Blur 16.0*** |
| --- | --- |
| <img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/example_mask2mask_solid.png" width=35% height=35%> | <img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/example_mask2mask_blur.png" width=35% height=35%> |

------
#### PngColor Mask to HEX String
Convert specified `Index` of `PngColorMasks` to HEX value. e.g. `RGB(255,0,255)` to `#FF00FF`

| Inputs | Description |
| --- | --- |
| `PngColorMasks` | List from ` Mira/Mask/Create PNG Mask` |
| `Index` | The block index number. |

| Outputs | Description |
| --- | --- |
| `mask_color` | The color RGB in HEX for `Regional Conditioning By Color Mask (Inspire)` or etc. |

------
#### PngColor Mask to INT RGB
Convert specified `Index` `PngColorMasks` to RGB value for `🔧 Mask From Color` or etc. e.g. `RGB(255,0,255)` 

| Inputs | Description |
| --- | --- |
| `PngColorMasks` | List from ` Mira/Mask/Create PNG Mask` |
| `Index` | The block index number. |

| Outputs | Description |
| --- | --- |
| `R` | Red |
| `G` | Green |
| `B` | Blue |

------
#### PngColor Masks to List
Convert ranged `PngColorMasks` to HEX value. **Dunno if there is a proper way to solve the output problem.**

| Inputs | Description |
| --- | --- |
| `PngColorMasks` | List from ` Mira/Mask/Create PNG Mask` |
| `Start_At_Index` | The first block index number you want. |

| Outputs | Description |
| --- | --- |
| `mask_color_[0-9]` | The color RGB in HEX for `Regional Conditioning By Color Mask (Inspire)` or etc. |

------
#### PngRectangles to Mask (List)
Convert ranged `PngRectangles` to Mask with Mask `Intenisity` and `Blur` function.

| Inputs | Description |
| --- | --- |
| `PngRectangles` | List from ` Mira/Mask/Create PNG Mask` |
| `Intenisity` | `Intenisity` of Mask, set to `1.0` for solid Mask. |
| `Blur` | The intensity of blur around the edge of Mask, set to `0` for a solid edge. |
| `Start_At_Index` | The first block index number you want. |

| Outputs | Description |
| --- | --- |
| Normal |
| `mask` | Mask with specified `Intenisity` and `Blur`. |
| List |
| `mask_[0-9]` | Masks List with specified `Intenisity` and `Blur`. |

Example   
<img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/example_pngrect2masks.png" width=35% height=35%>   

------
#### Create Mask With Canvas   
Create a new `mask` on defined `cavans`.   
In case you need `merge` multiple `masks`, try search `MaskComposite` with `operation add`.   
    
| Inputs | Description |
| --- | --- |
| `C_Width` | Width of cavans. |
| `C_Height` | Height of cavans. |
| `X` | The left point of new mask on cavans. |
| `Y` | The top point of new mask on cavans. |
| `Width` | Mask width. |
| `Height` | Mask height. |
| `Intenisity` | `Intenisity` of Mask, set to `1.0` for solid Mask. |
| `Blur` | The intensity of blur around the edge of Mask, set to `0` for a solid edge. |
        
| Outputs | Description |
| --- | --- |
| `mask` | New mask with defined cavans |

Example   
<img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/example_createmaskwithcavans.png" width=35% height=35%>   

------
#### Create Watermark Removal Mask
Creates multiple `masks` at the corners of the image for subsequent watermark detection and removal.    
Ideas from [comfyui-lama-remover](https://github.com/Layer-norm/comfyui-lama-remover)


| Inputs | Description |
| --- | --- |
| `C_Width` | Width of cavans. |
| `C_Height` | Height of cavans. |
| `Mask_W` | Mask width, maxium value are half of cavans width. |
| `Mask_H` | Mask height, maxium value are half of cavans height. |
| `Top_L` | Create mask from top left. |
| `Top_R` | Create mask from top right. |
| `Bottom_L` | Create mask from bottom left. |
| `Bottom_R` | Create mask from bottom right. |  
| `EdgeToEdge` | Preserve the N pixels at the outermost edges of the image to prevent image noise. Set to 0 for borderless. |
| `Intenisity` | `Intenisity` of Mask, set to `1.0` for solid Mask. |
| `Blur` | The intensity of blur around the edge of Mask, set to `0` for a solid edge. |
        
| Outputs | Description |
| --- | --- |
| `Mask` | New mask with defined cavans |

| ***Before*** | ***After*** |
| --- | --- |
| <img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/example_watermark_removal_mask_before.png" width=35% height=35%> |  <img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/example_watermark_removal_mask_after.png" width=35% height=35%> |

------
### Util
#### Create Canvas
Create Canvas information `Width` and `Height` for Latent with Landscape switch. There's an advanced version also controls `Batch` and `HiResMultiplier`.

| Inputs | Description |
| --- | --- |
| Basic |
| `Width`  `Height` | Image size. |
| Normal |
| `Landscape` | Swap `Width` and `Height` by one click. |
| Advanced |
| `Batch`  | Batch size. |
| `HiResMultiplier`  | Automatically calculated (in steps of 8) for HiResFix. |
| `Debug` | Debug information as String. |

| Outputs | Description |
| --- | --- |
| Basic & Normal |
| `Width`  `Height` | Image size. Swaps automatically when `Landscape` is Enabled. |
| Advanced | 
| `Batch`  | Batch size. |
| `HiRes Width` `HiRes Height`  | Width and Height for HiResFix or etc. <br />***NOTE:The result is not the product of the original data, but the nearest multiple of 8.***|

------
#### Random Tilling Layouts
Random Tilling Mask `Layout` Generator for `Create Tilling PNG Mask -> Layout`   

**Highly recommend connect the output `layout` or `Create PNG Mask -> Debug` to `ShowText` node.**   
Refer to [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)   

**Known Issue** about `Seed Generator`   
Switching `randomize` to `fixed` now works immediately.   
But, switching `fixed` to `randomize`, it need 2 times `Queue Prompt` to take affect. (Because of the ComfyUI logic)   
      
Solution: Try `Global Seed (Inspire)` from [ComfyUI-Inspire-Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack)   

**Reminder**   
The `rnd_seed` have nothing to do with the actual random numbers, you can't get the same `layout` with the same `rnd_seed`, it is recommended to use `ShowText` and `Notes` to save your favourite `layout`.   

**Hint**   
Set rows or colums to `0` for only one direction cuts. Whichever is set to `0` will automatically cut according to the other non-zero setting. Just in case all fours are `0`, it will return `1,1`.   
    
| Inputs | Description |
| --- | --- |
| `min_rows` `max_rows` | Range of how many `N cuts` you may want, set both to 0 to disable it. |
| `min_colums` `max_colums` | Range of how many `G cuts` you may want, set both to 0 to disable it. |
| `max_weights_gcuts` | The maxium weight of `G cuts` range from 1 to `max_weights_gcuts` |
| `max_weights_ncuts` | The maxium weight of `N cuts` range from 1 to `max_weights_ncuts` | 
| `rnd_seed`| Connect to the `Seed Generator` node, then use `Global Seed (Inspire)` node to control it properly. |
    
| Outputs | Description |
| --- | --- |
| `Layout` | Layouts string, you need connect it to `Create PNG Mask -> layout` |

Example   
<img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/example_random_layouts.png" width=35% height=35%>   

------
#### Random Nested Mask Layouts
Random Nested Mask `Layout` Generator for `Create Nested PNG Mask -> Layout`  
    
**Known Issue** same as upper one.
    
| Inputs | Description |
| --- | --- |
| `min_nested`, `max_nested` | Range of nest you want. |
| `min_weights`, `max_weights` | The weight of every nest. |
| `rnd_seed` | Connect to the `Seed Generator` node, then use `Global Seed (Inspire)` node to control it properly. |
            
| Outputs | Description |
| --- | --- |
| `Layout` | Layouts string, you need connect it to `Create Nested PNG Mask -> layout` |
| `top`, `bottom`, `left`, `right` | Random Boolean for `Create Nested PNG Mask -> Layout` |

Example   
<img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/example_random_nested_layouts.png" width=35% height=35%>   

------
#### Seed Generator
Random `Seed` Generator for `Random Layouts`, same as normal random seed generator.   

------
### Text
#### Text Switcher
Selects `text1` or `text2` depending on the `use_text2` and automatically adds `common_text` for output.

| Inputs | Description |
| --- | --- |
| `use_text2` | When `ENABLED`, will switch `Output` to `text2 + separator + common_text`. |
| `common_text_at_front` | When `ENABLED`, the common text is placed in front of the text (1 or 2). |
| `text1` | Default output text. |
| `text2` | Alternative text when `use_text2` is `ENABLED`. |
| `common_text`  | Common text input for quality tags and etc, leave it blank if you don't need it.. |

| Outputs | Description |
| --- | --- |
| `text`  | A combined text output. |

Example   
<img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/example_text_switcher.png" width=35% height=35%>   

------
### Logic
#### Boolean
Few `Boolean` stacks.   

#### Logic NOT
Always return `not Boolean`
    
| Input | Output |
| --- | --- |
| `True` | `False` |
| `False` | `True` |

#### Even or Odd
Check if a `Integer` is odd or even.   

| Input | Output |
| --- | --- |
| `Even` | `False` |
| `Odd` | `True` |

------
### Numeral
#### Convert Numeral to String
Convert `Integer` or `Float` to String.   

#### Floats
And, few `Float` stacks.   

------
### Arithmetic (WIP as I need......)
Addition, Subtraction, Multiplication and Division.   

**Multiplier now renamed to Arithmetic.**

#### Multiplication
`Integer` and `Float` Multiplier with various output interfaces.   
There is also an `Integer to Float` Multiplier, connect to `Seed Generator` (x0.1) for `Even or Odd` and `Text Switcher`.

| Inputs | Description |
| --- | --- |
| `int_value` `float_value` | The number you want to multiply. |
| `multiply_value` | How many times? |

| Outputs | Description |
| --- | --- |
| `Integer`  | `Integer` result. ***When converting `Floating` to `Integer`, the fractional part are discarded.***|
| `Float`  | `Float` result. |
| `String`  | Convert result to `String`. |

------
#### Subtraction
`Integer` Subtraction with various output interfaces.   

**Mostly usage for `Create Mask With Cavans`, connect `Y` with `Result` then connect `height` with `subtracted_value`.**

| Inputs | Description |
| --- | --- |
| `int_value` | Subtracted number. |
| `subtracted_value` | Subtracted by how much? |

| Outputs | Description |
| --- | --- |
| `Integer`  | `Integer` result. |
| `String`  | Convert result to `String`. |
| `subtracted_value` | As is |

Example   
<img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/example_subtraction.png" width=35% height=35%>   

------
## Overview - Regional Conditioning Mask with HiRes Fix

<img src="https://github.com/mirabarukaso/ComfyUI_Mira/blob/main/examples/overview01.png" width=50% height=50%>

------

## Change Logs
#### 2024.04.06 Ver 0.4.0.0   
・Add Create Nested Rectangle PNG Mask   
・Add Random Nested Layouts   
・Add Integer to Float Multiplication   
・Bugfix   
・Func enchantment   

v0.3.9.0   
・Add Create Watermark Removal Mask    
・Modified Text Switcher   

#### 2024.03.31 Ver 0.3.8.0   
・Multiplier now renamed to Arithmetic.   
・Add Integer Subtraction    

#### 2024.03.16 Ver 0.3.7.0
・Add Random Layouts [#1](https://github.com/mirabarukaso/ComfyUI_Mira/issues/1)

#### 2024.03.14 Ver 0.3.6.0
・Add Create Mask With Canvas   

#### 2024.02.22 Ver 0.3.5.0
・Add Text Switcher   
・Add simple Logic functions   
・Bugfix   

v0.3.3.0   
・Bugs fix   
・Renamed few nodes   
・Add PngRectanglesToMask (List)   
・Add CanvasCreator Basic & Normal   

#### 2024.02.21 Ver 0.3.0.0
・Initial release   
