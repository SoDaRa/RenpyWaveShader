"""
 Wave Shader Text Tag Ren'Py Module
 2022 Daniel Westfall <SoDaRa2595@gmail.com>

 http://twitter.com/sodara9
 I'd appreciate being given credit if you do end up using it! :D Would really
 make my day to know I helped some people out!
 Really hope this can help the community create some really neat ways to spice
 up their dialogue!
 http://opensource.org/licenses/mit-license.php
 Github: https://github.com/SoDaRa/RenpyWaveShader
 itch.io: https://wattson.itch.io/renpy-wave-shader
 Forum Post: https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=64378
"""
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
init python:
    # Applies wavy effects to text.
    # Accepts arguments for period, amp, speed, direction, double and melt
    # The following must be paired with a float parameter
    # 'a' for amp
    # 'p' for period
    # 's' for speed
    # The following determine if horizontal, vertical or both waves are used.
    # If followed by a 'b', both are used. Followed by 'y', only vertical is used
    # If followed by 'x', only horizontal is used
    # And if double or melt are provided, they enable those effects.
    # 'w' to decide wave direction
    # 'd' for double render
    # 'm' for melt render
    # Separate arguments with a '-'.
    # Example: "{wave=a10-p0.9-s2.5-wb-dx}" - amplitude 10.0, period 0.9, speed 2.5, both waves, double horizontally
    #
    # Notes:
    # - Because this doesn't cover all arguments for WaveShader, you can optionally
    #   use 'n' and follow it with the name of a WaveShader variable defined separately
    #   Example "{wave=nmy_wave_shader}" with 'my_wave_shader' being the variable it'll attempt to find.
    #   If done, 'n' should be the only parameter.
    # - The tag will automatically make the text slow.
    #   If you need it to be instantly shown (such as on a screen), add a {cps=0} within the tag.
    def wavy_tag(tag, argument, contents):
        new_list = [ ]
        amp, period, speed, dir, double, melt = 12, 20, 1, 'both', None, None
        tag_shader = WaveShader()
        if len(argument) > 0 and argument[0] == 'n':
            shader_name = argument[1:]
            copy_shader = globals()[shader_name]
            if isinstance(copy_shader, WaveShader):
                tag_shader = copy_shader
        elif len(argument) > 0:
            argument = argument.split('-')
            dir_dict = {'b':'both', 'x':'x', 'y':'y'}
            for arg in argument:
                if 'a' in arg:
                    amp = float(arg[1:])
                if 'p' in arg:
                    period = float(arg[1:])
                if 's' in arg:
                    speed = float(arg[1:])
                if 'w' in arg:
                    dir = dir_dict[arg[1]]
                if 'd' in arg:
                    double = dir_dict[arg[1]]
                if 'm' in arg:
                    melt = dir_dict[arg[1]]
            tag_shader = WaveShader(amp=amp, period=period, speed=speed, direction=dir, double=double, melt=melt)
        my_style = DispTextStyle() # Defined in kinetic_text_tags.rpy. Used for style information preservation.
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                text = Text(my_style.apply_style(text), slow = True)
                char_disp = At(text, globals()['WaveShaderApplyer'](tag_shader))
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    config.custom_text_tags["wave"] = wavy_tag

transform WaveShaderApplyer(func):
    function func
