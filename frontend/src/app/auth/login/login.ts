import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { AuthService } from '../auth'; 

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule,CommonModule],
  templateUrl: './login.html',
  styleUrl: './login.scss',
})
export class Login {
  username = '';
  password = '';
  loading = false;
  error = '';

  constructor(private auth: AuthService) {}
  doLogin() {
    const ok = this.auth.login(this.username, this.password);

    if (!ok) {
      this.error = "Credenciales incorrectas";
    }
  }

}
