.. title: Install Nikola on Windows 10
.. slug: install-nikola-on-windows-10
.. date: 2016-06-30 19:25:00 UTC+02:00
.. category: web-design
.. tags: nikola
.. link: 
.. description:
.. type: text

.. .............................................................................
.. default-role:: code
.. role:: html(raw)
    :format: html
.. .............................................................................


Because of the fact that **Nikola** site generator is written in **Python** scripting language, it should run on any major operating system. The installation process might vary depending on the system though. Here, I'm going to share how I've managed to install Nikola on Windows 10.

.. TEASER_END


.. class:: instruction-list li-bigskip

    - :html:`❶` Nikola is powered by `Python <https://www.python.org/>`_, so first you need to make sure Python is installed on your computer.



    - :html:`❷` To install Nikola, you will need a command-line console. Even though the default Windows console (cmd) should be perfectly suitable, I recommend to get `ConEmu <https://conemu.github.io/>`_, because it's configurable, feature-rich and looks much better.



    - :html:`❸` The best way to install Nikola is to use `pip` in a `virtualenv`. So, open console in admin mode at desired path and install `virtualenv`.

    .. code:: console 

        $ py -m pip install virtualenv
        $ virtualenv nikola
        $ cd nikola



    - :html:`❹` Download packages `lxml` and `Pillow` compiled for Windows and for your installed version of Python. Copy them into nikola folder and install them using `pip`. I downloaded the packages `here <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.

    .. code:: console

        $ pip install lxml-3.6.1-cp35-cp35m-win32.whl
        $ pip install Pillow-3.3.0-cp35-cp35m-win32.whl



    - :html:`❺` Finally, install Nikola with "extras" option.

    .. code:: console

        $ pip install --upgrade "Nikola[extras]"



    - :html:`❻` Now, you should have Nikola installed and ready to use. You can get all available commands by typing `nikola help`.

    .. code-block:: console

        $ nikola help
        Nikola is a tool to create static websites and blogs. For full documentation and more information,
        please visit https://getnikola.com/

        Available commands:
          nikola auto                 builds and serves a site; automatically detects site changes
          nikola bootswatch_theme     given a swatch name from bootswatch.com and a parent theme, creates a custom theme
          nikola build                run tasks
          nikola check                check links and files in the generated site
          nikola clean                clean action / remove targets
          nikola console              start an interactive Python console with access to your site
          nikola deploy               deploy the site
          nikola doit_auto            automatically execute tasks when a dependency changes
          nikola dumpdb               dump dependency DB
          nikola forget               clear successful run status from internal DB
          nikola github_deploy        deploy the site to GitHub Pages
          nikola help                 show help
          nikola ignore               ignore task (skip) on subsequent runs
          nikola import_wordpress     import a WordPress dump
          nikola info                 show info about a task
          nikola init                 create a Nikola site in the specified folder
          nikola install_theme        install theme into current site
          nikola list                 list tasks from dodo file
          nikola new_page             create a new page in the site
          nikola new_post             create a new blog post or site page
          nikola orphans              list all orphans
          nikola plugin               manage plugins
          nikola reset-dep            recompute and save the state of file dependencies without executing actions
          nikola rst2html             compile reStructuredText to HTML files
          nikola serve                start the test webserver
          nikola status               display site status
          nikola strace               use strace to list file_deps and targets
          nikola tabcompletion        generate script for tab-completion
          nikola theme                manage themes
          nikola version              print the Nikola version number

          nikola help                 show help / reference
          nikola help <command>       show command usage
          nikola help <task-name>     show task usage



    - :html:`❼` To test if Nikola works as intended, you can create a demo site by few commands and display it in your browser.

    .. code-block:: console

        $ nikola init --demo              # Create and init a demo site
        $ cd demo
        $ nikola build                    # Build - generate the output
        $ nikola serve -a 127.0.0.1 -b    # Display the site in your default browser


|

