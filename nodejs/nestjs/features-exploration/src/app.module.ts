import {Module, NestModule, MiddlewareConsumer, RequestMethod} from '@nestjs/common';
import {APP_FILTER, APP_GUARD} from '@nestjs/core';

import {AppController} from './controllers/app.controller';
import {AppService} from './services/app.service';
import {RequestLoggerMiddleware} from './middlewares/request-logger.middleware';
import {GenericExceptionFilter} from './exceptionfilter/generic-exception.filter';
import {PetsController} from './controllers/pets.controller';
import {PetsService} from './services/pets.service';
import {TokenGuard} from './guards/token.guard';
import {SecretsController} from './controllers/secret.controller';

@Module({
  imports: [],
  controllers: [
    AppController,
    SecretsController,
    PetsController,
  ],
  providers: [
    {
      provide: APP_GUARD,
      useClass: TokenGuard
    },
    {
      provide: APP_FILTER,
      useClass: GenericExceptionFilter
    },
    AppService,
    PetsService,
  ]
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer
      .apply(RequestLoggerMiddleware)
      .forRoutes({path: '**', method: RequestMethod.ALL})
  }
}
