.. title: Tweaking the Firestorm Viewer
.. slug: tweaking-firestorm-viewer
.. date: 2016-08-19 12:40:00 UTC+02:00
.. category: virtual-worlds/second-life
.. tags: second-life, firestorm
.. link: 
.. type: text
.. previewimage: FSLogo4x3.png
.. description:

.. default-role:: code
.. role:: html(raw)
    :format: html


.. figure:: FSLogoTrans.png
    :align: right

Just a few days ago, a new version **4.7.9** of the **Firestorm viewer** has been released. Since it brings a few of really neat features, like **avatar rendering complexity** controls, it still doesn't fix some of the older issues. So, let me summarize the issues I will try to tweak...

.. TEASER_END


.. class:: li-smallskip

    - The **UI fonts** are too tiny and hard to read (especially when you are using ultra HD monitor like I do). There is `Scale UI` slider, but sadly it still doesn't work well and produces odd glitches. The option `Font Size Adjustment` really makes fonts larger, but then the length of titles doesn't fit in the toolboxes that are not scale-able.

    - You still can't set the font size and family for the **script editor** and the default size is really hard to read.

    - There is no shortcut for **uploading mesh** and it is hidden too deep in the menu for a feature that creators need on daily basis.

    - The default option for uploading mesh LOD levels is the `generated` option, which is really useless. It would be great if Firestorm remembered the last used option for uploading mesh, so we wouldn't need to select what needed each time again and again.



Make UI fonts larger
====================

I went to Firestorm Preferences (Ctrl+P), Font options and added `1.0pt` to `Font Size Adjustment`, also I changed `Font Scheme` to `Open sans` that I find better readable than the default DejaVu font family.

.. figure:: pref_font.png
    :align: center


Now, we have all fonts larger and truly better readable, but when using the **Build Tools** floater we can notice the titles don't fit the floater width and it makes usage really annoying :(

To fix this glitch, we need to modify some XML files in the Firestorm install folder. Particularly the skin-related files...

.. class:: li-medskip

    - `Firestorm-Releasex64\skins\default\xui\en\floater_tools.xml`

    - `Firestorm-Releasex64\skins\default\xui\en\panel_tools_texture.xml`


These files specify how the Build Tools floater looks like, and you can find the width is fixed to `295px`, so I replaced all the values with width `330`. I also made few another minor tweaks to make the items looks better aligned.

Here, you can download my modified files and replace them in your Firestorm installation...


- `floater_tools.xml <floater_tools.xml>`_

- `panel_tools_texture.xml <panel_tools_texture.xml>`_


.. figure:: build_tools.png
    :align: center



Font size for the script editor
===============================

Since the font size for script editor can't be adjusted directly in Firestorm, we need to modify the file `Firestorm-Releasex64/fonts/fonts.xml`, which specifies all the used fonts. For script editor fonts, we need to locate the font named `Monospace`, then we can set both size and font family. Of course, after making any changes we need to restart the Firestorm to apply the changes.

.. code:: XML

    <font name="Monospace"
        comment="Name of monospace font">
        <file>SourceCodePro-Regular.ttf</file>
    </font>

    <font_size name="Monospace"
        comment="Size for monospaced font (points, or 1/72 of an inch)"
        size="9.0"
    />


Custom shortcut and menu for uploading mesh
===========================================

When you need to upload mesh objects very often, it gets very frustrating to search the mesh uploader in the menu each time. So, a custom shortcut and/or a custom menu would be really helpful here. To add a new menu with custom shortcut for mesh uploading, we need to locate the file...

- `Firestorm-Releasex64\skins\default\xui\en\menu_viewer.xml`

Then, add the following XML tags to specify the custom Upload menu. I chose `Ctrl+Alt+M` as the shortcut for uploading mesh and also added items to upload other kinds of content. And here, you can see how neat and handy our new custom menu looks :)


.. figure:: menu_upload.png
    :align: center


.. code:: XML

    <menu create_jump_keys="true" label="Upload" layout="topleft" name="Upload" tear_off="true" visible="true">
        <menu_item_call label="Mesh Model..." layout="topleft" name="Upload Model" shortcut="control|alt|M">
            <menu_item_call.on_click function="File.UploadModel" parameter=""/>
            <menu_item_call.on_enable function="File.EnableUploadModel"/>
            <menu_item_call.on_visible function="File.VisibleUploadModel"/>
        </menu_item_call>
        <menu_item_call label="Animation ([COST])..." layout="topleft" name="Upload Animation">
            <menu_item_call.on_click function="File.UploadAnim" parameter=""/>
            <menu_item_call.on_enable function="File.EnableUpload"/>
            <menu_item_call.on_visible function="Upload.CalculateCosts" parameter="Upload Animation"/>
        </menu_item_call>
        <menu_item_call label="Image ([COST])..." layout="topleft" name="Upload Image" shortcut="control|U">
            <menu_item_call.on_click function="File.UploadImage" parameter=""/>
            <menu_item_call.on_enable function="File.EnableUpload"/>
            <menu_item_call.on_visible function="Upload.CalculateCosts" parameter="Upload Image"/>
        </menu_item_call>
        <menu_item_call label="Sound ([COST])..." layout="topleft" name="Upload Sound">
            <menu_item_call.on_click function="File.UploadSound" parameter=""/>
            <menu_item_call.on_enable function="File.EnableUpload"/>
            <menu_item_call.on_visible function="Upload.CalculateCosts" parameter="Upload Sound"/>
        </menu_item_call>
        <menu_item_call label="Bulk ([COST] per file)..." layout="topleft" name="Bulk Upload">
            <menu_item_call.on_click function="File.UploadBulk" parameter=""/>
            <menu_item_call.on_visible function="Upload.CalculateCosts" parameter="Bulk Upload"/>
        </menu_item_call>
    </menu>


|


