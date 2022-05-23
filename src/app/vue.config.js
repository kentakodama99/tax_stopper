const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ]
})
module.exports = {
  outputDir: 'docs',
  assetsDir: "./",
  // publicPath: "./",
  publicPath: "/tax_stopper", // gitpage deploy
}
