import { Controller, Get, HttpCode, Header } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  @HttpCode(200)
  @Header('Content-type', 'text/html')
  getHello(): string {
    return this.appService.getHello();
  }
}
