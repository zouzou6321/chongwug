var gulp = require('gulp'),
    del = require('del'),
    glob = require('glob'),
    fs = require('fs'),
    argv = require('minimist')(process.argv.slice(2)),
    merge = require('merge-stream'),
    plugins = require('gulp-load-plugins')(),
    browserSync = require('browser-sync'),
    reload = browserSync.reload,
    spritesmith = require('gulp.spritesmith');

var config = require('./config.json'),
    prod = argv.prod === true ? true : false,
    dep = prod ? ['imgs'] : [];

gulp.task('sync', function(){
    browserSync({
        proxy: 'localhost:8000'
    });
});

gulp.task('sprites', function(){
     var spriteData = gulp.src(config.sprites.src).pipe(spritesmith({
        imgName: 'sprites.png',
        imgPath: '../imgs/sprites.png',
        cssName: '_sprites.scss',
        cssFormat: 'scss',
        engine: 'phantomjs',
        algorithm: 'binary-tree',
        cssVarMap: function (sprite) {
          sprite.name = 'sprite-' + sprite.name;
        },
        cssTemplate: './scss.template.mustache',
        cssOpts: {
          cssClass: function (item) {
            return '.sprite-' + item.name;
          }
        }
      }));

    spriteData.img.pipe(gulp.dest(config.sprites.imgDev));
    spriteData.css.pipe(gulp.dest(config.sprites.cssDev));
});


gulp.task('css', function(){
    var imgsMap = JSON.parse(fs.readFileSync('./imgs-manifest.json')),
        fontsMap = JSON.parse(fs.readFileSync('./fonts-manifest.json')),
        imgsKeys = Object.keys(imgsMap),
        imgsReg = new RegExp(imgsKeys.join('|'), 'gm'),
        fontsKeys = Object.keys(fontsMap),
        fontsReg = new RegExp(fontsKeys.join('|'), 'gm');

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
        .pipe(reload({stream: true}))
        //filter *.map
        .pipe(plugins.if(prod, plugins.filter('**/*.css')))
        .pipe(plugins.if(prod, plugins.replace(imgsReg, function(e){ return imgsMap[e]; })))
        .pipe(plugins.if(prod, plugins.replace(fontsReg, function(e){ return fontsMap[e]; })))
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
    var lib = config.js.lib,
        bootstrap = lib + '/ratchet',
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
        .pipe(plugins.if(prod, plugins.cache(plugins.imagemin({progressive: true}))))
        .pipe(plugins.if(prod, plugins.rev()))
        .pipe(plugins.if(prod, gulp.dest(config.imgs.prod)))
        .on('error', function(e){ console.log(e); })
        .pipe(plugins.if(prod, plugins.rev.manifest({path: 'imgs-manifest.json'})))
        .pipe(plugins.if(prod, gulp.dest('./')));
});

gulp.task('fonts', function(){
    gulp.src(config.fonts.src)
        .pipe(gulp.dest(config.fonts.dev))
        .pipe(plugins.if(prod, plugins.rev()))
        .pipe(plugins.if(prod, gulp.dest(config.fonts.prod)))
        .pipe(plugins.if(prod, plugins.rev.manifest({path: 'fonts-manifest.json'})))
        .pipe(plugins.if(prod, gulp.dest('./')))
        .on('error', function(e){ console.log(e); });
});

gulp.task('clean', function(){
    del('assets/**');
});

gulp.task('default', ['clean'], function(){
    gulp.start(['css', 'js', 'imgs', 'fonts']);
});


gulp.task('watch', ['sync'], function(){
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
