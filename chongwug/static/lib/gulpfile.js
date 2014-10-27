var gulp = require('gulp'),
    $ = require('gulp-load-plugins')();

gulp.task('assets', function(){
    var css = $.filter('**/*.css'),
        js = $.filter('**/*.js');

    gulp.src(['./src/**', '!./src/ckeditor/**'])
        .pipe(css)
        .pipe($.minifyCss({keepSpecialComments: 0, noAdvanced: true}))
        .pipe(css.restore())
        .pipe(js)
        .pipe($.uglify())
        .pipe(js.restore())
        .pipe(gulp.dest('./dist'));
});

gulp.task('copy', function(){
    gulp.src('./src/ckeditor/**', {base: './src'})
        .pipe(gulp.dest('./dist'));
});

gulp.task('default', ['assets', 'copy']);