import {Controller, Get} from "@nestjs/common";

import {Roles} from "../guards/role.metadata";

@Controller('secrets')
export class SecretsController {

  @Get()
  @Roles('ADMIN')
  getSecret(): string {
    return '42';
  }
}
