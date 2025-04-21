const { defineConfig } = require('@vue/cli-service');
const webpack = require('webpack');

module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: {
    plugins: [
      new webpack.DefinePlugin({
        __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: 'false',
      }),
    ],
  },
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000', // Flask backend
        changeOrigin: true,
        pathRewrite: { '^/api': '' },
      },
    },
  },
});
