import 'package:flutter/material.dart';
import 'dart:ui';

/*const primaryColor = const Color(0xFFfbab66);
const primaryLight = const Color(0xFFFF9F59);
const primaryDark = const Color(0xFFFF9F59);

const secondaryColor = const Color(0xFFFF9F59);
const secondaryLight = const Color(0xFFFF9F59);
const secondaryDark = const Color(0xFFFF9F59);

const Color gradientStart = const Color(0xFFfbab66);
const Color gradientEnd = const Color(0xFFf7418c);*/

const primaryColor = const Color(0xFF395F40);
const primaryLight = const Color(0xFFA3B4A8);
const primaryDark = const Color(0xFF0A3718);

const secondaryColor = const Color(0xFF5F3958);
const secondaryLight = const Color(0xFFE5B8DB);
const secondaryDark = const Color(0xFF472341);

const Color gradientStart = const Color(0xFF0A3718);
const Color gradientEnd = const Color(0xFFD5FFDB);

const primaryGradient = const LinearGradient(
  colors: const [gradientStart, gradientEnd],
  stops: const [0.0, 1.0],
  begin: Alignment.topCenter,
  end: Alignment.bottomCenter,
);

const chatBubbleGradient = const LinearGradient(
  colors: const [Color(0xFF0A3718), Color(0xFFD5FFDB)],
  begin: Alignment.topRight,
  end: Alignment.bottomLeft,
);

const chatBubbleGradient2 = const LinearGradient(
  colors: const [Color(0xFFf4e3e3), Color(0xFFf4e3e3)],
  begin: Alignment.topRight,
  end: Alignment.bottomLeft,
);
