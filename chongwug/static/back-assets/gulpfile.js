var gulp = require('gulp'),
    plugins = require('gulp-load-plugins')();

gulp.task('fonts', function(){
    gulp.src('./src/fonts/*')
        .pipe(gulp.dest('./dist/fonts'));
});

gulp.task('css', function(){
    gulp.src('./src/sass/**/*.scss')
        .pipe(plugins.sass({
            precision: 8
        }))
        .on( 'error', function(e){ console.log(e.toString()); })
        .pipe(plugins.cssmin({ noAdvanced:true }))
        .pipe(gulp.dest('./dist/css'));
});

gulp.task('js', function(){
    gulp.src('./src/js/**/*.js')
        .pipe(plugins.uglify())
        .pipe(gulp.dest('./dist/js'));
});

gulp.task('imgs', function(){
    gulp.src('./src/imgs/**/*.+(jpg|png|gif)')
        .pipe(plugins.imagemin({ progressive: true }))
        .pipe(gulp.dest('./dist/imgs'));
});

gulp.task('watch', function(){
    gulp.watch('./src/sass/**/*.scss', ['css']);
});

gulp.task('default', []);