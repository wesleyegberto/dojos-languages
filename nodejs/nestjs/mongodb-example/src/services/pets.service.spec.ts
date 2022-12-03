import { Test, TestingModule } from '@nestjs/testing';
import { PetsService } from './pets.service';



describe('PetsService', () => {
  let service: PetsService;
  

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [PetsService],
      providers: [
        
      ],
    }).compile();

    service = module.get(PetsService);
    
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });

  describe('create', () => {
    it('should', () => {

    });
  });

  describe('findById', () => {
    it('should', () => {

    });
  });

  describe('find', () => {
    it('should', () => {

    });
  });

  describe('findAll', () => {
    it('should', () => {

    });
  });

  describe('findByName', () => {
    it('should', () => {

    });
  });

  describe('calculatePetsTotalWeight', () => {
    it('should', () => {

    });
  });
});