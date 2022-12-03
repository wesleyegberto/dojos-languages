import {APP_GUARD} from "@nestjs/core";
import {INestApplication} from "@nestjs/common";
import {Test} from "@nestjs/testing";

import * as request from 'supertest';

import {TokenGuard} from "../guards/token.guard";
import {SecretsController} from "./secret.controller";

describe('Secret', () => {
  let app: INestApplication;

  beforeAll(async () => {
    const moduleRef = await Test.createTestingModule({
      controllers: [
        SecretsController,
      ],
      providers: [
        {
          provide: APP_GUARD,
          useClass: TokenGuard
        }
      ]
    }).compile();

    app = moduleRef.createNestApplication();
    await app.init();
  });

  afterAll(async () => {
    await app.close();
  });

  it('should reject a request secret without token', () => {
    return request(app.getHttpServer())
      .get('/secrets')
      .expect(403);
  });
});
