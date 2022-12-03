import {Injectable} from "@nestjs/common";

import {Pet} from "src/entities/pet";

@Injectable()
export class PetsService {
  pets: Array<Pet> = [];

  getAll(): Array<Pet> {
    return [...this.pets];
  }

  save(pet: Pet): Pet {
    if (!pet) return null;
    pet.id = this.pets.length + 1;
    this.pets.push(pet);
    return pet;
  }
}
