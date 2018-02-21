.. title: Starting a Personal Blog with Nikola
.. slug: starting-a-personal-blog-with-nikola
.. date: 2016-06-29 16:34:02 UTC+02:00
.. category: web-design/nikola
.. tags: mathjax, nikola, web-design
.. link: 
.. description:
.. type: text

.. default-role:: code
.. role:: text-info
.. role:: html(raw)
    :format: html

.. figure:: nikola_tesla_quote.tn.jpg
    :target: nikola_tesla_quote.jpg
    :align: right
    :figclass: thumbnail
    
    Nikola Tesla, one of the greatest inventors ever.


Hello and welcome to my new personal blog that I'm just creating using a site generator called `Nikola <http://getnikola.com/>`_. Indeed! it's named after the famous scientist and inventor **Nikola Tesla**, but that wasn't the only reason why I've decided for this interesting tool. Recently, I was tempted to set a personal blog, where I could post things I'm currently working on and my ideas before I totally forget them. Of course, I was facing a problem what site engine I should choose, because there are truly lots of options in the year of 2016!

Before I start discussing my experience with Nikola, let me explain why I've decided for this tool. I'm a very picky person when it comes to customization, so I looked for a tool that would satisfy all my desires, particularly...

.. TEASER_END


.. class:: li-smallskip

    - Have full control over every aspect of the style and layout to make a decent **desktop-first** website theme.

    - I'm not a fan of telephones, however smart they try to appear. So, mobile-first, ultra-responsive web designs that hide all navigations and makes you scroll heavily cannot really attract me.

    - Insert both blog posts and non-blog pages.

    - Type and render math (using syntax of **LaTeX**), because mathematics is indeed the language of nature, thus the most universal language ever :)

    - Use native **Jupyter** files (.ipynb) as source files for the site. :text-info:`Jupyter is a very handy web application that allows you to create and share documents containing live code, equations, visualizations and explanatory text. It supports many languages including Python, which makes it a perfect tool for writing scientific articles.`
    
    - Open source tool without any commercial ads is preferred (very important in todays over-commercialized world).


.. Tip::

    An example how Nikola can render math using the **MathJax** plugin. You can right-click the formula to get a menu with render options. Apropos, these are the famous Maxwell's equations describing electromagnetic field, probably the most fave equations of Nikola Tesla :)

    .. math::
        \nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \\
        \nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\
        \nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\
        \nabla \cdot \vec{\mathbf{B}} & = 0


Then, considering the very few requirements above, I've tried to choose an optimal website engine for my needs. Basically, I considered these options...



Use existing CMS (Content Management System)
    .. class:: pros-list

        - There is plenty of existing CMS to choose from like Wordpress, Drupal, Joomla, etc.

        - They are supposed to be the most user friendly and easy way for starting a new blog.

        - CMS have web based user interface that helps with writing/editing content.

    .. class:: cons-list

        - I've tried only a free CMS on wordpress.com, but was quite disappointed. With the free version, you are not allowed to modify CSS styles nor install any plugins (you have to pay around 30$ per month to be able to install plugins). Another issue is typing math - you often end with parsing errors even when your LaTeX code is completely valid. :text-info:`I don't say that Wordpress is bad, but to fully use its power, you would need to install and configure it properly on a paid server and have all needed permissions.`

        - CMS frameworks consume more processing time and server resources compared to static sites.

        - And the most critical problem for me, I didn't find any CMS that would support native Jupyter files (.ipynb) to generate posts and pages.


Design a website from scratch
    .. class:: pros-list

        - This approach should mean the best control over content since you could design the website exactly for your needs.

    .. class:: cons-list

        - It would be probably so time-consuming that would be hard to finish even a basic framework.


Use static site generator Nikola
    .. class:: pros-list

        - The last option I considered was a generator of static pages. Yes, I thought this option is obsolete in 2016 and features limited, but I was wrong!

        - Nikola is written in a modern scripting language **Python**.

        - No issues with writing **LaTeX** math formulas, unlike Wordpress.com which isn't math friendly.

        - Nikola supports **Jupyter** files (.ipynb) as source files for your site (Yay!).

        - The options for customization are endless with Nikola, you own your files, and you can do anything with them.

        - The obvious advantage is security and low lag since static pages don't use any heavy server-side framework.

    .. class:: cons-list

        - Since there is no database involved, you can organize the whole site just by a folder structure.

        - There is no web based interface for writing/editing content. That's not a big issue if you use a quality text editor, but it complicates the proofreading process - when you are reading a final post and need to correct something, you have to find the right source file, edit it in the text editor, build the site again and then refresh the page in the browser.



Getting to know Nikola
======================

.. figure:: nikola_tesla_quote2.tn.jpg
    :target: nikola_tesla_quote2.jpg
    :align: right
    :figclass: thumbnail
    
    Nikola Tesla in his laboratory.

Nikola is powered by `Python <https://www.python.org/>`_, so first make sure Python is installed on your computer. Then, installing the Nikola package is just a question of few console commands. It's all well documented `here <https://getnikola.com/getting-started.html>`_.

When everything installed and ready, you can create your first site by command `nikola init mysite`. Inserting posts and pages is basically done by adding textual source files (.rst, .md,...) into the dedicated folders. The names of these folders and all other site-related configurations can be found in the file `conf.py`. 

When all configured, just generate the final output by the neat command `nikola build` and you are done :) To display the site in the default browser, use `nikola serve -a 127.0.0.1 -b`.

Well, that was quite easy, but now it comes the harder part if we want to create an unique look for our new site.



Creating a custom look for Nikola site
----------------------------------------

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
            


I decided to create a theme based on **Bootstrap3** framework, which must be specified in the file `parent`. Basically, the look of the site based on Bootstrap is given by file with CSS styles named `bootstrap.css`. I really don't recommend to modify this file itself since it's a really huge file (over 6000 lines). But there is this useful online application http://bootstrap-live-customizer.com which enables you to play with all the colors and styles and then generate the desired CSS files. For any later fine-tuning, I've added files `custom.css`, `theme.css` to override existing styles and add some new ones to make things better arranged. If you are using Jupyter files, specify their styling by `nikola_ipython.css`.

Well, we have done some styling, but how to change the layout of the site? That's also easy to do with Nikola. You can use some template files from an existing theme and copy them into folder `[templates]`. Especially `base.tmpl` is essential, because it defines the actual layout for the whole site. Also, there are other templates to specify the layout for posts, indexes, etc.



Markdown vs. reStrtructuredText
---------------------------------

Before starting to create the actual content for the new site, you need to decide which format of source files to use for post and pages. Nikola supports lots of these textual formats, but probably the most useful is **Markdown** (.md) or **reStructuredText - reST** (.rst). I've been hesitating a lot which one would be better for my needs. Even-though I'm writing this post using reST, I'm still not so sure which one is better. Let me try to summarize pros and cons for both formats...


Markdown
    .. class:: pros-list

        - This format seems to be more popular and is used by lots of web applications.

        - You can directly insert HTML code without any redundant directives.

        - Syntax for hyperlinks is really simple e.g. `[Markdown](https://en.wikipedia.org/wiki/Markdown)`

    .. class:: cons-list

        - Markdown eats every second backslash on output. So, if you want symbol `\\` for break-lines in LaTeX math formulas, you need to type `\\\\` in Markdown, which is really annoying and redundant work.

        - I haven't found any elegant way how to insert styled images and figures, apart of inserting plain HTML code.
    
    
reStrtructuredText
    .. class:: pros-list

        - reStrtructuredText seems to be the default and preferred format for Nikola.

        - No problem with double backslash `\\` which is nice for inserting LaTeX math.

        - There are lots of useful directives for inserting code-blocks, images, figures, etc.

    .. class:: cons-list

        - The official documentation for reStructuredText is rather poor.

        - I didn't find a way how to explicitly specify a section header (h1, h2, ...). Header levels seem to be just derived from the structure of document.

        - To insert plain HTML, you need to use a special directive.



MathJax vs. KaTeX
-----------------

There are basically two options for rending math. `MathJax <https://www.mathjax.org/>`_ is the default option for Nikola and also for Jupyter notebooks. It has nice render quality and I haven't faced any serious problems using it. The only problem seem to be quite slow rendering time, and also the need to re-render all math after reloading the page.

On the other side, `KaTeX <https://github.com/Khan/KaTeX>`_ seems to be much faster to render, and there is no obvious re-rendering after page reloading. The font quality is also nice or maybe even better than MathJax. But I have faced serious problems that made me give up using KaTeX for my site. For example, I wasn't able to insert inline math using standard `$..$` directive, and TeX environments produced by Nikola are also not supported. All this makes KaTeX still too immature for usage with Nikola and Jupyter.



Deploying Nikola Site to GitHub
-------------------------------

When you are happy with the new site, you just need to choose a webhosting service. There are really lots of options, because Nikola generates static pages, thus doesn't require to run any server-side scripts. Finally, I've chosen **GitHub**, because it offers free space for static pages and doesn't contain any annoying commercial ads.

GitHub is originally a service for version control system called **Git**, and the possibility for hosting static pages is quite new. Therefore, to use this service, one need to get familiar with the Git protocol first. This makes things a bit more complicated in contrast to other webhostings, where you can just use FTP for uploading your site. On the other side, if you are interested in programming, learning to use Git is definitely worth of it.

So, to deploy a new site to GitHub, first you must have a GitHub account. Then, create a new repository named after the site URL - in my case I created a repository named `meshlogic.github.io`, because my user name is "meshlogic". Now, we can do some basic customization in the Nikola config file `conf.py`.


.. code:: python

    GITHUB_DEPLOY_BRANCH = 'master'  # Deploy the Nikola output to the master branch of your repository
    GITHUB_SOURCE_BRANCH = 'src'     # Deploy Nikola project source files to src branch of your repository
    GITHUB_COMMIT_SOURCE = True


When everything ready to deploy, open console in the path of the Nikola project and start using Git. Of course, you need to have Git installed on your computer and available from command line.


.. code:: console
    
    $ git config --global user.name "USER_NAME"
    $ git config --global user.email "USER_EMAIL"
    $ git init
    $ git remote add origin https://github.com/meshlogic/meshlogic.github.io.git
    $ git pull origin master --allow-unrelated-histories


Note that `git init` creates a hidden folder `[.git]` inside your project folder. `git remote` makes a branch named "origin" linked to your GitHub repository specified by its URL. `git pull` seems to be necessary to run even when your repository is still empty (at least in my case it was).

Finally, run a simple command `nikola github_deploy`, which commits the output and pushes it to GitHub. Now if everything went right, your site should be running online :)



Conclusion
==========

Static site generator **Nikola** is indeed a very interesting tool! It's very flexible and in most cases you can achieve exactly what you want, like creating a custom look for every aspect of your website. Also, it's the only system, I know about, that enables to use native **Jupyter** files (.ipynb) for posts and pages.

Of course, there is always space for improvements. For example, I don't like that Nikola requires to maintain two or three separate folder trees by default. One folder tree for text source files and another for images and other files, which seems to be a redundant work. But eventually, I was able to override that settings, and I can maintain only a single folder tree for all content-related files.

Of course, it's questionable what's the better approach for staring a new blog, to use a static site generator like Nikola or some more popular CMS engine like Wordpress? But that just depends on everyone's requirements and preferences. 

I would say Wordpress is better and more user friendly for a blog containing only text and pictures. But if you intend to include source codes, LaTeX math formulas and Jupyter articles, Nikola offers a very handy alternative that works without any major issues.



