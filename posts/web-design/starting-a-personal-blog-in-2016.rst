.. title: Starting a Personal Blog with Nikola
.. slug: starting-a-personal-blog-in-2016
.. date: 2016-06-29 16:34:02 UTC+02:00
.. tags: mathjax, nikola, jupyter
.. category: web-design
.. link: 
.. description:
.. type: text

.. .............................................................................
.. default-role:: code
.. role:: text-info
.. role:: html(code)
    :language: html
.. .............................................................................


.. figure:: nikola_tesla_quote.tn.jpg
    :target: nikola_tesla_quote.jpg
    :align: right
    :figclass: thumbnail
    
    Nikola Tesla, one of the greatest inventors ever.


Hello and welcome to my new personal blog that I'm just creating using a site generator called `Nikola <http://getnikola.com/>`_. Indeed! it's named after the famous scientist and inventor **Nikola Tesla**, but that wasn't the only reason why I've decided for this interesting tool. Recently, I was tempted to set a personal blog, where I could post things I'm currently working on, or my ideas before I totally forget them. Of course, I was faced with the problem what site engine to choose, because there is truly lots of options in the year of 2016.

Before I start discussing my experience with Nikola, let me explain why I've decided for this tool. I'm a very picky person when it comes to customization and I looked for a tool that would satisfy all my needs, particularly...

- Have full control over the style and layout of the website.

- Enable to insert both blog posts and non-blog pages.

- Be able to type math (ideally using syntax of **TeX**), because mathematics is indeed the language of nature, thus the most universal language ever :)

- Use native **Jupyter** files (.ipynb) as source files for the site. :text-info:`Jupyter is a very handy web application that allows you to create and share documents containing live code, equations, visualizations and explanatory text. It supports many languages including Python, which makes it a perfect tool for writing scientific articles.`

- Open source tool without any commercial ads is preferred (very important in todays over-commercial world).

.. TEASER_END


Side note: :text-info:`An example how Nikola can render math using MathJax plugin. You can right-click the equation, get menu and see the TeX code (ShowMathAs - TeXCommands). Apropos, this is the famous Maxwell's equations describing electromagnetic field, probably one of the most favourite equations of Nikola Tesla :)`

.. math::
    \nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \\
    \nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\
    \nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\
    \nabla \cdot \vec{\mathbf{B}} & = 0


Then, considering the very few requirements above, I've tried to choose the optimal website engine for my needs. Basically, I considered these options...


.. class:: list-title

    Use existing CMS (Content Management System)

.. raw:: html

    <ul class="simple custom-list">
    <li class="pro-item">
        There is plenty of existing CMS to choose from like Wordpress, Drupal, Joomla, etc.
    </li>
    <li class="pro-item">
        They are supposed to be the most user friendly and quick way for starting a new blog.
    </li>
    <li class="con-item">
        I've never tried any CMS, but I guess any options for customization will be very limited since they are designed for users who know nothing about html or CSS. Also, CMS tend to be very complex and script-heavy, so it would take lots effort to dig inside its code to do some customizations.
    </li>
    <li class="con-item">
        I haven't found any CMS that would support native Jupyter files (.ipynb).
    </li>
    </ul>

.. class:: list-title

    Design a website from scratch

.. raw:: html

    <ul class="simple custom-list">
    <li class="pro-item">
        This approach should mean the best control over content since I could design the website exactly for my needs.
    </li>
    <li class="con-item">
        It would probably require to learn and use some server side language like PHP and some database.
    </li>
    <li class="con-item">
        It would be probably so time consuming that would be hard to even finish it.
    </li>
    </ul>

.. class:: list-title

    Use static site generator Nikola

.. raw:: html

    <ul class="simple custom-list">
    <li>
        The last option I considered was a generator of static pages. Yes, I thought this option is obsolete in 2016 and features limited, but I was wrong!
    </li>
    <li class="pro-item">
        Nikola is written in Python, which I'm familiar with, I use it also for coding Blender addons and Jypyter articles.
    </li>
    <li class="pro-item">
        Nikola supports Jupyter files (.ipynb) as source files for your site (Yay!).
    </li>
    <li class="pro-item">
        The options for customization are endless with Nikola, you own your files, and you can do anything with them.
    </li>
    <li class="pro-item">
        That all means you can create any possible look and feel of the site you might dream about.
    </li>
    <li class="pro-item">
        The obvious advantage is security since static pages don't use any heavy server-side framework.
    </li>
    </ul>
    

Getting to know Nikola
======================

.. figure:: nikola_tesla_quote2.tn.jpg
    :target: nikola_tesla_quote2.jpg
    :align: right
    :figclass: thumbnail
    
    Nikola Tesla in his laboratory.

Nikola is powered by `Python <https://www.python.org/>`_, so first we need to make sure Python is installed on our computer. Then, installing Nikola package is just question of few console commands. It's all well documented `here <https://getnikola.com/getting-started.html>`_.

When everything installed and ready, we can create our first site by command `nikola init mysite`. Inserting posts and pages is basically done by adding textual source files (.rst, .md, ...) into the dedicated folders. The names of these folders and all other site-related configurations can be found in the file `conf.py`. After we configured the site and added some content, we can just generate the output with static pages by simple, lovely command `nikola build` and we are done:) To display the site in our default browser we can use `nikola serve -b`.

Well that was quite easy, but now it comes the harder part if we want to create our unique look for the site.


Create custom look for Nikola site
==================================

There are some ready to use themes for Nikola, but really none of them corresponded to what I wanted to create. The good thing is that you don't need to create a new theme from scratch, but you can inherit it from an existing theme. All you need to do is just copy files you want to modify from an existing theme into a new folder inside `[themes]`. Then the folder tree for the new theme should look similar to this...

.. code-block:: 

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
            
I decided to create a theme based on **Bootstrap3** framework, so it must be specified in the file `parent`. Basically, the look of the site based on Bootstrap is given by file with CSS styles named `bootstrap.css`. I really don't recommend to modify this file itself since it's a really huge file (over 6000 lines). But we can use this useful online application http://bootstrap-live-customizer.com that enables to play with all the colors and styles and then generate the desired CSS file for us. For any later fine-tuning, I've added files `custom.css`, `theme.css` to override existing styles or add some new ones, and make things better arranged. If we are using Jupyter files, we can specify their styling by `nikola_ipython.css`.

Well, we have done some styling, but how to change the layout of our site? That's also easy to do with Nikola. We can use some template files from an existing theme and copy them into folder `[templates]`. Especially `base.tmpl` is essential, because it defines the actual layout for the whole site.



Markdown vs. reStrtructuredText
===============================

Before starting to create the actual content for our new site, we need to decide which format of source files to use for our post and pages. Nikola supports lots of these textual formats, but probably the most useful is **Markdown** (.md) or **reStructuredText - reST** (.rst). I've been hesitating a lot which one would be better for my needs. Even-though I'm writing this post using reST, I'm still not so sure which one is better. Let me try to summarize pros and cons for both formats...


.. class:: list-title

    Markdown

.. raw:: html

    <ul class="simple custom-list">
    <li class="pro-item">
        This format seems to be more popular and is used by lots of web applications.
    </li>
    <li class="pro-item">
        You can directly insert html code without any redundant directives.
    </li>
    <li class="pro-item">
        Syntax for hyperlinks is really simple e.g. <code>[Markdown](https://en.wikipedia.org/wiki/Markdown)</code>
    </li>
    <li class="con-item">
        Markdown eats every second backslash on output. So, if you want symbol <code>\\</code> for break-lines in TeX math formulas, you need to type <code>\\\\</code> in Markdown, which is really annoying and redundant work.
    </li>
    <li class="con-item">
        I haven't found any elegant way how to insert styled images and figures, apart of inserting plain html code.
    </li>
    </ul>
    
    
.. class:: list-title

    reStrtructuredText

.. raw:: html

    <ul class="simple custom-list">
    <li class="pro-item">
        reStrtructuredText seems to be the default and preferred format for Nikola.
    </li>
    <li class="pro-item">
        No problem with double backslash <code>\\</code> which is nice for inserting TeX math.
    </li>
    <li class="pro-item">
        There are lots of useful directives for inserting code-blocks, images, figures, etc.
    </li>
    <li class="con-item">
        The official documentation for reStrtructuredText is very poor and not well arranged.
    </li>
    <li class="con-item">
        I didn't find a way how to explicitly specify a section header (h1, h2, ...). Header levels seem to be just derived from the structure of document.
    </li>
    <li class="con-item">
        To insert plain html, you need to use a special directive.
    </li>


MathJax vs. KaTeX
=================

There are basically two options for rending math. `MathJax <https://www.mathjax.org/>`_ is the default option for Nikola and also for Jupyter notebooks. It has nice render quality and I haven't faced any serious problems using it. The only problem seem to be quite slow rendering time, and also the need to re-render all math after reloading the page.

On the other side, `KaTeX <https://github.com/Khan/KaTeX>`_ seems to be much faster to render, and there is no obvious re-rendering after page reloading. The font quality is also nice or maybe even better than MathJax. But I have faced serious problems that made me give up using KaTeX for my site. For example, I wasn't able to insert inline math using standard `$..$` directive, and TeX environments produced by Nikola are also not supported. All this makes KaTeX still too immature for usage with Nikola and Jupyter.



Conclusion
==========

Static site generator Nikola is indeed a very interesting tool! It's very flexible and in most cases you can achieve exactly what you want, like creating a custom look for every aspect of your website. Also, it's the only system, I know about, that enables to use native Jupyter files (.ipynb) for posts.

Of course, there is always space for improvements. For example, I don't like that by defaults, Nikola requires to maintain two or three separate folder trees. One folder tree for textual source files, another one for images and another for files, which seems to be a redundant work. Eventually, I was able to override that settings, and now I can maintain only a single folder tree that contains all post-related files.

Indeed, it's questionable what's the better approach for staring a new website, to use system like Nikola or some popular CMS engine like Wordpress? But that just depends on everyone's requirements and preferences.











