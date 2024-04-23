import React, { useContext, useEffect, useState } from "react";
import { Row, Col, Container, Card, Image } from "react-bootstrap";
import "./Details.css";
import Cart from "./Cart";
import ProductCard from "./Cards/ProductCard";
import { Product } from "./ProductDetails";
import { useParams } from "react-router-dom";
import AuthContext from "./Context/AuthContext";

const Details = () => {
  const skateProduct = Product.filter((product) => product.type === "product");

  const { id } = useParams();
  const productDetails = Product.find((product) => product.id === id);

  const { setBooking } = useContext(AuthContext);
  const [formData, setFormData] = useState({
    selectDate: "",
    membership: "",
    selectSession: "",
    numAdmits: "",
  });

  const handleInputChange = (e) => {
    const { id, value } = e.target;
    setFormData({ ...formData, [id]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const productData = Product.find(
      (option) => option.id === formData.membership
    );

    setBooking((prevBooking) => [
      ...prevBooking,
      {
        productId: formData.membership,
        quantity: formData.numAdmits,
        data: productData,
        date: formData.selectDate,
        time: formData.selectSession,
      },
    ]);
    setFormData({
      selectDate: "",
      membership: "",
      selectSession: "",
      numAdmits: "",
    });
  };

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [id]);

  return (
    <>
      <div className=" clearfix"></div>
      <Container className="mt-5 pt-2">
        {/* detail page */}
        <Card className="b-zero">
          <Row className="align-items-center">
            <Col
              xs={12}
              md={6}
              className="d-flex align-items-center justify-content-center"
            >
              {/* <Card.Img
                src={productDetails.image}
                alt={productDetails.title}
                height={300}
                style={{ objectFit: "cover",width:'100%'}}
              /> */}
              <div
                className="d-flex justify-content-center align-content-center"
                style={{ height: "20rem" }}
              >
                <Image
                  src={productDetails.image}
                  alt="Product"
                  className=" object-fit-cover w-100"
                />
              </div>
            </Col>
            <Col xs={12} md={6} className="p-3">
              <h3>{productDetails.title}</h3>
              <h5>{productDetails.sub_title}</h5>
              <p className="p-text">{productDetails.description}</p>
              <h6>PRICE : AED {productDetails.price}</h6>
            </Col>
          </Row>
        </Card>

        <div className=" clearfix"></div>
        <div className="row ml-0 mr-0 mt-0">
          {/* skating title */}
          <Row className="align-items-center justify-content-center mb-5 px-md-5">
            <Col sm={12} md={12} lg={3}>
              <hr />
            </Col>
            <Col sm={12} md={12} lg={6}>
              <p
                className="fs-1 fw-light text-center"
                style={{ margin: "0 4px" }}
              >
                SKATING PRODUCT
              </p>
            </Col>
            <Col sm={12} md={12} lg={3}>
              <hr />
            </Col>
          </Row>

          {/* Skating product */}

          <Row className="justify-content-center m-1">
            {skateProduct.map((product) => (
              <Col
                key={product.id}
                xs={12}
                sm={6}
                md={4}
                lg={3}
                className="d-flex justify-content-center align-items-center"
              >
                <div style={{ width: "260px", padding: "2%" }}>
                  <ProductCard
                    image={product.image}
                    name={product.title}
                    id={product.id}
                  />
                </div>
              </Col>
            ))}
          </Row>
        </div>

        {/* Booking Form */}

        <div className="booking-main">
          <div className="booking-body">
            <h5 className="title-bg">BOOK NOW</h5>
            <form className="row g-4" onSubmit={handleSubmit}>
              <div className="col-md-3">
                <input
                  type="date"
                  id="selectDate"
                  className="p-2"
                  value={formData.selectDate}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <div className="col-md-3">
                <select
                  id="membership"
                  className="p-2"
                  style={{ height: "42px" }}
                  value={formData.membership}
                  onChange={handleInputChange}
                >
                  <option>Select Membership</option>
                  {Product.filter((product) => product.type !== "product").map(
                    (option) => (
                      <option key={option.id} value={option.id}>
                        {option.title}-AED{option.price}
                      </option>
                    )
                  )}
                </select>
              </div>
              <div className="col-md-3">
                <select
                  id="selectSession"
                  className="p-2"
                  style={{ height: "42px" }}
                  value={formData.selectSession}
                  onChange={handleInputChange}
                >
                  <option>Select Session</option>
                  <option value="session1">11:00 AM - 12:00 PM</option>
                  <option value="session2">12:30 PM - 01:30 PM</option>
                  <option value="session3">2:00 PM - 03:00 PM</option>
                  <option value="session4">03:30 PM - 04:30 PM</option>
                  <option value="session5">05:00 AM - 06:00 PM</option>
                </select>
              </div>
              <div className="col-md-3">
                <input
                  type="number"
                  id="numAdmits"
                  className="p-2"
                  min={1}
                  required
                  value={formData.numAdmits}
                  onChange={handleInputChange}
                  placeholder="Number of Admissions"
                />
              </div>
              <div className="col-md-12 text-center">
                <button className="form-button" type="submit">
                  BOOK NOW
                </button>
              </div>
            </form>
          </div>
        </div>
      </Container>

      {/* Cart Page */}
      <div className="pt-4">
        <Cart />
      </div>
    </>
  );
};

export default Details;
