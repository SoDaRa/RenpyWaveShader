init python:
    # I made this solely to make it a bit easier to set the values in the wave shader. I don't expect this to be useful outside of this use case.
    class TesterWaveShader(WaveShader):
        def set_period_x(self, new):
            self.period = (new, self.period[1])
            self.first_time = True
        def set_period_y(self, new):
            self.period = (self.period[0], new)
            self.first_time = True
        def set_amp_x(self, new):
            self.amp = (new, self.amp[1])
            self.first_time = True
        def set_amp_y(self, new):
            self.amp = (self.amp[0], new)
            self.first_time = True
        def set_speed_x(self, new):
            self.speed = (new, self.speed[1])
            self.first_time = True
        def set_speed_y(self, new):
            self.speed = (self.speed[0], new)
            self.first_time = True
        def set_direction(self, new):
            options_dict = {"vertical": 2.0, "y": 2.0, "horizontal": 1.0, "x": 1.0, "both": 0.0}
            self.dir = options_dict[new]
            self.first_time = True
        def set_damp_x(self, new):
            self.damp = (new, self.damp[1])
            self.first_time = True
        def set_damp_y(self, new):
            self.damp = (self.damp[0], new)
            self.first_time = True

        def set_double(self, new):
            options_dict = {"vertical": 2.0, "y": 2.0, "horizontal": 1.0, "x": 1.0, "both": 0.0, None: -1.0}
            self.double = options_dict[new]
            self.first_time = True
        def set_double_params(self, period_x, amp_x, speed_x, period_y, amp_y, speed_y):
            self.double_params_x = (period_x, amp_x, speed_x)
            self.double_params_y = (period_y, amp_y, speed_y)
            self.first_time = True
        def set_double_period_x(self, new):
            self.double_params_x = (new, self.double_params_x[1], self.double_params_x[2])
            self.first_time = True
        def set_double_amp_x(self, new):
            self.double_params_x = (self.double_params_x[0], new, self.double_params_x[2])
            self.first_time = True
        def set_double_speed_x(self, new):
            self.double_params_x = (self.double_params_x[0], self.double_params_x[1], new)
            self.first_time = True
        def set_double_period_y(self, new):
            self.double_params_y = (new, self.double_params_y[1], self.double_params_y[2])
            self.first_time = True
        def set_double_amp_y(self, new):
            self.double_params_y = (self.double_params_y[0], new, self.double_params_y[2])
            self.first_time = True
        def set_double_speed_y(self, new):
            self.double_params_y = (self.double_params_y[0], self.double_params_y[1], new)
            self.first_time = True

        def set_melt(self, new):
            options_dict = {"vertical": 2.0, "y": 2.0, "horizontal": 1.0, "x": 1.0, "both": 0.0, None: -1.0}
            self.melt = options_dict[new]
            self.first_time = True
        def set_melt_params(self, period_x, amp_x, speed_x, period_y, amp_y, speed_y):
            self.melt_params_x = (period_x, amp_x, speed_x)
            self.melt_params_y = (period_y, amp_y, speed_y)
            self.first_time = True
        def set_melt_period_x(self, new):
            self.melt_params_x = (new, self.melt_params_x[1], self.melt_params_x[2])
            self.first_time = True
        def set_melt_amp_x(self, new):
            self.melt_params_x = (self.melt_params_x[0], new, self.melt_params_x[2])
            self.first_time = True
        def set_melt_speed_x(self, new):
            self.melt_params_x = (self.melt_params_x[0], self.melt_params_x[1], new)
            self.first_time = True
        def set_melt_period_y(self, new):
            self.melt_params_y = (new, self.melt_params_y[1], self.melt_params_y[2])
            self.first_time = True
        def set_melt_amp_y(self, new):
            self.melt_params_y = (self.melt_params_y[0], new, self.melt_params_y[2])
            self.first_time = True
        def set_melt_speed_y(self, new):
            self.melt_params_y = (self.melt_params_y[0], self.melt_params_y[1], new)
            self.first_time = True

        def set_repeat_x(self, new):
            property_dict = {'clamp': GL_CLAMP_TO_EDGE, 'mirrored': GL_MIRRORED_REPEAT, 'mirror': GL_MIRRORED_REPEAT, 'repeat': GL_REPEAT}
            if self.repeat is None:
                self.repeat = (GL_CLAMP_TO_EDGE, GL_CLAMP_TO_EDGE)
            self.repeat = (property_dict[new], self.repeat[1])
            self.first_time = True
        def set_repeat_y(self, new):
            property_dict = {'clamp': GL_CLAMP_TO_EDGE, 'mirrored': GL_MIRRORED_REPEAT, 'mirror': GL_MIRRORED_REPEAT, 'repeat': GL_REPEAT}
            if self.repeat is None:
                self.repeat = (GL_CLAMP_TO_EDGE, GL_CLAMP_TO_EDGE)
            self.repeat = (self.repeat[0], property_dict[new])
            self.first_time = True
style tester_frame:
    xalign 0.5 xmaximum 400
screen wave_tester():
    default my_wave_shader = TesterWaveShader()
    default amp_x = 12.0
    default amp_y = 12.0
    default period_x = 20.0
    default period_y = 20.0
    default speed_x = 1.0
    default speed_y = 1.0
    default direction = "Both"
    default damp_x = 2.0
    default damp_y = 2.0
    default double = None
    default double_amp_x = 12.0
    default double_period_x = 20.0
    default double_speed_x = 1.0
    default double_amp_y = 12.0
    default double_period_y = 20.0
    default double_speed_y = 1.0
    default melt = None
    default melt_amp_x = 12.0
    default melt_period_x = 20.0
    default melt_speed_x = 1.0
    default melt_amp_y = 12.0
    default melt_period_y = 20.0
    default melt_speed_y = 1.0
    default repeat_x = "Clamp"
    default repeat_y = "Clamp"
    add 'nito' at right, WaveShaderApplyer(my_wave_shader)
    ## TODO ADD RESET BUTTON!!!!
    frame:
        xysize (450, 720)
        viewport:
            xalign 0.5
            draggable True
            mousewheel True
            pagekeys True
            xysize (425, 720)
            scrollbars "vertical"
            vbox:
                xalign 0.5
                frame:
                    style 'tester_frame'
                    hbox:
                        textbutton "Reset" action [SetScreenVariable('direction', "Both"), SetScreenVariable('repeat_x', "Clamp"), SetScreenVariable('repeat_y', "Clamp"), SetScreenVariable('amp_x', 12.0), SetScreenVariable('amp_y', 12.0), SetScreenVariable('period_x', 20.0), SetScreenVariable('period_y', 20.0), SetScreenVariable('speed_x', 1.0), SetScreenVariable('speed_y', 1.0),
                        SetScreenVariable('damp_x', 2.0), SetScreenVariable('damp_y', 2.0),
                        SetScreenVariable('double', None), SetScreenVariable('double_amp_x', 12.0), SetScreenVariable('double_amp_y', 12.0), SetScreenVariable('double_period_x', 20.0), SetScreenVariable('double_period_y', 20.0), SetScreenVariable('double_speed_x', 1.0), SetScreenVariable('double_speed_y', 1.0),
                        SetScreenVariable('melt', None), SetScreenVariable('melt_amp_x', 12.0), SetScreenVariable('melt_amp_y', 12.0), SetScreenVariable('melt_period_x', 20.0), SetScreenVariable('melt_period_y', 20.0), SetScreenVariable('melt_speed_x', 1.0), SetScreenVariable('melt_speed_y', 1.0), SetScreenVariable('my_wave_shader', TesterWaveShader(repeat="clamp"))] selected False
                        null width 80
                        textbutton "End Demo" action Return()
                frame:
                    style 'tester_frame'
                    vbox:
                        text "Direction" xalign 0.5
                        hbox:
                            textbutton "Both" action [SetScreenVariable('direction', "Both"), Function(my_wave_shader.set_direction, "both"), Function(renpy.restart_interaction)]
                            textbutton "Vertical" action [SetScreenVariable('direction', "Vertical"), Function(my_wave_shader.set_direction, "vertical"), Function(renpy.restart_interaction)]
                            textbutton "Horizontal" action [SetScreenVariable('direction', "Horizontal"), Function(my_wave_shader.set_direction, "horizontal"), Function(renpy.restart_interaction)]
                frame:
                    style 'tester_frame'
                    vbox:
                        text "Repeat X" xalign 0.5
                        hbox:
                            textbutton "Clamp" action [SetScreenVariable('repeat_x', "Clamp"), Function(my_wave_shader.set_repeat_x, "clamp"), Function(renpy.restart_interaction)]
                            textbutton "Repeat" action [SetScreenVariable('repeat_x', "Repeat"), Function(my_wave_shader.set_repeat_x, "repeat"), Function(renpy.restart_interaction)]
                            textbutton "Mirror" action [SetScreenVariable('repeat_x', "Mirror"), Function(my_wave_shader.set_repeat_x, "mirror"), Function(renpy.restart_interaction)]
                frame:
                    style 'tester_frame'
                    vbox:
                        text "Repeat Y" xalign 0.5
                        hbox:
                            textbutton "Clamp" action [SetScreenVariable('repeat_y', "Clamp"), Function(my_wave_shader.set_repeat_y, "clamp"), Function(renpy.restart_interaction)]
                            textbutton "Repeat" action [SetScreenVariable('repeat_y', "Repeat"), Function(my_wave_shader.set_repeat_y, "repeat"), Function(renpy.restart_interaction)]
                            textbutton "Mirror" action [SetScreenVariable('repeat_y', "Mirror"), Function(my_wave_shader.set_repeat_y, "mirror"), Function(renpy.restart_interaction)]
                if direction in ('Both', 'Horizontal'):
                    frame:
                        style 'tester_frame'
                        vbox:
                            text "Amp X" xalign 0.5
                            text "{:.3f}".format(amp_x) xalign 0.5
                            bar value ScreenVariableValue('amp_x', 200.0, step=1) released [Function(my_wave_shader.set_amp_x, amp_x), Function(renpy.restart_interaction)]
                    frame:
                        style 'tester_frame'
                        vbox:
                            text "Period X" xalign 0.5
                            text "{:.3f}".format(period_x) xalign 0.5
                            bar value ScreenVariableValue('period_x', 20.0, step=0.1) released [Function(my_wave_shader.set_period_x, period_x), Function(renpy.restart_interaction)]
                    frame:
                        style 'tester_frame'
                        vbox:
                            text "Speed X" xalign 0.5
                            text "{:.3f}".format(speed_x) xalign 0.5
                            bar value ScreenVariableValue('speed_x', 10.0, step=0.1) released [Function(my_wave_shader.set_speed_x, speed_x), Function(renpy.restart_interaction)]
                if direction in ('Both', 'Vertical'):
                    frame:
                        style 'tester_frame'
                        vbox:
                            text "Amp Y" xalign 0.5
                            text "{:.3f}".format(amp_y) xalign 0.5
                            bar value ScreenVariableValue('amp_y', 200.0, step=1) released [Function(my_wave_shader.set_amp_y, amp_y), Function(renpy.restart_interaction)]
                    frame:
                        style 'tester_frame'
                        vbox:
                            text "Period Y" xalign 0.5
                            text "{:.3f}".format(period_y) xalign 0.5
                            bar value ScreenVariableValue('period_y', 20.0, step=0.1) released [Function(my_wave_shader.set_period_y, period_y), Function(renpy.restart_interaction)]
                    frame:
                        style 'tester_frame'
                        vbox:
                            text "Speed Y" xalign 0.5
                            text "{:.3f}".format(speed_y) xalign 0.5
                            bar value ScreenVariableValue('speed_y', 10.0, step=0.1) released [Function(my_wave_shader.set_speed_y, speed_y), Function(renpy.restart_interaction)]
                frame:
                    style 'tester_frame'
                    vbox:
                        text "Damp X" xalign 0.5
                        text "{:.3f}".format(damp_x-1.0) xalign 0.5
                        side 'tl tr bl br t b':
                            xalign 0.5
                            textbutton '-0.01' action [SetScreenVariable('damp_x', damp_x - 0.01), Function(my_wave_shader.set_damp_x, damp_x-1.01), Function(renpy.restart_interaction)]
                            textbutton '+0.01' action [SetScreenVariable('damp_x', damp_x + 0.01), Function(my_wave_shader.set_damp_x, damp_x-.99), Function(renpy.restart_interaction)]
                            textbutton '-0.001' action [SetScreenVariable('damp_x', damp_x - 0.001), Function(my_wave_shader.set_damp_x, damp_x-1.001), Function(renpy.restart_interaction)]
                            textbutton '+0.001' action [SetScreenVariable('damp_x', damp_x + 0.001), Function(my_wave_shader.set_damp_x, damp_x-.999), Function(renpy.restart_interaction)]
                            null width 80
                            null width 80
                        bar value ScreenVariableValue('damp_x', 2.0, step=0.1) released [Function(my_wave_shader.set_damp_x, damp_x-1.0), Function(renpy.restart_interaction)]


                frame:
                    style 'tester_frame'
                    vbox:
                        text "Damp Y" xalign 0.5
                        text "{:.3f}".format(damp_y-1.0) xalign 0.5
                        side 'tl tr bl br t b':
                            xalign 0.5
                            textbutton '-0.01' action [SetScreenVariable('damp_y', damp_y - 0.01), Function(my_wave_shader.set_damp_y, damp_y-1.01), Function(renpy.restart_interaction)]
                            textbutton '+0.01' action [SetScreenVariable('damp_y', damp_y + 0.01), Function(my_wave_shader.set_damp_y, damp_y-.99), Function(renpy.restart_interaction)]
                            textbutton '-0.001' action [SetScreenVariable('damp_y', damp_y - 0.001), Function(my_wave_shader.set_damp_y, damp_y-1.001), Function(renpy.restart_interaction)]
                            textbutton '+0.001' action [SetScreenVariable('damp_y', damp_y + 0.001), Function(my_wave_shader.set_damp_y, damp_y-.999), Function(renpy.restart_interaction)]
                            null width 80
                            null width 80
                        bar value ScreenVariableValue('damp_y', 2.0, step=0.1) released [Function(my_wave_shader.set_damp_y, damp_y-1.0), Function(renpy.restart_interaction)]
                frame:
                    style 'tester_frame'
                    vbox:
                        text "Double" xalign 0.5
                        hbox:
                            textbutton "None" action [SetScreenVariable('double', None), Function(my_wave_shader.set_double, None), Function(renpy.restart_interaction)]
                            textbutton "Both" action [SetScreenVariable('double', "Both"), Function(my_wave_shader.set_double, "both"), Function(my_wave_shader.set_double_params, double_period_x, double_amp_x, double_speed_x, double_period_y, double_amp_y, double_speed_y), Function(renpy.restart_interaction)]
                            textbutton "Vertical" action [SetScreenVariable('double', "Vertical"), Function(my_wave_shader.set_double, "vertical"), Function(my_wave_shader.set_double_params, double_period_x, double_amp_x, double_speed_x, double_period_y, double_amp_y, double_speed_y), Function(renpy.restart_interaction)]
                            textbutton "Horizontal" action [SetScreenVariable('double', "Horizontal"), Function(my_wave_shader.set_double, "horizontal"), Function(my_wave_shader.set_double_params, double_period_x, double_amp_x, double_speed_x, double_period_y, double_amp_y, double_speed_y), Function(renpy.restart_interaction)]
                if double != None:
                    if double in ('Both', 'Horizontal'):
                        frame:
                            style 'tester_frame'
                            vbox:
                                text "Double Amp X" xalign 0.5
                                text "{:.3f}".format(double_amp_x) xalign 0.5
                                textbutton "Set to Amp X" action [SetScreenVariable('double_amp_x', amp_x), Function(my_wave_shader.set_double_amp_x, amp_x), Function(renpy.restart_interaction)] xalign 0.5
                                bar value ScreenVariableValue('double_amp_x', 200.0, step=1) released [Function(my_wave_shader.set_double_amp_x, double_amp_x), Function(renpy.restart_interaction)]
                        frame:
                            style 'tester_frame'
                            vbox:
                                text "Double Period X" xalign 0.5
                                text "{:.3f}".format(double_period_x) xalign 0.5
                                textbutton "Set to Period X" action [SetScreenVariable('double_period_x', period_x), Function(my_wave_shader.set_double_period_x, period_x), Function(renpy.restart_interaction)] xalign 0.5
                                bar value ScreenVariableValue('double_period_x', 20.0, step=0.1) released [Function(my_wave_shader.set_double_period_x, double_period_x), Function(renpy.restart_interaction)]
                        frame:
                            style 'tester_frame'
                            vbox:
                                text "Double Speed X" xalign 0.5
                                text "{:.3f}".format(double_speed_x) xalign 0.5
                                textbutton "Set to Speed X" action [SetScreenVariable('double_speed_x', speed_x), Function(my_wave_shader.set_double_speed_x, speed_x), Function(renpy.restart_interaction)] xalign 0.5
                                bar value ScreenVariableValue('double_speed_x', 10.0, step=0.1) released [Function(my_wave_shader.set_double_speed_x, double_speed_x), Function(renpy.restart_interaction)]
                    if double in ('Both', 'Vertical'):
                        frame:
                            style 'tester_frame'
                            vbox:
                                text "Double Amp Y" xalign 0.5
                                text "{:.3f}".format(double_amp_y) xalign 0.5
                                textbutton "Set to Amp Y" action [SetScreenVariable('double_amp_y', amp_y), Function(my_wave_shader.set_double_amp_y, amp_y), Function(renpy.restart_interaction)] xalign 0.5
                                bar value ScreenVariableValue('double_amp_y', 200.0, step=1) released [Function(my_wave_shader.set_double_amp_y, double_amp_y), Function(renpy.restart_interaction)]

                        frame:
                            style 'tester_frame'
                            vbox:
                                text "Double Period Y" xalign 0.5
                                text "{:.3f}".format(double_period_y) xalign 0.5
                                textbutton "Set to Period Y" action [SetScreenVariable('double_period_y', period_y), Function(my_wave_shader.set_double_period_y, period_y), Function(renpy.restart_interaction)] xalign 0.5
                                bar value ScreenVariableValue('double_period_y', 20.0, step=0.1) released [Function(my_wave_shader.set_double_period_y, double_period_y), Function(renpy.restart_interaction)]

                        frame:
                            style 'tester_frame'
                            vbox:
                                text "Double Speed Y" xalign 0.5
                                text "{:.3f}".format(double_speed_y) xalign 0.5
                                textbutton "Set to Speed Y" action [SetScreenVariable('double_speed_y', speed_y), Function(my_wave_shader.set_double_speed_y, speed_y), Function(renpy.restart_interaction)] xalign 0.5
                                bar value ScreenVariableValue('double_speed_y', 10.0, step=0.1) released [Function(my_wave_shader.set_double_speed_y, double_speed_y), Function(renpy.restart_interaction)]
                frame:
                    style 'tester_frame'
                    vbox:
                        text "Melt" xalign 0.5
                        hbox:
                            textbutton "None" action [SetScreenVariable('melt', None), Function(my_wave_shader.set_melt, None), Function(renpy.restart_interaction)]
                            textbutton "Both" action [SetScreenVariable('melt', "Both"), Function(my_wave_shader.set_melt, "both"), Function(my_wave_shader.set_melt_params, melt_period_x, melt_amp_x, melt_speed_x, melt_period_y, melt_amp_y, melt_speed_y), Function(renpy.restart_interaction)]
                            textbutton "Vertical" action [SetScreenVariable('melt', "Vertical"), Function(my_wave_shader.set_melt, "vertical"), Function(my_wave_shader.set_melt_params, melt_period_x, melt_amp_x, melt_speed_x, melt_period_y, melt_amp_y, melt_speed_y), Function(renpy.restart_interaction)]
                            textbutton "Horizontal" action [SetScreenVariable('melt', "Horizontal"), Function(my_wave_shader.set_melt, "horizontal"), Function(my_wave_shader.set_melt_params, melt_period_x, melt_amp_x, melt_speed_x, melt_period_y, melt_amp_y, melt_speed_y), Function(renpy.restart_interaction)]
                if melt != None:
                    if melt in ('Both', 'Horizontal'):
                        frame:
                            style 'tester_frame'
                            vbox:
                                text "Melt Amp X" xalign 0.5
                                text "{:.3f}".format(melt_amp_x) xalign 0.5
                                textbutton "Set to Amp X" action [SetScreenVariable('melt_amp_x', amp_x), Function(my_wave_shader.set_melt_amp_x, amp_x), Function(renpy.restart_interaction)] xalign 0.5
                                bar value ScreenVariableValue('melt_amp_x', 200.0, step=1) released [Function(my_wave_shader.set_melt_amp_x, melt_amp_x), Function(renpy.restart_interaction)]
                        frame:
                            style 'tester_frame'
                            vbox:
                                text "Melt Period X" xalign 0.5
                                text "{:.3f}".format(melt_period_x) xalign 0.5
                                textbutton "Set to Period X" action [SetScreenVariable('melt_period_x', period_x), Function(my_wave_shader.set_melt_period_x, period_x), Function(renpy.restart_interaction)] xalign 0.5
                                bar value ScreenVariableValue('melt_period_x', 20.0, step=0.1) released [Function(my_wave_shader.set_melt_period_x, melt_period_x), Function(renpy.restart_interaction)]
                        frame:
                            style 'tester_frame'
                            vbox:
                                text "Melt Speed X" xalign 0.5
                                text "{:.3f}".format(melt_speed_x) xalign 0.5
                                textbutton "Set to Speed X" action [SetScreenVariable('melt_speed_x', speed_x), Function(my_wave_shader.set_melt_speed_x, speed_x), Function(renpy.restart_interaction)] xalign 0.5
                                bar value ScreenVariableValue('melt_speed_x', 10.0, step=0.1) released [Function(my_wave_shader.set_melt_speed_x, melt_speed_x), Function(renpy.restart_interaction)]
                    if melt in ('Both', 'Vertical'):
                        frame:
                            style 'tester_frame'
                            vbox:
                                text "Melt Amp Y" xalign 0.5
                                text "{:.3f}".format(melt_amp_y) xalign 0.5
                                textbutton "Set to Amp Y" action [SetScreenVariable('melt_amp_y', amp_y), Function(my_wave_shader.set_melt_amp_y, amp_y), Function(renpy.restart_interaction)] xalign 0.5
                                bar value ScreenVariableValue('melt_amp_y', 200.0, step=1) released [Function(my_wave_shader.set_melt_amp_y, melt_amp_y), Function(renpy.restart_interaction)]

                        frame:
                            style 'tester_frame'
                            vbox:
                                text "Melt Period Y" xalign 0.5
                                text "{:.3f}".format(melt_period_y) xalign 0.5
                                textbutton "Set to Period Y" action [SetScreenVariable('melt_period_y', period_y), Function(my_wave_shader.set_melt_period_y, period_y), Function(renpy.restart_interaction)] xalign 0.5
                                bar value ScreenVariableValue('melt_period_y', 20.0, step=0.1) released [Function(my_wave_shader.set_melt_period_y, melt_period_y), Function(renpy.restart_interaction)]
                        frame:
                            style 'tester_frame'
                            vbox:
                                text "Melt Speed Y" xalign 0.5
                                text "{:.3f}".format(melt_speed_y) xalign 0.5
                                textbutton "Set to Speed Y" action [SetScreenVariable('melt_speed_y', speed_y), Function(my_wave_shader.set_melt_speed_y, speed_y), Function(renpy.restart_interaction)] xalign 0.5
                                bar value ScreenVariableValue('melt_speed_y', 10.0, step=0.1) released [Function(my_wave_shader.set_melt_speed_y, melt_speed_y), Function(renpy.restart_interaction)]
