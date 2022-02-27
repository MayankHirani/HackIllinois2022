const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ],
  devServer: {
    compress: true,
    disableHostCheck: true,
    allowedHosts: [
        '.heroku.com', '.herokuapps.com'
    ]
  }
})
