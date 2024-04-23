import React from "react";
import Carousel from "react-bootstrap/Carousel";
import Image from "react-bootstrap/Image";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import image1 from "../../images/men1.webp";
import image2 from "../../images/men2.webp";

const AboutCarousel = () => {
  return (
    <Carousel controls fade >
      {[
        { id: "due", name: "Due", src: image1 },
        { id: "jone", name: "Jone", src: image2 },
      ].map((person) => (
        <Carousel.Item key={person.id} className="text-center" >
          <Image
            src={person.src}
            alt={`${person.name} avatar`}
            className="shadow-1-strong mb-4 rounded-circle"
            style={{ width: "150px", height: "150px", objectFit: "cover" }}
          />
          {/* <LazyLoadImage
                    src={person.src}
                    alt={`${person.name} avatar`}
                    className="shadow-1-strong mb-4 rounded-circle"
                    style={{ width: "150px", height: "150px", objectFit: 'cover' }}
                    loading='lazy'
                    effect='blur'
                /> */}
          <Row className="justify-content-center">
            <Col lg="8">
              <h5 className="mb-3">{person.name}</h5>
              <p>Founder</p>
              <p className="text-muted">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus
                et deleniti nesciunt sint eligendi reprehenderit reiciendis,
                quibusdam illo, beatae quia fugit consequatur laudantium velit
                magnam error. Consectetur distinctio fugit doloremque.
              </p>
            </Col>
          </Row>
        </Carousel.Item>
      ))}
    </Carousel>
  );
};
export default AboutCarousel;
