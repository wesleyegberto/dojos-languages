import {Reflector} from "@nestjs/core";
import {CanActivate, ExecutionContext, Injectable} from "@nestjs/common";

@Injectable()
export class TokenGuard implements CanActivate {
  constructor(private reflector: Reflector) {}

  canActivate(context: ExecutionContext): boolean {
    const roles = this.reflector.get<string[]>('roles', context.getHandler());
    if (!roles) {
      return true;
    }

    console.log('Guard - verifying if roles is in request', roles);
    const request = context.switchToHttp().getRequest();
    const user = request.user;
    if (!user) {
      return false;
    }
    return this.matchRoles(roles, user.roles);
  }

  matchRoles(roles: string[], userRoles: string[] | null): boolean {
    if (!userRoles)
      return false;

    return !!roles.find(r => userRoles.findIndex(ur => ur === r) >= 0);
  }
}
