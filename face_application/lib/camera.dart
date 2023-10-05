import 'dart:io';

import 'package:camera/camera.dart';
import 'package:flutter/material.dart';
List<CameraDescription>? cameras;
Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  cameras = await availableCameras();
  runApp(const MyApp());
}
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}
class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);
  final String title;
  @override
  _MyHomePageState createState() => _MyHomePageState();
}
class _MyHomePageState extends State<MyHomePage> {
  CameraController? controller;
  String imagePath = "";
  @override
  void initState() {
    super.initState();
    controller = CameraController(cameras![1], ResolutionPreset.max);
    controller?.initialize().then((_) {
      if (!mounted) {
        return;
      }
      setState(() {});
    });
  }
  @override
  void dispose() {
    controller?.dispose();
    super.dispose();
  }
  @override
  Widget build(BuildContext context) {
    if (!controller!.value.isInitialized) {
      return Container();
    }
    return Scaffold(
      body: SafeArea(
        child: Center(
          child: Column(
            children: [
              const SizedBox(
                height: 50,
              ),
              SizedBox(
                width: 200,
                height: 200,
                child: AspectRatio(
                  aspectRatio: controller!.value.aspectRatio,
                  child: CameraPreview(controller!),
                ),
              ),
              TextButton(
                  onPressed: () async {
                    try {
                      final image = await controller!.takePicture();
                      setState(() {
                        imagePath = image.path;
                      });
                    } catch (e) {
                      print(e);
                    }
                  },
                  child: const Text("Take Photo")),
              if (imagePath != "")
                SizedBox(
                    width: 300,
                    height: 300,
                    child: Image.file(
                      File(imagePath),
                    ))
            ],
          ),
        ),
      ),
    );
  }
}