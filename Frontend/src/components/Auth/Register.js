import React, { useState } from "react";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

import { Container, Row, Col, Button, Form, Image } from "react-bootstrap";
import image1 from "../../images/register.png";
import logo from "../../images/logo.png";
import axiosInstance from "../utils/axiosIntance";
import { useNavigate } from "react-router-dom";

function Register() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    email: "",
    username: "",
    first_name: "",
    last_name: "",
    password: "",
    password2: "",
    phone_number: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axiosInstance.post(
        "api/user/register/",
        formData,
        {}
      );
      if (response.status === 201) {
        toast.success("OTP sent successfully", {
          onClose: () => {
            navigate("/otp");
          },
        });
      } else {
        toast.error("Failed to send OTP");
      }
    } catch (error) {
      console.error(error);
      if (error.response) {
        const statusCode = error.response.status;
        if (statusCode === 400) {
          Object.entries(error.response.data).forEach(([key, value]) =>
            toast.error(`${key}: ${value[0]}`)
          );
        } else if (statusCode === 401) {
          toast.error(error.response.data.detail);
        } else {
          toast.error("An unexpected error occurred. Please try again.");
        }
      } else {
        toast.error("An unexpected error occurred. Please try again.");
      }
    }
  };

  return (
    <Container>
      <ToastContainer />
      <Row className="justify-content-center">
        <Col md={6} className="d-flex justify-content-center">
          <Image
            src={image1}
            alt="Register form"
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
              padding: "7%",
            }}
          />
        </Col>
        <Col md={6} className="p-4">
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
            <Form onSubmit={handleSubmit}>
              <Form.Group className="mb-4 ">
                <Form.Control
                  type="email"
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                  placeholder="Email address"
                />
              </Form.Group>
              <Form.Group className="mb-4">
                <Form.Control
                  type="text"
                  name="username"
                  value={formData.username}
                  onChange={handleChange}
                  placeholder="Username"
                />
              </Form.Group>
              <Form.Group className="mb-4">
                <Form.Control
                  type="text"
                  name="first_name"
                  value={formData.first_name}
                  onChange={handleChange}
                  placeholder="First Name"
                />
              </Form.Group>
              <Form.Group className="mb-4">
                <Form.Control
                  type="text"
                  name="last_name"
                  value={formData.last_name}
                  onChange={handleChange}
                  placeholder="Last Name"
                />
              </Form.Group>
              <Form.Group className="mb-4">
                <Form.Control
                  type="text"
                  name="phone_number"
                  value={formData.phone_number}
                  onChange={handleChange}
                  placeholder="Phone Number"
                />
              </Form.Group>

              <Form.Group className="mb-4">
                <Form.Control
                  type="password"
                  name="password"
                  value={formData.password}
                  onChange={handleChange}
                  placeholder="Password"
                />
              </Form.Group>
              <Form.Group className="mb-4">
                <Form.Control
                  type="password"
                  name="password2"
                  value={formData.password2}
                  onChange={handleChange}
                  placeholder="Confirm Password"
                />
              </Form.Group>

              <Button
                className="mb-4 w-100"
                style={{ backgroundColor: "#0367A6" }}
                type="submit"
              >
                Register
              </Button>
            </Form>
            <p className="" style={{ color: "#393f81" }}>
               already have an account?{" "}
              <a href="/login" style={{ color: "#393f81" }}>
                login here
              </a>
            </p>
          </div>
        </Col>
      </Row>
    </Container>
  );
}

export default Register;
