import { INestApplicationContext} from '@nestjs/common';
import { NestFactory } from '@nestjs/core';
import { SQSHandler } from 'aws-lambda';
import { AppModule } from './app.module';
import {AppService} from './app.service';

let cachedApp: INestApplicationContext;

async function initApp(): Promise<INestApplicationContext> {
  if (cachedApp) {
    console.log('Using cached context');
    return cachedApp;
  }

  console.log('Starting new context');
  cachedApp = await NestFactory.createApplicationContext(AppModule);
  cachedApp.init();
  return cachedApp;
}

export const handler: SQSHandler = async (event, context) => {
  console.log('Evento safado que vai bugar!')
  console.log(event, context);

  const app = await initApp();
  const service = app.get(AppService);
  service.processMessage(event, context);
};

// handler(null, null, null);