# Demo Image Declarations
image eb_bg 1:
    "bg1"
    xysize (1280,720)
    function WaveShader(amp=0.0, melt="vertical", melt_params=(20.0,12.0,0.25), repeat='repeat')
image eb_bg 2:
    'bg2'
    xysize (1280,720)
    function WaveShader(period=15, amp=5.0, speed=0.25, direction='x', double="x")
image grey = Solid("a0a0a0")
image comments_video = Movie(play='images/instructions_vid.webm', loop=False)
define test_text_wave = WaveShader(amp = 0, melt="both", melt_params=(20,5.0,0.1))
label start:
    scene grey with dissolve
    "Hiya, and welcome to the demo project for my wave shader module."
    "First a quick note on installation (since I always forget to note that in the demo)."
    show installation1 at top
    "To use this in your project. Simply take the wave_shader.rpy from this project's game folder and put it in your own."
    hide installation1
    show installation2 at top
    "If you would like to use the wave text effect, you should also copy the wavey_tag.rpy as well."
    hide installation2
    "Now on with the actual showcase."
    scene eb_bg 1 with dissolve
    "As you can see, it's quite good at capturing melty water like effects."
    show nito at center with dissolve:
        function WaveShader(period = 3, amp=50.0, repeat='mirrored', double="both")
    "And it can be applied to all displayables through the use of ATL."
    scene eb_bg 2 with dissolve
    "It's especially great at making trippy imagry. And can even be applied to text through a text tag."
    "{wave=ntest_text_wave}Though likely will be hard to read.{/wave}"
    "{wave}You probably can't even read this.{/wave}"
    "{wave=a20.0-s0.25-p20-db-mb}{size=50}{b}{color=ff0000}Especially text like this.{/wave}"
    scene bg3
    show bg3 as wave_overlay:
        alpha 0.5
        function WaveShader(amp = 0, melt="both", melt_params=(20,1.0,0.1))
    with dissolve
    "It can also be used in more subtle ways as well."
    "But it's hard for this demo to showcase all the effects possible. So I made a screen just so you can try messing with its parameters and get a feel for how it works."
    show comments_video with dissolve:
        xysize (1280,720)
        6
        ease 1.5 alpha 0
    "Documentation on what each of the parameters do can be found in the comments of wave_shader.rpy."
    hide comments_video with dissolve
    "Feel free to change the Nito.png image for something else if you want to mess with it for your own visuals!"
    "Some values in the demo are capped to keep values more moderate, but can be larger in practice."
    "Also, warning to those who maybe photosensitive, it's very easy to make a very strobing image with this. So try to keep the values low if you want to be careful."
    $ quick_menu = False
    scene grey
    call screen wave_tester with dissolve

    # This ends the game.

    return
