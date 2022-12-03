import { PetsController } from './pets.controller';
import {PetsService} from '../services/pets.service';
import {Pet} from '../entities/pet';

describe('AppController', () => {
  let petsCtrl: PetsController;

  let mockedPetsService: PetsService;

  beforeEach(async () => {
    mockedPetsService = {
      getAll: () => [],
      save: _ => null
    } as PetsService;

    petsCtrl = new PetsController(mockedPetsService);
  });

  describe('Pets', () => {
    it('should return a list of pets', () => {
      spyOn(mockedPetsService, 'getAll').and.returnValue([ { id: 42, name: 'Marley', breed: 'Shitzu' } ]);
      const pets = petsCtrl.getAll();

      expect(pets).toBeTruthy();
      expect(pets.length).toBe(1);
      expect(pets[0]).toEqual({
        id: 42,
        name: 'Marley',
        breed: 'Shitzu'
      });
    });

    it('should save a given pet', () => {
      const expectedPet = new Pet('Bob', 'Unknown');
      expectedPet.id = 42;
      spyOn(mockedPetsService, 'save').and.returnValue(expectedPet);

      const newPet = new Pet('Bob', 'Unknown');

      const actualPet = petsCtrl.save(newPet);

      expect(actualPet).toEqual(expectedPet);
    });
  });
});
