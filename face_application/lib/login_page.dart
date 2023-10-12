// import 'package:face_rec/facerec_page.dart';
// import 'package:flutter/material.dart';

// class LoginPage extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: Text('Login Page'), // 设置页面标题为 "Login Page"
//       ),
//       body: Padding(
//         padding: EdgeInsets.all(16.0), // 设置内边距为 16 像素
//         child: Column(
//           mainAxisAlignment: MainAxisAlignment.center,
//           children: <Widget>[
//             Text(
//               'Let Us Sign You In', // Getting started 文字
//               style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
//             ),
//             SizedBox(height: 10.0),
//             Text(
//               'Welcome back,you have been missed!', // 提示文字
//               style: TextStyle(fontSize: 16),
//             ),
//             SizedBox(height: 20.0),
//             TextField(
//               decoration: InputDecoration(
//                 labelText: 'Username', // 设置输入框标签为 "Username"
//               ),
//             ),
//             SizedBox(height: 10.0), // 添加 10 像素的垂直间距
//             TextField(
//               decoration: InputDecoration(
//                 labelText: 'Password', // 设置输入框标签为 "Password"
//               ),
//               obscureText: true, // 隐藏密码输入内容
//             ),
//             SizedBox(height: 20.0), // 添加 20 像素的垂直间距
//             ElevatedButton(
//               onPressed: () {
//                 Navigator.push(
//                   context,
//                   MaterialPageRoute(builder: (context) => FaceRecognitionPage()),
//                 );
//               },
//               style: ElevatedButton.styleFrom(
//                 primary: Colors.purple[100], // 按钮背景颜色为淡紫色
//                 minimumSize: Size(double.infinity, 50), // 设置按钮最小宽度和高度
//               ),
//               child: Text(
//                 'Log In', // 按钮文本为 "Log In"
//                 style: TextStyle(
//                   color: Colors.white, // 按钮文字颜色为白色
//                   fontSize: 18, // 设置文字大小
//                 ),
//               ),
//             ),
//             SizedBox(height: 10.0), // 在两个按钮之间添加 10 像素的垂直间距
//             ElevatedButton(
//               onPressed: () {
//                 Navigator.pushNamed(context, '/signup');  // 跳转到注册页面
//               },
//               style: ElevatedButton.styleFrom(
//                 primary: Colors.purple[100], // 按钮背景颜色为淡紫色
//                 minimumSize: Size(double.infinity, 50), // 设置按钮最小宽度和高度
//               ),
//               child: Text(
//                 'Sign Up', // 按钮文本为 "Sign Up"
//                 style: TextStyle(
//                   color: Colors.white, // 按钮文字颜色为白色
//                   fontSize: 18, // 设置文字大小
//                 ),
//               ),
//             ),
//             TextButton(
//               onPressed: () {
//                 Navigator.pushNamed(context, '/forgot_password');  // 跳转到忘记密码页面
//               },
//               child: Text('Forgot Password?'), // 设置按钮文本为 "Forgot Password?"
//             ),
//           ],
//         ),
//       ),
//     );
//   }
// }
