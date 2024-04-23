import React from "react";
import { Container, Row, Col } from "react-bootstrap";

export default function Footer() {
  return (
    <footer className="bg-light text-center text-lg-start text-muted">
      <section className="mt-5 pt-3">
        <Container className="text-center text-md-start mt-5">
          <Row className="mt-3">
            <Col md="2" lg="4" xl="3" className="mx-auto mb-4">
              <h6 className="text-uppercase fw-bold mb-4">Skate Gate</h6>
              <p>
                Skating is a dynamic and exhilarating activity that involves
                gliding across a smooth surface on specialized footwear,
                typically with wheels (inline skating or roller skating) or
                blades (ice skating)
              </p>
            </Col>
            {/* 
            <Col md="2" lg="2" xl="2" className='mx-auto mb-4'>
              <h6 className='text-uppercase fw-bold mb-4'>Services</h6>
              <p>
                <a href='/' className='text-reset'>
                  Ice Skate
                </a>
              </p>
              <p>
                <a href='/' className='text-reset'>
                Coaching
                </a>
              </p>
              <p>
                <a href='/' className='text-reset'>
                  Ice Hockey
                </a>
              </p>
              <p>
                <a href='/' className='text-reset'>
                Ice Dance 
                </a>
              </p>
            </Col> */}

            <Col md="4" lg="3" xl="3" className="mx-auto mb-md-0 mb-4">
              <h6 className="text-uppercase fw-bold mb-4">Contact</h6>
              <p>Ajman</p>
              <p>skategate@example.com</p>
            </Col>
          </Row>
        </Container>
      </section>

      <div
        className="text-center p-4"
        style={{ backgroundColor: "rgba(0, 0, 0, 0.05)" }}
      >
        © 2024 <a href="https://mitesolutions.com">Mite Solutions LLC</a>
      </div>
    </footer>
  );
}
