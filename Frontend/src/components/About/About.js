import React, { useEffect, useState } from "react";
import Card from "react-bootstrap/Card";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import AboutCarousel from "./AboutCarousel";
import image1 from "../../images/image1.jpg";
import image2 from "../../images/image2.jpg";
import image3 from "../../images/image3.jpg";
import image4 from "../../images/dance5.jpg";
import Preloader from "../Preloader/Preloader";

const imageUrls = [image1, image2, image3];

const About = () => {
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    setTimeout(() => {
      setIsLoading(false);
    }, 700);
  }, []);

  return (
    <>
      {isLoading ? (
        <Preloader />
      ) : (
        <div>
          <div style={{ width: "100%" }}>
            <img
              src={image4}
              style={{ width: "100%", objectFit: "cover", maxHeight: "50vh" }}
              alt="Skate ground"
              loading="lazy"
            />
          </div>

          <div className="p-lg-5" style={{ marginTop: "-10%" ,backgroundColor:'#F2F2F2'}}>
            {/* About Carousel */}
            <Card>
              <Card.Body>
                <AboutCarousel />
              </Card.Body>
            </Card>
          </div>
            {/* Events */}
          <div style={{ backgroundColor: "#F2F2F2", padding: "4%" }}>
            <Row className="justify-content-center text-center">
              <Row className="align-items-center p-5 ">
                <Col>
                  <hr />
                </Col>
                <Col xs="auto">
                  <p className="fs-2 fw-light" style={{ margin: "0 4px" }}>
                    EVENTS
                  </p>
                </Col>
                <Col>
                  <hr />
                </Col>
              </Row>

              {imageUrls.map((imageUrl, index) => (
                <Col key={imageUrl} xs={12} sm={6} md={4} lg={3}>
                  <Card
                    style={{
                      maxWidth: "400px",
                      maxHeight: "500px",
                      margin: "2%",
                    }}
                  >
                    <img
                      variant="top"
                      src={imageUrl}
                      style={{ height: "250px", objectFit: "cover" }}
                      alt={`Event ${index + 1}`}
                    />
                    <Card.Body>
                      <Card.Title>Event {index + 1}</Card.Title>
                    </Card.Body>
                  </Card>
                </Col>
              ))}
            </Row>
          </div>
        </div>
      )}
    </>
  );
};

export default About;
