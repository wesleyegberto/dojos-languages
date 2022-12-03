import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { Schema } from 'mongoose';
import * as castAggregation from 'mongoose-cast-aggregation';

import { Pet, PetSchema } from './models/Pet.schema';
import { PetsController } from './controllers/pets.controller';
import { PetsService } from './services/pets.service';

@Module({
  imports: [
    MongooseModule.forRoot('mongodb://root:supersecret@localhost/sample'),
    // register the model in current scope
    // MongooseModule.forFeature([
    //   {name: Pet.name, schema: PetSchema}
    // ]),
    MongooseModule.forFeatureAsync([
      {
        name: Pet.name,
        useFactory: (): Schema<any> => {
          const schema = PetSchema;
          schema.plugin(castAggregation);
          schema.pre('save', () => console.log('About to write a Pet'));
          schema.post('save', () => console.log('A Pet was written'));
          schema.pre('aggregate', () => {
            console.log('About to execute Pet aggregation');
          });
          schema.post('aggregate', result => {
            console.log('Pet aggregation was executed', result);
          });
          return schema;
        },
      },
    ]),
  ],
  controllers: [PetsController],
  providers: [PetsService],
})
export class AppModule {}
