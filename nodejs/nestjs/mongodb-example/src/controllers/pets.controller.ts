import {Controller, Get, Post, Body, Query, Param} from "@nestjs/common";

import {PetsService} from "../services/pets.service";
import {Pet} from "src/models/Pet.schema";
import {CreatePetDto} from "src/dto/create-pet.dto";

@Controller("pets")
export class PetsController {
  constructor(private petsService: PetsService) {}

  @Get()
  async findAll(@Query('name') name?: string): Promise<Pet[]> {
    return await this.petsService.find(name);
  }

  @Post()
  async create(@Body() pet: CreatePetDto): Promise<Pet> {
    return await this.petsService.create(pet);
  }

  @Get(":id")
  async findById(@Param('id') id: string): Promise<Pet> {
    return await this.petsService.findById(id);
  }

  @Get("weights/total")
  async calculatePetsTotalWeight(): Promise<number> {
    return await this.petsService.calculatePetsTotalWeight();
  }
}
