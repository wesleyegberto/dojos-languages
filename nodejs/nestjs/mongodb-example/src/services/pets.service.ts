import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';

import extractDecimalNumber from '../utils/mongo-number-decimal-extract';
import { Pet } from '../models/Pet.schema';
import { CreatePetDto } from '../dto/create-pet.dto';

@Injectable()
export class PetsService {
  constructor(@InjectModel(Pet.name) private petModel: Model<Pet>) {}

  async create(pet: CreatePetDto): Promise<Pet> {
    const createdPet = new this.petModel(pet);
    return createdPet.save();
  }

  async findById(id: string): Promise<Pet> {
    return this.petModel.findById(id);
  }

  async find(name?: string): Promise<Pet[]> {
    if (name && name.length) return await this.findByName(name);
    return await this.findAll();
  }

  async findAll(): Promise<Pet[]> {
    return this.petModel.find().exec();
  }

  async findByName(name: string): Promise<Pet[]> {
    return this.petModel.find({ name }).exec();
  }

  async calculatePetsTotalWeight(): Promise<number> {
    let result = await this.petModel
      .aggregate()
      .group({
        _id: 1,
        totalWeight: { $sum: '$weight' },
      })
      .project({
        totalWeight: '$totalWeight',
        // workaround NumberDecimal
        total: extractDecimalNumber('$totalWeight'),
      })
      // .model(PetsTotalWeightModel)
      .exec();
    if (result && result.length) {
      result = result[0];
      console.log(result.total);
    }
    return result;
  }
}
