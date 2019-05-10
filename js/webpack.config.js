const webpack = require("webpack");
const path = require("path")
const config = {
  devtool: "eval-source-map",
  entry: {
    privacy: __dirname + "/src/PrivacyPolicy.jsx",
    login: __dirname + "/src/Login.jsx",
    signup: __dirname + "/src/SignUp.jsx",
    settings: __dirname + "/src/Settings.jsx",
    user: __dirname + "/src/User.jsx",
  },
  output: {
    path: path.join(__dirname, "../app/static"),
    filename: "bundle-[name].js"
  },
  resolve: {
    extensions: [".js", ".jsx", ".css"]
  },
  module: {
    rules: [
      {
        test: /\.jsx?/,
        loader: "babel-loader",
        exclude: /node_modules/,
        query: {
          presets: ["react", "es2015"]
        }
      },
      {
        test: /\.css$/,
        loader: ['style-loader', 'css-loader']
      }
    ]
  }
};
module.exports = config;