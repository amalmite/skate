import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import ItemCard from "../Cards/ItemCard";
import { Product } from "../ProductDetails";

const MemberShip = () => {
  const membershipProduct = Product.filter(
    (product) => product.type === "membership"
  );

  return (
    <div
      style={{
        backgroundColor: "white",
        display: "flex",
        justifyContent: "center",
        alignItems:'center',
        padding:'5%'
      }}
    >
      <Container className="p-md-4">
        <Row className="align-items-center justify-content-center mb-5 px-md-5">
          <Col sm={12} md={12} lg={3}>
            <hr />
          </Col>
          <Col sm={12} md={12} lg={6}>
            <p className="fs-1 fw-light text-center" style={{ margin: "0 4px" }}>
              MEMBERSHIP
            </p>
          </Col>
          <Col sm={12} md={12} lg={3}>
            <hr />
          </Col>
        </Row>

        {/* Membsership cards */}

        <Row className="justify-content-center px-md-5 p-sm-2">
          {membershipProduct.map((product) => (
            <Col key={product.id} xs={12} sm={6} md={4} lg={3} className="d-flex justify-content-center">
              <div style={{ width: "260px" ,padding:'3%' }}>
                <ItemCard
                  image={product.image}
                  ft="BOOK NOW"
                  title={product.title}
                  id={product.id}
                />
              </div>
            </Col>
          ))}
        </Row>

        <div className="my-5">
          <p className="text-center" style={{fontFamily:'inh'}}>
            Discover the thrill of gliding across the smooth, glistening surface
            of our state-of-the-art ice rink at SKATE GATE. Nestled in the heart
            of Sharjah, our facility offers an exhilarating and unforgettable
            experience for ice skating enthusiasts of all ages and skill levels.
          </p>
        </div>
      </Container>
    </div>
  );
};

export default MemberShip;
