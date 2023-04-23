import { Injectable } from '@angular/core';
import {
    HttpEvent,
    HttpInterceptor,
    HttpHandler,
    HttpRequest,
    HttpErrorResponse,
} from '@angular/common/http';

import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';


@Injectable()
export class ErrorInterceptor implements HttpInterceptor {
    constructor() {}

    intercept(
        req: HttpRequest<any>,
        next: HttpHandler,
    ): Observable<HttpEvent<any>> {
        return next.handle(req).pipe(
            tap(
                () => {},
                err => {
                    if (err instanceof HttpErrorResponse) {
                        if (!navigator.onLine) {
                            return;
                        }
                        const response = err as HttpErrorResponse;
                        if (response.status === 500) {
                        } else if (response.status === 0) {
                        }
                    }
                },
            ),
        );
    }
}
