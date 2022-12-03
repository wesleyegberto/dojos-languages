import { Controller, Get, HttpException, HttpStatus } from '@nestjs/common';

import { AppService } from '../services/app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }

  @Get("error")
  throwError(): void {
    throw new HttpException('An error has been given to you', HttpStatus.INTERNAL_SERVER_ERROR);
  }
}
