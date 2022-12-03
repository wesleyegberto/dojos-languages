import { Injectable } from '@nestjs/common';
import { Context, SQSEvent } from 'aws-lambda';

@Injectable()
export class AppService {
  public processMessage(event: SQSEvent, context: Context) {
    console.log('Event', context.awsRequestId);

    if (!event.Records || !event.Records.length) {
      return;
    }

    event.Records.forEach(record => {
      console.log('Processing message', record);
    });
  }
}
