import React from "react";
import { Route } from "react-router-dom";
import Hoc from "./hoc/hoc";

import Login from "./containers/Login";
import Signup from "./containers/Signup";

const BaseRouter = () => (
  <Hoc>
    <Route exact path="/login/" component={Login} />
    <Route exact path="/signup/" component={Signup} />
  </Hoc>
);

export default BaseRouter;
