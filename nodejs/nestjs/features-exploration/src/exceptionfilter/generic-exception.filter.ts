import {ExceptionFilter, ArgumentsHost, Catch, HttpStatus, HttpException} from "@nestjs/common";
import {Request, Response} from "express";

// will catch any exception
@Catch()
export class GenericExceptionFilter implements ExceptionFilter {
  catch(exception: any, host: ArgumentsHost) {
    const httpContext = host.switchToHttp();
    // when using express we can reference it
    const request = httpContext.getRequest<Request>();
    const response = httpContext.getResponse<Response>();

    console.log(`${request.ip} - ${request.path} - An error has occurred: ${exception.message}`);

    let status = HttpStatus.INTERNAL_SERVER_ERROR;

    if (exception instanceof HttpException) {
      status = exception.getStatus();
    }

    response.status(status)
      .json({
        statusCode: status,
        timestamp: new Date().toISOString(),
        path: request.path,
        error: exception.message
      });
  }
}
