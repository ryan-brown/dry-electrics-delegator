const webpack = require("webpack");
const path = require("path")
const config = {
  devtool: "eval-source-map",
  entry: {
    privacy: __dirname + "/src/pages/PrivacyPolicy/PrivacyPolicy.jsx",
    login: __dirname + "/src/pages/Login/Login.jsx",
    signup: __dirname + "/src/pages/SignUp/SignUp.jsx",
    settings: __dirname + "/src/pages/Settings/Settings.jsx",
    user: __dirname + "/src/pages/User/User.jsx",
    notfound: __dirname + "/src/pages/NotFound/NotFound.jsx",
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