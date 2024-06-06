import 'package:flutter/material.dart';

class SplashScreen extends StatefulWidget {
  final Duration duration;
  final Widget navigateAfterDuration;

  SplashScreen({
    required this.duration,
    required this.navigateAfterDuration,
  });

  @override
  _SplashScreenState createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();
    _navigateToNextScreen();
  }

  _navigateToNextScreen() async {
    await Future.delayed(widget.duration);
    Navigator.of(context).pushReplacement(
      MaterialPageRoute(
        builder: (context) => widget.navigateAfterDuration,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        fit: StackFit.expand,
        children: <Widget>[
          Positioned.fill(
            child: Center(
              child: Image.asset(
                'assets/logo.gif',
                width: 200,
              ),
            ),
          ),
        ],
      ),
    );
  }
}
