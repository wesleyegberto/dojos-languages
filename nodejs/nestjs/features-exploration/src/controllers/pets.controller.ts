import {Controller, Get, Post, Body, HttpStatus, HttpCode} from "@nestjs/common";

import {PetsService} from "../services/pets.service";
import {Pet} from "../entities/pet";
import {FieldsNotNullPipe} from "../pipes/fields-not-null.pipe";

@Controller("pets")
export class PetsController {
  constructor(private petsService: PetsService) {}

  @Get()
  getAll(): Array<Pet> {
    return this.petsService.getAll();
  }

  @Post()
  @HttpCode(HttpStatus.CREATED)
  save(@Body(FieldsNotNullPipe) pet: Pet): any {
    return this.petsService.save(pet);
  }
}
