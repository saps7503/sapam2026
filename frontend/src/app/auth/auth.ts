import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthService  {
  private api = 'http://localhost:8000/api/login/'; // ← Ajusta con tu backend Django/NestJS

  constructor(private http: HttpClient) {}
  login(username: string, password: string): Observable<any> {
    return this.http.post(this.api, { username, password });
  }
}
