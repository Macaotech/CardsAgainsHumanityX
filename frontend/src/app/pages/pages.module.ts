import { BrowserModule } from '@angular/platform-browser';
import { GameComponent } from './game/game.component';
import { HomeComponent } from './home/home.component';
import { LobbyComponent } from './lobby/lobby.component';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { PagesRoute } from './pages.routes';
import { CommonModule } from '@angular/common';
@NgModule({
declarations: [HomeComponent, LobbyComponent , GameComponent],
imports: [
    CommonModule,
    RouterModule.forChild(PagesRoute),
    BrowserModule
],
exports: [],
providers: []
})
export class PagesModule {}
