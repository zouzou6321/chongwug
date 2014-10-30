var gulp = require('gulp'),
    del = require('del'),
    glob = require('glob'),
    fs = require('fs'),
    argv = require('minimist')(process.argv.slice(2)),
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
        .pipe(plugins.if(prod, plugins.rev.manifest({path: 'css-manifest.json'})))
        //save manifest to prod dir
        .pipe(plugins.if(prod, gulp.dest('./')));
});

gulp.task('js', function(){
    gulp.src(config.js.src)
        .pipe(gulp.dest(config.js.dev))
        .pipe(plugins.if(prod, plugins.uglify()))
        .on('error', function(e){
            console.log(e.toString());
        })
        .pipe(plugins.if(prod, plugins.rev()))
        .pipe(plugins.if(prod, gulp.dest(config.js.prod)))
        .pipe(plugins.if(prod, plugins.rev.manifest({path: 'js-manifest.json'})))
        .pipe(plugins.if(prod, gulp.dest('./')));
});

gulp.task('imgs', function(){
    gulp.src(config.imgs.src)
        .pipe(gulp.dest(config.imgs.dev))
        .pipe(plugins.if(prod, plugins.imagemin()))
        .pipe(plugins.if(prod, plugins.rev()))
        .pipe(plugins.if(prod, gulp.dest(config.imgs.prod)))
        .on('error', function(e){ console.log(e); })
        .pipe(plugins.if(prod, plugins.rev.manifest({path: 'imgs-manifest.json'})))
        .pipe(plugins.if(prod, gulp.dest('./')));
});

gulp.task('clean', function(){
    del('dev/**');
});

gulp.task('default', function(){
    gulp.start(['css', 'js', 'imgs']);
});

gulp.task('fonts', function(){
    gulp.src(config.fonts.src)
        .pipe(gulp.dest(config.fonts.dev))
        .pipe(plugins.if(prod, gulp.dest(config.fonts.prod)))
        .on('error', function(e){ console.log(e); });
});


gulp.task('watch', function(){
    plugins.watch({
        glob: config.imgs.src,
        emitOnGlob: false,
        passThrough: false
    }, function(files) {
        gulp.start('imgs');
    });

    gulp.watch(config.css.src, ['css']);
});
