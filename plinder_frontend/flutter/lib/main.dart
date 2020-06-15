import 'package:flutter/material.dart';

import 'package:bloc/bloc.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:plinderfrontend/repository/user_repository.dart';

import 'package:plinderfrontend/bloc/authentication_bloc.dart';
import 'package:plinderfrontend/splash/splash.dart';
import 'package:plinderfrontend/login/login_page.dart';
import 'package:plinderfrontend/home/home.dart';
import 'package:plinderfrontend/common/common.dart';
import 'package:plinderfrontend/theme.dart';

class SimpleBlocDelegate extends BlocDelegate {
  @override
  void onEvent(Bloc bloc, Object event) {
    super.onEvent(bloc, event);
    print(event);
  }

  @override
  void onTransition(Bloc bloc, Transition transition) {
    super.onTransition(bloc, transition);
    print (transition);
  }

  @override
  void onError(Bloc bloc, Object error, StackTrace stacktrace) {
    super.onError(bloc, error, stacktrace);
  }
}

void main() {
  BlocSupervisor.delegate = SimpleBlocDelegate();
  final userRepository = UserRepository();

  runApp(
    BlocProvider<AuthenticationBloc>(
      create: (context) {
        return AuthenticationBloc(
          userRepository: userRepository
        )..add(AppStarted());
      },
      child: App(userRepository: userRepository),
    )
  );
}

class App extends StatelessWidget {
  final UserRepository userRepository;

  App({Key key, @required this.userRepository}) : super(key: key);

  @override
  Widget build (BuildContext context) {
    return MaterialApp(
      title:'Plinder',
      theme: buildThemeData(),
      home: BlocBuilder<AuthenticationBloc, AuthenticationState>(
        builder: (context, state) {
          if (state is AuthenticationUnintialized) {
            return SplashPage();
          }
          if (state is AuthenticationAuthenticated) {
            return HomePage();
          }
          if (state is AuthenticationUnauthenticated) {
            return LoginPage(userRepository: userRepository,);
          }
          if (state is AuthenticationLoading) {
            return LoadingIndicator();
          }
        },
      ),
    );
  }
}


/* import 'package:flutter/material.dart';
//import 'package:plinderfrontend/_routing/routes.dart';
//import 'package:plinderfrontend/_routing/router.dart' as router;
import 'package:plinderfrontend/theme.dart';

class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Plinder',
      debugShowCheckedModeBanner: false,
      theme: buildThemeData(),
      //onGenerateRoute: router.generateRoute,
      //initialRoute: landingViewRoute,
    );
  }
} */

/* 
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_social/app.dart';
import 'package:flutter_social/utils/colors.dart';

void main() {
  SystemChrome.setSystemUIOverlayStyle(SystemUiOverlayStyle(
    statusBarColor: primaryDark
  ));
  runApp(App());
} */
