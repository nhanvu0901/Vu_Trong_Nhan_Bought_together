'use strict'
const {VueLoaderPlugin} = require('vue-loader')
const path = require('path');
const webpack = require('webpack')

module.exports = (env) => {
    console.log('Environment: ', env.NODE_ENV);
    let mode = env.NODE_ENV
    return {
        mode: mode,
        entry: [
            './app.js'
        ],
        output: {
            path: path.resolve(__dirname, '../js'),
            filename: 'index.js'
        },
        module: {
            rules: [{
                    test: /\.vue$/,
                    use: 'vue-loader'
                }, {
                    test: /\.css$/,
                    use: [
                        'vue-style-loader',
                        'css-loader',
                    ]
                }, {
                    test: /\.js$/,
                    exclude: [/node_modules/],
                    use: [{
                        loader: 'babel-loader',
                        options: {plugins: ['transform-vue-jsx']}
                    }]
                },
            ]
        },
        plugins: [
            new VueLoaderPlugin(),
            new webpack.DefinePlugin({
                __VUE_OPTIONS_API__: true,
                __VUE_PROD_DEVTOOLS__: false,
            }),
        ]
    };
};

