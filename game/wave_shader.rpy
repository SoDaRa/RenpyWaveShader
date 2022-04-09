"""
 Wave Shader Ren'Py Module
 2022 Daniel Westfall <SoDaRa2595@gmail.com>

 http://twitter.com/sodara9
 I'd appreciate being given credit if you do end up using it! :D Would really
 make my day to know I helped some people out!
 Really hope this can help the community create some cool visuals!
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

""" Notes on how to use """
#   This shader uses a time fed in from ATL instead of using u_time.
#   In my experience, u_time doesn't update at a steady enough framerate to be acceptable.
#   However, we can pump in the time from ATL at Renpy's framerate as a workaround. To do this,
#   I make use of the `function` statement in ATL to have a function get the animation_time from the call.
#   In this case, that function is actually a class that implements __call__ to mimic a regular function.
""" Important Part """
#   The function/class MUST RUN CONTINUOUSLY and thus I don't have it ever pass execution to
#   ATL statements after it. To work around this, I recommend using 'parallel'
#   to allow the function to keep running in one parallel block, then other ATL can be done in the other.

init -1 python:
    from renpy.uguu import GL_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT, GL_REPEAT
    renpy.register_shader("watt.wave", variables="""
        uniform float u_shader_time;
        uniform vec2 u_wave_period;
        uniform vec2 u_wave_amp;
        uniform vec2 u_wave_speed;
        uniform float u_direction;
        uniform vec2 u_damp;
        uniform float u_double;
        uniform vec3 u_double_params_x;
        uniform vec3 u_double_params_y;
        uniform float u_melt;
        uniform vec3 u_melt_params_x;
        uniform vec3 u_melt_params_y;

        uniform sampler2D tex0;
        uniform vec2 u_model_size;
        attribute vec2 a_tex_coord;
        varying vec2 v_coords;
    """, vertex_200 = """
        v_coords = a_tex_coord;
    """, fragment_300="""
        vec2 new_pos;
        vec2 wave_offset = vec2(0.0, 0.0);
        vec2 melt_offset = vec2(0.0, 0.0);
        vec2 double_offset = vec2(0.0, 0.0);
        vec2 double_pos = vec2(0.0, 0.0);
        vec2 damp = vec2(1.0, 1.0);
        vec4 new_color;
        vec4 double_color;

        if (u_damp.x >= 0.0 && u_damp.x != 1.0) {damp.x = pow(u_damp.x, v_coords.y * u_model_size.y);}
        else if (u_damp.x < 0.0) {damp.x = pow((-1.0 * u_damp.x), (1.0 - v_coords.y) * u_model_size.y);}
        if (u_damp.y >= 0.0 && u_damp.y != 1.0) {damp.y = pow(u_damp.y, v_coords.x * u_model_size.x);}
        else if (u_damp.y < 0.0) {damp.y = pow((-1.0 * u_damp.y), (1.0 - v_coords.x) * u_model_size.x);}

        if (u_direction < 2.0) {wave_offset.x = sin( u_wave_period.x * (v_coords.y + (u_shader_time * u_wave_speed.x))) * u_wave_amp.x * 0.01 * damp.x;}
        else {wave_offset.x = 0.0;}
        if (u_direction < 1.0 || u_direction >= 2.0) {wave_offset.y = sin( u_wave_period.y * (v_coords.x + (u_shader_time * u_wave_speed.y))) * u_wave_amp.y * 0.01 * damp.y;}
        else {wave_offset.y = 0.0;}

        if (u_melt >= 0.0){
            if (u_melt < 2.0) {melt_offset.x = sin( u_melt_params_x.x * (v_coords.x + (u_shader_time * u_melt_params_x.z))) * u_melt_params_x.y * 0.01 * damp.x;}
            else {melt_offset.x = 0.0;}
            if (u_melt < 1.0 || u_melt >= 2.0) {melt_offset.y = sin( u_melt_params_y.x * (v_coords.y + (u_shader_time * u_melt_params_y.z))) * u_melt_params_y.y * 0.01 * damp.y;}
            else {melt_offset.y = 0.0;}
        }
        new_pos.x = v_coords.x + wave_offset.x + melt_offset.x;
        new_pos.y = v_coords.y + wave_offset.y + melt_offset.y;

        new_color = texture2D(tex0,new_pos);

        if (u_double < 0.0) {gl_FragColor = new_color;}
        else{
            if (u_double < 2.0) {double_offset.x = sin( u_double_params_x.x * (v_coords.y + (u_shader_time * u_double_params_x.z))) * u_double_params_x.y * -0.01 * damp.x;}
            else {double_offset.x = 0.0;}
            if (u_double < 1.0 || u_double >= 2.0) {double_offset.y = sin( u_double_params_y.x * (v_coords.x + (u_shader_time * u_double_params_y.z))) * u_double_params_y.y * -0.01 * damp.y;}
            else {double_offset.y = 0.0;}
            double_pos.x = v_coords.x + double_offset.x + melt_offset.x;
            double_pos.y = v_coords.y + double_offset.y + melt_offset.y;
            double_color = texture2D(tex0,double_pos);
            gl_FragColor = mix(new_color, double_color, 0.5);
        }
    """)


    def advance_shader_time(trans, st, at):
        trans.u_shader_time = at
        return 0

    # Technically speaking, you can use the shader without using this class.
    # But this class handles a lot of passing in arguments that is required and would be tedious.
    # If you have another shader you would like to use, you may want to add a parameter to tell it
    # to just return after the __call__ function is run, setup the next shader, and
    # then just use 'function advance_shader_time` in the ATL to update time.
    class WaveShader(object):
        # All tuples (except for repeat) are sets of floats. The number specifies how many should be in the tuple.
        # STANDARD WAVE PARAMETERS
        # Note: For the following parameters, if a 2-tuple is supplied, the first element will affect the horizontal wave, the second will affect the vertical wave.
        #       If just a float, the value is used for both waves.
        # period:        (float/2-tuple) Affects the period of the sine wave. The higher this is, the more waves you tend to get.
        # amp:           (float/2-tuple) How far the waves move in either direction.
        # speed:         (float/2-tuple) How fast the sine wave moves with time.
        # direction:     (string) "vertical"/"y" causes only the vertical wave to be applied. "horizontal"/"x" causes only the horizontal wave to be applied.
        # damp:          (float/2-tuple) Dampens the wave as it proceeds. Should be kept between -1.0 and 1.0. Can help create the effect of perspective.
        #                                Such as the motion of water becoming less pronounced as it goes into the horizon.
        # ADDITIONAL EFFECT PARAMETERS
        # double:        (string) Renders a mirrored sine wave.
        #                         "both" will do it in both directions. "horizontal"/"x" will only do the horizontal wave, "vertical"/"y" only do the vertical wave
        # double_params: (3-tuple/6-tuple) Controls parameters for the mirrored waves. Usually can be omitted.
        #                                  By default, each wave will take the properties (period, amp, speed) of the standard wave parameters.
        #                                  When provided though, a 3-tuple will change both waves to what's provided.
        #                                  With a 6-tuple, the first 3 elements will affect the horizontal wave, and the last 3 will affect the vertical wave.
        #                                  (x_period, x_amp, x_speed, y_period, y_amp, y_speed)
        # melt:          (string) Causes the Vertical Oscillation effect in Earthbound, with some pixels being sampled multiple times. Leading to a squash and stretching of the image.
        #                         "both" will cause it to do melting in both directions. "horizontal" will only do melting horizontally, "vertical" doing the same but vertical
        #                         Note: If you would just like to use the melt effect, you can set amp = 0 and then use the melt_params to adjust the parameters.
        # melt_params:   (3-tuple/6-tuple) Similar to double_params, but affecting melt waves instead.
        # PROPERTY PARAMETER
        # repeat:        (string/2-string-tuple) Sets the gl_texture_wrap property. If a wave extends outside the texture, this will determine what it shows.
        #                                        "clamp" will made it so that the edge of the texture is just repeated for infinity
        #                                        "repeat" will repeat the texture off the edge. Imagine an infinite sequence of the same texture off the side of the texture.
        #                                        "mirror"/"mirrored" will have mirrored copies of the texture to infinity.
        #                                        A tuple, ie ("clamp", "repeat") will set the x behavior to clamping and y behavior to repeating. A single string will set it to the same value for both directions
        #                                        If omitted, the shader will inherit this property from the global state of OpenGL.
        def __init__(self, amp = 12.0, period = 20.0, speed = 1.0, direction = "both", damp = 1.0, double=None, double_params=None, melt=None, melt_params=None, repeat=None):
            # In Renpy's shaders, we don't have access to bools or ints. Only floats. So I use these in the shader to differentiate what waves should be included.
            options_dict = {"vertical": 2.0, "y": 2.0, "horizontal": 1.0, "x": 1.0, "both": 0.0, None: -1.0}
            property_dict = {'clamp': GL_CLAMP_TO_EDGE, 'mirrored': GL_MIRRORED_REPEAT, 'mirror': GL_MIRRORED_REPEAT, 'repeat': GL_REPEAT}
            # Helps make floats into 2-tuples or just gets a tuple if provided
            def float_or_tuple(param):
                if isinstance(param, (float, int)):
                    return (float(param), float(param))
                return param
            # Standard parameters
            self.period = float_or_tuple(period)
            self.amp = float_or_tuple(amp)
            self.speed = float_or_tuple(speed)
            if direction in options_dict:
                self.dir = options_dict[direction.lower()]
            else:
                self.dir = 0.0

            self.damp = float_or_tuple(damp)
            # Additional effect parameters
            if double is None:
                self.double = -1.0
                self.double_params_x = (0.0, 0.0, 0.0)
                self.double_params_y = (0.0, 0.0, 0.0)
            else:
                if double in options_dict:
                    self.double = options_dict[double.lower()]
                else:
                    self.double = 0.0
                if double_params is not None:
                    # Breaking up 3-tuples and 6-tuples
                    if len(double_params) == 6:
                        self.double_params_x = double_params[0:3]
                        self.double_params_y = double_params[3:]
                    else:
                        self.double_params_x = double_params
                        self.double_params_y = double_params
                else:
                    # Using the default period, amp and speed
                    self.double_params_x = (self.period[0], self.amp[0], self.speed[0])
                    self.double_params_y = (self.period[1], self.amp[1], self.speed[1])

            if melt is None:
                self.melt = -1.0
                self.melt_params_x = (0.0, 0.0, 0.0)
                self.melt_params_y = (0.0, 0.0, 0.0)
            else:
                if melt in options_dict:
                    self.melt = options_dict[melt.lower()]
                else:
                    self.melt = 0.0
                if melt_params is not None:
                    # Breaking up 3-tuples and 6-tuples
                    if len(melt_params) == 6:
                        self.melt_params_x = melt_params[0:3]
                        self.melt_params_y = melt_params[3:]
                    else:
                        self.melt_params_x = melt_params
                        self.melt_params_y = melt_params
                else:
                    # Using the default period, amp and speed
                    self.melt_params_x = (self.period[0], self.amp[0], self.speed[0])
                    self.melt_params_y = (self.period[1], self.amp[1], self.speed[1])
            # Property parameters
            self.repeat = None
            if isinstance(repeat, (unicode,str)):
                repeat = property_dict[repeat]
                self.repeat = (repeat, repeat)
            elif isinstance(repeat, tuple):
                self.repeat = (property_dict[repeat[0]], property_dict[repeat[1]])

            self.first_time = True

        # Note on potential additions:
        #   You can update the parameters over time if you'd like.
        #   Such as u_wave_amp could be increased or decreased over time with some modifications.
        def __call__(self, trans, st, at):
            if self.first_time or trans.shader != 'watt.wave':
                trans.shader = 'watt.wave'
                trans.mesh = True
                trans.u_shader_time = 0.0
                trans.u_wave_period = self.period
                trans.u_wave_amp = self.amp
                trans.u_wave_speed = self.speed
                trans.u_direction = self.dir
                trans.u_damp = self.damp
                trans.u_double = self.double
                trans.u_double_params_x = self.double_params_x
                trans.u_double_params_y = self.double_params_y
                trans.u_melt = self.melt
                trans.u_melt_params_x = self.melt_params_x
                trans.u_melt_params_y = self.melt_params_y
                if self.repeat != None:
                    trans.gl_texture_wrap = self.repeat
                self.first_time = False
            return advance_shader_time(trans, st, at)
