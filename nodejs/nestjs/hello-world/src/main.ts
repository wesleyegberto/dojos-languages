/**
 * Entry file of the application which uses the core function `NestFactory`
 * to create a Nest application.
 */
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  // `create` returns an instance which implements INestApplication
  const app = await NestFactory.create(AppModule);

  // to access platform-specific APIs
  // const app = await NestFactory.create<NestExpressApplication>(AppModule);

  await app.listen(3000);
}
bootstrap();
