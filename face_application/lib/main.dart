// import 'package:flutter/material.dart';
// import 'login_page.dart'; //引入登录页面
// import 'signup_page.dart'; // 引入注册页面
// import 'phone_verification_page.dart'; // 引入验证码页面
// import 'forgot_password_page.dart'; // 引入忘记密码页面
// import 'email_verification_page.dart'; // 导入邮箱验证界面
// import 'facerec_page.dart'; //导入人脸识别界面
// import 'home_page.dart'; //导入主页
// import 'package:camera/camera.dart'; // 导入 camera 库
// import 'package:face_rec/camera_preview_page.dart'; // 导入相机预览页面

// List<CameraDescription>? cameras; // 初始化摄像头列表

// void main() async {
//   WidgetsFlutterBinding.ensureInitialized();
//   cameras = await availableCameras(); // 获取可用摄像头列表
//   runApp(MyApp());
// }

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       title: 'Your App Name',
//       theme: ThemeData(
//         primarySwatch: Colors.blue,
//       ),
//       initialRoute: '/', // 设置初始路由
//       routes: {
//         '/': (context) => LoginPage(), // 登录页面
//         '/signup': (context) => SignUpPage(), // 注册页面
//         '/verification': (context) => PhoneVerificationPage(), // 添加验证码页面路由
//         '/forgot_password': (context) => ForgotPasswordPage(), // 添加忘记密码页面路由
//         '/email_verification': (context) =>
//             EmailVerificationPage(), // 添加邮箱验证界面的路由
//         '/faceRecognition': (context) => FaceRecognitionPage(), // 添加人脸识别页面路由
//         '/home': (context) => HomePage(), // 添加主页路由
//         '/camera_preview': (context) => CameraPreviewPage(camera: cameras!.first), // 添加相机预览页面的路由
//       },
//     );
//   }
// }
