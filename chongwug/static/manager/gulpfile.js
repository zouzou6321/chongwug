var gulp = require('gulp'),
    argv = require('minimist')(process.argv.slice(2)),
    prod = argv.prod === true ? true : false,
    del = require('del'),
    plugins = require('gulp-load-plugins')();


gulp.task('clean', function(){
    del('assets/dev/**');
});

gulp.task('fonts', function(){
    var stream = gulp.src('assets/src/fonts/**')
        .pipe(gulp.dest('assets/dev/fonts'));

    if(prod){
        stream.pipe(gulp.dest('assets/dist/fonts'));
    }
});

gulp.task('css', function(){
    var stream = gulp.src('assets/src/scss/**/*.scss')
        .pipe(plugins.sass({
            precision: 8
        }))
        .on( 'error', function(e){ console.log(e.toString()); })
        .pipe(gulp.dest('assets/dev/css'));

    if(prod){
        stream.pipe(plugins.minifyCss({keepSpecialComments: 0, noAdvanced: true}))
            .pipe(gulp.dest('assets/dist/css'));
    }
});

gulp.task('js', function(){
    var stream = gulp.src('assets/src/js/**')
        .pipe(gulp.dest('assets/dev/js'));

    if(prod){
        stream.pipe(plugins.uglify())
            .pipe(gulp.dest('assets/dist/js'));
    }
});

gulp.task('imgs', function(){
    var stream = gulp.src('assets/src/imgs/**/*.+(jpg|png|gif)')
        .pipe(gulp.dest('assets/dev/imgs'));

    if(prod){
        stream.pipe(plugins.imagemin())
            .pipe(gulp.dest('assets/dist/imgs'))
    }
});

gulp.task('vendor', function(){
    var css = plugins.filter('**/*.css'),
        js = plugins.filter(['**/*.js', '!ckeditor/**']);

    var stream = gulp.src('assets/src/vendor/**')
        .pipe(gulp.dest('assets/dev/vendor'));

    if(prod){
        stream.pipe(css)
            .pipe(plugins.minifyCss({keepSpecialComments: 0, noAdvanced: true}))
            .pipe(css.restore())
            .pipe(js)
            .pipe(plugins.uglify())
            .pipe(js.restore())
            .pipe(gulp.dest('assets/dist/vendor'));
    }
});

gulp.task('watch', function(){
    gulp.watch('assets/src/scss/**/*.scss', ['css']);
});

gulp.task('default', ['js', 'css', 'imgs', 'fonts', 'vendor']);