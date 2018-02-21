<aside id="widget-recent-posts" class="widget bodypart">

        <h3 class="widget-title">
            Recent Posts
        </h3>

        <ul class="recent-posts">
                <li><a href="/posts/blender/addons/outliner-tweaks/">Outliner Tweaks - Blender Addon</a></li>
                <li><a href="/posts/software/xnview/blender-inspired-theme-xnview/">Blender Inspired Theme for XnViewMP Photo Manager</a></li>
                <li><a href="/posts/blender/addons/extra-material-list/">Extra Material List - Blender Addon</a></li>
        </ul>

    </aside>


    

        <aside id="widget-category-list" class="widget bodypart">

            <h3 class="widget-title">
                Categories
            </h3>

                        <ul class="category-list category-level-1">
                    <li>
                        <a href="/categories/cat_blender/">blender</a> <span class="widget-list-count">(13)</span>
                        <ul class="category-list category-level-2">
                    <li>
                        <a href="/categories/cat_blender/addons/">addons</a> <span class="widget-list-count">(6)</span>
                            </li>
                    <li>
                        <a href="/categories/cat_blender/materials/">materials</a> <span class="widget-list-count">(5)</span>
                            </li>
                    <li>
                        <a href="/categories/cat_blender/scripting/">scripting</a> <span class="widget-list-count">(1)</span>
                            </li>
                    <li>
                        <a href="/categories/cat_blender/themes/">themes</a> <span class="widget-list-count">(1)</span>
                            </li>
                        </ul>
                        </li>
                    <li>
                        <a href="/categories/cat_math/">math</a> <span class="widget-list-count">(4)</span>
                        <ul class="category-list category-level-2">
                    <li>
                        <a href="/categories/cat_math/curve-fitting/">curve-fitting</a> <span class="widget-list-count">(2)</span>
                            </li>
                    <li>
                        <a href="/categories/cat_math/linear-algebra/">linear-algebra</a> <span class="widget-list-count">(2)</span>
                            </li>
                        </ul>
                        </li>
                    <li>
                        <a href="/categories/cat_software/">software</a> <span class="widget-list-count">(1)</span>
                            </li>
                    <li>
                        <a href="/categories/cat_virtual-worlds/">virtual-worlds</a> <span class="widget-list-count">(1)</span>
                        <ul class="category-list category-level-2">
                    <li>
                        <a href="/categories/cat_virtual-worlds/second-life/">second-life</a> <span class="widget-list-count">(1)</span>
                            </li>
                        </ul>
                        </li>
                    <li>
                        <a href="/categories/cat_web-design/">web-design</a> <span class="widget-list-count">(2)</span>
                        <ul class="category-list category-level-2">
                    <li>
                        <a href="/categories/cat_web-design/nikola/">nikola</a> <span class="widget-list-count">(2)</span>
                            </li>
                        </ul>
                        </li>
                        </ul>

            
        </aside>


    

        <aside id="widget-tag-list" class="widget bodypart">

            <h3 class="widget-title">
                Tags
            </h3>

                <ul class="tag-list">
                            <li><a href="/categories/blender/">blender</a> <span class="widget-count">(13)</span></li>
                            <li><a href="/categories/python/">python</a> <span class="widget-count">(10)</span></li>
                            <li><a href="/categories/blender-addon/">blender-addon</a> <span class="widget-count">(6)</span></li>
                            <li><a href="/categories/jupyter/">jupyter</a> <span class="widget-count">(4)</span></li>
                            <li><a href="/categories/math/">math</a> <span class="widget-count">(4)</span></li>
                            <li><a href="/categories/curve-fitting/">curve-fitting</a> <span class="widget-count">(2)</span></li>
                            <li><a href="/categories/linear-algebra/">linear-algebra</a> <span class="widget-count">(2)</span></li>
                            <li><a href="/categories/nikola/">nikola</a> <span class="widget-count">(2)</span></li>
                            <li><a href="/categories/numpy/">numpy</a> <span class="widget-count">(2)</span></li>
                            <li><a href="/categories/web-design/">web-design</a> <span class="widget-count">(2)</span></li>
                            <li><a href="/categories/firestorm/">firestorm</a> <span class="widget-count">(1)</span></li>
                            <li><a href="/categories/second-life/">second-life</a> <span class="widget-count">(1)</span></li>
                            <li><a href="/categories/xnview/">xnview</a> <span class="widget-count">(1)</span></li>
                </ul>
            
        </aside>




    <aside id="widget-flickr" class="widget bodypart">

        <h3 class="widget-title">
            Recent Pics on Flickr
        </h3>

        <div id="widget-flickr-pics"></div>

        <script>
            (function() {
                var flickerAPI = "https://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?";
                $.getJSON( flickerAPI, {
                    id: "155478827@N06",
                    format: "json"
                })

                .done(function( data ) {
                    $.each(data.items, function(i, item) {
                        var $append = '';
                        $append += '<div>';
                        $append += '<a href="' + item.link + '" target="_blank">';
                        $append += '<img src="' + item.media.m + '">';
                        $append += '</a></div>';

                        $('#widget-flickr-pics').append($append);

                        if (i === 2)
                            return false;
                    });

                });
            })();
        </script>
        
    </aside>


