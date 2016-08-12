.. title: Starting a Personal Blog with Nikola
.. slug: starting-a-personal-blog-with-nikola
.. date: 2016-06-29 16:34:02 UTC+02:00
.. tags: mathjax, nikola
.. category: web-design
.. link: 
.. description:
.. type: text

.. .............................................................................
.. default-role:: code
.. role:: text-info
.. role:: html(raw)
    :format: html
.. .............................................................................


.. figure:: nikola_tesla_quote.tn.jpg
    :target: nikola_tesla_quote.jpg
    :align: right
    :figclass: thumbnail
    
    Nikola Tesla, one of the greatest inventors ever.


Hello and welcome to my new personal blog that I'm just creating using a site generator called `Nikola <http://getnikola.com/>`_. Indeed! it's named after the famous scientist and inventor **Nikola Tesla**, but that wasn't the only reason why I've decided for this interesting tool. Recently, I was tempted to set a personal blog, where I could post things I'm currently working on, or my ideas before I totally forget them. Of course, I was faced with the problem what site engine I should choose, because there is truly lots of options in the year of 2016.

Before I start discussing my experience with Nikola, let me explain why I've decided for this tool. I'm a very picky person when it comes to customization, so I looked for a tool that would satisfy all my needs, particularly...


.. class:: basic-list

    - Have full control over every aspect of the style and layout.

    - I'm not a fan of phones, however smart they try to appear. So, I really don't care about mobile-first, responsive web design that hides all relevant information and menus and just pushes irrelevant photos to the whole screen!

    - Enable to insert both blog posts and non-blog pages.

    - Be able to type math (ideally using Syntax of **TeX**), because mathematics is indeed the language of nature, thus the most universal language ever :)

    - Use native **Jupyter** files (.ipynb) as source files for the site. :text-info:`Jupyter is a very handy web application that allows you to create and share documents containing live code, equations, visualizations and explanatory text. It supports many languages including Python, which makes it a perfect tool for writing scientific articles.`

    - Open source tool without any commercial ads is preferred (very important in todays over-commercialized world).

.. TEASER_END


Side note: :text-info:`An example how Nikola can render math using MathJax plugin. You can right-click the equation, get menu and see the TeX code (Show Math As - TeX Commands). Apropos, these are the famous Maxwell's equations describing electromagnetic field, probably one of the most favourite equations of Nikola Tesla :)`

.. math::
    \nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \\
    \nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\
    \nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\
    \nabla \cdot \vec{\mathbf{B}} & = 0



Then, considering the very few requirements above, I've tried to choose the optimal website engine for my needs. Basically, I considered these options...


Use existing CMS (Content Management System)
    .. class:: pros-list

        - There is plenty of existing CMS to choose from like Wordpress, Drupal, Joomla, etc.

        - They are supposed to be the most user friendly and easy way for starting a new blog.

    .. class:: cons-list

        - I've never tried any CMS, but I guess options for customization will be limited since they are designed for users who know nothing about HTML or CSS. Also, CMS tend to be very complex and script-heavy, so it would take lots of effort to do the desired customizations.

        - On CMS sites, every time a reader wants a page, a whole lot of database queries are made. Then a whole pile of code chews that data, and HTML is produced, which is sent to the user. All that requires time and server resources.

        - And the most critical problem, I haven't found any CMS that would support native Jupyter files (.ipynb).


Design a website from scratch
    .. class:: pros-list

        - This approach should mean the best control over content since I could design the website exactly for my needs.

    .. class:: cons-list

        - It would be probably so time-consuming that would be hard to even finish the basic framework.


Use static site generator Nikola
    .. class:: pros-list

        - The last option I considered was a generator of static pages. Yes, I thought this option is obsolete in 2016 and features limited, but I was wrong!

        - Nikola is written in Python that I'm familiar with, I also use it for coding Blender addons and Jypyter articles.

        - Nikola supports Jupyter files (.ipynb) as source files for your site (Yay!).

        - The options for customization are endless with Nikola, you own your files, and you can do anything with them.

        - That all means you can create any possible look and feel of the site you might dream about.

        - The obvious advantage is security since static pages don't use any heavy server-side framework.  



Getting to know Nikola
======================

.. figure:: nikola_tesla_quote2.tn.jpg
    :target: nikola_tesla_quote2.jpg
    :align: right
    :figclass: thumbnail
    
    Nikola Tesla in his laboratory.

Nikola is powered by `Python <https://www.python.org/>`_, so first you need to make sure Python is installed on your computer. Then, installing Nikola package is just question of few console commands. It's all well documented `here <https://getnikola.com/getting-started.html>`_.

When everything installed and ready, we can create our first site by command `nikola init mysite`. Inserting posts and pages is basically done by adding textual source files (.rst, .md,...) into the dedicated folders. The names of these folders and all other site-related configurations can be found in the file `conf.py`. After we configured our site and added some content, we can just generate the final output by the neat command `nikola build` and we are done :) To display the site in your default browser, you can use `nikola serve -a 127.0.0.1 -b`.

Well, that was quite easy, but now it comes the harder part if we want to create an unique look for our new site.



Creating custom look for Nikola site
------------------------------------

There are some ready to use themes for Nikola, but really none of them corresponded to what I wanted to create. The good thing is that you don't need to create a new theme from scratch, but you can inherit it from an existing theme. All you need to do is just copy files you want to modify from an existing theme into a new folder inside `[themes]`. Then the folder tree for the new theme should look similar to this...

.. code::

    [themes]
        [mytheme]
            [assets]
                [css]
                    bootstrap.css
                    bootstrap.min.css
                    custom.css
                    nikola_ipython.css
                    theme.css
                [img]
                [js]
                    custom.js
            [templates]
                base.tmpl
            bundles
            parent
            

I decided to create a theme based on **Bootstrap3** framework, which must be specified in the file `parent`. Basically, the look of the site based on Bootstrap is given by file with CSS styles named `bootstrap.css`. I really don't recommend to modify this file itself since it's a really huge file (over 6000 lines). But we can use this useful online application http://bootstrap-live-customizer.com that enables to play with all the colors and styles and then generate the desired CSS files for us. For any later fine-tuning, I've added files `custom.css`, `theme.css` to override existing styles or add some new ones, and make things better arranged. If we are using Jupyter files, we can specify their styling by `nikola_ipython.css`.

Well, we have done some styling, but how to change the layout of our site? That's also easy to do with Nikola. We can use some template files from an existing theme and copy them into folder `[templates]`. Especially `base.tmpl` is essential, because it defines the actual layout for the whole site. Also, we can add other templates and modify the layout for posts, indexes, etc.



Markdown vs. reStrtructuredText
-------------------------------

Before starting to create the actual content for our new site, we need to decide which format of source files to use for our post and pages. Nikola supports lots of these textual formats, but probably the most useful is **Markdown** (.md) or **reStructuredText - reST** (.rst). I've been hesitating a lot which one would be better for my needs. Even-though I'm writing this post using reST, I'm still not so sure which one is better. Let me try to summarize pros and cons for both formats...


Markdown
    .. class:: pros-list

        - This format seems to be more popular and is used by lots of web applications.

        - You can directly insert HTML code without any redundant directives.

        - Syntax for hyperlinks is really simple e.g. `[Markdown](https://en.wikipedia.org/wiki/Markdown)`

    .. class:: cons-list

        - Markdown eats every second backslash on output. So, if you want symbol `\\` for break-lines in TeX math formulas, you need to type `\\\\` in Markdown, which is really annoying and redundant work.

        - I haven't found any elegant way how to insert styled images and figures, apart of inserting plain HTML code.
    
    
reStrtructuredText
    .. class:: pros-list

        - reStrtructuredText seems to be the default and preferred format for Nikola.

        - No problem with double backslash `\\` which is nice for inserting TeX math.

        - There are lots of useful directives for inserting code-blocks, images, figures, etc.

    .. class:: cons-list

        - The official documentation for reStrtructuredText is very poor and not well arranged.

        - I didn't find a way how to explicitly specify a section header (h1, h2, ...). Header levels seem to be just derived from the structure of document.

        - To insert plain HTML, you need to use a special directive.



MathJax vs. KaTeX
-----------------

There are basically two options for rending math. `MathJax <https://www.mathjax.org/>`_ is the default option for Nikola and also for Jupyter notebooks. It has nice render quality and I haven't faced any serious problems using it. The only problem seem to be quite slow rendering time, and also the need to re-render all math after reloading the page.

On the other side, `KaTeX <https://github.com/Khan/KaTeX>`_ seems to be much faster to render, and there is no obvious re-rendering after page reloading. The font quality is also nice or maybe even better than MathJax. But I have faced serious problems that made me give up using KaTeX for my site. For example, I wasn't able to insert inline math using standard `$..$` directive, and TeX environments produced by Nikola are also not supported. All this makes KaTeX still too immature for usage with Nikola and Jupyter.



Deploying Nikola Site to GitHub
-------------------------------

When we are happy with our new site, we just need to choose a webhosting service. We have really lots of options here, because Nikola generates static pages, thus doesn't require to run any server-side scripts. Finally, I've chosen **GitHub**, because it offers free space for static pages and doesn't contain any annoying commercial ads.

GitHub is originally a service for version control system called **Git**, and the possibility for hosting static pages is quite new. Therefore, to use this service, one need to get familiar with Git protocol first. This makes things a bit more complicated in contrast to other webhostings, where you can just use FTP for uploading your site. On the other side, if you are interested in programming, learning to use Git is definitely worth of it.

So, to deploy a new site to GitHub, first we must have a GitHub account. Then, we need to create a new repository named after the site URL - in my case I created a repository named `meshlogic.github.io`, because my user name is "meshlogic". Now, we can do some basic customization in the Nikola config file `conf.py`.


.. code:: python

    GITHUB_DEPLOY_BRANCH = 'master'  # Deploy the Nikola output to the master branch of your repository
    GITHUB_SOURCE_BRANCH = 'src'     # Deploy Nikola project source files to src branch of your repository
    GITHUB_COMMIT_SOURCE = True


When everything ready to deploy, we open console in the path of our Nikola project and start using Git. Of course, you need to have Git installed on your computer and available from command line.


.. code:: console
    
    $ git config --global user.name "USER_NAME"
    $ git config --global user.email "USER_EMAIL"
    $ git init
    $ git remote add origin https://github.com/meshlogic/meshlogic.github.io.git
    $ git pull origin master --allow-unrelated-histories


Note that `git init` creates a hidden folder `[.git]` inside your project folder. `git remote` makes a branch named "origin" linked to your GitHub repository specified by its URL. `git pull` seems to be necessary to run even when your repository is still empty (at least in my case it was).

Finally, we can run simple command `nikola github_deploy`, which commits the output and pushes it to GitHub. Now if everything went right, your site should be running :)



Conclusion
==========

Static site generator **Nikola** is indeed a very interesting tool! It's very flexible and in most cases you can achieve exactly what you want, like creating a custom look for every aspect of your website. Also, it's the only system, I know about, that enables to use native **Jupyter** files (.ipynb) for posts and pages.

Of course, there is always space for improvements. For example, I don't like that by defaults, Nikola requires to maintain two or three separate folder trees. One folder tree for textual source files, another one for images and another for files, which seems to be a redundant work. Eventually, I was able to override that settings, and now I can maintain only a single folder tree that contains all post-related files.

Indeed, it's questionable what's the better approach for staring a new website, to use highly-customizable system like Nikola or some more popular CMS engine like Wordpress? But that just depends on everyone's requirements and preferences :)




