import { Injectable, NestMiddleware } from '@nestjs/common';

@Injectable()
export class RequestLoggerMiddleware implements NestMiddleware {
  use(req: any, res: any, next: Function) {
    console.log('Incoming - Request', req.headers);
    next();
    console.log(`Outcoming - Response - ${res.statusCode}`);
  }
}
