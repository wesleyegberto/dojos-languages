import {Injectable, PipeTransform, ArgumentMetadata, BadRequestException} from "@nestjs/common";
import { plainToClass } from 'class-transformer';

@Injectable()
export class FieldsNotNullPipe implements PipeTransform {
  transform(value: any, metadata: ArgumentMetadata) {
    console.log(`FieldsNotNullPipe - ${metadata.metatype} - Validating payload`, value);

    if (!value) {
      throw new BadRequestException('Not allowed emtpy payload');
    }

    const object = plainToClass(metadata.metatype, value);
    console.log(object);

    const fieldWithNullValue = Object.keys(object)
      .find(f => !value[f]);

    if (fieldWithNullValue) {
      throw new BadRequestException(`Not allowed null values, please, verify the field '${fieldWithNullValue}'`);
    }

    return value;
  }
}
