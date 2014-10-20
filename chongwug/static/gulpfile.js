var gulp = require('gulp'),
    glob = require('glob'),
    fs = require('fs'),
    argv = require('minimist')(process.argv.slice(2)),
    merge = require('merge-stream'),
    plugins = require('gulp-load-plugins')();

var config = require('./config.json'),
    prod = argv.prod === true ? true : false,
    dep = prod ? ['imgs'] : [];

gulp.task('css', dep, function(){
    var map = JSON.parse(fs.readFileSync('./imgs-manifest.json')),
        keys = Object.keys(map),
        reg = new RegExp(keys.join('|'), 'gm');

    gulp.src(config.css.src)
        // compile sass
//        .pipe(plugins.rubySass({
//            noCache: true,
//            sourcemap: false,
//            style: 'expanded'
//        }))
        .pipe(plugins.sass({
            precision: 8
        }))
        .on( 'error', function(e){console.log(e)})
//        .pipe(plugins.newer(config.css.dev))
        //.pipe(plugins.autoprefixer())
        //csscomb
        //.pipe(plugins.csscomb())
        // save to dev dir
        //.pipe(plugins.cssshrink())
//        .pipe(plugins.uncss({
//            html: ['http://localhost:8000', 'http://localhost:8000/home']
//        }))
        .pipe(gulp.dest(config.css.dev))
        //filter *.map
        .pipe(plugins.if(prod, plugins.filter('**/*.css')))
        .pipe(plugins.if(prod, plugins.replace(reg, function(e){ return map[e]; })))
        //compress css
        .pipe(plugins.if(prod, plugins.minifyCss({keepSpecialComments: 0, noAdvanced: true})))
        //version css
        .pipe(plugins.if(prod, plugins.rev()))
        //save to prod dir
        .pipe(plugins.if(prod, gulp.dest(config.css.prod)))
        //generate manifest
        .pipe(plugins.if(prod, plugins.rev.manifest()))
        //rename
        .pipe(plugins.rename({basename: 'css-manifest'}))
        //save manifest to prod dir
        .pipe(plugins.if(prod, gulp.dest('./')));
});

gulp.task('js', function(){
    var lib = config.js.lib,
        bootstrap = lib + '/bootstrap',
        map = require('./' + lib + '/basic-plugins.json'),
        arr = [];

    for(var i in map){
        if(map.hasOwnProperty(i) && map[i]){
            arr.push(bootstrap + '/' + i + '.js');
        }
    }

    merge(gulp.src(arr).pipe(plugins.concat('lib/plugins.js')), gulp.src(config.js.src))
        .pipe(gulp.dest(config.js.dev))
        .pipe(plugins.if(prod, plugins.uglify()))
        .pipe(plugins.if(prod, plugins.rev()))
        .pipe(plugins.if(prod, gulp.dest(config.js.prod)))
        .pipe(plugins.if(prod, plugins.rev.manifest()))
        .pipe(plugins.rename({basename: 'js-manifest'}))
        .pipe(plugins.if(prod, gulp.dest('./')));
});

gulp.task('imgs', function(){
    gulp.src(config.imgs.src)
        .pipe(gulp.dest(config.imgs.dev))
        .pipe(plugins.if(prod, plugins.imagemin({progressive: true})))
        .pipe(plugins.if(prod, plugins.rev()))
        .pipe(plugins.if(prod, gulp.dest(config.imgs.prod)))
        .on('error', function(e){ console.log(e); })
        .pipe(plugins.if(prod, plugins.rev.manifest()))
        .pipe(plugins.rename({basename: 'imgs-manifest'}))
        .pipe(plugins.if(prod, gulp.dest('./')));
});

gulp.task('fonts', function(){
    gulp.src(config.fonts.src)
        .pipe(gulp.dest(config.fonts.dev))
        .pipe(plugins.if(prod, gulp.dest(config.fonts.prod)))
        .on('error', function(e){ console.log(e); });
});

gulp.task('clean', function(){
    gulp.src('assets/*', {read: false})
        .pipe(plugins.clean());
});

gulp.task('default', ['clean'], function(){
    gulp.start(['css', 'js', 'imgs', 'fonts']);
});


gulp.task('watch', function(){
    plugins.watch({
                    glob: config.imgs.src,
                emitOnGlob: false,
        passThrough: false
    }, function(files) {
        console.log(files)
        gulp.start('imgs');
    });

    gulp.watch(config.css.src, ['css']);

//    plugins.watch({glob: config.css.src}, function(){
//        gulp.start('css');
//    });
});

gulp.task('react', function(){
    gulp.src('./src/js/components/*.js')
        .pipe(plugins.react())
        .pipe(gulp.dest('./assets/js/components'));
});