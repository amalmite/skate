import React from "react";
import { Card, CardBody, Row, Col, CardFooter } from "react-bootstrap";

const FavoriteCard = ({ image, month, price, title, description }) => {


  return (
    <>
    {/* Favorite card */}
      <Card className="b-zero">
        <img
          variant="top"
          src={image}
          alt="Favorite"
          height={260}
          style={{ objectFit: "cover" }}
        />
        <CardBody>
        <Row className="p-3">
            <Col xs={12} md={6}>
              <p className="fs-6 fw-normal">{title}</p>
            </Col>

            <Col xs={12} md={6}>
              <p className="fs-6">
                {description.length > 56
                  ? `${description.slice(0, 56)}...`
                  : description}
              </p>
            </Col>
          </Row>
        </CardBody>
        <CardFooter className="p-0">
          <Row
            noGutters
            className="text-white text-center align-items-center w-100 m-0"
          >
            <Col
              md={8}
              sm={6}
              xs={12}
              className="d-flex justify-content-center justify-content-md-start align-items-center py-3"
              style={{ backgroundColor: "#1ca7c8" }}
            >
              <p className="mb-0">DURATION: {month}</p>
            </Col>
            <Col
              md={4}
              sm={6}
              xs={12}
        
              className="d-flex justify-content-center justify-content-md-start align-items-center py-3"
              style={{ backgroundColor: "#1d98b9" }}
            >
              <p className="mb-0 fw-bold">AED {price}</p>
            </Col>
          </Row>
        </CardFooter>
      </Card>
    </>
  );
};

export default FavoriteCard;
