import { Injectable } from "@angular/core";
import { Product } from "../interfaces/product.interface";
import {HttpClient, HttpParameterCodec, HttpParams,} from '@angular/common/http';
import { Observable } from "rxjs";


export class HttpQueryEncoderCodec implements HttpParameterCodec {
  encodeKey(k: string): string {
      return encodeURIComponent(k);
  }

  encodeValue(v: string): string {
      return encodeURIComponent(v);
  }

  decodeKey(k: string): string {
      return decodeURIComponent(k);
  }

  decodeValue(v: string): string {
      return decodeURIComponent(v);
  }
}


@Injectable()
export class ApiService {
  URL_PATH = 'http://localhost:8000/api';

  products = {
    create: (product: Partial<Product>) => this.post<any>(`/products/`, product),
    update: (product: Partial<Product>) => this.patch<any>(`/products/${product.id}`, product),
    list: (filters?: {[key: string]: string }, limit?: number, offset?: number) =>
      this.get<Product[]>(`/products/`, {...filters, limit, offset}),
    get: (id: string) => this.get<Product>(`/products/${id}`)
  }

  constructor(public http: HttpClient){}

  private buildParams(params: any = {}) {
    params = params || {};
    let searchParams = new HttpParams({
        encoder: new HttpQueryEncoderCodec(),
    });
    for (const [key, param] of Object.entries<any>(params)) {
        if (Array.isArray(param)) {
            for (const value of param) {
                searchParams = searchParams.append(key, value);
            }
        } else if (param !== undefined) {
            searchParams = searchParams.set(key, param);
        }
    }
    return searchParams;
}

private url(url: string, params: any = {}) {
    const searchParams = this.buildParams(params);
    return `${this.URL_PATH}${url}?${searchParams}`;
}

private get<T>(url: string, params: any = {}): Observable<T> {
    const searchParams = this.buildParams(params);

    return this.http
        .get<T>(`${this.URL_PATH}${url}`, {
            params: searchParams,
        });
}

private post<T>(url: string, body: any = null, params: any = {}) {
    const searchParams = this.buildParams(params);

    return this.http
        .post<T>(`${this.URL_PATH}${url}`, body, {
            params: searchParams,
        });
}

private postXml<T>(url: string, body: any = null, params: any = {}) {
    return this.http
        .post<T>(`${this.URL_PATH}${url}`, body, params);
}

private put<T>(url: string, body: any) {
    return this.http.put<T>(`${this.URL_PATH}${url}`, body);
}

private patch<T>(url: string, body: any) {
    return this.http.patch<T>(`${this.URL_PATH}${url}`, body);
}

private delete<T>(url: string) {
    return this.http.delete<T>(`${this.URL_PATH}${url}`);
}
}
