import { Test, TestingModule } from '@nestjs/testing';
import {HttpException} from '@nestjs/common';

import { AppController } from './app.controller';
import { AppService } from '../services/app.service';

describe('AppController', () => {
  let appController: AppController;

  beforeEach(async () => {
    const app: TestingModule = await Test.createTestingModule({
      controllers: [AppController],
      providers: [AppService],
    }).compile(); // bootstraps the module with its dependencies

    appController = app.get<AppController>(AppController);
  });

  describe('root', () => {
    it('should return "Hello World!"', () => {
      expect(appController.getHello())
        .toBe('Hello World!');
    });

    it('should throw an error', () => {
      expect(appController.throwError)
        .toThrow(HttpException);
    });
  });
});
