import {Schema, Prop, SchemaFactory} from "@nestjs/mongoose";
import { Document, Schema as mongooseSchema } from 'mongoose';

@Schema()
export class Pet extends Document {

  @Prop({ required: true })
  name: string;

  @Prop()
  breed: string;

  @Prop({
    type: mongooseSchema.Types.Decimal128,
    get: val => {
      console.log('getter', val);
      return val;
    },
    transform: val => {
      console.log('transform', val);
      return val ? val.toString() : val;
    },

  })
  weight: number;
}

export const PetSchema = SchemaFactory.createForClass(Pet);
