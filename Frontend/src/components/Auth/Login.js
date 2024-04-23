import React, { useContext } from "react";
import { Container, Row, Col, Button, Form, Image } from "react-bootstrap";
import image1 from "../../images/register.png";
import logo from "../../images/logo.png";
import AuthContext from "../Context/AuthContext";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function Login() {
  const { login } = useContext(AuthContext);

  return (
    <Container>
      <ToastContainer />
      <Row className="justify-content-center">
        <Col md={6} className="d-flex justify-content-center">
          <Image
            src={image1}
            alt="login form"
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
              padding: "7%",
            }}
          />
        </Col>
        <Col md={6} style={{marginTop:'15%'}}>
          <div className="d-flex flex-column justify-content-center">
            <div className="d-flex flex-row justify-content-center align-items-center mt-2">
              <img
                alt=""
                src={logo}
                width="100"
                height="70"
                className="d-inline-block align-top"
              />
            </div>
            <div className="d-flex justify-content-center align-items-center">
              <h5 className="fw-normal my-4">Sign up your account</h5>
            </div>
            <Form onSubmit={login}>
              <Form.Group className="mb-4">
                <Form.Control
                  type="text"
                  name="username"
                  id="username"
                  placeholder="Email address"
                />
              </Form.Group>
              <Form.Group className="mb-4">
                <Form.Control
                  type="password"
                  name="password"
                  id="password"
                  placeholder="Password"
                />
              </Form.Group>

              <Button
                className="mb-4 w-100"
                style={{ backgroundColor: "#0367A6" }}
                type="submit"
              >
                Login
              </Button>
            </Form>
            <p className="" style={{ color: "#393f81" }}>
              Don't have an account?{" "}
              <a href="/register" style={{ color: "#393f81" }}>
                register here
              </a>
            </p>
              <a href="/forgotpassword" style={{ color: "#393f81" }}>
              Forgot Password?
                
              </a>
          </div>
        </Col>
      </Row>
    </Container>
  );
}

export default Login;
