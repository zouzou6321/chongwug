var   fs = require('fs')
    , through = require('through2')
    , plugins = require('gulp-load-plugins')();

module.exports = function(prod){
  var stream = through.obj();

  stream = stream.pipe(plugins.sass());

  stream.on('error', function(error){
    console.log(error.toString());
  });

  if(prod){
    var map = JSON.parse(fs.readFileSync('./imgs-manifest.json')),
        keys = Object.keys(map),
        reg = new RegExp(keys.join('|'), 'gm');

    
  }


  return stream;
};

//
//
// var map = JSON.parse(fs.readFileSync('./imgs-manifest.json')),
//     keys = Object.keys(map),
//     reg = new RegExp(keys.join('|'), 'gm');
//
//
//     .on( 'error', function(e){console.log(e)})
// //        .pipe(plugins.newer(config.css.dev))
//     //.pipe(plugins.autoprefixer())
//     //csscomb
//     //.pipe(plugins.csscomb())
//     // save to dev dir
//     .pipe(gulp.dest(config.css.dev))
//     //filter *.map
//     .pipe(plugins.if(prod, plugins.filter('**/*.css')))
//     .pipe(plugins.if(prod, plugins.replace(reg, function(e){ return map[e]; })))
//     //compress css
//     .pipe(plugins.if(prod, plugins.cssmin({noAdvanced:true})))
//     //version css
//     .pipe(plugins.if(prod, plugins.rev()))
//     //save to prod dir
//     .pipe(plugins.if(prod, gulp.dest(config.css.prod)))
//     //generate manifest
//     .pipe(plugins.if(prod, plugins.rev.manifest()))
//     //rename
//     .pipe(plugins.rename({basename: 'css-manifest'}))
//     //save manifest to prod dir
//     .pipe(plugins.if(prod, gulp.dest('./')));
