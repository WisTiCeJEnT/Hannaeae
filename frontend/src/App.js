import React, { Component } from "react";
import "./App.css";
import {
  Form,
  Button,
  Row,
  Col,
  Spinner,
  Dropdown,
  DropdownButton
} from "react-bootstrap";

class MyForm extends React.Component {
  constructor() {
    super();
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit = event => {
    event.preventDefault();
    const data = {
      req_msg: event.target[0].value,
      res_msg: event.target[1].value,
      category: event.target[2].value,
      mode: parseInt(event.target[3].value)
    };
    console.log(data);
    fetch("https://hannaeae.herokuapp.com/add", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });
  };

  render() {
    return (
      <Row className="show-grid" float="center">
        <Col xs={12} xsOffset={6}>
          <Spinner name="folding-cube" />
          <Form onSubmit={this.handleSubmit}>
            <Form.Group as={Row} controlId="formHorizontalEmail">
              <Form.Label column sm={2}>
                คำถาม
              </Form.Label>
              <Col sm={10}>
                <Form.Control
                  id="question"
                  type="text"
                  placeholder="ใส่คำถาม"
                />
              </Col>
            </Form.Group>

            <Form.Group as={Row} controlId="formHorizontalEmail">
              <Form.Label column sm={2}>
                คำตอบ
              </Form.Label>
              <Col sm={10}>
                <Form.Control id="answer" type="text" placeholder="ใส่คำตอบ" />
              </Col>
            </Form.Group>
            <Form.Group as={Row} controlId="formHorizontalEmail">
              <Form.Label column sm={2}>
                หมวด
              </Form.Label>
              <Col sm={10}>
                <Form.Control id="category" type="int" placeholder="ใส่หมวด" />
              </Col>
            </Form.Group>
            <Form.Group as={Row}>
              <Form.Label as="legend" column sm={2}>
                หมวด
              </Form.Label>
              <Col sm={10}>
                <Form.Control as="select">
                  <option value={1}>บอทตอบเราถาม</option>
                  <option value={2}>บอทถามเราตอบ</option>
                  <option value={3}>คำผวน</option>
                </Form.Control>
              </Col>
            </Form.Group>

            <Col sm={{ span: 10, offset: 2 }}>
              <Button type="submit">ส่ง!!!</Button>
            </Col>
          </Form>
        </Col>
      </Row>
    );
  }
}

export default MyForm;
